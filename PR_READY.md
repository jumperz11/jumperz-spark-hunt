# PR Ready Fixes

These are focused JUMPERZ fix branches prepared from confirmed Spark Compete packets.

## Upstream PR Audit

- No active upstream PRs are currently open for these JUMPERZ fix branches.
- Packet 001 previously had upstream PR https://github.com/vibeforge1111/vibeship-spark-intelligence/pull/183, now closed.
- Packets 002, 009, and 020-086 have fork branches ready but no upstream PRs yet.
- Open upstream PRs only after reviewer routing confirms the preferred owner surface, or if the Spark Compete organizers explicitly ask for direct PR submission.

## Spark Compete Packet Routing Note

The Spark Compete site currently requires complete `spark-compete-hotfix-v1` JSON in every new PR body. Because `vibeforge1111/vibeship-spark-intelligence` is not listed in `/allowed-repos.json`, the top review queue is prepared as `reviewer_routed_packet` material until reviewers confirm a direct PR lane.

The reviewer-routed schema accepts only a `vibeforge1111/Spark-Agent-Site` issue or PR URL as the public intake surface. The packets below use `https://github.com/vibeforge1111/Spark-Agent-Site/issues/184` as the schema-shaped reviewer intake URL to replace if reviewers assign a different Spark-Agent-Site routing issue. Do not open upstream PRs until that routing path is confirmed.

## Recommended Submission Order

Use this order for reviewer scoring. It matches `TOP_REVIEW_QUEUE.md` and prioritizes the first 10 schema-ready reviewer-routed packets.

1. Packet 001: missing `spark os compile --json`; foundational agent-readiness fix.
2. Packet 021: missing-project handling for `spark os compile`; stacked follow-up after Packet 001.
3. Packet 009: mission command compatibility; directly tied to Spark Compete starter mission command friction.
4. Packet 022: `spark opportunities` default crash; independent, low-risk CLI traceback fix.
5. Packet 040: `spark advice-feedback` failed recording exits zero; independent CLI automation fix.
6. Packet 041: `spark capture --list/--reject` ignored; independent CLI review-loop fix.
7. Packet 042: missing `spark opportunities accept/dismiss` exits zero; independent CLI automation fix.
8. Packet 043: `spark outcome-link` accepts invalid targets; independent outcome-validation safety fix.
9. Packet 048: `spark hypotheses --outcome` reports false success; independent validation-loop fix.
10. Packet 049: `spark contradictions --resolve` reports false success; independent validation-loop fix.

Next clean batch after reviewer routing clears the first 10:

11. Packet 063: `spark process` invalid runtime limits; independent bridge-worker mutation safety fix.
12. Packet 065: `spark validate-ingest` negative limit traceback; independent ingest-diagnostic hardening fix.
13. Packet 081: `spark surprises` crashes on persisted surprise rows; independent learning-evidence display fix.
14. Packet 078: `spark sync-context --limit -1` writes exports; independent bootstrap-context safety fix.
15. Packet 080: `spark eidos` list views ignore zero and negative display limits; independent decision-packet evidence display fix.

Remaining PR-ready branches stay documented below for later routing, but the goal now is reviewer clarity and acceptance for the first batch rather than more packet volume.

## Packet Validation Status

Validated against `https://compete.sparkswarm.ai/api/packet/validate` on 2026-05-25 after adding the required `spark-compete-hotfix-v1` JSON blocks.

- Packets 001, 021, 009, 040, 041, 042, 043, 048, and 049 returned `pass`.
- Packet 022 returned `pass_with_warnings` with `packet_valid: true` and `security_owner_review_expected`; keep it in the queue, but expect reviewer/lab confirmation before points unlock.

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
[spark-compete] Add Spark OS compile command
```

Suggested PR body:

````markdown
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

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "Missing safe Spark OS compile command for agent discovery",
    "actual_behavior": "Spark agents have no safe aggregate command that exposes public-safe capability, authority, trace, memory, project, repo-board, and gap surfaces for owner routing.",
    "expected_behavior": "Spark should provide a safe read-only compile command so agents can inspect the system without exposing private repo maps or raw memory.",
    "repro_steps": [
      "Install or open the Spark CLI checkout.",
      "Try to run spark os compile --json.",
      "Observe that the public-safe aggregate discovery command is missing before this branch."
    ],
    "affected_workflow": "Spark agent system discovery and owner routing"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: spark os compile --json was missing. After: the branch emits spark.os.compile.v1 with authority, capability, gaps, memory, project, repo_board, and trace sections plus CLI test coverage.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/HUNT_PROOF.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/spark-os-compile-command?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/spark-os-compile-command"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Add a read-only Spark OS compile command that returns redacted aggregate discovery surfaces for agents.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_os.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_os.py -q; PYTHONPATH=. python -m spark.cli os compile --json"
  },
  "pr": {
    "branch": "codex/spark-os-compile-command",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

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
[spark-compete] Add Spark Compete mission command compatibility
```

Suggested PR body:

