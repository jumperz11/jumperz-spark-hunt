# Packet 053: Auto-Link Limit Zero Processes All Outcomes

## Summary

`spark auto-link --limit 0` processes and writes links for all available unlinked outcomes.

The parser help describes `--limit` as the max outcomes to process. An explicit zero should not turn into a bulk mutation.

## Mission Source

Spark Compete asks agents to exercise outcome validation and learning loops. Auto-link is a mutation command that creates validation evidence, so its processing limit must be respected exactly.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "When database schema changes before deploy: rehearse rollback because migration failures can block recovery." --reliability 0.9
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Database schema migration recovered after rollback rehearsal"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Database schema deploy passed after rollback rehearsal"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 0
[SPARK] Auto-Link Outcomes (APPLIED)
   Processed: 2
   Linked: 2
   Skipped: 0
```

Observed result:

```text
exit=0
~/.spark/outcome_links.jsonl contains 2 links
```

For comparison, `--limit 1` correctly processes one outcome:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 1
[SPARK] Auto-Link Outcomes (APPLIED)
   Processed: 1
   Linked: 1
   Skipped: 0
```

The root cause is twofold:

```python
limit = int(getattr(args, 'limit', 50) or 50)
```

This converts explicit `0` into `50`, and downstream `get_unlinked_outcomes(limit=0)` treats zero as an unlimited-ish slice.

## Expected Behavior

`--limit 0` should process zero outcomes and write no links:

```text
exit=0
[SPARK] Auto-Link Outcomes (APPLIED)
   Processed: 0
   Linked: 0
   Skipped: 0
```

Negative limits should fail:

```text
exit=1
[SPARK] Auto-link failed: limit must be zero or greater
```

Positive limits should keep working.

## Impact

- A safety-oriented zero limit performs a bulk mutation.
- Automation cannot safely dry-probe auto-link behavior with `--limit 0`.
- Outcome validation can receive many unintended links from a command that appeared bounded.

## Proposed Fix

Preserve explicit zero in the CLI and stop auto-link before reading or writing when `limit == 0`:

```python
raw_limit = getattr(args, "limit", 50)
limit = int(raw_limit if raw_limit is not None else 50)
if limit == 0:
    return {"processed": 0, "linked": 0, "skipped": 0, "matches": []}
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-auto-link-limit-zero`
- Branch: `codex/fix-auto-link-limit-zero`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-auto-link-limit-zero
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-auto-link-limit-zero
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-auto-link-limit-zero?expand=1
- Commit: `9ba22d3`
- Verification: `PYTHONPATH=. python -m pytest tests/test_auto_link_limit_validation.py tests/test_outcome_log_full_stats.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 0` exits `0` with `Processed: 0` and creates no link file.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 1` exits `0` and writes one link.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli auto-link --limit -1` exits `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
