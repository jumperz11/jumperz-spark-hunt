# JUMPERZ Farming Board

This board tracks legitimate Spark Compete farming work: real findings, safe proof, and reviewer-routable packets. No duplicate spam, fake teams, or upstream pushes.

## Live Status

- Team: JUMPERZ
- Site status: Registered
- Rank snapshot: 16
- Public points snapshot: 0
- Last checked: 2026-05-21 12:15 UTC
- Clean repo: https://github.com/jumperz11/jumperz-spark-hunt

## Completed

| ID | Packet | Status | Notes |
| --- | --- | --- | --- |
| 001 | [Missing `spark os compile --json`](HUNT_PROOF.md) | Fork branch pushed; prior upstream PR closed | `codex/spark-os-compile-command` pushed to `jumperz11`; upstream PR #183 is closed, no active upstream PR open. |
| 002 | [CLI status/health mojibake](packets/002-cli-status-health-mojibake.md) | Fork branch pushed | `codex/fix-cli-status-mojibake` pushed to `jumperz11`; no upstream PR opened. |
| 003 | [Proof repo not routable from registration](packets/003-proof-repo-not-routable-from-registration.md) | Proof ready | Registration accepts a profile URL, but rejects clean proof repo URLs and has no submission field. |
| 004 | [Proof kit has no submission handoff](packets/004-proof-kit-has-no-submission-handoff.md) | Proof ready | Proof kit explains PR evidence but gives no site-native proof/reviewer handoff. |
| 005 | [Leaderboard stale example copy](packets/005-leaderboard-stale-example-copy.md) | Proof ready | Board renders real teams while still saying rows are examples. |
| 006 | [Mission copy buttons indistinguishable](packets/006-mission-copy-buttons-indistinguishable.md) | Proof ready | 60 mission copy controls share the same `Copy` accessible text. |
| 007 | [Proof drawer confusing toggle name](packets/007-proof-drawer-toggle-accessible-name.md) | Proof ready | Open proof drawer exposes contradictory `CloseOpen` text to agents/assistive tech. |
| 008 | [Mission library confusing toggle name](packets/008-mission-library-toggle-accessible-name.md) | Proof ready | Expanded mission drawer exposes `Close Open` text before the mission list. |
| 009 | [Starter missions reference missing CLI commands](packets/009-starter-missions-reference-missing-cli-commands.md) | Fork branch pushed | `codex/fix-mission-command-compat` pushed to `jumperz11`; no upstream PR opened. |
| 010 | [Registration says ready for review with no handoff](packets/010-registration-ready-for-review-no-handoff.md) | Proof ready | Success message claims review readiness but exposes no team id, proof route, or reviewer handoff. |
| 011 | [Telegram missions have no visible bot route](packets/011-telegram-missions-no-bot-route.md) | Proof ready | Missions target Telegram agents, but the page does not show a bot link, handle, or fallback route. |
| 012 | [Practice repo name is not linked](packets/012-practice-repo-name-is-not-linked.md) | Proof ready | Site names `spark-personality-chip-labs`, but does not link to the existing GitHub repo. |
| 013 | [Leaderboard hides public score band](packets/013-leaderboard-hides-public-score-band.md) | Proof ready | API exposes `Registered`, but UI drops the band and renders only `0 pts`. |
| 014 | [Leaderboard ignores API rank](packets/014-leaderboard-ignores-api-rank.md) | Proof ready | API returns `rank`, but UI recomputes rank from array position. |
| 015 | [Navigation current state stuck on teams](packets/015-nav-current-stuck-on-teams.md) | Proof ready | `aria-current="page"` stays on `teams` even at `#agent-playbook`. |
| 016 | [Carousel tabs missing tabpanel linkage](packets/016-carousel-tabs-missing-tabpanel-linkage.md) | Proof ready | Tabs have ARIA tab roles but panels lack tabpanel/id/control linkage. |
| 017 | [HEAD requests return 404 for live routes](packets/017-head-requests-return-404-for-live-routes.md) | Proof ready | `GET /` and `GET /api/leaderboard` return 200, but `HEAD` returns 404. |
| 018 | [Carousel tabs missing keyboard navigation](packets/018-carousel-tabs-missing-keyboard-navigation.md) | Proof ready | Tablist controls have click handlers but no arrow/Home/End keyboard behavior. |
| 019 | [Empty leaderboard falls back to mock standings](packets/019-empty-leaderboard-falls-back-to-mock-standings.md) | Proof ready | A valid empty API response would show preview teams instead of an empty live state. |
| 020 | [Services advertises dead Pulse URL](packets/020-services-advertises-dead-pulse-url.md) | Fork branch pushed | `codex/fix-pulse-service-status` pushed to `jumperz11`; no upstream PR opened. |
| 021 | [OS compile missing project emits traceback](packets/021-os-compile-missing-project-traceback.md) | Fork branch pushed | `codex/fix-os-compile-missing-project` pushed to `jumperz11`; no upstream PR opened. |

## Active Queue

| Priority | Mission | Target |
| --- | --- | --- |
| P0 | Convert the PR-ready fix queue into the reviewer-preferred submission surface | Packets 001, 002, 009, 020, 021 |
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