````markdown
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

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "usage_friction",
    "severity": "medium",
    "title": "Starter missions reference missing Spark CLI commands",
    "actual_behavior": "Several Spark Compete starter mission commands fail as invalid choices even though the public site tells teams to try them.",
    "expected_behavior": "Referenced starter mission commands should return safe read-only compatibility guidance or a clear equivalent command path.",
    "repro_steps": [
      "Read the Spark Compete starter missions.",
      "Run spark smoke first-run, spark providers status, spark live status, spark security audit, or spark update.",
      "Observe invalid-choice failures before this branch."
    ],
    "affected_workflow": "Spark Compete starter mission onboarding"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: site-referenced starter commands returned argparse invalid-choice failures. After: the branch returns read-only compatibility guidance for the referenced command paths.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/009-starter-missions-reference-missing-cli-commands.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-mission-command-compat?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-mission-command-compat"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Add safe compatibility shims for the site-referenced starter mission commands without performing destructive update or security actions.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_mission_compat.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_mission_compat.py -q"
  },
  "pr": {
    "branch": "codex/fix-mission-command-compat",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

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
[spark-compete] Handle missing Spark OS project paths
```

Suggested PR body:

````markdown
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

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "Spark OS compile traceback on missing project path",
    "actual_behavior": "spark os compile --project with a missing path can emit a Python traceback or empty stdout instead of structured failure output.",
    "expected_behavior": "Missing project paths should exit non-zero with structured JSON and no traceback so agents can recover safely.",
    "repro_steps": [
      "Start from the Packet 001 OS compile command branch.",
      "Run spark os compile --json --project against a missing path.",
      "Observe traceback or unsafe empty output before this hardening branch."
    ],
    "affected_workflow": "Spark OS compile project inspection"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: missing --project path produced traceback/empty output. After: the branch exits 1 with structured JSON on stdout and no Python traceback on stderr.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/021-os-compile-missing-project-traceback.md",
      "https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/spark-os-compile-command...codex/fix-os-compile-missing-project?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-os-compile-missing-project",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/spark-os-compile-command?expand=1"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Validate project paths before repo-board collection and return a structured error when the path is missing.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_os.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_os.py -q"
  },
  "pr": {
    "branch": "codex/fix-os-compile-missing-project",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

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
[spark-compete] Make spark opportunities show a safe default view
```

Suggested PR body:

````markdown
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

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark opportunities default subcommand traceback",
    "actual_behavior": "Running spark opportunities without a subcommand can traceback instead of showing a safe opportunities inbox view.",
    "expected_behavior": "spark opportunities should default to a safe read-only list/inbox view or a clear usage response.",
    "repro_steps": [
      "Run spark opportunities with no subcommand.",
      "Observe the traceback before this branch.",
      "Run the branch and confirm it shows a safe default opportunities view."
    ],
    "affected_workflow": "Spark opportunities CLI workflow"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: spark opportunities could traceback without a subcommand. After: the branch routes the command to a safe default inbox view with focused test coverage.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/022-opportunities-default-subcommand-traceback.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-default?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-default"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Wire the parent opportunities command to a safe default display path instead of falling through to a traceback.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_opportunities.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_opportunities.py -q"
  },
  "pr": {
    "branch": "codex/fix-opportunities-default",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

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

## Packet 033: EIDOS Evidence Creates Stores

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/033-eidos-evidence-creates-stores.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-evidence-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-evidence-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `93fb1ef Keep EIDOS evidence stats read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_evidence_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `spark eidos --evidence` in a fresh `HOME` exits `0`, prints the zero evidence report, and creates no files.

Suggested PR title:

```text
Keep EIDOS evidence stats read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --evidence` from creating EIDOS and evidence stores in fresh environments
- returns zero evidence stats without opening SQLite when no evidence store exists
- adds CLI regression coverage for fresh-home evidence behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/033-eidos-evidence-creates-stores.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_evidence_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --evidence`
```

## Packet 034: EIDOS Deferred Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/034-eidos-deferred-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-deferred-readonly
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-deferred-readonly?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `ecf1f34 Keep EIDOS deferred stats read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_deferred_readonly.py tests/test_eidos.py::TestEidosStore -q`
- Behavior check: `spark eidos --deferred` in a fresh `HOME` exits `0`, prints the zero deferred report, and creates no files.

Suggested PR title:

```text
Keep EIDOS deferred stats read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --deferred` from creating the EIDOS store in fresh environments
- returns zero deferred stats without opening SQLite when no EIDOS database exists
- adds CLI regression coverage plus an existing-overdue-row readback check

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/034-eidos-deferred-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_deferred_readonly.py tests/test_eidos.py::TestEidosStore -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --deferred`
```

## Packet 035: EIDOS Migrate Dry Run Creates Store

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/035-eidos-migrate-dry-run-creates-store.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-migrate-dry-run
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-migrate-dry-run?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `d6d14f7 Keep EIDOS migration dry run read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_migrate_dry_run_readonly.py -q`
- Behavior check: `spark eidos --migrate --dry-run` in a fresh `HOME` exits `0` and creates no files; non-dry-run migration still creates/uses `~/.spark/eidos.db`.

Suggested PR title:

```text
Keep EIDOS migration dry run read-only
```

Suggested PR body:

```markdown
## Summary
- prevents `spark eidos --migrate --dry-run` from creating the EIDOS store in fresh environments
- keeps non-dry-run migration behavior unchanged
- adds CLI regression coverage for dry-run and apply-mode migration behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/035-eidos-migrate-dry-run-creates-store.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_migrate_dry_run_readonly.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --migrate --dry-run`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli eidos --migrate`
```

## Packet 036: Advisory Setup Writes Defaults Non-Interactively

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/036-advisory-setup-noninteractive-writes-defaults.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advisory-noninteractive
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advisory-noninteractive?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `5a1c9e2 Keep advisory setup noninteractive read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_advisory_noninteractive.py tests/test_advisory_preferences.py -q`
- Behavior check: `spark advisory` in a fresh non-interactive `HOME` exits `0` and creates no files; explicit `spark advisory set` still writes preference files.

Suggested PR title:

```text
Keep advisory setup non-interactive runs read-only
```

Suggested PR body:

```markdown
## Summary
- prevents guided `spark advisory` setup from silently accepting defaults in non-interactive runs
- keeps explicit preference write commands such as `spark advisory set` unchanged
- adds CLI regression coverage for fresh-home non-interactive advisory setup

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/036-advisory-setup-noninteractive-writes-defaults.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_advisory_noninteractive.py tests/test_advisory_preferences.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli advisory`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli advisory set`
```

## Packet 037: Project View Commands Write Context

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/037-project-view-commands-write-context.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-readonly-views
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-status-readonly-context...codex/fix-project-readonly-views?expand=1
- Base: `jumperz11/vibeship-spark-intelligence:codex/fix-status-readonly-context`
- Commit: `e58d6ec Keep project view commands read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_project_readonly_views.py tests/test_project_context.py -q`
- Behavior check: `spark project status` and `spark project questions` in a fresh `HOME` exit `0`, print their reports, and create no files or directories under `HOME`.

Important routing note:

Packet 037 is stacked on Packet 026 because it reuses the read-only project-context helper from that fix. Open it after Packet 026 is routed/accepted, or combine only if reviewers ask for a bundled project-context PR.

Suggested PR title:

```text
Keep project view commands read-only
```

Suggested PR body:

```markdown
## Summary
- keeps `spark project status` from creating project-context cache files during read-only inspection
- keeps `spark project questions` from persisting generated question profiles during preview
- adds CLI regression coverage for fresh-home project view commands

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/037-project-view-commands-write-context.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_project_readonly_views.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project status`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project questions`
```

## Packet 038: CLI View Commands Emit Mojibake

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/038-cli-view-commands-mojibake.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-cli-view-mojibake
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-cli-status-mojibake...codex/fix-cli-view-mojibake?expand=1
- Base: `jumperz11/vibeship-spark-intelligence:codex/fix-cli-status-mojibake`
- Commit: `1e8207e Fix mojibake in CLI view commands`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_status_health_output.py tests/test_cli_view_output_mojibake.py -q`
- Behavior check: `events`, `learnings`, `surprises`, `voice`, `voice --growth`, `timeline`, and `bridge --status` emit no common mojibake markers.

Important routing note:

Packet 038 is stacked on Packet 002 because it uses the same ASCII marker style and fixes adjacent CLI view outputs. Open it after Packet 002 is routed/accepted, or combine only if reviewers ask for a bundled CLI output PR.

Suggested PR title:

```text
Fix mojibake in CLI view commands
```

Suggested PR body:

```markdown
## Summary
- replaces corrupted headings in read-only CLI view commands with ASCII-safe markers
- fixes bridge status markers and separators to avoid mojibake
- adds regression coverage for common CLI view surfaces

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/038-cli-view-commands-mojibake.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_status_health_output.py tests/test_cli_view_output_mojibake.py -q`
- `PYTHONPATH=. python -m spark.cli events`
- `PYTHONPATH=. python -m spark.cli learnings`
- `PYTHONPATH=. python -m spark.cli surprises`
- `PYTHONPATH=. python -m spark.cli voice`
- `PYTHONPATH=. python -m spark.cli bridge --status`
```

## Packet 039: Bridge Preview Writes Project State

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/039-bridge-preview-writes-project-state.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-bridge-readonly-context
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-project-readonly-views...codex/fix-bridge-readonly-context?expand=1
- Base: `jumperz11/vibeship-spark-intelligence:codex/fix-project-readonly-views`
- Commit: `00f7568 Keep bridge context preview read-only`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_bridge_readonly_context.py tests/test_cli_project_readonly_views.py tests/test_project_context.py -q`
- Behavior check: `spark bridge` in a fresh `HOME` exits `0`, prints active context, and creates no files or directories under `HOME`.

Important routing note:

Packet 039 is stacked on Packet 037 because it reuses the read-only project profile/question helpers. Open it after Packet 037 is routed/accepted, or combine only if reviewers ask for a bundled project-context PR.

Suggested PR title:

```text
Keep bridge context preview read-only
```

Suggested PR body:

```markdown
## Summary
- keeps bare `spark bridge` context preview from creating project-context cache files
- prevents preview-only generated project questions from being persisted as project profiles
- keeps explicit `spark bridge --update` as the write path

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/039-bridge-preview-writes-project-state.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_bridge_readonly_context.py tests/test_cli_project_readonly_views.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli bridge`
```

## Packet 040: Advice Feedback Failure Exits Zero

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/040-advice-feedback-failure-exits-zero.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advice-feedback-failure-exit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advice-feedback-failure-exit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `2fd5e99 Return failure when advice feedback is not recorded`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_advice_feedback_exit.py -q`
- Behavior check: `spark advice-feedback` without `--tool` or `--advice-id` exits `1` and prints the existing failure message; `spark advice-feedback --pending` still exits `0`.

Suggested PR title:

```text
[spark-compete] Return failure when advice feedback recording fails
```

Suggested PR body:

````markdown
## Summary
- makes failed `spark advice-feedback` recording attempts exit non-zero
- preserves the existing failure message for missing advice target input
- keeps read-only `spark advice-feedback --pending` behavior successful

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/040-advice-feedback-failure-exits-zero.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_advice_feedback_exit.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli advice-feedback`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli advice-feedback --pending`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark advice-feedback failure exits zero",
    "actual_behavior": "Failed advice feedback recording can report a successful zero exit code, causing automation and reviewers to trust a failed write.",
    "expected_behavior": "Failed advice feedback recording should exit non-zero and surface the failure clearly.",
    "repro_steps": [
      "Trigger an advice-feedback recording failure.",
      "Check the process exit code before this branch.",
      "Observe the command incorrectly exits zero before the fix."
    ],
    "affected_workflow": "Spark advice feedback recording and automation"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: failed advice feedback recording exited zero. After: the branch returns a non-zero failure exit and adds focused regression coverage.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/040-advice-feedback-failure-exits-zero.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advice-feedback-failure-exit?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advice-feedback-failure-exit"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Propagate advice-feedback write failures to the CLI exit status so automation cannot treat failed feedback as successful.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_advice_feedback_exit.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_advice_feedback_exit.py -q"
  },
  "pr": {
    "branch": "codex/fix-advice-feedback-failure-exit",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 041: Capture List and Reject Are Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/041-capture-list-reject-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-capture-list-reject
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-capture-list-reject?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `1f55628 Wire capture list and reject actions`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_capture_actions.py -q`
- Behavior check: `spark capture --list` prints pending suggestions or the empty state; `spark capture --reject missing` exits `1` and prints `[MISS] Not found / not pending`.

Suggested PR title:

```text
[spark-compete] Wire capture list and reject actions
```

Suggested PR body:

````markdown
## Summary
- wires `spark capture --list` to the existing pending suggestion formatter
- wires `spark capture --reject` to the existing reject helper
- returns non-zero when accept/reject cannot find a pending suggestion

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/041-capture-list-reject-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_capture_actions.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli capture --list`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli capture --reject missing`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark capture list and reject controls are ignored",
    "actual_behavior": "Advertised capture review controls such as list and reject can be ignored, leaving users unable to manage captured evidence reliably.",
    "expected_behavior": "Capture list and reject controls should execute the advertised review-loop actions with clear output.",
    "repro_steps": [
      "Create or inspect captured review items.",
      "Run the advertised capture list/reject actions.",
      "Observe ignored behavior before this branch."
    ],
    "affected_workflow": "Spark capture review loop"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: capture list/reject controls were ignored. After: the branch wires the actions and adds focused capture-action tests.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/041-capture-list-reject-ignored.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-capture-list-reject?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-capture-list-reject"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Connect capture list and reject CLI options to the underlying review-loop behavior with clear success/failure handling.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_capture_actions.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_capture_actions.py -q"
  },
  "pr": {
    "branch": "codex/fix-capture-list-reject",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 042: Missing Opportunities Exit Zero

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/042-opportunities-missing-exits-zero.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-missing-exit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-missing-exit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `2c96c6e Return failure for missing opportunities`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_opportunities_missing_exit.py -q`
- Behavior check: `spark opportunities accept missing` and `spark opportunities dismiss missing` exit `1` while explicit `spark opportunities list` still exits `0`.

Suggested PR title:

```text
[spark-compete] Fail missing opportunities accept and dismiss targets
```

Suggested PR body:

````markdown
## Summary
- makes missing `spark opportunities accept` targets exit non-zero
- makes missing `spark opportunities dismiss` targets exit non-zero
- keeps explicit opportunity listing behavior successful

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/042-opportunities-missing-exits-zero.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_opportunities_missing_exit.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli opportunities accept missing`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli opportunities dismiss missing`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli opportunities list`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark opportunities accept/dismiss missing targets exit zero",
    "actual_behavior": "Missing opportunities accept or dismiss targets can return a successful zero exit code even though no opportunity was changed.",
    "expected_behavior": "Missing opportunity targets should return failure and explain that no matching opportunity was accepted or dismissed.",
    "repro_steps": [
      "Run opportunities accept or dismiss against a missing target.",
      "Check the exit code before this branch.",
      "Observe false-success zero exit before the fix."
    ],
    "affected_workflow": "Spark opportunities accept/dismiss automation"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: missing accept/dismiss targets could exit zero. After: the branch returns a failure exit for missing targets with regression coverage.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/042-opportunities-missing-exits-zero.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-missing-exit?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-missing-exit"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Validate opportunity IDs before reporting success and return non-zero when the target cannot be found.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_opportunities_missing_exit.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_opportunities_missing_exit.py -q"
  },
  "pr": {
    "branch": "codex/fix-opportunities-missing-exit",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 043: Outcome Link Accepts Invalid Targets

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/043-outcome-link-invalid-targets.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-link-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-link-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `5efe22b`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_validation.py tests/test_outcome_log_full_stats.py -q`
- Behavior check: missing outcome IDs and invalid confidence values now exit `1` without creating `outcome_links.jsonl`; existing outcomes still link, including `--confidence 0`.

Suggested PR title:

```text
[spark-compete] Validate outcome link targets
```

Suggested PR body:

````markdown
## Summary
- rejects `spark outcome-link` requests for missing outcome IDs before writing a link row
- rejects link confidence values outside the documented `0-1` range
- preserves valid links for existing outcomes, including `--confidence 0`

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/043-outcome-link-invalid-targets.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_validation.py tests/test_outcome_log_full_stats.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-link missing insight:key`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-link missing insight:key --confidence 2`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark outcome-link accepts invalid targets",
    "actual_behavior": "Outcome link validation can accept invalid outcome IDs or confidence values, polluting proof-loop evidence.",
    "expected_behavior": "Outcome linking should reject missing or malformed targets and invalid confidence values before recording links.",
    "repro_steps": [
      "Run spark outcome-link with invalid target IDs or malformed confidence.",
      "Observe acceptance before this branch.",
      "Run the branch and confirm validation rejects the bad input."
    ],
    "affected_workflow": "Spark outcome proof-link validation"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: invalid outcome-link targets could be accepted. After: the branch validates IDs/confidence and adds outcome-link regression tests.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/043-outcome-link-invalid-targets.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-link-validation?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-link-validation"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Add explicit outcome target and confidence validation before recording outcome links.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_outcome_link_validation.py",
      "tests/test_outcome_log_full_stats.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_validation.py tests/test_outcome_log_full_stats.py -q"
  },
  "pr": {
    "branch": "codex/fix-outcome-link-validation",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 044: Project Answer Accepts Missing Question ID

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/044-project-answer-missing-question-id.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-answer-missing-id
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-answer-missing-id?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `1e080ec`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_project_answer_validation.py tests/test_project_context.py -q`
- Behavior check: missing project question IDs now exit `1` without recording answer rows or memory; valid known and suggested question IDs still record.

Suggested PR title:

```text
Reject unknown project answer IDs
```

Suggested PR body:

```markdown
## Summary
- validates `spark project answer` IDs against the generated project question set before recording
- rejects typo or missing question IDs with a non-zero exit
- preserves valid answers for known profile questions and suggested question IDs

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/044-project-answer-missing-question-id.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_project_answer_validation.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project answer missing --text hello`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project answer eng_arch --text hello`
```

## Packet 045: Curiosity Fill Missing Gap Exits Zero

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/045-curiosity-fill-missing-gap.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-curiosity-fill-missing-gap
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-curiosity-fill-missing-gap?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `b579d25`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_curiosity_fill.py tests/test_project_context.py -q`
- Behavior check: missing curiosity gap IDs now exit `1`; existing fill behavior still succeeds.

Suggested PR title:

```text
Return failure for missing curiosity gaps
```

Suggested PR body:

```markdown
## Summary
- returns a boolean from `CuriosityEngine.fill_gap` so callers can distinguish missing gaps
- makes `spark curiosity --fill <missing>` exit non-zero with an explicit not-found message
- keeps successful fill behavior unchanged for existing gap IDs

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/045-curiosity-fill-missing-gap.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_curiosity_fill.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -W ignore::DeprecationWarning -m spark.cli curiosity --fill missing --answer hello`
```

## Packet 046: Chips Missing Targets Exit Zero

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/046-chips-missing-targets-exit-zero.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-chips-missing-target-exits
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-chips-missing-target-exits?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `e0949b0`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_chips_missing_targets.py tests/test_chips_runtime_filters.py -q`
- Behavior check: missing chip target commands now exit `1`; aggregate read-only chip views remain successful.

Suggested PR title:

```text
Return failure for missing chip targets
```

Suggested PR body:

```markdown
## Summary
- returns non-zero exits for missing required chip IDs and not-found chip targets
- validates `spark chips insights <id>` against installed chips before treating it as an empty-insights state
- preserves successful aggregate chip list/status/question views

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/046-chips-missing-targets-exit-zero.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_chips_missing_targets.py tests/test_chips_runtime_filters.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli chips activate missing`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli chips status missing`
```

## Packet 047: Project Phase Accepts Invalid Values

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/047-project-phase-accepts-invalid-values.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-phase-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-phase-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `57531b1`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_project_phase_validation.py tests/test_project_context.py -q`
- Behavior check: invalid project phases now exit `1` before creating `.spark`; valid phases still persist normally.

Suggested PR title:

```text
Validate project phase values
```

Suggested PR body:

```markdown
## Summary
- validates `spark project phase --set` against the supported phase list
- rejects unsupported phases before loading or writing project state
- keeps valid phase changes and phase-specific question generation intact

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/047-project-phase-accepts-invalid-values.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_project_phase_validation.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project phase --set invalid`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project phase --set prototype`
```

## Packet 048: Hypotheses Outcome Missing Target Reports Success

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/048-hypotheses-outcome-missing-target.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-hypotheses-outcome-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-hypotheses-outcome-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `4be997d`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_hypotheses_outcome_validation.py tests/test_project_context.py -q`
- Behavior check: missing, malformed, and non-integer hypothesis outcome targets now exit `1` without false success or traceback.

Suggested PR title:

```text
[spark-compete] Validate hypotheses outcome targets
```

Suggested PR body:

````markdown
## Summary
- makes hypothesis outcome recording return a success/failure signal
- returns non-zero exits for missing hypothesis prediction targets and malformed outcome specs
- replaces non-integer index tracebacks with a CLI-safe diagnostic

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/048-hypotheses-outcome-missing-target.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_hypotheses_outcome_validation.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli hypotheses --outcome missing:0 --correct`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli hypotheses --outcome missing:notint --correct`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark hypotheses outcome reports success for missing targets",
    "actual_behavior": "Prediction-loop outcome linking can report success for missing or malformed targets.",
    "expected_behavior": "Hypothesis outcome commands should fail clearly when the target is missing or malformed.",
    "repro_steps": [
      "Run spark hypotheses with an outcome target that does not exist or is malformed.",
      "Observe false success before this branch.",
      "Run the branch and confirm the bad target is rejected."
    ],
    "affected_workflow": "Spark hypothesis outcome validation"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: missing or malformed hypothesis outcome targets could report success. After: the branch rejects invalid targets with focused tests.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/048-hypotheses-outcome-missing-target.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-hypotheses-outcome-validation?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-hypotheses-outcome-validation"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Validate hypothesis outcome targets before reporting success or updating project context.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_hypotheses_outcome_validation.py",
      "tests/test_project_context.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_hypotheses_outcome_validation.py tests/test_project_context.py -q"
  },
  "pr": {
    "branch": "codex/fix-hypotheses-outcome-validation",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 049: Contradictions Resolve Missing Index Reports Success

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/049-contradictions-resolve-missing-index.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-contradictions-resolve-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-contradictions-resolve-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `3e27436`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_contradictions_resolve.py tests/test_project_context.py -q`
- Behavior check: missing contradiction indexes now exit `1`; existing contradiction indexes still resolve.

Suggested PR title:

```text
[spark-compete] Validate contradiction resolve indexes
```

Suggested PR body:

````markdown
## Summary
- makes contradiction resolution report whether a target index existed
- returns a non-zero exit for missing contradiction indexes
- preserves successful resolution for existing contradiction indexes

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/049-contradictions-resolve-missing-index.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_contradictions_resolve.py tests/test_project_context.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli contradictions --resolve 0 --resolution-type update --resolution test`

## Spark Compete Hotfix Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184",
  "team": {
    "name": "JUMPERZ",
    "members": [
      "JUMPERZ",
      "Basjee01",
      "acexqt"
    ],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": [
      "jumperz11"
    ]
  },
  "target_repo": {
    "id": "reviewer-routed/private-or-ambiguous-owner",
    "source": "https://compete.sparkswarm.ai/allowed-repos.json",
    "owner_surface": "private-or-ambiguous-owner"
  },
  "issue": {
    "type": "bug",
    "severity": "medium",
    "title": "spark contradictions resolve reports success for missing indexes",
    "actual_behavior": "Contradiction resolution can report success even when the requested contradiction index does not exist.",
    "expected_behavior": "Contradiction resolution should fail clearly unless a real contradiction was found and resolved.",
    "repro_steps": [
      "Run spark contradictions --resolve with a missing index.",
      "Observe success before this branch.",
      "Run the branch and confirm missing indexes fail."
    ],
    "affected_workflow": "Spark contradiction resolution validation"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: missing contradiction indexes could report success. After: the branch rejects missing indexes and adds contradiction-resolution regression coverage.",
    "links": [
      "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/049-contradictions-resolve-missing-index.md",
      "https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-contradictions-resolve-validation?expand=1",
      "https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-contradictions-resolve-validation"
    ],
    "forbidden": [
      "pdf",
      "zip",
      "exe",
      "unknown downloads",
      "shortened links",
      "archives",
      "binaries",
      "tokens",
      "browser cookies",
      "wallet material",
      "raw logs",
      "raw conversations",
      "raw memory",
      "raw patches",
      "private repo maps",
      "private scoring details"
    ]
  },
  "proposed_fix": {
    "approach": "Validate contradiction indexes before reporting successful resolution or changing state.",
    "files_expected": [
      "spark/cli.py",
      "tests/test_cli_contradictions_resolve.py",
      "tests/test_project_context.py"
    ],
    "tests_or_smoke": "PYTHONPATH=. python -m pytest tests/test_cli_contradictions_resolve.py tests/test_project_context.py -q"
  },
  "pr": {
    "branch": "codex/fix-contradictions-resolve-validation",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": [
      "packet",
      "team",
      "pr_author",
      "repo",
      "actual_behavior",
      "expected_behavior",
      "repro_steps",
      "before_after_proof",
      "tests_or_smoke",
      "duplicate_notes",
      "risk_notes",
      "review_claim"
    ],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/184"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": [
      "redacted_terminal_excerpt",
      "failing_test",
      "passing_test"
    ],
    "duplicate_notes": "Checked the curated JUMPERZ top review queue and no active upstream PR is open for this branch. This packet requests reviewer routing instead of guessing a private or ambiguous owner surface.",
    "risk_notes": "Reviewer routing requested because the target repository is not listed in the public allowed target list. Packet evidence is limited to public GitHub links and redacted behavior summaries.",
    "review_state_requested": "pr_review"
  }
}
```
````

## Packet 050: Learn Command Accepts Invalid Input And Crashes On Filtered Insights

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/050-learn-input-validation.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-learn-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-learn-input-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `83d8aac`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_learn_validation.py tests/test_cognitive_noise_filter.py -q`
- Behavior check: invalid categories, out-of-range reliability, empty insight text, and filtered insights now exit `1` with CLI-safe diagnostics; valid actionable input still stores.

