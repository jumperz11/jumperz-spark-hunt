# Packet 084: Curiosity Questions Limit Ignored

## Summary

`spark curiosity --questions` ignores explicit zero and accepts negative display limits when stored knowledge gaps exist.

The CLI passes `args.limit or 10`, so `--limit 0` becomes the default window. The helper then slices with Python's negative slice behavior, so `--limit -1` exits successfully while returning a misleading subset.

## Mission Source

Spark Compete asks agents to inspect learning and question-generation surfaces. Even though the curiosity engine is deprecated, the CLI command is still exposed and produces reviewer-visible proof output.

## Before Evidence

Repro on upstream `main` with two seeded open knowledge gaps:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit 0
============================================================
  Open Questions (2)
============================================================

  [WHY] Why did the tests fail?
    Topic: tests
    Priority: 0.90
    From: tests failed...

  [HOW] How should deploy recover?
    Topic: deploy
    Priority: 0.80
    From: deploy failed...

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit -1
============================================================
  Open Questions (1)
============================================================

  [WHY] Why did the tests fail?
    Topic: tests
    Priority: 0.90
    From: tests failed...

$ echo $?
0
```

Observed result: zero still prints rows, and a negative limit exits successfully.

## Expected Behavior

Zero should show an empty bounded view, and negative limits should fail cleanly:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit 0
============================================================
  Open Questions (0)
============================================================

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit -1
[SPARK] curiosity question limit must be >= 0

$ echo $?
1
```

## Impact

- Agents cannot request a zero-row curiosity question view.
- Negative limits create plausible-looking but incorrect evidence.
- The shared `get_open_questions(..., limit=0)` helper returns all rows instead of an empty window.

## Proposed Fix

Preserve explicit zero and reject negative values in the shared helper, then convert validation errors into CLI-safe exits:

```python
limit = 10 if limit is None else int(limit)
if limit < 0:
    raise ValueError("curiosity question limit must be >= 0")
if limit == 0:
    return []
```

```python
try:
    gaps = engine.get_open_questions(limit=args.limit)
except ValueError as e:
    raise SystemExit(f"[SPARK] {e}") from e
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-curiosity-questions-limit`
- Branch: `codex/fix-curiosity-questions-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-curiosity-questions-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-curiosity-questions-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-curiosity-questions-limit?expand=1
- Commit: `1e9f6cd`
- Verification: `PYTHONPATH=. python -m pytest tests/test_curiosity_questions_limit.py -q` passed.
- Behavior check: isolated `HOME` curiosity questions respect `--limit 0` and reject `--limit -1` with exit `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
