# Reviewer Brief

## Task

Route or score JUMPERZ's first 10 Spark Compete fixes.

## Important Framing

JUMPERZ is not claiming 86 missions.

JUMPERZ has **86 documented Spark Compete findings/fix packets** produced while following the hunt loop. The Spark Compete site's 60 missions are starter prompts, not the boundary.

## Current Ask

Should JUMPERZ open upstream PRs for the first 10 fixes, or should reviewers score from fork compare links first?

## Why Reviewer-Routed

`vibeforge1111/vibeship-spark-intelligence` is not listed in `https://compete.sparkswarm.ai/allowed-repos.json`.

Per the Spark Compete submission spec, unclear or private owner surfaces should use a reviewer-routed packet through a public `vibeforge1111/Spark-Agent-Site` issue or PR.

Canonical reviewer-routed intake issue:
https://github.com/vibeforge1111/Spark-Agent-Site/issues/46

## Direct Allowed-Repo Fallback

Because reviewer routing has not replied yet, JUMPERZ also opened one focused public PR in an allowed repo:

https://github.com/vibeforge1111/spark-cli/pull/392

This PR fixes a current `spark-cli` Windows test reliability issue where a `bash.exe` shim can exist on PATH but fail to execute. The packet in the PR body validates as `packet_valid: true` with `pass_with_warnings` because installer-related changes require security-owner/lab review.

## Start Here

1. Mission coverage:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/MISSION_COVERAGE.md
2. Top 10 queue:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/TOP_REVIEW_QUEUE.md
3. PR-ready packet bodies:
   https://github.com/jumperz11/jumperz-spark-hunt/blob/main/PR_READY.md
4. Reviewer handoff:
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
