# Packet 086: Contradictions Display Limit Ignored

## Summary

`spark contradictions --unresolved` ignores explicit zero and accepts negative display limits when unresolved contradictions exist.

The unresolved view slices with `args.limit or 10`, so `--limit 0` becomes the default window and `--limit -1` returns a misleading subset. The header can also report the full unresolved count while printing fewer rows.

## Mission Source

Spark Compete asks agents to inspect learning and validation loops. Contradictions are direct evidence that Spark detected conflicting beliefs, so the unresolved view should respect bounded display limits.

## Before Evidence

Repro on upstream `main` with two seeded unresolved contradictions:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit 0
============================================================
  Unresolved Contradictions (2)
============================================================

  [0] DIRECT (confidence: 0.95)
    Existing: Always run broad tests...
    New: Never run broad tests...

  [1] DIRECT (confidence: 0.85)
    Existing: Prefer small patches...
    New: Avoid small patches...

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit -1
============================================================
  Unresolved Contradictions (2)
============================================================

  [0] DIRECT (confidence: 0.95)
    Existing: Always run broad tests...
    New: Never run broad tests...

$ echo $?
0
```

Observed result: zero displays rows, and negative limits exit successfully with a sliced subset.

## Expected Behavior

Zero should show an empty bounded view, and negative limits should fail cleanly:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit 0
============================================================
  Unresolved Contradictions (0)
============================================================

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit -1
[SPARK] contradiction limit must be >= 0

$ echo $?
1
```

## Impact

- Agents cannot request a zero-row contradiction proof window.
- Negative limits create misleading contradiction evidence.
- The header can disagree with the number of rows printed.

## Proposed Fix

Validate the unresolved display limit before slicing, then print the bounded row count:

```python
limit = int(args.limit)
if limit < 0:
    raise SystemExit("[SPARK] contradiction limit must be >= 0")
unresolved = detector.get_unresolved()[:limit]
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-contradictions-display-limit`
- Branch: `codex/fix-contradictions-display-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-contradictions-display-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-contradictions-display-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-contradictions-display-limit?expand=1
- Commit: `1efefaa`
- Verification: `PYTHONPATH=. python -m pytest tests/test_contradictions_display_limit.py -q` passed.
- Behavior check: isolated `HOME` contradictions respect `--limit 0`, reject `--limit -1` with exit `1`, and keep positive-limit headers bounded.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
