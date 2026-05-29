# JUMPERZ Spark Compete Review Hub

Public review hub for the JUMPERZ Spark Compete work.

This repository is not an upstream patch branch. It is a clean control room for reviewer routing, packet drafts, proof notes, and PR status while fixes live in the owning `vibeforge1111/*` repositories.

## Current Status

- Team: `JUMPERZ`
- Members: `JUMPERZ`, `Basjee01`, `acexqt`
- Device-holder GitHub: [`jumperz11`](https://github.com/jumperz11)
- Current mode: focused upstream PR repair and reviewer follow-up
- Main tracker: [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md)

## How To Review

Start with [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md). It lists each active PR, the latest reviewer state, packet status, verification commands, and the next required action.

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

- [ACTIVE_REVIEW.md](ACTIVE_REVIEW.md) - live PR control room
- [REVIEWER_BRIEF.md](REVIEWER_BRIEF.md) - older reviewer context and routing history
- [REVIEWER_HANDOFF.md](REVIEWER_HANDOFF.md) - handoff notes
- [JUMPERZ_SCORECARD.md](JUMPERZ_SCORECARD.md) - scorecard-style summary
- [MISSION_COVERAGE.md](MISSION_COVERAGE.md) - historical mission coverage notes
- [packets/](packets/) - older packet drafts and finding notes

## Operating Rule

Before opening or changing any PR, check the latest GitHub comments first. If a reviewer has asked for repair, proof, split, owner review, or packet changes, handle that before starting a new lane.
