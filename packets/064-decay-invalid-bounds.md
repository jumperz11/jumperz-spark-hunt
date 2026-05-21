# Packet 064: Decay Accepts Invalid Bounds

## Summary

`spark decay` accepts invalid pruning bounds and can report stale-prune success for recent insights.

Passing `--max-age-days -1` should fail before pruning, but upstream accepts it and enters the prune path. Out-of-range `--min-effective` values and negative dry-run limits are also accepted.

## Mission Source

Spark Compete asks agents to exercise learning and validation loops with clean proof. Decay pruning is a destructive learning-state maintenance command, so invalid bounds should never reach the mutation path.

## Before Evidence

Repro on upstream `main` with an isolated home and one recent low-reliability insight:

```console
$ tmp="$(mktemp -d)"
$ mkdir -p "$tmp/.spark"
$ cat > "$tmp/.spark/cognitive_insights.json" <<EOF
{"wisdom:recent_low":{"category":"wisdom","insight":"Recent low reliability insight","evidence":["seed"],"confidence":0.1,"context":"seed","counter_examples":[],"created_at":"2026-05-20T19:01:29","times_validated":0,"times_contradicted":0,"promoted":false}}
EOF
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days -1 --min-effective 0.2
[SPARK] Pruned 1 stale insights
$ echo "$?"
0
```

Observed result:

```text
negative max age is accepted
decay enters the destructive prune path
command exits successfully
```

The existing persistence bug from Packet 058 can leave the pruned key on disk, but this packet is separate: invalid pruning bounds should be rejected before any prune attempt.

## Expected Behavior

- Reject negative `--max-age-days` values.
- Reject `--min-effective` values below `0` or above `1`.
- Reject negative dry-run `--limit` values.
- Validate before loading the cognitive learner or touching Spark state.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days -1 --min-effective 0.2
[SPARK] Max age days must be zero or greater

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 2
[SPARK] Min effective reliability must be between 0 and 1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --max-age-days 0 --min-effective 0.2 --limit -1
[SPARK] Decay limit must be zero or greater
```

All invalid invocations exit with status `1` and leave `cognitive_insights.json` unchanged.

## Impact

- Recent learnings can be routed into a destructive prune path by invalid age input.
- Automation sees invalid decay commands as successful.
- Reviewer/proof runs cannot distinguish a legitimate prune from malformed bounds.

## Proposed Fix

Validate decay CLI bounds before loading the cognitive learner:

```python
if max_age_days < 0:
    raise SystemExit(1)
if min_effective < 0.0 or min_effective > 1.0:
    raise SystemExit(1)
if limit < 0:
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-decay-input-validation`
- Branch: `codex/fix-decay-input-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-decay-input-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-decay-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-decay-input-validation?expand=1
- Commit: `7253936`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_decay_input_validation.py tests/test_cognitive_learner.py -q` passed.
- Behavior check: isolated `HOME` rejects invalid decay bounds and preserves the seeded `cognitive_insights.json` hash.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
