# Packet 076: Outcome Links Limit Ignored

## Summary

`spark outcome-links --limit 0` and `spark outcome-links --limit -1` both list all outcome-insight links and exit successfully.

The command shows validation attribution evidence, so display bounds should be respected exactly.

## Mission Source

Spark Compete asks agents to inspect outcome-validation loops. Outcome links are explicit evidence tying outcomes back to insights, so malformed display limits should not expose all links or return false success.

## Before Evidence

Repro on upstream `main` with an isolated home and two outcome links:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit 0
[SPARK] Outcome-Insight Links (2):
   l1... o1... -> i1 [validated=N result=-]
   l2... o2... -> i2 [validated=Y result=validated]

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit -1
[SPARK] Outcome-Insight Links (2):
   l1... o1... -> i1 [validated=N result=-]
   l2... o2... -> i2 [validated=Y result=validated]

$ echo $?
0
```

Observed result: zero and negative limits both behave like unlimited reads.

## Expected Behavior

- `--limit 0` should display zero links.
- Negative limits should exit non-zero.
- Positive limits should keep showing the requested number of newest links.
- `get_outcome_links(limit=None)` should remain the explicit full-scan API.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit -1
[SPARK] Outcome links failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit 0
[SPARK] No links found.

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit 1
[SPARK] Outcome-Insight Links (1):
   l2... o2... -> i2 [validated=Y result=validated]
```

## Impact

- Agents cannot safely request a zero-row validation-link probe.
- Negative limits produce successful but misleading output.
- Reviewer proof can accidentally expose all outcome-insight links.

## Proposed Fix

Distinguish `None` from numeric limits in `get_outcome_links()`:

```python
if limit is None:
    return links
limit = int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
if limit == 0:
    return []
```

Also preserve explicit zero in the CLI instead of converting it to the default.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-links-limit`
- Branch: `codex/fix-outcome-links-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-links-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-links-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-links-limit?expand=1
- Commit: `9ad2741`
- Verification: `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows no rows for `--limit 0`, and shows one newest link for `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
