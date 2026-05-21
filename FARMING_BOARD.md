# JUMPERZ Farming Board

This board tracks legitimate Spark Compete farming work: real findings, safe proof, and reviewer-routable packets. No duplicate spam, fake teams, or upstream pushes.

## Live Status

- Team: JUMPERZ
- Site status: Registered
- Rank snapshot: 16
- Public points snapshot: 0
- Last checked: 2026-05-21 19:31 UTC
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
| 022 | [Opportunities default subcommand traceback](packets/022-opportunities-default-subcommand-traceback.md) | Fork branch pushed | `codex/fix-opportunities-default` pushed to `jumperz11`; no upstream PR opened. |
| 023 | [Outcome command records unknown in non-interactive mode](packets/023-outcome-noninteractive-records-unknown.md) | Fork branch pushed | `codex/fix-outcome-noninteractive` pushed to `jumperz11`; no upstream PR opened. |
| 024 | [Memory config missing traceback](packets/024-memory-config-missing-traceback.md) | Fork branch pushed | `codex/fix-memory-config-missing` pushed to `jumperz11`; no upstream PR opened. |
| 025 | [Project missing path writes context](packets/025-project-missing-path-writes-context.md) | Fork branch pushed | `codex/fix-project-missing-path` pushed to `jumperz11`; no upstream PR opened. |
| 026 | [Status writes project context](packets/026-status-writes-project-context.md) | Fork branch pushed | `codex/fix-status-readonly-context` pushed to `jumperz11`; no upstream PR opened. |
| 027 | [Memory purge dry run creates store](packets/027-memory-purge-dry-run-creates-store.md) | Fork branch pushed | `codex/fix-memory-purge-dry-run` pushed to `jumperz11`; no upstream PR opened. |
| 028 | [EIDOS purge dry run creates store](packets/028-eidos-purge-dry-run-creates-store.md) | Fork branch pushed | `codex/fix-eidos-purge-dry-run` pushed to `jumperz11`; no upstream PR opened. |
| 029 | [EIDOS stats creates store](packets/029-eidos-stats-creates-store.md) | Fork branch pushed | `codex/fix-eidos-stats-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 030 | [EIDOS validate migration creates store](packets/030-eidos-validate-migration-creates-store.md) | Fork branch pushed | `codex/fix-eidos-validate-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 031 | [EIDOS list views create store](packets/031-eidos-list-views-create-store.md) | Fork branch pushed | `codex/fix-eidos-list-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 032 | [EIDOS metrics creates store](packets/032-eidos-metrics-creates-store.md) | Fork branch pushed | `codex/fix-eidos-metrics-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 033 | [EIDOS evidence creates stores](packets/033-eidos-evidence-creates-stores.md) | Fork branch pushed | `codex/fix-eidos-evidence-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 034 | [EIDOS deferred creates store](packets/034-eidos-deferred-creates-store.md) | Fork branch pushed | `codex/fix-eidos-deferred-readonly` pushed to `jumperz11`; no upstream PR opened. |
| 035 | [EIDOS migrate dry run creates store](packets/035-eidos-migrate-dry-run-creates-store.md) | Fork branch pushed | `codex/fix-eidos-migrate-dry-run` pushed to `jumperz11`; no upstream PR opened. |
| 036 | [Advisory setup writes defaults non-interactively](packets/036-advisory-setup-noninteractive-writes-defaults.md) | Fork branch pushed | `codex/fix-advisory-noninteractive` pushed to `jumperz11`; no upstream PR opened. |
| 037 | [Project view commands write context](packets/037-project-view-commands-write-context.md) | Fork branch pushed | `codex/fix-project-readonly-views` pushed to `jumperz11`; no upstream PR opened. |
| 038 | [CLI view commands emit mojibake](packets/038-cli-view-commands-mojibake.md) | Fork branch pushed | `codex/fix-cli-view-mojibake` pushed to `jumperz11`; no upstream PR opened. |
| 039 | [Bridge preview writes project state](packets/039-bridge-preview-writes-project-state.md) | Fork branch pushed | `codex/fix-bridge-readonly-context` pushed to `jumperz11`; no upstream PR opened. |
| 040 | [Advice feedback failure exits zero](packets/040-advice-feedback-failure-exits-zero.md) | Fork branch pushed | `codex/fix-advice-feedback-failure-exit` pushed to `jumperz11`; no upstream PR opened. |
| 041 | [Capture list and reject are ignored](packets/041-capture-list-reject-ignored.md) | Fork branch pushed | `codex/fix-capture-list-reject` pushed to `jumperz11`; no upstream PR opened. |
| 042 | [Missing opportunities exit zero](packets/042-opportunities-missing-exits-zero.md) | Fork branch pushed | `codex/fix-opportunities-missing-exit` pushed to `jumperz11`; no upstream PR opened. |
| 043 | [Outcome link accepts invalid targets](packets/043-outcome-link-invalid-targets.md) | Fork branch pushed | `codex/fix-outcome-link-validation` pushed to `jumperz11`; no upstream PR opened. |
| 044 | [Project answer accepts missing question ID](packets/044-project-answer-missing-question-id.md) | Fork branch pushed | `codex/fix-project-answer-missing-id` pushed to `jumperz11`; no upstream PR opened. |
| 045 | [Curiosity fill missing gap exits zero](packets/045-curiosity-fill-missing-gap.md) | Fork branch pushed | `codex/fix-curiosity-fill-missing-gap` pushed to `jumperz11`; no upstream PR opened. |
| 046 | [Chips missing targets exit zero](packets/046-chips-missing-targets-exit-zero.md) | Fork branch pushed | `codex/fix-chips-missing-target-exits` pushed to `jumperz11`; no upstream PR opened. |
| 047 | [Project phase accepts invalid values](packets/047-project-phase-accepts-invalid-values.md) | Fork branch pushed | `codex/fix-project-phase-validation` pushed to `jumperz11`; no upstream PR opened. |
| 048 | [Hypotheses outcome missing target reports success](packets/048-hypotheses-outcome-missing-target.md) | Fork branch pushed | `codex/fix-hypotheses-outcome-validation` pushed to `jumperz11`; no upstream PR opened. |
| 049 | [Contradictions resolve missing index reports success](packets/049-contradictions-resolve-missing-index.md) | Fork branch pushed | `codex/fix-contradictions-resolve-validation` pushed to `jumperz11`; no upstream PR opened. |
| 050 | [Learn command accepts invalid input](packets/050-learn-input-validation.md) | Fork branch pushed | `codex/fix-learn-input-validation` pushed to `jumperz11`; no upstream PR opened. |
| 051 | [Sync banks accepts invalid inputs](packets/051-sync-banks-input-validation.md) | Fork branch pushed | `codex/fix-sync-banks-input-validation` pushed to `jumperz11`; no upstream PR opened. |
| 052 | [Auto-link accepts invalid thresholds](packets/052-auto-link-threshold-validation.md) | Fork branch pushed | `codex/fix-auto-link-threshold-validation` pushed to `jumperz11`; no upstream PR opened. |
| 053 | [Auto-link limit zero writes all](packets/053-auto-link-zero-limit-writes-all.md) | Fork branch pushed | `codex/fix-auto-link-limit-zero` pushed to `jumperz11`; no upstream PR opened. |
| 054 | [Outcome validate limit zero validates links](packets/054-outcome-validate-zero-limit.md) | Fork branch pushed | `codex/fix-outcome-validate-zero-limit` pushed to `jumperz11`; no upstream PR opened. |
| 055 | [Outcome auto-link zero window still links](packets/055-outcome-autolink-window-zero.md) | Fork branch pushed | `codex/fix-outcome-autolink-window` pushed to `jumperz11`; no upstream PR opened. |
| 056 | [Outcome negative link count still records](packets/056-outcome-link-count-negative.md) | Fork branch pushed | `codex/fix-outcome-link-count-validation` pushed to `jumperz11`; no upstream PR opened. |
| 057 | [Process zero max iterations still runs](packets/057-process-zero-max-iterations-writes-state.md) | Fork branch pushed | `codex/fix-process-max-iterations-zero` pushed to `jumperz11`; no upstream PR opened. |
| 058 | [Decay prune reports success but leaves insight](packets/058-decay-prune-not-persisted.md) | Fork branch pushed | `codex/fix-decay-prune-persistence` pushed to `jumperz11`; no upstream PR opened. |
| 059 | [Sync context negative gates export low-quality memory](packets/059-sync-context-negative-gates-export-low-quality.md) | Fork branch pushed | `codex/fix-sync-context-threshold-validation` pushed to `jumperz11`; no upstream PR opened. |
| 060 | [Growth timeline writes state into source checkout](packets/060-growth-timeline-writes-checkout.md) | Fork branch pushed | `codex/fix-growth-tracker-home-path` pushed to `jumperz11`; no upstream PR opened. |
| 061 | [Personality state writes into source checkout](packets/061-personality-state-writes-checkout.md) | Fork branch pushed | `codex/fix-voice-aha-home-path` pushed to `jumperz11`; no upstream PR opened. |
| 062 | [Eval accepts invalid thresholds](packets/062-eval-invalid-thresholds.md) | Fork branch pushed | `codex/fix-eval-threshold-validation` pushed to `jumperz11`; no upstream PR opened. |
| 063 | [Process runtime limits still run worker](packets/063-process-runtime-limits.md) | Fork branch pushed | `codex/fix-process-runtime-validation` pushed to `jumperz11`; no upstream PR opened. |
| 064 | [Decay accepts invalid bounds](packets/064-decay-invalid-bounds.md) | Fork branch pushed | `codex/fix-decay-input-validation` pushed to `jumperz11`; no upstream PR opened. |
| 065 | [Validate-ingest negative limit traceback](packets/065-validate-ingest-negative-limit.md) | Fork branch pushed | `codex/fix-validate-ingest-limit` pushed to `jumperz11`; no upstream PR opened. |
| 066 | [Personality evolution input tracebacks](packets/066-personality-evolution-input-tracebacks.md) | Fork branch pushed | `codex/fix-personality-evolution-input` pushed to `jumperz11`; no upstream PR opened. |
| 067 | [Config malformed dot-path writes empty keys](packets/067-config-malformed-dot-path.md) | Fork branch pushed | `codex/fix-config-key-validation` pushed to `jumperz11`; no upstream PR opened. |
| 068 | [Config malformed JSON traceback](packets/068-config-malformed-json-traceback.md) | Fork branch pushed | `codex/fix-config-json-errors` pushed to `jumperz11`; no upstream PR opened. |
| 069 | [Config non-object runtime crash](packets/069-config-non-object-runtime-crash.md) | Fork branch pushed | `codex/fix-config-object-shape` pushed to `jumperz11`; no upstream PR opened. |
| 070 | [Logs tail bounds ignored](packets/070-logs-tail-bounds.md) | Fork branch pushed | `codex/fix-logs-tail-validation` pushed to `jumperz11`; no upstream PR opened. |
| 071 | [Logs invalid since filter ignored](packets/071-logs-since-invalid-filter.md) | Fork branch pushed | `codex/fix-logs-since-validation` pushed to `jumperz11`; no upstream PR opened. |
| 072 | [Validation scan negative limit reports success](packets/072-validation-scan-negative-limit.md) | Fork branch pushed | `codex/fix-validation-scan-limit` pushed to `jumperz11`; no upstream PR opened. |
| 073 | [Learnings limit ignored](packets/073-learnings-limit-ignored.md) | Fork branch pushed | `codex/fix-learnings-limit-validation` pushed to `jumperz11`; no upstream PR opened. |
| 074 | [Events limit ignored](packets/074-events-limit-ignored.md) | Fork branch pushed | `codex/fix-events-limit-validation` pushed to `jumperz11`; no upstream PR opened. |
| 075 | [Outcome unlinked limit ignored](packets/075-outcome-unlinked-limit-ignored.md) | Fork branch pushed | `codex/fix-outcome-unlinked-limit` pushed to `jumperz11`; no upstream PR opened. |
| 076 | [Outcome links limit ignored](packets/076-outcome-links-limit-ignored.md) | Fork branch pushed | `codex/fix-outcome-links-limit` pushed to `jumperz11`; no upstream PR opened. |
| 077 | [Advice feedback pending limit ignored](packets/077-advice-feedback-pending-limit.md) | Fork branch pushed | `codex/fix-advice-pending-limit` pushed to `jumperz11`; no upstream PR opened. |

## Active Queue

| Priority | Mission | Target |
| --- | --- | --- |
| P0 | Convert the PR-ready fix queue into the reviewer-preferred submission surface | Packets 001, 002, 009, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076, 077 |
| P0 | Verify advice-feedback pending respects zero and rejects negative limits | Packet 077 |
| P0 | Verify outcome-links respects zero and rejects negative limits | Packet 076 |
| P0 | Verify outcome-unlinked respects zero and rejects negative limits | Packet 075 |
| P0 | Verify events display respects zero and rejects negative limits | Packet 074 |
| P0 | Verify learnings display respects zero and rejects negative limits | Packet 073 |
| P0 | Verify validation scan rejects negative limits before loop execution | Packet 072 |
| P0 | Verify logs rejects invalid since filters instead of returning all lines | Packet 071 |
| P0 | Verify logs tail bounds reject negative values and preserve zero | Packet 070 |
| P0 | Verify non-object runtime tuneables cannot crash CLI startup | Packet 069 |
| P0 | Verify config reports malformed runtime JSON without tracebacks or overwrite | Packet 068 |
| P0 | Verify config rejects malformed dot paths before writing runtime tuneables | Packet 067 |
| P0 | Verify personality evolution rejects malformed signals cleanly | Packet 066 |
| P0 | Verify validate-ingest rejects negative scan limits cleanly | Packet 065 |
| P0 | Verify decay rejects invalid bounds before pruning | Packet 064 |
| P0 | Verify process rejects invalid runtime bounds before worker mutation | Packet 063 |
| P0 | Verify eval rejects invalid thresholds before reporting metrics | Packet 062 |
| P0 | Verify personality state stores under user home | Packet 061 |
| P0 | Verify growth timeline stores state under user home | Packet 060 |
| P0 | Verify sync-context rejects invalid quality gates | Packet 059 |
| P0 | Verify decay pruning persists deleted insights | Packet 058 |
| P0 | Verify process drain respects zero and negative max iterations | Packet 057 |
| P0 | Verify outcome rejects negative link counts before recording | Packet 056 |
| P0 | Verify outcome auto-link respects zero and negative windows | Packet 055 |
| P0 | Verify outcome validation respects zero and negative limits | Packet 054 |
| P0 | Verify auto-link respects zero and negative limits | Packet 053 |
| P0 | Verify auto-link rejects invalid similarity thresholds | Packet 052 |
| P0 | Verify sync-banks rejects invalid thresholds and categories | Packet 051 |
| P0 | Verify learn command rejects invalid inputs and filtered insights cleanly | Packet 050 |
| P0 | Verify contradiction resolution rejects missing indexes | Packet 049 |
| P0 | Verify hypothesis outcomes reject missing targets | Packet 048 |
| P0 | Verify project phase rejects unsupported values | Packet 047 |
| P0 | Verify chip target commands return non-zero on missing IDs | Packet 046 |
| P1 | Verify deprecated curiosity fill reports missing gaps | Packet 045 |
| P0 | Verify project answers reject missing question IDs | Packet 044 |
| P0 | Verify outcome links reject invalid targets | Packet 043 |
| P0 | Verify missing opportunity actions return non-zero | Packet 042 |
| P0 | Verify capture review actions are wired | Packet 041 |
| P0 | Verify failed feedback recording returns non-zero | Packet 040 |
| P0 | Verify bridge context preview stays read-only | Packet 039 |
| P0 | Verify remaining CLI view outputs are readable | Packet 038 |
| P0 | Verify project view commands stay read-only | Packet 037 |
| P0 | Verify guided setup commands do not write defaults non-interactively | Packet 036 |
| P0 | Verify EIDOS migration dry-run stays read-only | Packet 035 |
| P0 | Verify EIDOS deferred status stays read-only | Packet 034 |
| P0 | Verify EIDOS evidence stats stays read-only | Packet 033 |
| P0 | Verify EIDOS metrics stays read-only | Packet 032 |
| P0 | Verify EIDOS list views stay read-only | Packet 031 |
| P0 | Verify EIDOS migration validation stays read-only | Packet 030 |
| P0 | Verify EIDOS stats stays read-only in fresh environments | Packet 029 |
| P0 | Verify EIDOS dry-run purge does not initialize stores | Packet 028 |
| P0 | Verify dry-run purge commands do not initialize stores | Packet 027 |
| P0 | Verify status command stays read-only in fresh environments | Packet 026 |
| P0 | Verify project commands reject explicit missing paths before writing state | Packet 025 |
| P0 | Verify memory setup handles missing Clawdbot config | Packet 024 |
| P0 | Verify outcome capture does not write fake non-interactive rows | Packet 023 |
| P0 | Verify opportunity inbox default command recovery | Packet 022 |
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