Suggested PR title:

```text
Validate learn command inputs
```

Suggested PR body:

```markdown
## Summary
- returns non-zero exits for invalid learn categories and reliability outside 0-1
- rejects empty insight text before initializing learner state
- handles filtered insights without a None dereference traceback

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/050-learn-input-validation.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_learn_validation.py tests/test_cognitive_noise_filter.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn invalid "x"`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom "x" --reliability 1.2`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom ""`
```

## Packet 051: Sync Banks Accepts Invalid Thresholds And Categories

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/051-sync-banks-input-validation.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-banks-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-banks-input-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `cfd8733`
- Test: `PYTHONPATH=. python -m pytest tests/test_sync_banks_validation.py tests/test_memory_emotion_integration.py -q`
- Behavior check: invalid reliability thresholds and unknown category filters now exit `1`; valid dry-run sync still works.

Suggested PR title:

```text
Validate sync banks inputs
```

Suggested PR body:

```markdown
## Summary
- rejects `sync-banks --min-reliability` values outside the documented 0-1 range
- rejects unknown sync-banks category filters instead of silently doing zero work
- converts sync-banks validation errors into CLI-safe non-zero exits

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/051-sync-banks-input-validation.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_sync_banks_validation.py tests/test_memory_emotion_integration.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-banks --min-reliability -1`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli sync-banks --categories bogus`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-banks --min-reliability 0.7 --dry-run`
```

