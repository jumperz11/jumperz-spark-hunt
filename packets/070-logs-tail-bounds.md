# Packet 070: Logs Tail Bounds Ignored

## Summary

`spark logs --tail 0` prints all log lines, and `spark logs --tail -1` exits successfully with a sliced subset.

The flag is documented as the number of lines to show, so zero should show zero lines and negative values should fail before reading logs.

## Mission Source

Spark Compete asks agents to inspect operational readiness surfaces. Logs are a core diagnostic path for services, so malformed tail bounds should not return misleading successful output.

## Before Evidence

Repro on upstream `main` with an isolated log directory:

```console
$ printf 'one\ntwo\nthree\n' > "$tmp/logs/sparkd.log"

$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail 0

  === sparkd (3 lines) ===
  one
  two
  three

$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail -1 --json
{
  "ok": true,
  "command": "logs",
  "logs": [
    {
      "service": "sparkd",
      "lines": [
        "two",
        "three"
      ],
      "count": 2
    }
  ]
}
```

Observed result: explicit zero becomes "show everything", and negative tail values return successful JSON.

## Expected Behavior

- `--tail 0` returns zero lines.
- Negative `--tail` exits non-zero with a Spark-safe message.
- Positive tail values keep returning the last N lines.

After the fix:

```console
$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail -1 --json
{
  "ok": false,
  "error": "tail must be zero or greater"
}

$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail 0 --json
{
  "ok": true,
  "command": "logs",
  "logs": [
    {
      "service": "sparkd",
      "lines": [],
      "count": 0
    }
  ]
}
```

## Impact

- Agents cannot safely request a zero-line metadata probe.
- Negative limits produce successful machine-readable output instead of a validation failure.
- Operational diagnostics can return more log content than requested.

## Proposed Fix

Validate tail bounds before reading logs and preserve explicit zero:

```python
if tail_n < 0:
    print(...)
    sys.exit(1)

if tail_n == 0:
    lines = []
elif len(lines) > tail_n:
    lines = lines[-tail_n:]
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-logs-tail-validation`
- Branch: `codex/fix-logs-tail-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-logs-tail-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-logs-tail-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-logs-tail-validation?expand=1
- Commit: `5c0ffb3`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_logs_tail_validation.py -q` passed.
- Behavior check: isolated `SPARK_LOG_DIR` rejects `--tail -1`, returns zero lines for `--tail 0`, and returns the last two lines for `--tail 2`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
