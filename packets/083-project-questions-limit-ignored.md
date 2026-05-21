# Packet 083: Project Questions Limit Ignored

## Summary

`spark project questions` ignores explicit zero and accepts negative display limits.

The project question helper collapses `--limit 0` into the default window and clamps every limit to at least one row, so agents cannot request an empty bounded proof window and negative values produce misleading output.

## Mission Source

Spark Compete asks agents to inspect project learning and onboarding surfaces. Suggested project questions are part of the context-gathering loop, so bounded views should behave predictably for automated review.

## Before Evidence

Repro on upstream `main` with an isolated `HOME`:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit 0
[SPARK] Suggested questions:
   - [goal] gen_goal: What is the project goal in one sentence?
   - [done] gen_done: How will we know it's complete?
   - [risk] gen_risk: What could make this fail later?

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit -1
[SPARK] Suggested questions:
   - [goal] gen_goal: What is the project goal in one sentence?

$ echo $?
0
```

Observed result: zero still prints rows, and a negative limit exits successfully.

## Expected Behavior

Zero should show no rows, and negative limits should fail cleanly:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit 0
[SPARK] No unanswered questions.

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit -1
[SPARK] project question limit must be >= 0

$ echo $?
1
```

## Impact

- Agents cannot request a zero-row project question view.
- Negative limits produce plausible-looking but incorrect reviewer evidence.
- Shared helper behavior can mislead any caller that uses `get_suggested_questions(..., limit=0)`.

## Proposed Fix

Preserve explicit zero and reject negative values in the shared helper, then convert helper validation errors into CLI-safe exits:

```python
limit = 3 if limit is None else int(limit)
if limit < 0:
    raise ValueError("project question limit must be >= 0")
if limit == 0:
    return []
```

```python
try:
    suggested = get_suggested_questions(profile, limit=limit)
except ValueError as e:
    raise SystemExit(f"[SPARK] {e}") from e
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-project-questions-limit`
- Branch: `codex/fix-project-questions-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-questions-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-project-questions-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-questions-limit?expand=1
- Commit: `3949a8d`
- Verification: `PYTHONPATH=. python -m pytest tests/test_project_questions_limit.py -q` passed.
- Behavior check: isolated `HOME` project questions respect `--limit 0` and reject `--limit -1` with exit `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
