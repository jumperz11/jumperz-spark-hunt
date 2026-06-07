# Reviewer Brief

## Task

Review JUMPERZ's current allowed-repo Spark Compete queue without adding more submission volume.

## Current Snapshot

Last organized: 2026-06-07 12:41 UTC

- Shortest reviewer path: [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md)
- Current allowed repo focus: `vibeforge1111/spark-cli`
- Open `spark-cli` PRs authored by `jumperz11`: 128
- Draft PRs: 0
- PRs with `spark-compete-hotfix-v1` packet JSON in the body: 127
- Sole missing packet: [#756](https://github.com/vibeforge1111/spark-cli/pull/756), which is not a `[spark-compete]` PR
- Fresh owner/reviewer comments requiring JUMPERZ action since 2026-06-07 00:00 UTC: none found
- Current reviewer path: start with the live allowed-repo top queue in [TOP_REVIEW_QUEUE.md](TOP_REVIEW_QUEUE.md), not the older fork-only queue.

## Important Framing

JUMPERZ is not claiming 86 missions.

JUMPERZ has **86 documented Spark Compete findings/fix packets** produced while following the hunt loop. The Spark Compete site's 60 missions are starter prompts, not the boundary.

## Current Ask

Please review the current top allowed-repo queue first:

1. [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) - SSH host port validation, current `fc49c16`, `pass`
2. [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) - hosted allowed-host guard, current `fc49c16`, `pass`
3. [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) - SSH doctor path redaction, current `fc49c16`, `pass`
4. [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) - Spark OS compile local-root redaction, current `fc49c16`, `pass`
5. [#1069](https://github.com/vibeforge1111/spark-cli/pull/1069) - sandbox output local-path redaction, current `fc49c16`, `pass_with_warnings`
6. [#1052](https://github.com/vibeforge1111/spark-cli/pull/1052) - sandbox authorization-header redaction, current `fc49c16`, `pass_with_warnings`
7. [#1086](https://github.com/vibeforge1111/spark-cli/pull/1086) - ssh-add approval boundary, current `fc49c16`, `pass_with_warnings`
8. [#1215](https://github.com/vibeforge1111/spark-cli/pull/1215) - ssh-keygen private-key approval boundary, current `fc49c16`, `pass_with_warnings`
9. [#1255](https://github.com/vibeforge1111/spark-cli/pull/1255) - SSH tunnel approval boundary, current `fc49c16`, `pass_with_warnings`
10. [#1053](https://github.com/vibeforge1111/spark-cli/pull/1053) - git clean approval boundary, current `fc49c16`, `pass_with_warnings`

The old question about whether to open upstream PRs for fork-only packets remains historical context. It should not block review of the current allowed-repo PR queue.

## Why Reviewer-Routed

`vibeforge1111/vibeship-spark-intelligence` is not listed in `https://compete.sparkswarm.ai/allowed-repos.json`.

Per the Spark Compete submission spec, unclear or private owner surfaces should use a reviewer-routed packet through a public `vibeforge1111/Spark-Agent-Site` issue or PR.

Canonical reviewer-routed intake issue:
https://github.com/vibeforge1111/Spark-Agent-Site/issues/46

## Direct Allowed-Repo Fallback

Because reviewer routing has not replied yet, JUMPERZ also opened one focused public PR in an allowed repo:

https://github.com/vibeforge1111/spark-cli/pull/392

This PR fixes a current `spark-cli` Windows test reliability issue where a `bash.exe` shim can exist on PATH but fail to execute. Mac Lab passed, and maintainers adopted the fix into master through https://github.com/vibeforge1111/spark-cli/pull/407. Credit remains tied to original PR #392 as the reviewed submission.

JUMPERZ also opened one focused public docs-routing PR in an allowed repo:

https://github.com/vibeforge1111/Spark-Agent-Site/pull/47

This PR fixes a stale Domain chips feedback route from `spark-skill-graphs` to `spark-domain-chip-labs`. Mac Lab passed, and maintainers adopted the fix through https://github.com/vibeforge1111/Spark-Agent-Site/pull/55. Private account-pending credit was recorded.

JUMPERZ also opened one focused public Telegram copy/knowledge PR in an allowed repo:

https://github.com/vibeforge1111/spark-telegram-bot/pull/224

This PR removes retired `spark-skill-graphs` naming from Telegram pro-tier copy and self-awareness knowledge. The packet in the PR body validates as `packet_valid: true` and `pass_with_warnings` with `telegram_proof_unavailable` because no safe disposable Telegram test chat is available.

Current PR #224 routing note: upstream `main` now contains patch-equivalent maintainer commit `014f17f` (`Remove stale skill catalog copy`). A May 29 reshape-first comment says the old PR branch mixes agent-knowledge cleanup, tier logic, and tests. JUMPERZ should not force-push it unless reviewers ask; the clean handling is to confirm whether PR #224 should be closed as adopted/overtaken by `014f17f` with credit tied to the original reviewed submission.

JUMPERZ also opened one focused follow-up docs-routing PR in an allowed repo:

https://github.com/vibeforge1111/Spark-Agent-Site/pull/56

This PR routes Memory chip feedback to `spark-domain-chip-labs` instead of `domain-chip-memory`, which is outside the Spark Compete allowed public repo list. The packet in the PR body validates as `packet_valid: true` and `pass` with zero warnings.

JUMPERZ also opened one higher-impact registry-readiness PR in an allowed repo:

https://github.com/vibeforge1111/spark-cli/pull/419

This PR updates lagging blessed registry pins and matching attestations so `spark verify --registry-pins --json` passes on current upstream `master`. The packet in the PR body validates as `packet_valid: true` and `pass_with_warnings` with `security_owner_review_expected`; full pytest passes with `627 passed, 7 skipped, 104 subtests passed`.

Current public-points blocker: reviewer comments identify `team_account_unverified` / account gates. The PR author account `jumperz11` must be listed on the registered JUMPERZ team before public points can appear. The public team form rejects a JUMPERZ resubmission with `team_exists`, so reviewer-side verification or an edit to the existing JUMPERZ team record is needed. Gate re-check requested on PR #47: https://github.com/vibeforge1111/Spark-Agent-Site/pull/47#issuecomment-4553973648

## Start Here

1. Mission coverage:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/MISSION_COVERAGE.md
2. Reviewer scorecard:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/JUMPERZ_SCORECARD.md
3. Top 10 queue:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/TOP_REVIEW_QUEUE.md
4. PR-ready packet bodies:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/PR_READY.md
5. Reviewer handoff:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEWER_HANDOFF.md

## Top 10 Packet Status

- Packet 001: `pass`
- Packet 021: `pass`
- Packet 009: `pass`
- Packet 022: `packet_valid: true`, `pass_with_warnings`, `security_owner_review_expected`
- Packet 040: `pass`
- Packet 041: `pass`
- Packet 042: `pass`
- Packet 043: `pass`
- Packet 048: `pass`
- Packet 049: `pass`

## Recommended Reviewer Action

Answer one of:

- `Open PRs in TOP_REVIEW_QUEUE order.`
- `Do not open PRs yet; reviewers will score from compare links.`
- `Rework these packets first: <list>.`

## Do Not Misread

- Do not treat packet IDs as site mission IDs.
- Do not read this as a claim that JUMPERZ completed 86 missions.
- Do not route random upstream PRs while owner routing is unclear.
- Do not score by packet volume alone; JUMPERZ is asking reviewers to start with the curated top 10.
