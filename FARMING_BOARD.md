# JUMPERZ Farming Board

This board tracks legitimate Spark Compete farming work: real findings, safe proof, and reviewer-routable packets. No duplicate spam, fake teams, or upstream pushes.

## Live Status

- Team: JUMPERZ
- Site status: Registered
- Rank snapshot: 16
- Public points snapshot: 0
- Last checked: 2026-05-17 22:18 UTC
- Clean repo: https://github.com/jumperz11/jumperz-spark-hunt

## Completed

| ID | Packet | Status | Notes |
| --- | --- | --- | --- |
| 001 | [Missing `spark os compile --json`](HUNT_PROOF.md) | Proof ready | First mission command from the hunt brief failed before discovery. |
| 002 | [CLI status/health mojibake](packets/002-cli-status-health-mojibake.md) | Proof ready | `spark status` and `spark health` render corrupted icon/checkmark text. |
| 003 | [Proof repo not routable from registration](packets/003-proof-repo-not-routable-from-registration.md) | Proof ready | Registration accepts a profile URL, but rejects clean proof repo URLs and has no submission field. |

## Active Queue

| Priority | Mission | Target |
| --- | --- | --- |
| P0 | Verify CLI first-run/status readability | Spark CLI |
| P0 | Check command-not-found and recovery copy | Spark CLI install flow |
| P1 | Check support bundle redaction wording | Proof kit / support flow |
| P1 | Check public-track routing when upstream is unavailable | Reviewer routing |
| P2 | Check leaderboard duplicate/team update UX | Competition site |

## Farming Rules

- One packet per unique issue.
- Every packet needs before evidence, impact, expected behavior, and validation/proposed fix.
- Keep proof redacted and bounded.
- Do not submit duplicate teams or fake activity.
- Do not open upstream PRs unless explicitly approved.
