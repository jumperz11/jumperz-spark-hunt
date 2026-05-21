# Packet 052: Auto-Link Accepts Invalid Similarity Thresholds

## Summary

`spark auto-link --min-similarity -1` accepts an invalid threshold and writes weak outcome-insight links.

In a repro where the default `0.25` threshold skips a weak match, the negative threshold creates a link with only `0.08` similarity.

## Mission Source

Spark Compete asks agents to exercise outcome validation and learning loops. Auto-linking outcomes to insights creates validation evidence, so invalid thresholds must not create low-confidence proof rows.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "When database schema changes before deploy: rehearse rollback because migration failures can block recovery." --reliability 0.9
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Database timeout recovered after retry"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.25
[SPARK] Auto-Link Outcomes (APPLIED)
   Processed: 1
   Linked: 0
   Skipped: 1
```

The same data with an invalid threshold writes a weak link:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity -1
[SPARK] Auto-Link Outcomes (APPLIED)
   Processed: 1
   Linked: 1
   Skipped: 0

   Top matches:
   [0.08] Database timeout recovered after re... -> When database schema changes before...
```

Persisted link:

```json
{
  "confidence": 0.07692307692307693,
  "notes": "auto-linked (similarity=0.08)"
}
```

`--min-similarity 2` also exits `0` with zero work, despite the help text documenting a `0-1` range.

## Expected Behavior

Invalid auto-link thresholds should fail before reading or writing links:

```text
exit=1
[SPARK] Auto-link failed: min_similarity must be between 0 and 1
```

Valid thresholds in the documented range should keep working.

## Impact

- Negative thresholds can create weak validation links that normal defaults correctly skip.
- Downstream outcome validation can consume low-similarity links as if they were evidence.
- Automation cannot distinguish invalid threshold runs from legitimate no-op runs when the command exits `0`.

## Proposed Fix

Validate the auto-link threshold in the library and convert validation errors into CLI-safe failures:

```python
min_similarity = float(min_similarity)
if not 0.0 <= min_similarity <= 1.0:
    raise ValueError("min_similarity must be between 0 and 1")
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-auto-link-threshold-validation`
- Branch: `codex/fix-auto-link-threshold-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-auto-link-threshold-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-auto-link-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-auto-link-threshold-validation?expand=1
- Commit: `52897ef`
- Verification: `PYTHONPATH=. python -m pytest tests/test_auto_link_threshold_validation.py tests/test_outcome_log_full_stats.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity -1` exits `1` and creates no link file.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.25 --dry-run` exits `0`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
