# Packet 004: Proof Kit Has No Submission Handoff

## Summary

The proof kit explains how to capture before/after evidence and link proof in a PR body, but the site does not provide a visible submission handoff for teams that have proof links but do not yet have a reviewer-assigned repo or PR route.

This is a site UX/routing issue, especially for teams using a clean proof hub while waiting for reviewer routing.

## Surface

- Proof kit section
- Agent playbook section
- Public API discovery
- Team-to-reviewer handoff

## Before Evidence

The visible proof kit includes:

```text
Capture the broken state
Capture the improved state
Link proof in the PR body
```

The guardrails include:

```text
Use screenshots, redacted bounded terminal excerpts, tests, GitHub links,
access-controlled Google Docs, or permissioned chat links.
```

But no visible field, form, endpoint, or link lets a registered team attach a proof URL from the site after registration.

Read-only endpoint probes:

```text
/api/proof       404 {"error":"not_found"}
/api/submissions 404 {"error":"not_found"}
/api/prs         404 {"error":"not_found"}
```

## Expected Behavior

The site should give teams one clear handoff after proof is created, such as:

- a `Submit proof` link,
- a `submission_url` field,
- an issue template link,
- a reviewer-routing form,
- or a clear instruction saying exactly where to post clean proof hubs when no upstream PR should be opened.

## Impact

- Registered teams can produce clean proof but have no obvious site-native way to hand it to reviewers.
- Teams may open upstream PRs prematurely just to create a visible artifact.
- Teams may create duplicate or noisy submissions because the canonical handoff is unclear.
- Reviewers may need to reconstruct identity, proof, and routing from separate links.

## Proposed Fix

Add a post-registration proof handoff path:

```text
Team registered -> Add proof link -> Reviewer routes / accepts / requests more info
```

Minimal version:

```json
{
  "team_name": "JUMPERZ",
  "proof_url": "https://github.com/jumperz11/jumperz-spark-hunt",
  "packet_url": "https://github.com/jumperz11/jumperz-spark-hunt/blob/main/REVIEW_BOARD.md"
}
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
