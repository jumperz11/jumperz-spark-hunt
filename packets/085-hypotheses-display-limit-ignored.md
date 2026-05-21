# Packet 085: Hypotheses Display Limit Ignored

## Summary

`spark hypotheses` ignores explicit zero and accepts negative display limits in both testable and pending views.

The testable view uses `args.limit or 5`, so `--limit 0` becomes the default. Both testable and pending views also allow negative values to reach Python slicing, producing plausible-looking but incorrect output with exit `0`.

## Mission Source

Spark Compete asks agents to inspect learning, validation, and prediction loops. Hypotheses and pending predictions are direct proof of the prediction loop, so bounded views should be deterministic and reject invalid limits.

## Before Evidence

Repro on upstream `main` with two seeded hypotheses and pending predictions:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit 0
============================================================
  Testable Hypotheses (2)
============================================================

  [HYPOTHESIS] Fast tests catch regressions
    Confidence: 0.90

  [TESTING] Small patches review better
    Confidence: 0.80

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit -1
============================================================
  Testable Hypotheses (1)
============================================================

  [HYPOTHESIS] Fast tests catch regressions
    Confidence: 0.90

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit 0
============================================================
  Pending Predictions (2)
============================================================

  Hypothesis: Fast tests catch regressions...
    Prediction: next change fails fast

  Hypothesis: Small patches review better...
    Prediction: next review is quick

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit -1
============================================================
  Pending Predictions (2)
============================================================

  Hypothesis: Fast tests catch regressions...
    Prediction: next change fails fast

$ echo $?
0
```

Observed result: zero displays rows, and negative limits exit successfully. The pending header also reports the unbounded count while printing a sliced subset.

## Expected Behavior

Zero should show empty bounded views, and negative limits should fail cleanly:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit 0
============================================================
  Testable Hypotheses (0)
============================================================

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit 0
============================================================
  Pending Predictions (0)
============================================================

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit -1
[SPARK] hypothesis limit must be >= 0

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit -1
[SPARK] hypothesis limit must be >= 0
```

## Impact

- Agents cannot request a zero-row hypothesis proof window.
- Negative limits create misleading testable hypothesis and pending prediction evidence.
- Pending prediction output can disagree with its own header.

## Proposed Fix

Validate the shared testable helper and the pending display limit before slicing:

```python
limit = 5 if limit is None else int(limit)
if limit < 0:
    raise ValueError("hypothesis limit must be >= 0")
if limit == 0:
    return []
```

```python
limit = int(args.limit)
if limit < 0:
    raise SystemExit("[SPARK] hypothesis limit must be >= 0")
pending = tracker.get_pending_predictions()[:limit]
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-hypotheses-display-limit`
- Branch: `codex/fix-hypotheses-display-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-hypotheses-display-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-hypotheses-display-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-hypotheses-display-limit?expand=1
- Commit: `d4b2f66`
- Verification: `PYTHONPATH=. python -m pytest tests/test_hypotheses_display_limit.py -q` passed.
- Behavior check: isolated `HOME` hypotheses testable and pending views respect `--limit 0` and reject `--limit -1` with exit `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
