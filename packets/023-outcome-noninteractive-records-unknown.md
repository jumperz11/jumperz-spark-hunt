# Packet 023: Outcome Command Records Unknown In Non-Interactive Mode

## Summary

`spark outcome` records an `unknown` negative outcome when stdin closes before an outcome is provided.

The command prompts for `yes/no/partial`, catches the input failure, substitutes `unknown`, and appends a durable outcome row. A read-only agent probe can therefore pollute outcome stats without any user-provided result.

## Mission Source

Spark Compete rewards real workflow bugs that affect agent operation. Outcome capture feeds Spark's learning and scoring loops, so accidental writes from non-interactive CLI probes are high-signal.

## Before Evidence

Read-only repro on upstream `main` using an isolated home directory:

```console
$ HOME="$(mktemp -d)" spark outcome </dev/null
Outcome (yes/no/partial): Notes (optional): [SPARK] Outcome recorded: unknown (polarity=neg)
```

Observed result:

```text
exit=0
~/.spark/outcomes.jsonl contains one explicit_checkin row
result=unknown
polarity=neg
```

## Expected Behavior

If no result is provided and stdin is closed, Spark should not append an outcome. It should tell the caller how to provide an explicit result:

```console
$ spark outcome </dev/null
Outcome (yes/no/partial): [SPARK] Outcome not recorded: pass --result yes|no|partial or run interactively.
```

Explicit command usage should continue to work:

```console
$ spark outcome --result yes --text worked --tool pytest
[SPARK] Outcome recorded: yes (polarity=pos)
```

## Impact

- Non-interactive agents can corrupt outcome statistics while merely exploring the CLI.
- A missing input is treated as a negative result, which can bias learning/effectiveness metrics.
- The command performs a durable write without a real user outcome.

## Proposed Fix

When `input()` raises `EOFError` or the result remains blank, return without writing:

```python
try:
    result = input("Outcome (yes/no/partial): ").strip()
except (EOFError, KeyboardInterrupt):
    print("[SPARK] Outcome not recorded: pass --result yes|no|partial or run interactively.")
    return
if not result:
    print("[SPARK] Outcome not recorded: pass --result yes|no|partial or run interactively.")
    return
```

Add regression coverage for the closed-stdin path and for explicit `--result` recording.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-noninteractive`
- Branch: `codex/fix-outcome-noninteractive`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-noninteractive
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-noninteractive
- Commit: `a23d2c0 Avoid recording outcome when stdin closes`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_outcome.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark outcome </dev/null` exits `0` and does not create `~/.spark/outcomes.jsonl`.
- Control check: `spark outcome --result yes --text worked --tool pytest` still records one positive outcome.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
