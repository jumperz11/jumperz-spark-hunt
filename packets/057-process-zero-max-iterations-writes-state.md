# Packet 057: Process Zero Max Iterations Still Runs Worker

## Summary

`spark process --drain --max-iterations 0` still runs one bridge-worker cycle and writes Spark state.

The option is documented as the maximum number of cycles when draining. An explicit zero maximum should not start a worker cycle or create state files.

## Mission Source

Spark Compete asks agents to run missions through Spark CLI workflows. The bridge worker touches learning, validation, prediction, project context, and heartbeat state, so ignored run limits are high-signal mutation bugs.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --max-iterations 0 --timeout 0.01 --interval 0
Chips directory not found: /path/to/vibeship-spark-intelligence/chips
[SPARK] Cycle errors: context
[SPARK] bridge_worker cycles: 1, patterns processed: 0
```

Observed result:

```text
exit=0
~/.spark/pipeline_metrics.json
~/.spark/pending_memory.json
~/.spark/pipeline_state.json
~/.spark/eidos.db
~/.spark/projects/<project>.json
~/.spark/sync_stats.json
~/.spark/project_context.json
~/.spark/prediction_state.json
~/.spark/memory_capture_state.json
~/.spark/bridge_worker_heartbeat.json
```

## Expected Behavior

`--drain --max-iterations 0` should be a zero-cycle no-op:

```text
[SPARK] bridge_worker cycles: 0, patterns processed: 0
exit=0
no ~/.spark state files created by the worker
```

Negative max-iteration values should fail before running:

```text
[SPARK] Max iterations must be zero or greater
exit=1
```

## Impact

- Automation cannot use `--max-iterations 0` as a safe dry/no-op bound.
- A command that appears bounded still starts the bridge worker and writes learning/validation state.
- Invalid negative values are not rejected before the worker path.

## Proposed Fix

Validate max iterations before entering the worker loop:

```python
max_iterations = int(args.max_iterations)
if max_iterations < 0:
    print("[SPARK] Max iterations must be zero or greater")
    raise SystemExit(1)
if args.drain and max_iterations == 0:
    print("[SPARK] bridge_worker cycles: 0, patterns processed: 0")
    return
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-process-max-iterations-zero`
- Branch: `codex/fix-process-max-iterations-zero`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-process-max-iterations-zero
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-process-max-iterations-zero
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-process-max-iterations-zero?expand=1
- Commit: `5a5469a`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_process_max_iterations.py -q` passed.
- Behavior checks:
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli process --drain --max-iterations 0 --timeout 0.01 --interval 0` exits `0`, reports zero cycles, and creates no worker state files.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli process --drain --max-iterations -1 --timeout 0.01 --interval 0` exits `1` before creating worker state.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