## Packet 052: Auto-Link Accepts Invalid Similarity Thresholds

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/052-auto-link-threshold-validation.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-auto-link-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-auto-link-threshold-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `52897ef`
- Test: `PYTHONPATH=. python -m pytest tests/test_auto_link_threshold_validation.py tests/test_outcome_log_full_stats.py -q`
- Behavior check: invalid negative similarity thresholds now exit `1` before link writes; normal dry-run thresholds still work.

Suggested PR title:

```text
Validate auto-link similarity threshold
```

Suggested PR body:

```markdown
## Summary
- rejects `auto-link --min-similarity` values outside the documented 0-1 range
- prevents negative thresholds from creating low-similarity validation links
- converts auto-link threshold validation into a CLI-safe non-zero exit

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/052-auto-link-threshold-validation.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_auto_link_threshold_validation.py tests/test_outcome_log_full_stats.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.25 --dry-run`
```

## Packet 053: Auto-Link Limit Zero Processes All Outcomes

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/053-auto-link-zero-limit-writes-all.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-auto-link-limit-zero
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-auto-link-limit-zero?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `9ba22d3`
- Test: `PYTHONPATH=. python -m pytest tests/test_auto_link_limit_validation.py tests/test_outcome_log_full_stats.py -q`
- Behavior check: `auto-link --limit 0` now processes zero outcomes and writes no link file; `--limit 1` still writes one link; negative limits exit `1`.

Suggested PR title:

```text
Respect auto-link zero limit
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `auto-link --limit 0` instead of converting it to the default limit
- makes limit zero process no outcomes and write no links
- rejects negative auto-link limits with a CLI-safe non-zero exit

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/053-auto-link-zero-limit-writes-all.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_auto_link_limit_validation.py tests/test_outcome_log_full_stats.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli auto-link --min-similarity 0.1 --limit 1`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli auto-link --limit -1`
```

## Packet 054: Outcome Validate Limit Zero Validates Links

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/054-outcome-validate-zero-limit.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-validate-zero-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-validate-zero-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `15766a0`
- Test: `PYTHONPATH=. python -m pytest tests/test_outcome_validate_limit.py tests/test_validation_loop.py -q`
- Behavior check: `outcome-validate --limit 0` now processes zero links and leaves validation state untouched; `--limit 1` still validates one link; negative limits exit `1`.

Suggested PR title:

```text
Respect outcome validation zero limit
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `outcome-validate --limit 0` instead of converting it to the default limit
- makes limit zero process no links and avoid learner/link mutations
- rejects negative outcome-validation limits with a CLI-safe non-zero exit

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/054-outcome-validate-zero-limit.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_outcome_validate_limit.py tests/test_validation_loop.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-validate --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-validate --limit 1`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome-validate --limit -1`
```

## Packet 055: Outcome Auto-Link Zero Window Still Links Exposures

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/055-outcome-autolink-window-zero.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-autolink-window
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-autolink-window?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `27ae56e`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_autolink_window.py -q`
- Behavior check: `outcome --auto-link --link-window-mins 0` records without linked insights; positive windows still link; negative windows exit `1` before recording.

