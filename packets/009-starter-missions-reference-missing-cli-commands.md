# Packet 009: Starter Missions Reference Missing CLI Commands

## Summary

Several Spark Compete starter missions reference `spark` CLI commands that are not exposed by the installed Spark CLI.

This sends teams toward command paths that fail before they can complete the mission.

## Surface

- Agent playbook starter missions
- Spark CLI
- First-run / provider / security / live-status workflows

## Before Evidence

Starter missions reference:

```text
spark smoke first-run
spark providers status
spark security audit
spark update
spark live status
```

Installed CLI rejects those top-level commands:

```text
spark: error: argument command: invalid choice: 'providers'
spark: error: argument command: invalid choice: 'smoke'
spark: error: argument command: invalid choice: 'live'
spark: error: argument command: invalid choice: 'security'
spark: error: argument command: invalid choice: 'update'
```

The currently exposed command list includes commands such as:

```text
os, status, services, up, ensure, down, sync, queue, process,
validate, learnings, promote, write, sync-context, health, events,
advisory, memory, project, chips
```

## Expected Behavior

Starter missions should either:

- reference commands that exist in the current public CLI,
- include the nearest current command beside legacy/future command names,
- or label future/planned commands clearly.

Example:

```text
Run `spark health` and `spark status` for first-run readiness.
If your build exposes `spark smoke first-run`, use that instead.
```

## Impact

- Teams lose time on command-not-found failures.
- Non-coder teammates may think their install is broken.
- Mission evidence gets noisy because teams must distinguish missing commands from actual runtime failures.

## Proposed Fix

Add a small command compatibility pass to the agent playbook generation:

```text
mission command -> current CLI command -> fallback command
```

For example:

- `spark smoke first-run` -> `spark health` / `spark status`
- `spark providers status` -> `spark memory --show` plus provider docs, or expose `providers`
- `spark live status` -> `spark services` / `spark status`
- `spark security audit` -> add command or change mission wording
- `spark update` -> add command or change mission wording

## Fix Branch

Prepared on the `jumperz11` fork, not opened upstream yet:

- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-mission-command-compat
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-mission-command-compat?expand=1
- Commit: `760d522 Add Spark Compete mission command compatibility`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_mission_compat.py -q` passed.
- Behavior check: `spark smoke first-run`, `spark providers status`, `spark live status`, `spark security audit`, and `spark update` now return read-only mission compatibility guidance instead of argparse invalid-choice errors.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
