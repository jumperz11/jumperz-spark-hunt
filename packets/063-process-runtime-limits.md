# Packet 063: Process Runtime Limits Still Run Worker

## Summary

`spark process --drain` accepts invalid runtime bounds and still runs a bridge worker cycle.

Passing `--timeout -1` should fail before work starts, but upstream runs one full cycle, writes a heartbeat, and initializes multiple Spark state files.

## Mission Source

Spark Compete asks agents to run CLI missions in clean worktrees and report before/after proof. `spark process` is a high-impact background worker path, so invalid runtime limits must not start mutation-heavy processing.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --timeout -1 --interval 0 --max-iterations 100
Chips directory not found: /path/to/vibeship-spark-intelligence/chips
[SPARK] Cycle errors: context
[SPARK] bridge_worker cycles: 1, patterns processed: 0
$ echo "$?"
0
$ find "$tmp/.spark" -maxdepth 2 -type f | sort
$tmp/.spark/bridge_worker_heartbeat.json
$tmp/.spark/eidos.db
$tmp/.spark/eidos_curriculum_history.jsonl
$tmp/.spark/eidos_curriculum_latest.json
$tmp/.spark/eidos_llm_counter.txt
$tmp/.spark/exports/SPARK_ADVISORY_PAYLOAD.json
$tmp/.spark/exports/gemini_system.md
$tmp/.spark/exports/gpt_instructions.md
$tmp/.spark/memory_capture_state.json
$tmp/.spark/pending_memory.json
$tmp/.spark/pipeline_metrics.json
$tmp/.spark/pipeline_state.json
$tmp/.spark/prediction_state.json
$tmp/.spark/project_context.json
$tmp/.spark/projects/spark-audit-cli-edges.json
$tmp/.spark/sync_stats.json
```

Observed result:

```text
negative timeout is accepted
command exits successfully
bridge worker runs once and writes state
```

`--timeout 0` is also ignored in drain mode because the loop checks `if timeout_s`, so an explicit zero-second drain budget is treated as no timeout.

## Expected Behavior

- Reject negative `--timeout`, `--interval`, `--memory-limit`, and `--pattern-limit` values before running the worker.
- Treat `spark process --drain --timeout 0` as a zero-cycle no-op.
- Preserve non-drain behavior: a one-shot `spark process --timeout 0` can still run one cycle because timeout is documented for drain mode.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --timeout -1 --interval 0 --max-iterations 100
[SPARK] Timeout must be zero or greater

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --timeout 0 --interval 0 --max-iterations 100
[SPARK] bridge_worker cycles: 0, patterns processed: 0
```

The negative timeout exits with status `1`. The zero-timeout drain exits `0` without creating `.spark` files.

## Impact

- Invalid process bounds can trigger a mutation-heavy worker cycle.
- Agents cannot safely dry-probe `spark process` with a zero or invalid runtime budget.
- Review worktrees and isolated-home runs get polluted by worker state despite invalid input.

## Proposed Fix

Validate runtime limits in `cmd_process` before calling `run_bridge_cycle`, and short-circuit zero-timeout drain runs:

```python
if timeout_s < 0:
    raise SystemExit(1)
if args.drain and timeout_s == 0:
    print("[SPARK] bridge_worker cycles: 0, patterns processed: 0")
    return
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-process-runtime-validation`
- Branch: `codex/fix-process-runtime-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-process-runtime-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-process-runtime-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-process-runtime-validation?expand=1
- Commit: `c668028`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_process_runtime_validation.py tests/test_bridge_cycle_safety.py -q` passed.
- Behavior check: isolated `HOME` rejects negative timeout and performs zero-cycle drain with no `.spark` files created.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