Suggested PR title:

```text
Respect outcome auto-link window
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `outcome --auto-link --link-window-mins 0` instead of converting it to the default window
- avoids last-exposure fallback when the requested auto-link window is zero
- rejects negative auto-link windows before recording an outcome

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/055-outcome-autolink-window-zero.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_outcome_autolink_window.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins 1`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --auto-link --link-window-mins -1`
```

## Packet 056: Outcome Negative Link Count Still Records Outcome

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/056-outcome-link-count-negative.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-link-count-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-link-count-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `e1cc32e`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_count.py -q`
- Behavior check: `outcome --link-count -1` exits `1` before creating an outcome file; `--link-count 0` still records an unlinked outcome; positive counts still link recent exposures.

Suggested PR title:

```text
Validate outcome link count
```

Suggested PR body:

```markdown
## Summary
- rejects negative `outcome --link-count` values before recording an outcome
- keeps explicit `--link-count 0` as a valid unlinked outcome write
- preserves positive link-count behavior for recent exposure linking

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/056-outcome-link-count-negative.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_count.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --link-count -1`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli outcome --result success --text "Deploy succeeded after a separate check" --link-count 0`
```

## Packet 057: Process Zero Max Iterations Still Runs Worker

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/057-process-zero-max-iterations-writes-state.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-process-max-iterations-zero
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-process-max-iterations-zero?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `5a5469a`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_process_max_iterations.py -q`
- Behavior check: `process --drain --max-iterations 0` reports zero cycles and creates no worker state; negative max iterations exit `1`; positive drain runs still execute normally.

Suggested PR title:

```text
Respect process zero max iterations
```

Suggested PR body:

