# Packet 081: Surprises View Crashes On Persisted Rows

## Summary

`spark surprises --limit 1` crashes with `AttributeError` when the surprise store contains a persisted surprise row.

The tracker returns recent surprises as dictionaries, but the CLI calls `.format_visible()` as if each row were an `AhaMoment` object.

## Mission Source

Spark Compete asks agents to inspect learning and validation loops. Surprise rows are one of the clearest signals that Spark learned from unexpected outcomes, so the view should not crash when real surprise data exists.

## Before Evidence

Repro on upstream `main` with one seeded surprise row:

```console
$ PYTHONPATH=. python -m spark.cli surprises --limit 1
Traceback (most recent call last):
  File ".../spark/cli.py", line 3770, in main
    commands[args.command](args)
  File ".../spark/cli.py", line 1806, in cmd_surprises
    print(s.format_visible())
          ^^^^^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'format_visible'

Recent Surprises (showing 1)

$ echo $?
1
```

Observed result: the command prints the header, then crashes before showing the stored surprise.

## Expected Behavior

Persisted surprise rows should render like captured `AhaMoment` objects:

```console
$ PYTHONPATH=. python -m spark.cli surprises --limit 1
Recent Surprises (showing 1)

Surprise! Unexpected Success
   Expected: fail
   Got: pass
   Confidence gap: 80%
   Lesson: check row shape

$ echo $?
0
```

## Impact

- Agents cannot review stored surprise evidence once the file contains rows.
- Validation and prediction loops can write surprise rows that later break the CLI view.
- Reviewer proof for learning-from-surprise behavior becomes a traceback instead of evidence.

## Proposed Fix

Convert persisted dict rows back into `AhaMoment` before formatting:

```python
for s in surprises:
    if isinstance(s, dict):
        print(AhaMoment(**s).format_visible())
    else:
        print(s.format_visible())
```

This preserves object rows while supporting the existing persisted shape.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-surprises-row-format`
- Branch: `codex/fix-surprises-row-format`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-surprises-row-format
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-surprises-row-format
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-surprises-row-format?expand=1
- Commit: `62a4db8`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_surprises.py -q` passed.
- Behavior check: seeded persisted surprise row renders and exits `0`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
