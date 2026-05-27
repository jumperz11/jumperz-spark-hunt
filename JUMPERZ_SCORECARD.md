# JUMPERZ Spark Compete Scorecard

Updated: 2026-05-27T12:20:30Z

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

## Direct Allowed-Repo PRs

| PR | Repo | Status | Validator | Tests / Proof | Remaining Gate |
| --- | --- | --- | --- | --- | --- |
| https://github.com/vibeforge1111/Spark-Agent-Site/pull/47 | Spark-Agent-Site | Mac Lab passed; adopted through trusted maintainer PR #55; private account-pending credit recorded | `packet_valid: true`, `pass` | docs readiness, security release surface, command docs, command smoke | account/team mapping and public release gates |
| https://github.com/vibeforge1111/spark-cli/pull/392 | spark-cli | Mac Lab passed; adopted into master through maintainer PR #407; credit tied to original PR | `packet_valid: true`, `pass_with_warnings`, `security_owner_review_expected` | `PYTHONPATH=src python -m pytest -q` -> 623 passed, 7 skipped, 99 subtests passed | security owner review, account/team mapping, public release gates |
| https://github.com/vibeforge1111/spark-telegram-bot/pull/224 | spark-telegram-bot | Mac Lab passed; PR open and mergeable | `packet_valid: true`, `pass_with_warnings`, `telegram_proof_unavailable` | build plus targeted and full bot tests | maintainer/lab Telegram proof, account/team mapping, public release gates |
| https://github.com/vibeforge1111/Spark-Agent-Site/pull/56 | Spark-Agent-Site | Open and mergeable; waiting for review | `packet_valid: true`, `pass`, 0 warnings | docs readiness, security release surface, command docs | review/lab/adoption and account/team mapping |

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

## Best Reviewer Path

1. Clear account/team mapping for `jumperz11` -> `JUMPERZ`.
2. Keep PR #47 and PR #392 credit tied to the original reviewed submissions, as reviewer comments already state.
3. Review PR #56 as a narrow additional allowed-repo fallback PR with a clean passing packet.
4. For PR #224, use maintainer/lab Telegram proof because JUMPERZ does not have a safe disposable Telegram test chat.
5. Route the original top queue only after reviewer confirmation; do not treat the 86 packet count as a claim of 86 missions.

## Proof Hub Links

- Reviewer handoff: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_HANDOFF.md
- Reviewer brief: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_BRIEF.md
- Mission coverage: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/MISSION_COVERAGE.md
- Top review queue: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/TOP_REVIEW_QUEUE.md
- PR-ready queue: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/PR_READY.md
- Submission packet: https://github.com/jumperz11/jumperz-spark-hunt/blob/main/SUBMISSION.md
