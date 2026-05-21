# Packet 045: Curiosity Fill Missing Gap Exits Zero

## Summary

`spark curiosity --fill missing --answer hello` reports that a missing gap was filled and exits `0`.

The underlying curiosity engine silently returns when the gap ID is not present, but the CLI always prints success. This is a deprecated command path, but it is still exposed by the CLI and can mislead agents that probe knowledge-gap workflows.

## Mission Source

Spark Compete missions ask agents to exercise gaps and learning flows. Even deprecated command paths should not claim a mutation succeeded when no target was found.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -W ignore::DeprecationWarning -m spark.cli curiosity --fill missing --answer hello
[SPARK] Gap missing filled. Valuable: True
```

Observed result:

```text
exit=0
no gap was actually filled
```

`CuriosityEngine.fill_gap()` returned silently when the ID was absent, and `cmd_curiosity()` ignored that outcome.

## Expected Behavior

Missing gap IDs should fail:

```text
exit=1
[SPARK] Gap not found for id: missing
```

Existing gap IDs should continue to fill successfully.

## Impact

- Agents can report that a knowledge gap was filled when nothing changed.
- Scripts cannot distinguish a missing gap from a successful fill.
- The command contradicts normal mutation-command semantics.

## Proposed Fix

Return a boolean from `fill_gap()` and make the CLI exit non-zero when it returns `False`:

```python
filled = engine.fill_gap(gap_id, answer, valuable)
if not filled:
    print(f"[SPARK] Gap not found for id: {gap_id}")
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-curiosity-fill-missing-gap`
- Branch: `codex/fix-curiosity-fill-missing-gap`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-curiosity-fill-missing-gap
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-curiosity-fill-missing-gap
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-curiosity-fill-missing-gap?expand=1
- Commit: `b579d25`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_curiosity_fill.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" PYTHONPATH=. python -W ignore::DeprecationWarning -m spark.cli curiosity --fill missing --answer hello` exits `1`.
- Behavior check: existing gap fills still report success.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
