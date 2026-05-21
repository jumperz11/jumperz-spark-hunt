# Packet 074: Events Limit Ignored

## Summary

`spark events --limit 0` ignores the explicit zero and prints recent queue events. `spark events --limit -1` exits successfully with a misleading zero-event view.

The command is a raw event evidence surface, so display bounds should be respected exactly.

## Mission Source

Spark Compete asks agents to inspect operational and learning traces. The events view is one of the first surfaces an agent uses to prove what happened, so malformed display limits should not return false-success diagnostics.

## Before Evidence

Repro on upstream `main` with an isolated home and two queued events:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit 0

[events] Recent Events (showing 2 of 2)

[user_prompt]
[error] ERROR: boom...

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit -1

[events] Recent Events (showing 0 of 2)

$ echo $?
0
```

Observed result: zero is converted to the default limit, and negative limits return success.

## Expected Behavior

- `--limit 0` should display zero event rows.
- Negative limits should exit non-zero.
- Positive limits should keep showing the requested number of recent events.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit -1
[SPARK] Events limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit 0

[events] Recent Events (showing 0 of 2)

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit 1

[events] Recent Events (showing 1 of 2)

[error] ERROR: boom...
```

## Impact

- Agents cannot safely request a zero-row event metadata probe.
- Negative limits produce successful but misleading output.
- Reviewer proof can accidentally expose more event content than requested.

## Proposed Fix

Validate display limits before reading recent events:

```python
limit = int(args.limit)
if limit < 0:
    print("[SPARK] Events limit must be zero or greater")
    sys.exit(1)
events = [] if limit == 0 else read_recent_events(limit)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-events-limit-validation`
- Branch: `codex/fix-events-limit-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-events-limit-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-events-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-events-limit-validation?expand=1
- Commit: `edb35f0`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_events_limit.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows no rows for `--limit 0`, and shows one recent event for `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
