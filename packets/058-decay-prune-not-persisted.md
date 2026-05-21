# Packet 058: Decay Prune Reports Success But Leaves Insight On Disk

## Summary

`spark decay --apply` reports that stale insights were pruned, but the deleted insight remains in `~/.spark/cognitive_insights.json`.

The in-memory map removes the key, then the save path reloads disk and merges the same key back because pruning does not use the deletion-aware save path.

## Mission Source

Spark Compete asks agents to exercise learning, validation, and maintenance workflows. Decay pruning is a destructive maintenance command, so a false success message is high-signal: operators believe stale low-reliability memory was removed when it was not.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "Always validate payload contracts before rollout" --reliability 0.1

âœ“ Learned [wisdom]: Always validate payload contracts before rollout
  Reliability: 10%

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 0.2
[SPARK] Pruned 1 stale insights
```

Observed result:

```text
exit=0
~/.spark/cognitive_insights.json still contains wisdom:always_validate_payload_contracts_before
```

## Expected Behavior

When the command reports `Pruned 1 stale insights`, the matching key should also be removed from `cognitive_insights.json`.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 0.2
[SPARK] Pruned 1 stale insights
$ cat "$tmp/.spark/cognitive_insights.json"
{}
```

## Impact

- The CLI reports a destructive cleanup that did not actually persist.
- Stale low-reliability insights remain available to later retrieval/promotion paths.
- Operators and automation cannot trust the prune count as evidence of cleanup.

## Root Cause

`CognitiveLearner.prune_stale()` deletes keys from `self.insights`, then calls `_save_insights()` without `drop_keys`. The save implementation reloads disk first and merges in-memory insights into that disk map, so deleted keys can be resurrected from the pre-prune file.

## Proposed Fix

Use the existing deletion-aware save path:

```python
if to_delete:
    self._save_insights(drop_keys=set(to_delete))
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-decay-prune-persistence`
- Branch: `codex/fix-decay-prune-persistence`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-decay-prune-persistence
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-decay-prune-persistence
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-decay-prune-persistence?expand=1
- Commit: `7e7a30c`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cognitive_decay_prune.py tests/test_cognitive_learner.py -q` passed.
- Behavior check: `HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 0.2` reports one prune and leaves `cognitive_insights.json` as `{}` after the matching low-reliability insight is removed.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
