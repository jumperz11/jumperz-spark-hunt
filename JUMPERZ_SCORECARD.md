# JUMPERZ Spark Compete Scorecard

Updated: 2026-06-07T12:41:00Z

Purpose: give Spark Compete reviewers one fast, machine-readable view of JUMPERZ work that already has reviewer-visible signal.

## Identity

- Team: JUMPERZ
- Members: JUMPERZ, Basjee01, acexqt
- PR author GitHub: jumperz11
- Team PR GitHub accounts requested: jumperz11
- Device-holder GitHub: https://github.com/jumperz11
- Packet framing: JUMPERZ has **86 documented Spark Compete findings/fix packets**, not 86 missions.

## Current Gate

Primary public-points blocker: `team_account_unverified` / account-team mapping.

Needed reviewer/admin action:

```text
Verify or update the existing JUMPERZ team record so PR author GitHub account jumperz11 maps to team JUMPERZ.
```

Why this needs reviewer/admin action: the public Spark Compete team form rejects a JUMPERZ resubmission with `team_exists`, so JUMPERZ cannot self-edit the already registered team record from the public form.

Gate re-check request:
https://github.com/vibeforge1111/Spark-Agent-Site/pull/47#issuecomment-4553973648

## Current Review Queue Health

The current allowed-repo focus is conversion of existing `vibeforge1111/spark-cli` PRs on the public `fc49c16` r24-v2 baseline, not new volume.

Shortest reviewer path: [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md)

