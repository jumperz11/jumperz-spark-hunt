# Packet 072: Validation Scan Negative Limit Reports Success

## Summary

`spark validate --limit -1` exits successfully and reports a zero-work validation scan.

The command scans recent queue events for validation signals, so invalid negative limits should fail before the validation loop runs.

## Mission Source

Spark Compete asks agents to inspect learning and validation loops. Validation scan output can become reviewer evidence, so malformed scan bounds must not look like successful zero-work diagnostics.

## Before Evidence

Repro on upstream `main` with an isolated home and one queued user prompt:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit -1
[SPARK] Validation scan
  processed: 0
  validated: 0
  contradicted: 0
  surprises: 0

$ echo $?
0
```

For comparison, `--limit 0` also reports zero work, and `--limit 1` processes the queued event. The negative run is indistinguishable from a legitimate zero-row scan by exit code.

## Expected Behavior

- Negative `--limit` values exit non-zero.
- Invalid limits do not write validation state.
- `--limit 0` remains a valid no-op.
- Positive limits keep processing queued events.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit -1
[SPARK] Validation scan failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit 0
[SPARK] Validation scan
  processed: 0
  validated: 0
  contradicted: 0
  surprises: 0

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit 1
[SPARK] Validation scan
  processed: 1
  validated: 0
  contradicted: 0
  surprises: 0
```

## Impact

- Agents can treat malformed validation scans as successful diagnostics.
- Reviewer proof can include false zero-work validation output.
- Invalid bounds reach a shared validation function without library-level protection.

## Proposed Fix

Validate scan limits in `process_validation_events()` and convert library validation failures into CLI-safe exits:

```python
limit = int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-validation-scan-limit`
- Branch: `codex/fix-validation-scan-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-validation-scan-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-validation-scan-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-validation-scan-limit?expand=1
- Commit: `2064984`
- Verification: `PYTHONPATH=. python -m pytest tests/test_validation_loop.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1` with exit `1` and no validation state write, preserves `--limit 0` as a no-op, and processes one queued event with `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
