# Start Here

Last organized: 2026-06-07 13:25 UTC

This is the canonical reviewer entry point for current JUMPERZ Spark Compete work.

## 60-Second Review Path

Review these four existing `vibeforge1111/spark-cli` PRs first. They are current-base, non-draft, packet-ready, and have `pass` validator status.

| Order | PR | Why this is first |
| --- | --- | --- |
| 1 | [spark-cli #1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | SSH host port validation; clean input-validation lane. |
| 2 | [spark-cli #1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | Hosted allowed-host guard; clean validation lane. |
| 3 | [spark-cli #1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | SSH doctor path redaction; clean diagnostic lane. |
| 4 | [spark-cli #1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | Spark OS compile local-root redaction; clean proof-safety lane. |

All four are based on public upstream `fc49c16` / `spark-cli-public-installer-2026-06-03-r24-v2`. Each PR body starts with `Reviewer Fast Path` so the proof summary appears before packet JSON.

## After Those Four

Use [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md) for the full current-base top 10 and remaining gates.

Use [TOP_REVIEW_QUEUE.md](TOP_REVIEW_QUEUE.md) only when you need branch names, validator states, and routing detail.

Use [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md) only when you need the full timeline.

## Do Not Start With

- the raw open PR list
- legacy fork packet IDs
- older-base PRs unless a reviewer asks for focused rebase
- `pass_with_warnings` security-control lanes before the clean `pass` lanes above

## Current Ask

Please review the four PRs above first. No new PRs are being opened while this queue waits for review signal.
