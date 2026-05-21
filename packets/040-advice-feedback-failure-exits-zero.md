# Packet 040: Advice Feedback Failure Exits Zero

## Summary

`spark advice-feedback` with no target prints a failure message but exits with status `0`.

Because the command is meant to record feedback, a failed recording attempt should return non-zero so scripts and agents do not treat the operation as successful.

## Mission Source

Spark Compete asks agents to probe feedback and operational loops. Exit codes are part of the agent contract: a command that says it failed but exits successfully is hard for automation to handle correctly.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark advice-feedback
[SPARK] Advice feedback failed: Provide advice_id or tool
```

Observed result:

```text
exit=0
```

The CLI calls `record_advice_feedback()`, receives `{"status": "error", "message": "Provide advice_id or tool"}`, prints the failure, and then returns normally.

## Expected Behavior

Failed feedback recording should be machine-detectable:

```text
exit=1
[SPARK] Advice feedback failed: Provide advice_id or tool
```

Read-only inspection paths such as `spark advice-feedback --pending` should continue to exit `0`.

## Impact

- Scripts can treat a failed feedback record as successful.
- Agents may continue as if advice feedback was persisted when no target was provided.
- The command violates a basic CLI expectation: failure text should pair with a failure exit status.

## Proposed Fix

Raise `SystemExit(1)` when `record_advice_feedback()` returns an error:

```python
if result.get("status") == "ok":
    ...
else:
    print(f"[SPARK] Advice feedback failed: {result.get('message')}")
    raise SystemExit(1)
```

Keep successful recording and `--pending` behavior unchanged.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-advice-feedback-failure-exit`
- Branch: `codex/fix-advice-feedback-failure-exit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advice-feedback-failure-exit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-advice-feedback-failure-exit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advice-feedback-failure-exit?expand=1
- Commit: `2fd5e99 Return failure when advice feedback is not recorded`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_advice_feedback_exit.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark advice-feedback` exits `1` and prints the existing failure message.
- Control check: `HOME="$(mktemp -d)" spark advice-feedback --pending` still exits `0`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
