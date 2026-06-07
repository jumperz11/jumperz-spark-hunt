# JUMPERZ Spark Compete Review Hub

Public review hub for the JUMPERZ Spark Compete work.

## Reviewer Start

Start here: [START_HERE.md](START_HERE.md)

The fastest useful review path is four current-base `spark-cli` PRs with `pass` validator status:

1. [spark-cli #1051](https://github.com/vibeforge1111/spark-cli/pull/1051)
2. [spark-cli #1058](https://github.com/vibeforge1111/spark-cli/pull/1058)
3. [spark-cli #1059](https://github.com/vibeforge1111/spark-cli/pull/1059)
4. [spark-cli #1081](https://github.com/vibeforge1111/spark-cli/pull/1081)

Do not start with the raw open PR list. Use the curated route above first.

This repository is not an upstream patch branch. It is a clean control room for reviewer routing, packet drafts, proof notes, and PR status while fixes live in the owning `vibeforge1111/*` repositories.

## Current Status

- Team: `JUMPERZ`
- Members: `JUMPERZ`, `Basjee01`, `acexqt`
- Device-holder GitHub: [`jumperz11`](https://github.com/jumperz11)
- Current mode: focused upstream PR repair and reviewer follow-up
- Canonical start page: [START_HERE.md](START_HERE.md)
- Reviewer start page: [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md)
- Review pattern audit: [REVIEW_PATTERN_AUDIT.md](REVIEW_PATTERN_AUDIT.md)
- Main tracker: [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md)

## How To Review

Start with [START_HERE.md](START_HERE.md). It gives the shortest current review route and the first four PRs to inspect. Use [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md) for the full top 10, and [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md) only when you need the detailed timeline.

The current priority is quality over volume:

- keep every PR scoped to one root cause and one owner surface
- respond to maintainer comments before opening new work
- include safe before/after proof only
- avoid raw logs, private maps, secrets, screenshots with sensitive data, archives, binaries, and unrelated scoring discussion
- update packet wording when the validator or reviewer flags a trust-boundary issue

## Active Work Areas

- Spark CLI repair and onboarding behavior
- Spark Agent Site release and docs surfaces
- Spark Voice Comms hook boundaries
- Spark Personality hook boundaries
- Spark Researcher citation and advisory-boundary handling
- Spawner UI dependency baseline
- Spark Intelligence Builder attachment-hook handling
- Spark Character live-search prompt boundaries

## Useful Files

- [START_HERE.md](START_HERE.md) - canonical reviewer entry point
- [REVIEWER_START_HERE.md](REVIEWER_START_HERE.md) - shortest current reviewer path
- [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md) - live PR control room
- [REVIEW_PATTERN_AUDIT.md](REVIEW_PATTERN_AUDIT.md) - what recent reviews, merges, and adoptions show
- [REVIEWER_BRIEF.md](REVIEWER_BRIEF.md) - older reviewer context and routing history
- [REVIEWER_HANDOFF.md](REVIEWER_HANDOFF.md) - handoff notes
- [JUMPERZ_SCORECARD.md](JUMPERZ_SCORECARD.md) - scorecard-style summary
- [MISSION_COVERAGE.md](MISSION_COVERAGE.md) - historical mission coverage notes
- [packets/](packets/) - older packet drafts and finding notes

## Operating Rule

Before opening or changing any PR, check the latest GitHub comments first. If a reviewer has asked for repair, proof, split, owner review, or packet changes, handle that before starting a new lane.
