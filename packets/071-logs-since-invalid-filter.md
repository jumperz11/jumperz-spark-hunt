# Packet 071: Logs Invalid Since Filter Ignored

## Summary

`spark logs --since <bad-value>` silently ignores the malformed time filter and returns all matching log lines with a successful exit code.

The `--since` flag is meant to limit logs by relative time, so invalid values should fail before reading logs.

## Mission Source

Spark Compete asks agents to inspect operational diagnostics and service readiness. Log filtering is a core troubleshooting path, and malformed filters should not return misleading machine-readable success.

## Before Evidence

Repro on upstream `main` with an isolated log directory:

```console
$ printf 'one\ntwo\nthree\n' > "$tmp/logs/sparkd.log"

$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --since nope --json
{
  "ok": true,
  "command": "logs",
  "logs": [
    {
      "service": "sparkd",
      "lines": [
        "one",
        "two",
        "three"
      ],
      "count": 3
    }
  ]
}
```

Observed result: the invalid filter is treated as if no `--since` filter was provided.

## Expected Behavior

- Invalid `--since` values exit non-zero.
- JSON output should report a machine-readable failure.
- Valid relative values such as `30m`, `1h`, and `2d` should keep working.

After the fix:

```console
$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --since nope --json
{
  "ok": false,
  "error": "since must use a relative time like 30m, 1h, or 2d"
}

$ SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --since 1h --json
{
  "ok": true,
  "command": "logs",
  "logs": [
    {
      "service": "sparkd",
      "lines": [
        "one",
        "two",
        "three"
      ],
      "count": 3
    }
  ]
}
```

## Impact

- Agents can believe a filtered log query succeeded while receiving unfiltered data.
- Automation cannot distinguish malformed diagnostic filters from a valid all-lines query.
- A typo in a troubleshooting command can expose more log content than requested.

## Proposed Fix

Parse and validate `--since` once before reading logs:

```python
cutoff = _parse_since(since)
if cutoff is None:
    print(...)
    sys.exit(1)
```

Then apply the parsed cutoff to every target log file.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-logs-since-validation`
- Branch: `codex/fix-logs-since-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-logs-since-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-logs-since-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-logs-since-validation?expand=1
- Commit: `ae3c6e1`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_logs_since_validation.py -q` passed.
- Behavior check: isolated `SPARK_LOG_DIR` rejects `--since nope` with exit `1`, while `--since 1h` still reads the expected log snapshot.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
