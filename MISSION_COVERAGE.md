# Spark Compete Coverage

This file maps JUMPERZ work back to the Spark Compete site brief.

## How To Read This Repo

- The site's 60 starter missions are prompts to begin hunting.
- JUMPERZ packet numbers are finding IDs, not site mission IDs.
- Packets may come from a starter mission, from the agent-readable brief, or from real Spark friction found while using Spark.
- The site says useful Spark bugs, improvements, and focused hotfix PRs are valid beyond the starter mission list.

## Site Ask

| Site ask | JUMPERZ evidence |
| --- | --- |
| Register a 3-person team | Team JUMPERZ registration fields in [SUBMISSION.md](SUBMISSION.md). |
| Use Spark until something breaks | Packets 001-086 document real site, CLI, workflow, proof-routing, and Spark behavior findings. |
| Capture safe before/after proof | Each packet includes bounded repro evidence, expected behavior, impact, and submission status. |
| Ship focused hotfix PRs | [PR_READY.md](PR_READY.md) lists fork branches, commits, tests, compare links, and PR bodies. |
| Let reviewers verify value | [REVIEWER_HANDOFF.md](REVIEWER_HANDOFF.md) gives fast links, strongest packets, and routing request. |

## Mission-Aligned Buckets

| Site mission theme | Packet coverage | Reviewer use |
| --- | --- | --- |
| Team/proof/routing surfaces | 003-019 | Site and submission UX issues that block or confuse team participation and proof handoff. |
| System discovery and first-run readiness | 001, 002, 009, 020-026, 036-039 | CLI readiness, missing commands, first-run diagnostics, and read-only probe safety. |
| Safe operational and dry-run behavior | 027-035, 057-065, 070-072 | Commands that should preview, validate, or bound work before writing state or running workers. |
| Learning, memory, and validation loops | 040-056, 066, 073-086 | Advice feedback, outcomes, hypotheses, contradictions, learnings, events, EIDOS, and display-limit proof surfaces. |
| Reviewer-ready PR queue | 001, 002, 009, 020-086 | Focused branches pushed to `jumperz11/vibeship-spark-intelligence`; no upstream PR opened without routing approval. |

## Recommended Reviewer Path

1. Start with [REVIEWER_HANDOFF.md](REVIEWER_HANDOFF.md) for the strongest packets and routing request.
2. Use [PR_READY.md](PR_READY.md) for branch URLs, commit IDs, suggested PR titles, and verification commands.
3. Score packets as findings/fixes, not as numbered site missions.
4. Treat the 60 site missions as coverage prompts; the submitted packets are the concrete reproduced issues and fixes.

## Current Count

- Site starter missions: 60 prompts.
- JUMPERZ proof packets: 86 findings.
- Packet 001 lives in [HUNT_PROOF.md](HUNT_PROOF.md).
- Packets 002-086 live in [packets/](packets/).

## Guardrail

JUMPERZ is not claiming 86 site missions completed. JUMPERZ is claiming 86 documented Spark Compete findings/fix packets produced while following the site's hunt loop.
