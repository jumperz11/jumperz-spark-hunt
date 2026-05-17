# JUMPERZ Farming Board

This board tracks legitimate Spark Compete farming work: real findings, safe proof, and reviewer-routable packets. No duplicate spam, fake teams, or upstream pushes.

## Live Status

- Team: JUMPERZ
- Site status: Registered
- Rank snapshot: 16
- Public points snapshot: 0
- Last checked: 2026-05-17 22:18 UTC
- Clean repo: https://github.com/jumperz11/jumperz-spark-hunt

## Completed

| ID | Packet | Status | Notes |
| --- | --- | --- | --- |
| 001 | [Missing `spark os compile --json`](HUNT_PROOF.md) | Proof ready | First mission command from the hunt brief failed before discovery. |
| 002 | [CLI status/health mojibake](packets/002-cli-status-health-mojibake.md) | Proof ready | `spark status` and `spark health` render corrupted icon/checkmark text. |
| 003 | [Proof repo not routable from registration](packets/003-proof-repo-not-routable-from-registration.md) | Proof ready | Registration accepts a profile URL, but rejects clean proof repo URLs and has no submission field. |
| 004 | [Proof kit has no submission handoff](packets/004-proof-kit-has-no-submission-handoff.md) | Proof ready | Proof kit explains PR evidence but gives no site-native proof/reviewer handoff. |
| 005 | [Leaderboard stale example copy](packets/005-leaderboard-stale-example-copy.md) | Proof ready | Board renders real teams while still saying rows are examples. |
| 006 | [Mission copy buttons indistinguishable](packets/006-mission-copy-buttons-indistinguishable.md) | Proof ready | 60 mission copy controls share the same `Copy` accessible text. |
| 007 | [Proof drawer confusing toggle name](packets/007-proof-drawer-toggle-accessible-name.md) | Proof ready | Open proof drawer exposes contradictory `CloseOpen` text to agents/assistive tech. |
| 008 | [Mission library confusing toggle name](packets/008-mission-library-toggle-accessible-name.md) | Proof ready | Expanded mission drawer exposes `Close Open` text before the mission list. |
| 009 | [Starter missions reference missing CLI commands](packets/009-starter-missions-reference-missing-cli-commands.md) | Proof ready | Missions mention `spark providers`, `smoke`, `live`, `security`, and `update` commands that the installed CLI rejects. |
| 010 | [Registration says ready for review with no handoff](packets/010-registration-ready-for-review-no-handoff.md) | Proof ready | Success message claims review readiness but exposes no team id, proof route, or reviewer handoff. |
| 011 | [Telegram missions have no visible bot route](packets/011-telegram-missions-no-bot-route.md) | Proof ready | Missions target Telegram agents, but the page does not show a bot link, handle, or fallback route. |
| 012 | [Practice repo name is not linked](packets/012-practice-repo-name-is-not-linked.md) | Proof ready | Site names `spark-personality-chip-labs`, but does not link to the existing GitHub repo. |

## Active Queue

| Priority | Mission | Target |
| --- | --- | --- |
| P0 | Verify CLI first-run/status readability | Spark CLI |
| P0 | Check command-not-found and recovery copy | Spark CLI install flow |
| P1 | Check support bundle redaction wording | Proof kit / support flow |
| P1 | Check public-track routing when upstream is unavailable | Reviewer routing |
| P2 | Check leaderboard duplicate/team update UX | Competition site |

## Farming Rules

- One packet per unique issue.
- Every packet needs before evidence, impact, expected behavior, and validation/proposed fix.
- Keep proof redacted and bounded.
- Do not submit duplicate teams or fake activity.
- Do not open upstream PRs unless explicitly approved.
