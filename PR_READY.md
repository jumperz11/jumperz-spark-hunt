# PR Ready Fixes

These are focused JUMPERZ fix branches prepared from confirmed Spark Compete packets.

## Upstream PR Audit

- No active upstream PRs are currently open for these JUMPERZ fix branches.
- Packet 001 previously had upstream PR https://github.com/vibeforge1111/vibeship-spark-intelligence/pull/183, now closed.
- Packets 002, 009, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, and 032 have fork branches ready but no upstream PRs yet.
- Open upstream PRs only after reviewer routing confirms the preferred owner surface, or if the Spark Compete organizers explicitly ask for direct PR submission.

## Recommended Submission Order

1. Packet 001: missing `spark os compile --json`; foundational agent-readiness fix.
2. Packet 021: missing-project handling for `spark os compile`; stacked follow-up after Packet 001.
3. Packet 002: CLI status/health mojibake; independent, low-risk output quality fix.
4. Packet 020: dead Pulse URL reporting; independent service-status correctness fix.
5. Packet 022: `spark opportunities` default crash; independent, low-risk CLI traceback fix.
6. Packet 023: `spark outcome` non-interactive write; independent outcome-data safety fix.
7. Packet 024: `spark memory` missing config crash; independent first-run setup fix.
8. Packet 025: `spark project` missing path writes context; independent project-path validation fix.
9. Packet 026: `spark status` writes project context; independent read-only status fix.
10. Packet 027: `spark memory-purge-telemetry --dry-run` writes a store; independent dry-run safety fix.
11. Packet 028: `spark eidos-purge-telemetry --dry-run` writes a store; independent dry-run safety fix.
12. Packet 029: `spark eidos --stats` writes a store; independent read-only stats fix.
13. Packet 030: `spark eidos --validate-migration` writes a store; independent validation safety fix.
14. Packet 031: EIDOS list views write a store; independent read-only list fix.
15. Packet 032: `spark eidos --metrics` writes a store; independent read-only metrics fix.
16. Packet 009: mission command compatibility; high relevance to Spark Compete missions, broader command-surface change.

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

## Packet 023: Outcome Command Records Unknown In Non-Interactive Mode

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/023-outcome-noninteractive-records-unknown.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-noninteractive
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-noninteractive?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `a23d2c0 Avoid recording outcome when stdin closes`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_outcome.py -q`
- Behavior check: `spark outcome </dev/null` exits `0`, prints `Outcome not recorded`, and does not create `~/.spark/outcomes.jsonl`; explicit `--result yes` still records one positive outcome.

Suggested PR title:

```text
Avoid recording outcome when stdin closes
```

Suggested PR body:

```markdown
## Summary
- prevents `spark outcome` from recording an `unknown` negative row when stdin closes
- tells non-interactive callers to pass an explicit `--result`
- adds regression coverage for closed stdin and explicit result recording

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/023-outcome-noninteractive-records-unknown.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_outcome.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome </dev/null`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result yes --text worked --tool pytest`
```

## Packet 024: Memory Config Missing Traceback

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/024-memory-config-missing-traceback.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-memory-config-missing
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-memory-config-missing?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `8173558 Handle missing Clawdbot memory config`
- Test: `PYTHONPATH=. python -m pytest tests/test_clawdbot_memory_setup.py -q`
- Behavior check: `spark memory --show` in a fresh `HOME` prints `(not set)`; `spark memory --set off --no-restart` creates `~/.clawdbot/clawdbot.json` instead of raising `FileNotFoundError`.

Suggested PR title:

```text
Handle missing Clawdbot memory config
```

Suggested PR body:

```markdown
## Summary
- treats missing Clawdbot config as an empty memorySearch configuration
- creates the config parent directory before saving memorySearch settings
- adds regression coverage for fresh-environment show and set paths

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/024-memory-config-missing-traceback.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_clawdbot_memory_setup.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli memory --show`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli memory --set off --no-restart`
```

## Packet 025: Project Missing Path Writes Context

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/025-project-missing-path-writes-context.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-missing-path
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-missing-path?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `4492c40 Reject missing project paths in CLI`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_project.py -q`
- Behavior check: `spark project status --project <missing-path>` exits `1`, prints `Project path not found`, and writes no `~/.spark` files.

Suggested PR title:

```text
Reject missing project paths in CLI
```

Suggested PR body:

```markdown
## Summary
- validates explicit `spark project --project` paths before loading project profile/context
- rejects missing paths and non-directory paths with a clear CLI message
- adds regression coverage for missing and existing explicit project paths

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/025-project-missing-path-writes-context.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_project.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project status --project /tmp/spark-definitely-missing-project`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project status --project "$(mktemp -d)"`
```

