# Active Review

Last checked: 2026-06-07 13:35 UTC

This file tracks the current reviewer-facing state only. Older timeline details were removed from the top-level docs so reviewers do not land on stale fork-era routing or outdated proof notes.

## Current Reviewer Path

Canonical start page: [START_HERE.md](START_HERE.md)

Review these four current-base `vibeforge1111/spark-cli` PRs first:

1. [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) - SSH host port validation, `pass`
2. [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) - hosted allowed-host guard, `pass`
3. [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) - SSH doctor path redaction, `pass`
4. [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) - Spark OS compile local-root redaction, `pass`

Use [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md) for the full current-base top 10 and [TOP_REVIEW_QUEUE.md](TOP_REVIEW_QUEUE.md) for branch-level detail.

## Current State

- Public upstream baseline: `fc49c16` / `spark-cli-public-installer-2026-06-03-r24-v2`
- Current mode: review conversion, not new PR volume
- Fresh actionable reviewer comments found in latest sweep: none
- Top four PRs: current-base, non-draft, packet-ready, validator `pass`
- Top 10 PR bodies: include `Reviewer Fast Path`
- Older-base useful PRs: do not rebase unless reviewers ask
- New PRs: do not open while this queue is waiting for review signal

## Latest Meaningful Changes

- 2026-06-07 13:35 UTC: removed outdated top-level Markdown clutter and old static-hub packet/archive sections. The root docs now keep the current reviewer route small and clear.
- 2026-06-07 13:25 UTC: added root-level [START_HERE.md](START_HERE.md) and made it the canonical first screen in README and the static hub.
- 2026-06-07 13:15 UTC: recorded [REVIEW_PATTERN_AUDIT.md](REVIEW_PATTERN_AUDIT.md), showing that reviewer-readable triage beats raw PR volume.
- 2026-06-07 12:55 UTC: added `Reviewer Fast Path` sections to the current top 10 PR bodies.

## Safety Rules

- Do not add token/admin/private/local-path material to packets, comments, screenshots, logs, or tracker notes.
- Do not comment-bump PRs.
- Reply only to actionable reviewer asks: proof, packet repair, focused rebase, scope split, security redesign, account/team routing, or safety notes.
- Treat protected-branch `BLOCKED` as a gate state unless GitHub reports `DIRTY`, `CONFLICTING`, or a reviewer asks for repair.
