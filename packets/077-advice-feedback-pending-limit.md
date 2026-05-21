# Packet 077: Advice Feedback Pending Limit Ignored

## Summary

`spark advice-feedback --pending --limit 0` lists the full pending advice feedback backlog, and `--limit -1` exits successfully with one request.

The command is a reviewer-facing inspection path for advice feedback requests, so display bounds should be exact and invalid limits should fail.

## Mission Source

Spark Compete missions ask agents to inspect feedback, validation, and proof loops. Advice feedback requests are part of Spark's review/evidence surface, so malformed pending-list limits can mislead automation and reviewers.

## Before Evidence

Repro on upstream `main` with an isolated home and three pending request rows:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit 0
[SPARK] Advice Feedback Requests (3):
  - tool=three ts=3
  - tool=two ts=2
  - tool=one ts=1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit -1
[SPARK] Advice Feedback Requests (1):
  - tool=three ts=3

$ echo $?
0
```

Observed result: zero is converted to the default limit, and negative limits return success.

## Expected Behavior

- `--limit 0` should display zero pending requests.
- Negative limits should exit non-zero.
- Positive limits should keep showing the requested number of newest requests.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit -1
[SPARK] Advice feedback requests failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit 0
[SPARK] No pending advice feedback requests.

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit 2
[SPARK] Advice Feedback Requests (2):
  - tool=three ts=3
  - tool=two ts=2
```

## Impact

- Agents cannot safely request a zero-row pending-feedback probe.
- Negative limits produce successful but misleading output.
- Reviewer proof can accidentally expose more pending advice requests than requested.

## Proposed Fix

Validate `list_requests()` limits before slicing:

```python
limit = 10 if limit is None else int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
if limit == 0:
    return []
```

Also preserve explicit zero in the CLI instead of converting it to the default.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-advice-pending-limit`
- Branch: `codex/fix-advice-pending-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advice-pending-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-advice-pending-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advice-pending-limit?expand=1
- Commit: `3510d4c`
- Verification: `PYTHONPATH=. python -m pytest tests/test_advice_feedback_correlation.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows no rows for `--limit 0`, and shows two newest requests for `--limit 2`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
