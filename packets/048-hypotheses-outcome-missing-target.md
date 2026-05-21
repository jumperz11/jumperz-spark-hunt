# Packet 048: Hypotheses Outcome Missing Target Reports Success

## Summary

`spark hypotheses --outcome missing:0 --correct` reports success and exits `0` when no matching hypothesis/prediction exists.

The same command path also returns success for malformed `--outcome` values and throws a traceback for non-integer prediction indexes.

## Mission Source

Spark Compete asks agents to exercise learning and validation loops. Hypothesis outcomes are explicit validation evidence, so missing or malformed targets must fail clearly instead of producing false success or tracebacks.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli hypotheses --outcome missing:0 --correct
[SPARK] Outcome recorded: correct
```

Observed result:

```text
exit=0
no hypothesis or prediction was updated
```

Malformed format:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli hypotheses --outcome badformat --correct
[SPARK] Invalid format. Use: --outcome <hypothesis_id>:<prediction_index>
```

Observed result:

```text
exit=0
```

Non-integer index:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli hypotheses --outcome missing:notint --correct
Traceback ...
ValueError: invalid literal for int() with base 10: 'notint'
```

## Expected Behavior

Missing targets should fail:

```text
exit=1
[SPARK] Hypothesis prediction not found: missing:0
```

Malformed formats and non-integer indexes should also exit `1` without tracebacks.

Valid hypothesis prediction outcomes should still record successfully.

## Impact

- Agents can report validation outcomes that were never persisted.
- Automation cannot distinguish missing targets from successful learning updates.
- Bad input can expose a Python traceback instead of a CLI-safe diagnostic.

## Proposed Fix

Make `HypothesisTracker.record_outcome()` return a boolean and make the CLI validate input:

```python
try:
    idx = int(parts[1])
except ValueError:
    print("[SPARK] Invalid prediction index. Use an integer index.")
    raise SystemExit(1)

if not tracker.record_outcome(h_id, idx, correct, args.notes or ""):
    print(f"[SPARK] Hypothesis prediction not found: {args.outcome}")
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-hypotheses-outcome-validation`
- Branch: `codex/fix-hypotheses-outcome-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-hypotheses-outcome-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-hypotheses-outcome-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-hypotheses-outcome-validation?expand=1
- Commit: `4be997d`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_hypotheses_outcome_validation.py tests/test_project_context.py -q` passed.
- Behavior check: missing hypothesis prediction targets now exit `1`.
- Behavior check: malformed outcome values now exit `1`.
- Behavior check: non-integer indexes now exit `1` with no traceback.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