```markdown
## Summary
- makes `spark process --drain --max-iterations 0` a true zero-cycle no-op
- rejects negative process max-iteration values before running the bridge worker
- preserves positive drain behavior and normal one-cycle processing

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/057-process-zero-max-iterations-writes-state.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_process_max_iterations.py -q`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli process --drain --max-iterations 0 --timeout 0.01 --interval 0`
- `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli process --drain --max-iterations -1 --timeout 0.01 --interval 0`
```

## Packet 058: Decay Prune Reports Success But Leaves Insight On Disk

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/058-decay-prune-not-persisted.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-decay-prune-persistence
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-decay-prune-persistence?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `7e7a30c`
- Test: `PYTHONPATH=. python -m pytest tests/test_cognitive_decay_prune.py tests/test_cognitive_learner.py -q`
- Behavior check: `decay --apply --max-age-days 0 --min-effective 0.2` now removes the pruned insight from `cognitive_insights.json` instead of reporting success while leaving it on disk.

Suggested PR title:

```text
Persist decay pruned insights
```

Suggested PR body:

```markdown
## Summary
- persists `spark decay --apply` deletions to `cognitive_insights.json`
- uses the existing deletion-aware save path so disk entries do not get merged back
- adds regression coverage for prune count matching on-disk state

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/058-decay-prune-not-persisted.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cognitive_decay_prune.py tests/test_cognitive_learner.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 0.2`
```

## Packet 059: Sync Context Negative Gates Export Low-Quality Memory

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/059-sync-context-negative-gates-export-low-quality.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-context-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-context-threshold-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `8a009cd`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_sync_context_validation.py -q`
- Behavior check: `sync-context` now rejects negative or above-one reliability gates and negative validation gates before writing context exports.

Suggested PR title:

```text
Validate sync-context thresholds
```

Suggested PR body:

```markdown
## Summary
- rejects `sync-context --min-reliability` values outside `0..1`
- rejects negative `sync-context --min-validations` values
- prevents invalid quality gates from writing low-reliability memory into agent context exports

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/059-sync-context-negative-gates-export-low-quality.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_sync_context_validation.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-reliability -1 --min-validations -1 --limit 1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-reliability 1.1 --limit 1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-validations -1 --limit 1`
```

## Packet 060: Growth Timeline Writes State Into Source Checkout

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/060-growth-timeline-writes-checkout.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-growth-tracker-home-path
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-growth-tracker-home-path?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `683bf28`
- Test: `PYTHONPATH=. python -m pytest tests/test_growth_tracker_storage.py -q`
- Behavior check: `timeline --limit 0` now writes growth state under isolated `HOME`, and the worktree does not receive `.spark/growth.json`.

Suggested PR title:

```text
Store growth timeline under home
```

Suggested PR body:

```markdown
## Summary
- stores growth timeline state under `Path.home() / ".spark" / "growth.json"`
- prevents `spark timeline` from creating or updating `.spark/growth.json` in the source checkout
- adds regression coverage for the growth tracker storage path

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/060-growth-timeline-writes-checkout.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_growth_tracker_storage.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli timeline --limit 0`
```

## Packet 061: Personality State Writes Into Source Checkout

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/061-personality-state-writes-checkout.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-voice-aha-home-path
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-voice-aha-home-path?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `ab47fb4`
- Test: `PYTHONPATH=. python -m pytest tests/test_personality_state_storage.py tests/test_validation_loop.py tests/test_convo_iq.py tests/test_niche_net.py -q`
- Behavior check: voice and surprise state now write under isolated `HOME`, and neither path is under the worktree.

Suggested PR title:

```text
Store personality state under home
```

Suggested PR body:

```markdown
## Summary
- stores Spark voice state under `Path.home() / ".spark"`
- stores aha/surprise state under `Path.home() / ".spark"`
- prevents personality runtime state from writing into the source checkout

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/061-personality-state-writes-checkout.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_personality_state_storage.py tests/test_validation_loop.py tests/test_convo_iq.py tests/test_niche_net.py -q`
- isolated `HOME` smoke for `SparkVoice().record_interaction()` and `AhaTracker().capture_surprise(...)`
```

## Packet 062: Eval Accepts Invalid Thresholds

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/062-eval-invalid-thresholds.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eval-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eval-threshold-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `55969b1`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_eval_validation.py -q`
- Behavior check: `spark eval --sim -1` and `spark eval --days -1` now exit with status `1` before reporting misleading metrics.

Suggested PR title:

```text
Validate evaluation thresholds
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark eval --days` values before evaluation
- rejects `spark eval --sim` values outside `0..1`
- prevents invalid thresholds from reporting false prediction/outcome matches

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/062-eval-invalid-thresholds.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_eval_validation.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eval --days 7 --sim -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eval --days -1 --sim 0.72`
```

## Packet 063: Process Runtime Limits Still Run Worker

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/063-process-runtime-limits.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-process-runtime-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-process-runtime-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `c668028`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_process_runtime_validation.py tests/test_bridge_cycle_safety.py -q`
- Behavior check: `spark process --drain --timeout -1` now exits `1` before running the worker, and `--timeout 0` drains zero cycles without creating `.spark` files.

Suggested PR title:

```text
Validate process runtime limits
```

Suggested PR body:

```markdown
## Summary
- rejects negative process timeout, interval, memory-limit, and pattern-limit values before bridge worker execution
- treats `spark process --drain --timeout 0` as a zero-cycle no-op
- keeps one-shot non-drain process behavior unchanged

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/063-process-runtime-limits.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_process_runtime_validation.py tests/test_bridge_cycle_safety.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --timeout -1 --interval 0 --max-iterations 100`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli process --drain --timeout 0 --interval 0 --max-iterations 100`
```

## Packet 064: Decay Accepts Invalid Bounds

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/064-decay-invalid-bounds.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-decay-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-decay-input-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `7253936`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_decay_input_validation.py tests/test_cognitive_learner.py -q`
- Behavior check: invalid decay bounds now exit `1` before loading the cognitive learner or changing the seeded `cognitive_insights.json`.

Suggested PR title:

```text
Validate decay command inputs
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark decay --max-age-days` values before pruning
- rejects `--min-effective` outside `0..1`
- rejects negative dry-run limits before loading cognitive state

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/064-decay-invalid-bounds.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_decay_input_validation.py tests/test_cognitive_learner.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days -1 --min-effective 0.2`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --apply --max-age-days 0 --min-effective 2`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli decay --max-age-days 0 --min-effective 0.2 --limit -1`
```

## Packet 065: Validate-Ingest Negative Limit Traceback

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/065-validate-ingest-negative-limit.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-validate-ingest-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-validate-ingest-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `8d865cf`
- Test: `PYTHONPATH=. python -m pytest tests/test_validate_ingest_limit.py tests/test_queue_concurrency.py -q`
- Behavior check: `spark validate-ingest --limit -1` now exits `1` with a Spark-safe message and no report write; `--limit 0` processes zero rows and writes a zero-window report.

Suggested PR title:

```text
Validate ingest scan limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark validate-ingest --limit` values before queue scanning
- prevents `deque(maxlen=-1)` tracebacks from malformed ingest diagnostics
- preserves `--limit 0` as a valid zero-row scan and report window

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/065-validate-ingest-negative-limit.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_validate_ingest_limit.py tests/test_queue_concurrency.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli validate-ingest --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli validate-ingest --limit 0`
```

