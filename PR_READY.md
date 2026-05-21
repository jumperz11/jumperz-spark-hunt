# PR Ready Fixes

These are focused JUMPERZ fix branches prepared from confirmed Spark Compete packets.

## Upstream PR Audit

- No active upstream PRs are currently open for these JUMPERZ fix branches.
- Packet 001 previously had upstream PR https://github.com/vibeforge1111/vibeship-spark-intelligence/pull/183, now closed.
- Packets 002, 009, 020, 021, and 022 have fork branches ready but no upstream PRs yet.
- Open upstream PRs only after reviewer routing confirms the preferred owner surface, or if the Spark Compete organizers explicitly ask for direct PR submission.

## Recommended Submission Order

1. Packet 001: missing `spark os compile --json`; foundational agent-readiness fix.
2. Packet 021: missing-project handling for `spark os compile`; stacked follow-up after Packet 001.
3. Packet 002: CLI status/health mojibake; independent, low-risk output quality fix.
4. Packet 020: dead Pulse URL reporting; independent service-status correctness fix.
5. Packet 022: `spark opportunities` default crash; independent, low-risk CLI traceback fix.
6. Packet 009: mission command compatibility; high relevance to Spark Compete missions, broader command-surface change.

## Packet 001: Missing Spark OS Compile Command

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/HUNT_PROOF.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/spark-os-compile-command
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/spark-os-compile-command?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `00397b9 Add Spark OS compile command`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q`
- Behavior check: `spark os compile --json` emits `spark.os.compile.v1` with `authority`, `capability`, `gaps`, `memory`, `project`, `repo_board`, and `trace` sections.

Suggested PR title:

```text
Add Spark OS compile command
```

Suggested PR body:

```markdown
## Summary
- adds `spark os compile --json` as a safe discovery command for agents
- emits aggregate/redacted capability, authority, trace, memory, project, repo-board, and gap surfaces
- adds CLI coverage for the command and parser path

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/HUNT_PROOF.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q`
- `PYTHONPATH=. python -m spark.cli os compile --json`
```

## Packet 002: CLI Status/Health Mojibake

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/002-cli-status-health-mojibake.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-cli-status-mojibake
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-cli-status-mojibake?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `86fcfb8 Fix CLI status and health mojibake`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_status_health_output.py -q`
- Behavior check: `spark status` and `spark health` no longer contain `ðŸ`, `âœ`, or `Ã¢` in the reported status/health surfaces.

Suggested PR title:

```text
Fix CLI status and health mojibake
```

Suggested PR body:

```markdown
## Summary
- replaces corrupted status/health glyph strings with ASCII-safe markers
- keeps the fix scoped to the Spark CLI status and health surfaces
- adds regression coverage that rejects known mojibake markers

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/002-cli-status-health-mojibake.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_status_health_output.py -q`
- `PYTHONPATH=. python -m spark.cli status`
- `PYTHONPATH=. python -m spark.cli health`
```

## Packet 020: Services Advertises Dead Pulse URL

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/020-services-advertises-dead-pulse-url.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-pulse-service-status
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-pulse-service-status?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `05b8eab Fix Pulse service status URL reporting`
- Test: `PYTHONPATH=. python -m pytest tests/test_service_status_formatting.py -q`
- Behavior check: `spark services` now prints `Spark Pulse: unavailable (app.py missing)` when Pulse is stopped and the app file is missing.

Suggested PR title:

```text
Fix Pulse service status URL reporting
```

Suggested PR body:

```markdown
## Summary
- stops advertising the Spark Pulse URL when Pulse is stopped and `app.py` is missing
- labels stopped, missing, unhealthy, and healthy Pulse states distinctly
- adds focused formatter coverage for the missing-app case

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/020-services-advertises-dead-pulse-url.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_service_status_formatting.py -q`
- `PYTHONPATH=. python -m spark.cli services`
```

## Packet 009: Starter Missions Reference Missing CLI Commands

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/009-starter-missions-reference-missing-cli-commands.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-mission-command-compat
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-mission-command-compat?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `760d522 Add Spark Compete mission command compatibility`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_mission_compat.py -q`
- Behavior check: `spark smoke first-run`, `spark providers status`, `spark live status`, `spark security audit`, and `spark update` now return read-only compatibility guidance.

Suggested PR title:

```text
Add Spark Compete mission command compatibility
```

Suggested PR body:

```markdown
## Summary
- adds read-only compatibility guidance for Spark Compete starter mission commands
- covers `spark smoke first-run`, `spark providers status`, `spark live status`, `spark security audit`, and `spark update`
- keeps behavior safe: no destructive update/security actions, only current CLI surface guidance

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/009-starter-missions-reference-missing-cli-commands.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_mission_compat.py -q`
- `PYTHONPATH=. python -m spark.cli smoke first-run`
- `PYTHONPATH=. python -m spark.cli providers status`
- `PYTHONPATH=. python -m spark.cli live status`
- `PYTHONPATH=. python -m spark.cli security audit`
- `PYTHONPATH=. python -m spark.cli update`
```

## Packet 021: OS Compile Missing Project Traceback

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/021-os-compile-missing-project-traceback.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-os-compile-missing-project
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/spark-os-compile-command...codex/fix-os-compile-missing-project?expand=1
- Base: `jumperz11/vibeship-spark-intelligence:codex/spark-os-compile-command`
- Commit: `0c2a743 Handle missing Spark OS project paths`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q`
- Behavior check: missing `--project` exits `1`, emits structured JSON on stdout, and emits no Python traceback on stderr.

Important routing note:

Packet 021 is stacked on the Packet 001 OS compile command branch. Open it after Packet 001 is routed/accepted, or combine it only if reviewers ask for a bundled PR.

Suggested PR title:

```text
Handle missing Spark OS project paths
```

Suggested PR body:

```markdown
## Summary
- validates `spark os compile --project` paths before repo-board collection
- returns structured JSON errors for missing project paths in `--json` mode
- prevents Python tracebacks and empty stdout for a common typo path

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/021-os-compile-missing-project-traceback.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q`
- `PYTHONPATH=. python -m spark.cli os compile --json --project /tmp/spark-definitely-missing-project`
```

## Packet 022: Opportunities Default Subcommand Traceback

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/022-opportunities-default-subcommand-traceback.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-default
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-default?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `ced1136 Fix opportunities default command`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_opportunities.py -q`
- Behavior check: `spark opportunities` exits `0` and prints the opportunity inbox instead of raising `AttributeError: 'Namespace' object has no attribute 'limit'`.

Suggested PR title:

```text
Fix opportunities default command
```

Suggested PR body:

```markdown
## Summary
- makes `spark opportunities` default safely to the list view
- uses default list filters when no `opportunities list` subparser args are present
- adds regression coverage for the no-subcommand path

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/022-opportunities-default-subcommand-traceback.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_opportunities.py -q`
- `PYTHONPATH=. python -m spark.cli opportunities`
```
