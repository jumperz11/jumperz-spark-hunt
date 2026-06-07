# Review Pattern Audit

Last checked: 2026-06-07 13:15 UTC

This note summarizes what the live GitHub search showed about why JUMPERZ PRs were reviewed, merged, adopted, or left waiting.

## Current Finding

The active blocker is not missing comments or missing public proof on the curated top queue. It is reviewer queue shape plus normal Spark Compete gates.

The useful path is:

1. Keep the current-base top 10 first.
2. Avoid new PR volume until those lanes move or reviewers ask for more.
3. Reply only to actionable reviewer asks: focused rebase, proof, packet repair, security redesign, account/team routing, or safety notes.
4. Treat `BLOCKED` on protected branches as a review/gate state unless GitHub reports `DIRTY`, `CONFLICTING`, or reviewers request a focused rebase.

## What Got Reviewed Before

Credited JUMPERZ examples followed one of three patterns:

- Direct merge after a focused, current branch and safe proof, such as `spark-domain-chip-labs` #28/#30 and `Spark-Agent-Site` #63.
- Maintainer adoption where the original PR stayed closed but received credit, such as `spark-cli` #392 and #517.
- Security-owner review followed by final ledger credit, where the earlier gate wording was not a final rejection.

The reviewer comments that mattered were not generic bumps. They asked for one of:

- focused rebase or clean replacement
- security-first redesign
- targeted proof or tests
- bounded safety notes around trust boundaries
- waiting for security-owner/lab/account/scoring gates

## What Others Are Doing

The open Spark Compete queue is broad across multiple authors, and large batches from other authors also have many zero-comment PRs. The merged sample is different: it is dominated by maintainer adoption PRs and smaller contributor fixes with clear scope.

This means raw volume is not the advantage right now. Reviewer-readable triage is the advantage.

## Next Reviewer-Optimal Move

Keep the top of the queue quiet and easy to review:

- Send reviewers to `REVIEWER_START_HERE.md`.
- Prefer #1051, #1058, #1059, and #1081 first because they are current-base, packet-ready, and have `pass` validator status.
- Do not rebase older useful PRs unless reviewers ask.
- Do not open more `spark-cli` security-control lanes until the current top queue gets a review signal.
