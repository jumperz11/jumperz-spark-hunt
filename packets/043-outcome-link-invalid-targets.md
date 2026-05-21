# Packet 043: Outcome Link Accepts Invalid Targets

## Summary

`spark outcome-link` creates validation links for missing outcome IDs and out-of-range confidence values.

The command is meant to connect a real outcome to an insight. When it accepts nonexistent outcomes or impossible confidence values, it creates proof-looking rows that downstream validation can treat as real evidence.

## Mission Source

Spark Compete asks agents to produce before/after proof and focused fixes. Outcome-to-insight links are part of that evidence path, so invalid links should be rejected before any JSONL write.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-link missing insight:key
[SPARK] Link created: ...
   Outcome: missing
   Insight: insight:key
```

Observed result:

```text
exit=0
~/.spark/outcome_links.jsonl created
```

Second repro:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-link missing insight:key --confidence 2
[SPARK] Link created: ...
   Outcome: missing
   Insight: insight:key
```

Observed result:

```text
exit=0
invalid confidence persisted
```

`cmd_outcome_link()` parsed the confidence and called `link_outcome_to_insight()` directly, with no target existence check and no range validation.

## Expected Behavior

Missing outcomes should fail before writing:

```text
exit=1
[SPARK] Outcome not found for id: missing
```

Out-of-range confidence values should fail before writing:

```text
exit=1
[SPARK] Link confidence must be between 0 and 1
```

Valid existing outcomes should still create links, including documented boundary values such as `--confidence 0`.

## Impact

- Agents can generate false validation evidence for outcomes that never existed.
- Confidence values outside the documented `0-1` range can pollute downstream scoring.
- Automation sees successful exits and may report a validation link was created correctly.

## Proposed Fix

Validate the CLI input before calling the JSONL writer:

```python
confidence = float(args.confidence if args.confidence is not None else 1.0)
if confidence < 0.0 or confidence > 1.0:
    print("[SPARK] Link confidence must be between 0 and 1")
    raise SystemExit(1)

known_outcome_ids = {str(outcome.get("outcome_id") or "") for outcome in read_outcomes(limit=None)}
if outcome_id not in known_outcome_ids:
    print(f"[SPARK] Outcome not found for id: {outcome_id}")
    raise SystemExit(1)
```

Keep the lower-level writer unchanged for internal callers that already work from real outcome records.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-link-validation`
- Branch: `codex/fix-outcome-link-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-link-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-link-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-link-validation?expand=1
- Commit: `5efe22b`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_validation.py tests/test_outcome_log_full_stats.py -q` passed.
- Behavior check: missing outcome IDs now exit `1` without creating `outcome_links.jsonl`.
- Behavior check: invalid confidence values now exit `1` without creating `outcome_links.jsonl`.
- Behavior check: existing outcomes still link successfully, and `--confidence 0` is preserved.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
