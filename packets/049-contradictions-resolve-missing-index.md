# Packet 049: Contradictions Resolve Missing Index Reports Success

## Summary

`spark contradictions --resolve 0 --resolution-type update --resolution test` reports success and exits `0` when there are no contradictions to resolve.

The resolver silently ignores out-of-range indexes, but the CLI always prints “resolved.”

## Mission Source

Spark Compete asks agents to exercise validation, contradiction, and learning loops. Resolution commands should not claim a contradiction was resolved unless a target existed.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli contradictions --resolve 0 --resolution-type update --resolution test
[SPARK] Contradiction 0 resolved as: update
```

Observed result:

```text
exit=0
no contradiction existed
no resolution was persisted
```

`ContradictionDetector.resolve()` silently returned for out-of-range indexes, and `cmd_contradictions()` ignored that result.

## Expected Behavior

Missing contradiction indexes should fail:

```text
exit=1
[SPARK] Contradiction not found for index: 0
```

Existing contradiction indexes should still resolve successfully.

## Impact

- Agents can report that a contradiction was resolved when no target existed.
- Automation cannot distinguish missing indexes from successful resolution.
- Validation/learning workflows receive false progress signals.

## Proposed Fix

Return a boolean from the resolver and make the CLI exit non-zero when the index is missing:

```python
if not detector.resolve(idx, res_type, res):
    print(f"[SPARK] Contradiction not found for index: {idx}")
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-contradictions-resolve-validation`
- Branch: `codex/fix-contradictions-resolve-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-contradictions-resolve-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-contradictions-resolve-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-contradictions-resolve-validation?expand=1
- Commit: `3e27436`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_contradictions_resolve.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli contradictions --resolve 0 --resolution-type update --resolution test` exits `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
