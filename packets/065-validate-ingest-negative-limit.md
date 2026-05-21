# Packet 065: Validate-Ingest Negative Limit Traceback

## Summary

`spark validate-ingest --limit -1` crashes with a Python traceback when a queue file exists.

The command is a schema-validation surface for recent queue events, so invalid scan limits should fail cleanly before report writing or queue scanning.

## Mission Source

Spark Compete asks agents to inspect Spark operational surfaces and report focused proof. Ingest validation is a natural first-run diagnostic for event capture health; it should not expose raw Python internals for malformed limits.

## Before Evidence

Repro on upstream `main` with an isolated home and a queue file:

```console
$ tmp="$(mktemp -d)"
$ mkdir -p "$tmp/.spark/queue"
$ printf '{bad json\n' > "$tmp/.spark/queue/events.jsonl"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate-ingest --limit -1
Traceback (most recent call last):
  ...
  File "lib/ingest_validation.py", line 17, in _tail_lines
    lines: deque = deque(maxlen=limit)
ValueError: maxlen must be non-negative
$ echo "$?"
1
```

Observed result:

```text
negative scan limit reaches the ingest scanner
deque(maxlen=-1) raises ValueError
CLI prints a traceback instead of a Spark-safe error
```

## Expected Behavior

- Reject negative `--limit` values before scanning queue files.
- Do not write `ingest_report.json` for invalid limits.
- Preserve `--limit 0` as a valid zero-row diagnostic.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate-ingest --limit -1
[SPARK] Ingest validation limit must be zero or greater
$ echo "$?"
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate-ingest --limit 0
[SPARK] Ingest validation
   Processed: 0
   Valid: 0
   Invalid: 0
```

The negative-limit run exits with status `1` and creates no ingest report. The zero-limit run exits `0` and writes a report with `"window": 0`.

## Impact

- Agent diagnostics can fail with raw tracebacks for a simple malformed limit.
- Automation cannot rely on a clean Spark error surface for ingest validation.
- Invalid report windows can be written when no queue file exists.

## Proposed Fix

Validate the limit in both the CLI command and scanner:

```python
limit = int(args.limit)
if limit < 0:
    raise SystemExit(1)
```

and:

```python
limit = int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-validate-ingest-limit`
- Branch: `codex/fix-validate-ingest-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-validate-ingest-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-validate-ingest-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-validate-ingest-limit?expand=1
- Commit: `8d865cf`
- Verification: `PYTHONPATH=. python -m pytest tests/test_validate_ingest_limit.py tests/test_queue_concurrency.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1` without traceback or report creation; `--limit 0` processes zero rows and writes a zero-window report.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
