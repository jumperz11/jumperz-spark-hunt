# Packet 046: Chips Missing Targets Exit Zero

## Summary

Target-specific `spark chips` commands print not-found messages but exit `0`.

Examples include `spark chips activate missing`, `spark chips deactivate missing`, and `spark chips status missing`. These commands report failure in text, but automation sees success.

## Mission Source

Spark Compete starter missions reference chip and project-understanding flows. Agents need reliable exit codes when probing chip install/activation surfaces.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli chips activate missing
[SPARK] Chip not found: missing
```

Observed result:

```text
exit=0
```

Second repro:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli chips status missing
[SPARK] Chip not found: missing
```

Observed result:

```text
exit=0
```

The same false-success pattern applied across missing chip targets and missing required chip IDs.

## Expected Behavior

Target-specific failures should exit non-zero:

```text
exit=1
[SPARK] Chip not found: missing
```

Read-only aggregate views should remain successful:

```text
spark chips list
spark chips status
spark chips questions
```

## Impact

- Agents can believe a chip was activated, deactivated, tested, or inspected when the target was missing.
- Scripts cannot distinguish missing chip IDs from successful command execution.
- Competition mission flows that probe chips get misleading success signals.

## Proposed Fix

Centralize target failures in `cmd_chips()` and raise `SystemExit(1)` for missing required IDs, missing files, failed installs, not-found chips, and unknown chip actions.

The patch also validates `spark chips insights <id>` against the installed chip registry so missing IDs no longer masquerade as an empty-insights state.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-chips-missing-target-exits`
- Branch: `codex/fix-chips-missing-target-exits`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-chips-missing-target-exits
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-chips-missing-target-exits
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-chips-missing-target-exits?expand=1
- Commit: `e0949b0`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_chips_missing_targets.py tests/test_chips_runtime_filters.py -q` passed.
- Behavior check: `spark chips activate missing` exits `1`.
- Behavior check: `spark chips status missing` exits `1`.
- Behavior check: `spark chips insights <existing-empty-chip>` still exits `0` with the no-insights message.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