## Packet 026: Status Writes Project Context

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/026-status-writes-project-context.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-status-readonly-context
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-status-readonly-context?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `f6123d2 Keep status project context read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_project_context.py -q`
- Behavior check: `spark status` in a fresh `HOME` exits `0` and creates no `~/.spark` files.

Suggested PR title:

```text
Keep status project context read-only
```

Suggested PR body:

```markdown
## Summary
- keeps `spark status` from writing project-context cache files
- makes `get_project_context(..., use_cache=False)` genuinely read-only
- threads the read-only option through profile/domain loading for status display

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/026-status-writes-project-context.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli status`
```

## Packet 027: Memory Purge Dry Run Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/027-memory-purge-dry-run-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-memory-purge-dry-run
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-memory-purge-dry-run?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `cb31a03 Keep memory purge dry run read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_memory_purge_telemetry.py -q`
- Behavior check: `spark memory-purge-telemetry --dry-run` in a fresh `HOME` exits `0` and creates no `~/.spark` files; non-dry-run mode still creates/uses the memory store.

Suggested PR title:

```text
Keep memory purge dry run read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark memory-purge-telemetry --dry-run` from creating the memory store in fresh environments
- reads an existing memory store through a read-only SQLite connection during dry runs
- adds regression coverage for missing-store and existing-store dry-run behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/027-memory-purge-dry-run-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_memory_purge_telemetry.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli memory-purge-telemetry --dry-run`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli memory-purge-telemetry`
```

## Packet 028: EIDOS Purge Dry Run Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/028-eidos-purge-dry-run-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-purge-dry-run
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-purge-dry-run?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `3af6e4d Keep EIDOS purge dry run read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_purge_telemetry.py -q`
- Behavior check: `spark eidos-purge-telemetry --dry-run` in a fresh `HOME` exits `0` and creates no `~/.spark` files; non-dry-run mode still creates/uses the EIDOS store.

Suggested PR title:

```text
Keep EIDOS purge dry run read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos-purge-telemetry --dry-run` from creating the EIDOS store in fresh environments
- returns empty dry-run stats before constructing the default store when no database exists
- adds regression coverage for missing-store and existing-store dry-run behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/028-eidos-purge-dry-run-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_purge_telemetry.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos-purge-telemetry --dry-run`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos-purge-telemetry`
```

## Packet 029: EIDOS Stats Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/029-eidos-stats-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-stats-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-stats-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `d68c846 Keep EIDOS stats read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_stats_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `spark eidos --stats` in a fresh `HOME` exits `0` and creates no `~/.spark/eidos.db`; plain `spark eidos` overview also stays read-only.

Suggested PR title:

```text
Keep EIDOS stats read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --stats` from creating the EIDOS store in fresh environments
- reads existing EIDOS stats through a read-only SQLite connection
- adds CLI regression coverage for fresh-home stats behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/029-eidos-stats-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_stats_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --stats`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos`
```

## Packet 030: EIDOS Validate Migration Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/030-eidos-validate-migration-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-validate-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-validate-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `e7f9517 Keep EIDOS migration validation read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_validate_migration_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `spark eidos --validate-migration` in a fresh `HOME` exits `0`, prints `Tables exist: False`, and creates no `~/.spark/eidos.db`.

Suggested PR title:

```text
Keep EIDOS migration validation read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --validate-migration` from creating the EIDOS store in fresh environments
- reports missing EIDOS tables accurately when no migration database exists
- reads existing migration stats through a read-only SQLite connection

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/030-eidos-validate-migration-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_validate_migration_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --validate-migration`
```

## Packet 031: EIDOS List Views Create Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/031-eidos-list-views-create-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-list-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-list-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `f157ea1 Keep EIDOS list views read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_list_views_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `--episodes`, `--distillations`, `--distillations --type heuristic`, `--policies`, `--steps`, and `--episode missing-episode` each exit `0` in a fresh `HOME` and create no files.

Suggested PR title:

```text
Keep EIDOS list views read-only
```

Suggested PR body:

```markdown
## Summary
- prevents EIDOS list views from creating the EIDOS store in fresh environments
- returns empty list output without initializing schema when no store exists
- adds CLI regression coverage for episodes, distillations, policies, and steps list views

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/031-eidos-list-views-create-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_list_views_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --episodes`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --distillations`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --policies`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --steps`
```

## Packet 032: EIDOS Metrics Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/032-eidos-metrics-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-metrics-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-metrics-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `b750cb4 Keep EIDOS metrics read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_metrics_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `spark eidos --metrics` in a fresh `HOME` exits `0`, prints the zero metrics report, and creates no files.

Suggested PR title:

```text
Keep EIDOS metrics read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --metrics` from creating the EIDOS store in fresh environments
- returns the zero metrics report without opening SQLite when no store exists
- adds CLI regression coverage for fresh-home metrics behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/032-eidos-metrics-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_metrics_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --metrics`
```
