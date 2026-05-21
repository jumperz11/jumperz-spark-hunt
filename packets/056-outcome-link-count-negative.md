# Packet 056: Outcome Negative Link Count Still Records Outcome

## Summary

`spark outcome --link-count -1` records a new outcome instead of rejecting the invalid link count.

The argument describes how many recent exposures to link. Negative counts are invalid and should fail before creating outcome evidence.

## Mission Source

Spark Compete asks agents to exercise outcome and validation workflows. Explicit outcomes are high-signal evidence, so invalid linking arguments should not still append outcome rows.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --link-count -1
[SPARK] Outcome recorded: success (polarity=pos)
```

Observed result:

```text
exit=0
~/.spark/outcomes.jsonl is created
```

Persisted row:

```json
{
  "event_type": "explicit_checkin",
  "text": "Deploy succeeded after a separate check",
  "result": "success"
}
```

## Expected Behavior

Negative link counts should fail before recording:

```text
exit=1
[SPARK] Link count must be zero or greater
```

`--link-count 0` should still record an unlinked outcome, and positive counts should continue reading recent exposures.

## Impact

- Invalid link options still create outcome evidence.
- Automation cannot rely on non-zero exit status to catch malformed link-count runs.
- Outcome logs can grow from commands that should have been rejected before mutation.

## Proposed Fix

Validate `link_count` before any link-count or link-latest logic:

```python
link_count = int(args.link_count or 0)
if link_count < 0:
    print("[SPARK] Link count must be zero or greater")
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-link-count-validation`
- Branch: `codex/fix-outcome-link-count-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-link-count-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-link-count-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-link-count-validation?expand=1
- Commit: `e1cc32e`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_count.py -q` passed.
- Behavior checks:
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --link-count -1` exits `1` before creating an outcome file.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --link-count 0` exits `0` and records an unlinked outcome.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
