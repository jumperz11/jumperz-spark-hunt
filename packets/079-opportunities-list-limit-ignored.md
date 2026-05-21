# Packet 079: Opportunities List Limit Ignored

## Summary

`spark opportunities list --limit 0` lists all recent opportunities, and `--limit -1` exits successfully with one opportunity.

The opportunity inbox is a reviewer-facing mission surface, so list bounds should be exact and malformed limits should fail.

## Mission Source

Spark Compete asks agents to inspect mission and opportunity workflows. Opportunity rows can turn into tasks and review evidence, so invalid display bounds should not produce successful output.

## Before Evidence

Repro on upstream `main` with an isolated home and two opportunity rows:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit 0
[SPARK] Opportunities (showing 2)
- opp2 | project:p | cat/high test
  Q: two
- opp1 | project:p | cat/low test
  Q: one

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit -1
[SPARK] Opportunities (showing 1)
- opp2 | project:p | cat/high test
  Q: two

$ echo $?
0
```

Observed result: zero becomes the default list size, and negative limits return success with a sliced subset.

## Expected Behavior

- `--limit 0` should display zero opportunities.
- Negative limits should exit non-zero.
- Positive limits should keep showing the requested newest opportunities.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit -1
[SPARK] Opportunities list failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit 0
[SPARK] Opportunities (showing 0)

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit 1
[SPARK] Opportunities (showing 1)
- opp2 | project:p | cat/high test
  Q: two
```

## Impact

- Agents cannot safely request a zero-row opportunity probe.
- Negative limits look like valid successful inbox reads.
- Reviewer proof can accidentally include opportunity rows beyond the requested bound.

## Proposed Fix

Validate `load_self_opportunities()` limits before reading and slicing:

```python
limit = 20 if limit is None else int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
if limit == 0:
    return []
```

Also preserve explicit zero in the CLI instead of converting it to the default.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-opportunities-list-limit`
- Branch: `codex/fix-opportunities-list-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-list-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-opportunities-list-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-list-limit?expand=1
- Commit: `4849a17`
- Verification: `PYTHONPATH=. python -m pytest tests/test_opportunity_inbox.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows zero rows for `--limit 0`, and shows the newest opportunity for `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