| Metric | Current value |
| --- | --- |
| Open `spark-cli` PRs by `jumperz11` | 128 |
| Drafts | 0 |
| PRs with `spark-compete-hotfix-v1` packet JSON | 127 |
| Sole missing packet | [#756](https://github.com/vibeforge1111/spark-cli/pull/756), non-competition `[codex]` PR |
| Fresh owner/reviewer comments needing JUMPERZ action since 2026-06-07 00:00 UTC | 0 |

Reviewer first-pass queue:

| Order | PR | Validator | Why first |
| --- | --- | --- | --- |
| 1 | [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | `pass` | SSH host port validation; current `fc49c16` r24-v2 base. |
| 2 | [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | `pass` | Hosted allowed-host guard; current `fc49c16` r24-v2 base. |
| 3 | [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | `pass` | SSH doctor path redaction; current `fc49c16` r24-v2 base. |
| 4 | [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | `pass` | Spark OS compile local-root redaction; current `fc49c16` r24-v2 base. |
| 5 | [#1069](https://github.com/vibeforge1111/spark-cli/pull/1069) | `pass_with_warnings` | Sandbox output local-path redaction; current `fc49c16` r24-v2 base. |
| 6 | [#1052](https://github.com/vibeforge1111/spark-cli/pull/1052) | `pass_with_warnings` | Sandbox authorization-header redaction; current `fc49c16` r24-v2 base. |
| 7 | [#1086](https://github.com/vibeforge1111/spark-cli/pull/1086) | `pass_with_warnings` | SSH agent mutation approval boundary; current `fc49c16` r24-v2 base. |
| 8 | [#1215](https://github.com/vibeforge1111/spark-cli/pull/1215) | `pass_with_warnings` | Private-key generation approval boundary; current `fc49c16` r24-v2 base. |
| 9 | [#1255](https://github.com/vibeforge1111/spark-cli/pull/1255) | `pass_with_warnings` | SSH tunnel approval boundary; current `fc49c16` r24-v2 base. |
| 10 | [#1053](https://github.com/vibeforge1111/spark-cli/pull/1053) | `pass_with_warnings` | `git clean` approval boundary; current `fc49c16` r24-v2 base. |

## Direct Allowed-Repo PRs

| PR | Repo | Status | Validator | Tests / Proof | Remaining Gate |
| --- | --- | --- | --- | --- | --- |
| https://github.com/vibeforge1111/Spark-Agent-Site/pull/47 | Spark-Agent-Site | Mac Lab passed; adopted through trusted maintainer PR #55; private account-pending credit recorded | `packet_valid: true`, `pass` | docs readiness, security release surface, command docs, command smoke | account/team mapping and public release gates |
| https://github.com/vibeforge1111/spark-cli/pull/392 | spark-cli | Mac Lab passed; adopted into master through maintainer PR #407; credit tied to original PR | `packet_valid: true`, `pass_with_warnings`, `security_owner_review_expected` | `PYTHONPATH=src python -m pytest -q` -> 623 passed, 7 skipped, 99 subtests passed | security owner review, account/team mapping, public release gates |
| https://github.com/vibeforge1111/spark-telegram-bot/pull/224 | spark-telegram-bot | Mac Lab passed; upstream `main` now contains patch-equivalent maintainer commit `014f17f`; PR remains open with May 29 reshape-first note | `packet_valid: true`, `pass_with_warnings`, `telegram_proof_unavailable` | build plus targeted and full bot tests | maintainer/lab Telegram proof, account/team mapping, public release gates; ask reviewer whether to close as adopted/overtaken |
| https://github.com/vibeforge1111/Spark-Agent-Site/pull/56 | Spark-Agent-Site | Open and mergeable; waiting for review | `packet_valid: true`, `pass`, 0 warnings | docs readiness, security release surface, command docs | review/lab/adoption and account/team mapping |
| https://github.com/vibeforge1111/spark-cli/pull/419 | spark-cli | Valid packet, but reviewer marked not merge-ready after maintainer registry adoption PR #421 | `packet_valid: true`, `pass_with_warnings`, `security_owner_review_expected` | original branch proved registry pins `ok: true`, provenance `ok: true`, full pytest -> 627 passed, 7 skipped, 104 subtests passed; current upstream `master` now verifies registry pins `ok: true` after #421 | no safe rebase claim remains unless fresh registry drift appears; account/team mapping |

## Reviewer Quotes / Outcomes

Spark-Agent-Site PR #47:

- "Spark Compete status: **Mac Lab passed**."
- "Adopted through trusted maintainer PR #55 and merged as `8727caac12a0dca9fc68d5615b228cb95fcffd89`."
- "Private account-pending credit has been recorded for this merged adoption."
- "Public/team points remain locked at 0 until team/account mapping and the public release gates are cleared."

spark-cli PR #392:

- "Spark Compete status: **Mac Lab passed**."
- "Adopted into master via maintainer PR #407."
- "Spark Compete credit remains tied to this original PR as the reviewed submission."

spark-telegram-bot PR #224:

- "Spark Compete status: **Mac Lab passed**."
- Current public points lock: `team_account_unverified`.
- Upstream `main` now contains patch-equivalent maintainer commit `014f17f` (`Remove stale skill catalog copy`).
- New May 29 reviewer note says the old PR branch needs split/rebase before owner review because it mixes agent-knowledge cleanup, tier logic, and tests. Do not force-push the branch unless reviewers ask; safest handling is to ask whether PR #224 should be treated as adopted/overtaken by `014f17f` and closed, with credit tied to the original reviewed submission.

spark-cli PR #419:

- "Spark Compete status: **valid packet with security-owner/lab warning, but not merge-ready**."
- Reviewer noted the branch conflicts with the already-merged registry adoption path in PR #421.
- Current upstream `master` now passes `spark verify --registry-pins --json`, so JUMPERZ should not force-push a stale registry branch unless a fresh, current registry-pin claim appears.

## Best Reviewer Path

1. Clear account/team mapping for `jumperz11` -> `JUMPERZ`.
2. Keep PR #47 and PR #392 credit tied to the original reviewed submissions, as reviewer comments already state.
3. Review PR #56 as a narrow additional allowed-repo fallback PR with a clean passing packet.
4. Treat PR #419 as a valid-but-overtaken registry-readiness submission unless a fresh registry drift appears after PR #421.
5. For PR #224, ask reviewers whether the PR should be closed as adopted/overtaken by upstream commit `014f17f`; if they require branch repair instead, split it to one scope before pushing.
6. Route the original top queue only after reviewer confirmation; do not treat the 86 packet count as a claim of 86 missions.

## Proof Hub Links

- Reviewer handoff: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_HANDOFF.md
- Reviewer start page: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_START_HERE.md
- Reviewer brief: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_BRIEF.md
- Mission coverage: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/MISSION_COVERAGE.md
- Top review queue: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/TOP_REVIEW_QUEUE.md
- PR-ready queue: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/PR_READY.md
- Submission packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/SUBMISSION.md