## Packet 066: Personality Evolution Input Tracebacks

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/066-personality-evolution-input-tracebacks.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-personality-evolution-input
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-personality-evolution-input?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `c1e84b1`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_personality_evolution_input.py tests/test_personality_evolver.py -q`
- Behavior check: malformed JSON, non-object JSON, and missing signal files now exit `1` with Spark-safe messages and no state-file writes.

Suggested PR title:

```text
Validate personality evolution signals input
```

Suggested PR body:

```markdown
## Summary
- handles malformed personality evolution JSON without tracebacks
- rejects non-object signal payloads before calling the evolver
- reports missing signals files with a Spark-safe error

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/066-personality-evolution-input-tracebacks.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_personality_evolution_input.py tests/test_personality_evolver.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '{bad json'`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '[1]'`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals-file "$tmp/missing.json"`
```

## Packet 067: Config Malformed Dot-Path Writes Empty Keys

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/067-config-malformed-dot-path.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-key-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-key-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `a7ac2e8`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_config_key_validation.py -q`
- Behavior check: malformed config keys now exit `1` before creating `~/.spark/tuneables.json`; valid `advisor.max_items` still writes nested runtime config.

Suggested PR title:

```text
Validate config dot-path keys
```

Suggested PR body:

```markdown
## Summary
- rejects empty and malformed `spark config` dot-path keys before reads or writes
- prevents empty-key sections from being persisted to runtime tuneables
- keeps valid dot-path config writes working

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/067-config-malformed-dot-path.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_config_key_validation.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config set "" 1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor..max_items 5`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor.max_items 5`
```

## Packet 068: Config Malformed JSON Traceback

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/068-config-malformed-json-traceback.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-json-errors
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-json-errors?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `d1f44aa`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_config_json_errors.py -q`
- Behavior check: malformed runtime config now exits `1` with a Spark-safe JSON diagnostic, and `config set` leaves the malformed file unchanged.

Suggested PR title:

```text
Handle malformed config JSON
```

Suggested PR body:

```markdown
## Summary
- handles malformed runtime tuneables JSON without a traceback
- reports the invalid config file and JSON location
- prevents `spark config set` from overwriting malformed runtime config

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/068-config-malformed-json-traceback.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_config_json_errors.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config show`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor.max_items 5`
```

## Packet 069: Config Non-Object Runtime Crash

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/069-config-non-object-runtime-crash.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-object-shape
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-object-shape?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `695da92`
- Test: `PYTHONPATH=. python -m pytest tests/test_config_object_shape.py -q`
- Behavior check: non-object runtime tuneables no longer crash CLI startup, `config show` exits safely, and valid object config still resolves.

Suggested PR title:

```text
Validate config object shape
```

Suggested PR body:

```markdown
## Summary
- prevents non-object runtime tuneables JSON from crashing shared config resolution
- reports non-object runtime config cleanly from `spark config`
- preserves normal object-shaped runtime tuneables behavior

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/069-config-non-object-runtime-crash.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_config_object_shape.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli --help`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config show`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli config get advisor.max_items`
```

## Packet 070: Logs Tail Bounds Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/070-logs-tail-bounds.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-logs-tail-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-logs-tail-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `5c0ffb3`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_logs_tail_validation.py -q`
- Behavior check: negative tails exit `1`, `--tail 0` returns zero lines, and positive tails still return the last N lines.

Suggested PR title:

```text
Validate logs tail bounds
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark logs --tail` values
- preserves explicit `--tail 0` as a zero-line log probe
- keeps positive tail limits returning the last N lines

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/070-logs-tail-bounds.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_logs_tail_validation.py -q`
- `SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail -1 --json`
- `SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail 0 --json`
- `SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --tail 2 --json`
```

## Packet 071: Logs Invalid Since Filter Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/071-logs-since-invalid-filter.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-logs-since-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-logs-since-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `ae3c6e1`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_logs_since_validation.py -q`
- Behavior check: invalid `--since` filters exit `1`; valid relative filters still read logs.

Suggested PR title:

```text
Validate logs since filter
```

Suggested PR body:

```markdown
## Summary
- rejects malformed `spark logs --since` values instead of silently ignoring them
- returns machine-readable JSON errors for invalid since filters
- keeps valid relative filters such as `1h` working

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/071-logs-since-invalid-filter.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_logs_since_validation.py -q`
- `SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --since nope --json`
- `SPARK_LOG_DIR="$tmp/logs" PYTHONPATH=. python -m spark.cli logs --service sparkd --since 1h --json`
```

## Packet 072: Validation Scan Negative Limit Reports Success

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/072-validation-scan-negative-limit.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-validation-scan-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-validation-scan-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `2064984`
- Test: `PYTHONPATH=. python -m pytest tests/test_validation_loop.py -q`
- Behavior check: negative validation limits exit `1`, explicit zero remains a no-op, and positive limits still process queued events.

Suggested PR title:

```text
Validate validation scan limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark validate --limit` values before validation loop execution
- preserves explicit `--limit 0` as a zero-row validation scan
- keeps positive validation scan limits processing queued events

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/072-validation-scan-negative-limit.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_validation_loop.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli validate --limit 1`
```

## Packet 073: Learnings Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/073-learnings-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-learnings-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-learnings-limit-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `ec2e8c0`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_learnings_limit.py -q`
- Behavior check: negative learnings limits exit `1`, explicit zero displays zero rows, and positive limits still show seeded learnings.

Suggested PR title:

```text
Validate learnings display limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark learnings --limit` values before loading learning state
- preserves explicit `--limit 0` as a zero-row learnings view
- keeps positive limits displaying recent captured learnings

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/073-learnings-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_learnings_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli learnings --limit 1`
```

## Packet 074: Events Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/074-events-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-events-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-events-limit-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `edb35f0`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_events_limit.py -q`
- Behavior check: negative event limits exit `1`, explicit zero displays zero rows, and positive limits still show recent queued events.

Suggested PR title:

```text
Validate events display limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark events --limit` values before reading the event queue
- preserves explicit `--limit 0` as a zero-row events view
- keeps positive limits displaying recent queued events

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/074-events-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_events_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli events --limit 1`
```

## Packet 075: Outcome Unlinked Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/075-outcome-unlinked-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-unlinked-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-unlinked-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `8153a5a`
- Test: `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q`
- Behavior check: negative unlinked-outcome limits exit `1`, explicit zero displays zero rows, and positive limits still show newest unlinked outcomes.

Suggested PR title:

```text
Validate unlinked outcome limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark outcome-unlinked --limit` values
- preserves explicit `--limit 0` as a zero-row outcome coverage view
- keeps positive limits displaying newest unlinked outcomes

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/075-outcome-unlinked-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit 1`
```

## Packet 076: Outcome Links Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/076-outcome-links-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-links-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-links-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `9ad2741`
- Test: `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q`
- Behavior check: negative outcome-link limits exit `1`, explicit zero displays zero rows, and positive limits still show newest links.

Suggested PR title:

```text
Validate outcome links limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark outcome-links --limit` values
- preserves explicit `--limit 0` as a zero-row validation-link view
- keeps `get_outcome_links(limit=None)` as the explicit full-scan API

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/076-outcome-links-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-links --limit 1`
```

## Packet 077: Advice Feedback Pending Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/077-advice-feedback-pending-limit.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-advice-pending-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-advice-pending-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `3510d4c`
- Test: `PYTHONPATH=. python -m pytest tests/test_advice_feedback_correlation.py -q`
- Behavior check: negative pending advice-feedback limits exit `1`, explicit zero displays zero rows, and positive limits still show newest requests.

Suggested PR title:

```text
Validate advice feedback pending limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark advice-feedback --pending --limit` values
- preserves explicit `--limit 0` as a zero-row pending request view
- keeps positive limits displaying newest advice feedback requests

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/077-advice-feedback-pending-limit.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_advice_feedback_correlation.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli advice-feedback --pending --limit 2`
```

