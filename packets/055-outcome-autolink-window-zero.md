# Packet 055: Outcome Auto-Link Zero Window Still Links Exposures

## Summary

`spark outcome --auto-link --link-window-mins 0` records an outcome with recent `linked_insights`.

The command says the auto-link window is in minutes. An explicit zero-minute window should not link a previous exposure, and a negative window should not record an outcome.

## Mission Source

Spark Compete asks agents to exercise learning and outcome validation loops. Outcome records with `linked_insights` become validation evidence, so the auto-link window needs exact, predictable behavior.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "When deploy checks pass: keep rollback evidence attached because validation depends on explicit outcomes." --reliability 0.9
$ sleep 1
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins 0
[SPARK] Outcome recorded: success (polarity=pos)
```

Observed outcome row:

```json
{
  "text": "Deploy succeeded after a separate check",
  "linked_texts": [
    "When deploy checks pass: keep rollback evidence attached because validation depends on explicit outcomes."
  ],
  "linked_insights": [
    "wisdom:when_deploy_checks_pass:_keep_rollback_e"
  ]
}
```

Negative windows behave similarly:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins -1
[SPARK] Outcome recorded: success (polarity=pos)
```

Root cause:

```python
window_s = float(args.link_window_mins or 30) * 60
```

An explicit `0` becomes the default `30`, and negative windows fall through to the last-exposure fallback.

## Expected Behavior

`--link-window-mins 0` should still record the outcome but should not attach previous exposures:

```json
{
  "text": "Deploy succeeded after a separate check"
}
```

Negative windows should fail before recording:

```text
exit=1
[SPARK] Auto-link window must be zero or greater
```

Positive windows should continue linking recent exposures.

## Impact

- A zero-minute window creates validation evidence from older exposures.
- Negative windows can still record linked outcomes instead of failing.
- Agents cannot safely bound auto-linking when recording explicit outcomes.

## Proposed Fix

Preserve explicit zero, reject negative windows, and only use the last-exposure fallback when the requested window is positive:

```python
link_window_mins = float(args.link_window_mins if args.link_window_mins is not None else 30.0)
if link_window_mins < 0:
    raise SystemExit(1)
if window_s > 0:
    exposures = read_exposures_within(...)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-autolink-window`
- Branch: `codex/fix-outcome-autolink-window`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-autolink-window
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-autolink-window
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-autolink-window?expand=1
- Commit: `27ae56e`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_autolink_window.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins 0` records the outcome without `linked_insights`.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins 1` still records `linked_insights`.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins -1` exits `1` before creating `.spark`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
