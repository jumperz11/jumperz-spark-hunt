# Packet 036: Advisory Setup Writes Defaults Non-Interactively

## Summary

`spark advisory` defaults to guided setup, but when run without a TTY it silently accepts the current defaults and writes `~/.spark/tuneables.json` plus `~/.spark/advice_packets/index.json`.

Non-interactive probes should not persist advisory preferences unless the caller uses an explicit write command such as `spark advisory set` or `spark advisory on`.

## Mission Source

Spark Compete asks agents to run missions and inspect command surfaces. Agents commonly execute CLI commands non-interactively, so a prompt-driven setup path that auto-selects defaults and writes state is a high-signal first-run safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark advisory

How much should Spark use past outcomes to suggest alternatives?
  1. Standard (Recommended) (current)
     Shows replay alternatives only when evidence is strong.
  2. Off
     Disables replay/counterfactual advisories.
  3. Replay-heavy
     Surfaces more historical alternatives with lower trigger threshold.

How verbose should advisory guidance be?
  1. Balanced (Recommended) (current)
     Mix of concise warnings and deeper actionable guidance.
  2. Concise
     Fewer advisories, higher rank threshold.
  3. Coach
     More guidance depth and alternatives per step.
[SPARK] Advisory Preferences
  advisory_on: yes
  advisory_runtime: up
  replay_advisory: on
  memory_mode: standard
  guidance_style: balanced
```

Observed result:

```text
exit=0
~/.spark/advice_packets/index.json is created
~/.spark/tuneables.json is created
```

`_pick_advisory_option()` returns the default option when `stdin` is not a TTY, then `cmd_advisory()` applies those defaults through `apply_advisory_preferences()`.

## Expected Behavior

Non-interactive guided setup should make no changes:

```text
exit=0
[SPARK] Advisory setup requires an interactive terminal. No changes made.
no ~/.spark/tuneables.json created
no ~/.spark/advice_packets/index.json created
```

Explicit write commands should continue to work:

```text
spark advisory set
spark advisory on
spark advisory off
```

## Impact

- Agent discovery can mutate first-run advisory state accidentally.
- CI or scripted probes can commit local preference files before the user has made a choice.
- The command looks like an interactive setup but behaves like an implicit write in non-interactive mode.

## Proposed Fix

Guard the `setup` path before asking questions or applying preferences:

```python
if advisory_cmd == "setup":
    if not sys.stdin.isatty():
        print("[SPARK] Advisory setup requires an interactive terminal. No changes made.")
        print("Use `spark advisory set` or `spark advisory on` to apply preferences non-interactively.")
        return
```

Keep explicit non-interactive commands unchanged.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-advisory-noninteractive`
- Branch: `codex/fix-advisory-noninteractive`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advisory-noninteractive
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-advisory-noninteractive
- Commit: `5a1c9e2 Keep advisory setup noninteractive read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_advisory_noninteractive.py tests/test_advisory_preferences.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark advisory` exits `0` and creates no files.
- Control check: `HOME="$(mktemp -d)" spark advisory set` still creates the expected advisory preference files.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