## Packet 078: Sync Context Negative Limit Writes Exports

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/078-sync-context-negative-limit.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-context-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-context-limit-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `5490e05`
- Test: `PYTHONPATH=. python -m pytest tests/test_context_sync_limit_validation.py tests/test_context_sync_mind.py tests/test_production_hardening.py -q`
- Behavior check: negative sync-context limits exit `1` before writing exports, explicit zero remains a zero-selection sync, and positive limits still write bounded context.

Suggested PR title:

```text
Validate sync context limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark sync-context --limit` values before loading or writing context
- preserves explicit `--limit 0` as a zero-insight sync
- prevents `_select_insights(limit=0)` from returning one item after the cap check

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/078-sync-context-negative-limit.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_context_sync_limit_validation.py tests/test_context_sync_mind.py tests/test_production_hardening.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --limit -1`
- `HOME="$tmp2" PYTHONPATH=. python -m spark.cli sync-context --limit 0`
```

## Packet 079: Opportunities List Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/079-opportunities-list-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-list-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-opportunities-list-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `4849a17`
- Test: `PYTHONPATH=. python -m pytest tests/test_opportunity_inbox.py -q`
- Behavior check: negative opportunity list limits exit `1`, explicit zero displays zero rows, and positive limits still show newest opportunities.

Suggested PR title:

```text
Validate opportunities list limit
```

Suggested PR body:

```markdown
## Summary
- rejects negative `spark opportunities list --limit` values
- preserves explicit `--limit 0` as a zero-row opportunity inbox view
- keeps positive limits displaying newest matching opportunities

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/079-opportunities-list-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_opportunity_inbox.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli opportunities list --limit 1`
```

## Packet 080: EIDOS List Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/080-eidos-list-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-list-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-list-limit-validation?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `9bdf052`
- Test: `PYTHONPATH=. python -m pytest tests/test_eidos_list_limits.py tests/test_eidos_store_distillation_dedupe.py -q`
- Behavior check: negative EIDOS list limits exit `1`, explicit zero displays zero rows, and positive episode limits still show newest episodes.

Suggested PR title:

```text
Validate EIDOS list limits
```

Suggested PR body:

```markdown
## Summary
- rejects negative EIDOS episode, distillation, and step list limits
- preserves explicit `--limit 0` as a zero-row EIDOS list view
- keeps positive limits displaying newest matching EIDOS rows

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/080-eidos-list-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_eidos_list_limits.py tests/test_eidos_store_distillation_dedupe.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit 1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --distillations --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --steps --limit -1`
```

## Packet 081: Surprises View Crashes On Persisted Rows

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/081-surprises-persisted-row-crash.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-surprises-row-format
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-surprises-row-format?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `62a4db8`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_surprises.py -q`
- Behavior check: seeded persisted surprise rows render and exit `0` instead of raising `AttributeError`.

Suggested PR title:

```text
Format persisted surprise rows
```

Suggested PR body:

```markdown
## Summary
- formats persisted surprise dictionaries as `AhaMoment` rows before display
- keeps existing object-style surprise rows supported
- adds CLI regression coverage for stored surprise evidence

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/081-surprises-persisted-row-crash.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_surprises.py -q`
- seeded `.spark/aha_moments.json`, then `PYTHONPATH=. python -m spark.cli surprises --limit 1`
```

## Packet 082: Voice Growth Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/082-voice-growth-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-voice-growth-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-voice-growth-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `0fc2eac`
- Test: `PYTHONPATH=. python -m pytest tests/test_cli_voice_growth_limit.py -q`
- Behavior check: seeded voice growth rows respect `--limit 0` and reject `--limit -1` with exit `1`.

Suggested PR title:

```text
Validate voice growth limits
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `spark voice --growth --limit 0` as a zero-row view
- rejects negative voice growth limits before display
- makes `SparkVoice.get_recent_growth(0)` return an empty window instead of all rows

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/082-voice-growth-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_cli_voice_growth_limit.py -q`
- seeded `.spark/voice.json`, then `PYTHONPATH=. python -m spark.cli voice --growth --limit 0`
- seeded `.spark/voice.json`, then `PYTHONPATH=. python -m spark.cli voice --growth --limit -1`
```

## Packet 083: Project Questions Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/083-project-questions-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-questions-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-questions-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `3949a8d`
- Test: `PYTHONPATH=. python -m pytest tests/test_project_questions_limit.py -q`
- Behavior check: isolated `HOME` project questions respect `--limit 0` and reject `--limit -1` with exit `1`.

Suggested PR title:

```text
Validate project question limits
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `spark project questions --limit 0` as a zero-row view
- rejects negative project question limits with a CLI-safe non-zero exit
- makes `get_suggested_questions(..., limit=0)` return an empty window instead of default rows

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/083-project-questions-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_project_questions_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli project questions --project "$tmp/proj" --limit -1`
```

## Packet 084: Curiosity Questions Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/084-curiosity-questions-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-curiosity-questions-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-curiosity-questions-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `1e9f6cd`
- Test: `PYTHONPATH=. python -m pytest tests/test_curiosity_questions_limit.py -q`
- Behavior check: isolated `HOME` curiosity questions respect `--limit 0` and reject `--limit -1` with exit `1`.

Suggested PR title:

```text
Validate curiosity question limits
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `spark curiosity --questions --limit 0` as a zero-row view
- rejects negative curiosity question limits with a CLI-safe non-zero exit
- makes `get_open_questions(..., limit=0)` return an empty window instead of all rows

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/084-curiosity-questions-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_curiosity_questions_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli curiosity --questions --limit -1`
```

## Packet 085: Hypotheses Display Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/085-hypotheses-display-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-hypotheses-display-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-hypotheses-display-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `d4b2f66`
- Test: `PYTHONPATH=. python -m pytest tests/test_hypotheses_display_limit.py -q`
- Behavior check: isolated `HOME` hypotheses testable and pending views respect `--limit 0` and reject `--limit -1` with exit `1`.

Suggested PR title:

```text
Validate hypotheses display limits
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `spark hypotheses --testable --limit 0` as a zero-row view
- preserves explicit `spark hypotheses --pending --limit 0` as a zero-row view
- rejects negative hypothesis display limits with a CLI-safe non-zero exit

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/085-hypotheses-display-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_hypotheses_display_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --testable --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli hypotheses --pending --limit -1`
```

## Packet 086: Contradictions Display Limit Ignored

- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/086-contradictions-display-limit-ignored.md
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-contradictions-display-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-contradictions-display-limit?expand=1
- Base: `vibeforge1111/vibeship-spark-intelligence:main`
- Commit: `1efefaa`
- Test: `PYTHONPATH=. python -m pytest tests/test_contradictions_display_limit.py -q`
- Behavior check: isolated `HOME` contradictions respect `--limit 0`, reject `--limit -1` with exit `1`, and keep positive-limit headers bounded.

Suggested PR title:

```text
Validate contradictions display limits
```

Suggested PR body:

```markdown
## Summary
- preserves explicit `spark contradictions --unresolved --limit 0` as a zero-row view
- rejects negative contradiction display limits with a CLI-safe non-zero exit
- reports the count of bounded unresolved rows instead of the unbounded source count

## Spark Compete
- Team: JUMPERZ
- Packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/packets/086-contradictions-display-limit-ignored.md

## Verification
- `PYTHONPATH=. python -m pytest tests/test_contradictions_display_limit.py -q`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit 0`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit -1`
- `HOME="$tmp" PYTHONPATH=. python -m spark.cli contradictions --unresolved --limit 1`
```
