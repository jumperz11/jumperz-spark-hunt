# Packet 073: Learnings Limit Ignored

## Summary

`spark learnings --limit 0` ignores the explicit zero and prints recent learnings. `spark learnings --limit -1` exits successfully with a nonsensical negative count.

The command is a reviewer-facing learning evidence surface, so display bounds should be respected exactly.

## Mission Source

Spark Compete asks agents to inspect learning loops and proof outputs. The learnings view is one of the main ways to audit what Spark has captured, so malformed display limits should not produce misleading output.

## Before Evidence

Repro on upstream `main` with an isolated home and one seeded learning:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn communication "User likes direct summaries"
[ok] Learned [communication]: User likes direct summaries
  Reliability: 70%

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit 0

[book] Recent Cognitive Insights (showing 1 of 1)

[communication] User likes direct summaries
   70% reliable | 0 validations | 2026-05-21

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit -1

[book] Recent Cognitive Insights (showing -1 of 1)
```

Observed result: zero is converted to the default limit, while negative values return success.

## Expected Behavior

- `--limit 0` should display zero learning rows.
- Negative limits should exit non-zero before loading or displaying learnings.
- Positive limits should keep displaying the requested number of rows.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit -1
[SPARK] Learnings limit must be zero or greater

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit 0

[book] Recent Cognitive Insights (showing 0 of 1)

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit 1

[book] Recent Cognitive Insights (showing 1 of 1)

[communication] User likes direct summaries
   70% reliable | 0 validations | 2026-05-21
```

## Impact

- Agents cannot safely request a zero-row metadata probe of captured learnings.
- Negative limits produce successful but misleading output.
- Reviewer proof can accidentally show more learning content than requested.

## Proposed Fix

Validate display limits before loading cognitive state and preserve explicit zero:

```python
limit = int(args.limit)
if limit < 0:
    print("[SPARK] Learnings limit must be zero or greater")
    sys.exit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-learnings-limit-validation`
- Branch: `codex/fix-learnings-limit-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-learnings-limit-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-learnings-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-learnings-limit-validation?expand=1
- Commit: `ec2e8c0`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_learnings_limit.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows no rows for `--limit 0`, and shows the seeded insight for `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
