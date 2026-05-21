# Packet 042: Missing Opportunities Exit Zero

## Summary

`spark opportunities accept <missing>` and `spark opportunities dismiss <missing>` print “not found” but exit with status `0`.

These are action commands. If the target opportunity cannot be resolved, scripts and agents need a non-zero exit code.

## Mission Source

Spark Compete asks agents to exercise opportunity and task-routing flows. False-success exit codes make automation believe an accept/dismiss action happened when nothing was changed.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark opportunities accept missing
[SPARK] Opportunity not found for id/prefix: missing
```

Observed result:

```text
exit=0
```

Second repro:

```console
$ HOME="$(mktemp -d)" spark opportunities dismiss missing
[SPARK] Opportunity not found for id/prefix: missing
```

Observed result:

```text
exit=0
```

`cmd_opportunities()` prints the not-found message and returns normally when `resolve_opportunity(prefix)` fails.

## Expected Behavior

Missing accept/dismiss targets should fail:

```text
exit=1
[SPARK] Opportunity not found for id/prefix: missing
```

List behavior should remain successful:

```text
spark opportunities list
```

## Impact

- Agents can report that an opportunity was accepted/dismissed when it was not found.
- Scripts cannot distinguish a missing target from a successful action.
- The action path violates normal CLI semantics for failed mutations.

## Proposed Fix

Exit non-zero when an accept/dismiss target does not resolve:

```python
row = resolve_opportunity(prefix)
if not row:
    print(f"[SPARK] Opportunity not found for id/prefix: {prefix}")
    raise SystemExit(1)
```

Keep list and successful action behavior unchanged.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-opportunities-missing-exit`
- Branch: `codex/fix-opportunities-missing-exit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-missing-exit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-opportunities-missing-exit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-missing-exit?expand=1
- Commit: `2c96c6e Return failure for missing opportunities`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_opportunities_missing_exit.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark opportunities accept missing` exits `1`.
- Behavior check: `HOME="$(mktemp -d)" spark opportunities dismiss missing` exits `1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
