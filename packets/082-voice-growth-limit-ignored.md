# Packet 082: Voice Growth Limit Ignored

## Summary

`spark voice --growth` ignores explicit zero and accepts negative display limits when growth moments exist.

The CLI converts `--limit 0` into the default limit with `args.limit or 5`, and the voice store slices with `[-limit:]`, so a negative limit returns a misleading subset instead of failing.

## Mission Source

Spark Compete asks agents to inspect personality, learning, and proof surfaces. Voice growth moments are user-visible evidence that Spark changed behavior over time, so the view should respect bounded display limits.

## Before Evidence

Repro on upstream `main` with two seeded voice growth moments:

```console
$ PYTHONPATH=. python -m spark.cli voice --growth --limit 0
Growth Moments (2)

   Before: guess
   After: measure
   Trigger: first

   Before: skip tests
   After: run tests
   Trigger: second

$ PYTHONPATH=. python -m spark.cli voice --growth --limit -1
Growth Moments (1)

   Before: skip tests
   After: run tests
   Trigger: second

$ echo $?
0
```

Observed result: explicit zero still prints rows, and a negative limit exits successfully while showing an arbitrary slice.

## Expected Behavior

Zero should display no growth rows, and negative limits should fail cleanly:

```console
$ PYTHONPATH=. python -m spark.cli voice --growth --limit 0
Growth Moments (0)

$ PYTHONPATH=. python -m spark.cli voice --growth --limit -1
[SPARK] voice growth limit must be >= 0

$ echo $?
1
```

## Impact

- Agents cannot request an empty bounded proof window for voice growth.
- Negative limits produce misleading evidence instead of a validation error.
- The underlying `SparkVoice.get_recent_growth(0)` helper returns all rows because `[-0:]` is the full list.

## Proposed Fix

Validate the CLI limit before loading rows, preserve explicit zero, and make the store helper treat zero as an empty window:

```python
limit = int(args.limit)
if limit < 0:
    raise SystemExit("[SPARK] voice growth limit must be >= 0")
moments = voice.get_recent_growth(limit)
```

```python
limit = int(limit)
if limit < 0:
    raise ValueError("growth limit must be >= 0")
if limit == 0:
    return []
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-voice-growth-limit`
- Branch: `codex/fix-voice-growth-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-voice-growth-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-voice-growth-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-voice-growth-limit?expand=1
- Commit: `0fc2eac`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_voice_growth_limit.py -q` passed.
- Behavior check: seeded voice growth rows respect `--limit 0` and reject `--limit -1` with exit `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
