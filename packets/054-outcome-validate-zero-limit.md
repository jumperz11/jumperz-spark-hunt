# Packet 054: Outcome Validate Limit Zero Validates Links

## Summary

`spark outcome-validate --limit 0` validates outcome links and mutates insight reliability.

The parser help describes `--limit` as the max links to process. An explicit zero should process no links, not validate every available link.

## Mission Source

Spark Compete asks agents to exercise outcome validation and learning loops. Outcome validation is a high-impact mutation command because it changes insight reliability and marks links as validated.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "When deploy checks pass: keep rollback evidence attached because validation depends on explicit outcomes." --reliability 0.9
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy checks passed with rollback evidence attached"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-link "$outcome_id" "$insight_key"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-validate --limit 0
[SPARK] Outcome Validation
   Processed: 1
   Validated: 1
   Contradicted: 0
   Surprises: 0
```

Observed result:

```text
exit=0
outcome_links.jsonl changes validated from false to true
cognitive_insights.json changes times_validated from 0 to 1
```

The root cause is that `cmd_outcome_validate()` converts explicit zero to `100`, and the lower-level JSONL readers also treat `limit <= 0` as unbounded:

```python
limit = int(args.limit or 100)
```

## Expected Behavior

`--limit 0` should process zero links and leave state unchanged:

```text
exit=0
[SPARK] Outcome Validation
   Processed: 0
   Validated: 0
   Contradicted: 0
   Surprises: 0
```

Negative limits should fail:

```text
exit=1
[SPARK] Outcome validation failed: limit must be zero or greater
```

Positive limits should keep validating normally.

## Impact

- A safety-oriented zero limit performs validation mutations.
- Automation cannot safely probe outcome validation with `--limit 0`.
- Insight reliability and validation links can be changed despite an explicit zero max.

## Proposed Fix

Preserve explicit zero in the CLI and short-circuit validation before loading learner state:

```python
raw_limit = getattr(args, "limit", 100)
limit = int(raw_limit if raw_limit is not None else 100)
if limit == 0:
    return {"processed": 0, "validated": 0, "contradicted": 0, "surprises": 0}
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-validate-zero-limit`
- Branch: `codex/fix-outcome-validate-zero-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-validate-zero-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-validate-zero-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-validate-zero-limit?expand=1
- Commit: `15766a0`
- Verification: `PYTHONPATH=. python -m pytest tests/test_outcome_validate_limit.py tests/test_validation_loop.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-validate --limit 0` exits `0`, processes `0`, leaves the link unvalidated, and leaves `times_validated` at `0`.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-validate --limit 1` exits `0` and validates one link.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-validate --limit -1` exits `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
