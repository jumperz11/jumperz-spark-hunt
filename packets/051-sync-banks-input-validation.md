# Packet 051: Sync Banks Accepts Invalid Thresholds And Categories

## Summary

`spark sync-banks` accepts invalid reliability thresholds and category filters.

`--min-reliability -1` syncs a 10% reliable insight into memory banks, and `--categories bogus` exits successfully with zero work.

## Mission Source

Spark Compete asks agents to exercise memory and learning loops. Syncing cognitive insights into retrieval banks is a mutation command, so threshold and category input must fail clearly when invalid.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "When preparing a focused fix, reproduce the failing command first and add a narrow regression test before changing the implementation." --reliability 0.1
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-banks --min-reliability -1
[SPARK] Sync Insights to Banks (APPLIED)
   Processed: 1
   Synced: 1
   Skipped (low reliability): 0
   Duplicates: 0

   Synced entries (1):
   [10%] wisdom: When preparing a focused fix, reproduce the failin...
```

Observed result:

```text
exit=0
~/.spark/banks/global_user.jsonl receives the 10% reliable insight
```

Invalid categories also look successful:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli sync-banks --categories bogus
[SPARK] Sync Insights to Banks (APPLIED)
   Processed: 0
   Synced: 0
   Skipped (low reliability): 0
   Duplicates: 0
```

Observed result:

```text
exit=0
no category was valid
```

## Expected Behavior

Invalid sync-banks inputs should fail before syncing:

```text
exit=1
[SPARK] Sync banks failed: min_reliability must be between 0 and 1
```

```text
exit=1
[SPARK] Sync banks failed: unknown categories: bogus
```

Valid threshold and category values should keep working.

## Impact

- Low-reliability insights can be promoted into retrieval memory by passing a negative threshold.
- Automation can treat invalid category filters as successful sync runs.
- Memory banks can receive noisy evidence that later affects advice retrieval.

## Proposed Fix

Validate `min_reliability` and category names in `sync_insights_to_banks()`, and convert validation errors into CLI-safe non-zero exits:

```python
if not 0.0 <= min_reliability <= 1.0:
    raise ValueError("min_reliability must be between 0 and 1")
if unknown_categories:
    raise ValueError(...)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-sync-banks-input-validation`
- Branch: `codex/fix-sync-banks-input-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-banks-input-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-sync-banks-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-banks-input-validation?expand=1
- Commit: `cfd8733`
- Verification: `PYTHONPATH=. python -m pytest tests/test_sync_banks_validation.py tests/test_memory_emotion_integration.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-banks --min-reliability -1` exits `1`.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli sync-banks --categories bogus` exits `1`.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-banks --min-reliability 0.7 --dry-run` exits `0`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
