# Packet 003: Proof Repo Is Not Routable From Registration

## Summary

The Spark Compete registration flow has no first-class place to attach a clean proof repository. The only GitHub field is labeled `Device holder GitHub` and accepts a username/profile, but rejects a repository URL such as `https://github.com/jumperz11/jumperz-spark-hunt`.

This creates a routing gap for teams that register first and then create a clean proof hub later.

## Surface

- Competition registration form
- `/api/teams` registration endpoint
- Public leaderboard row
- Reviewer routing / proof handoff

## Team Context

JUMPERZ registered with:

- Team name: JUMPERZ
- Members: JUMPERZ, Basjee01, acexqt
- Device-holder GitHub: https://github.com/jumperz11
- Clean proof repo: https://github.com/jumperz11/jumperz-spark-hunt

## Before Evidence

The visible site form rejects the clean proof repo URL in the GitHub field.

Input:

```text
https://github.com/jumperz11/jumperz-spark-hunt
```

Visible status:

```text
Add the LLM device holder's GitHub username or profile link.
```

The API also rejects the proof repo URL:

```bash
curl -X POST https://compete.sparkswarm.ai/api/teams \
  -H 'Content-Type: application/json' \
  --data '{
    "team": {
      "name": "JUMPERZ",
      "members": ["JUMPERZ", "Basjee01", "acexqt"],
      "llm_device_holder": "JUMPERZ",
      "llm_provider": "Other LLM",
      "contact": "https://github.com/jumperz11/jumperz-spark-hunt"
    }
  }'
```

Observed response:

```json
{
  "error": "invalid_contact",
  "message": "Use the LLM device holder's GitHub username or profile link."
}
```

The public leaderboard row also exposes only team/rank/points state, not any proof route:

```json
{
  "team": {
    "name": "JUMPERZ"
  },
  "public_points": 0,
  "public_score_band": "Registered",
  "rank": 16
}
```

## Expected Behavior

One of these would make routing smoother:

- Add an optional `proof_repo` or `submission_url` field.
- Add a post-registration update flow for proof links.
- Provide a clear reviewer submission route after successful registration.
- Show a stable team identifier teams can include in proof repos and PRs.

## Impact

- Teams can register successfully but have no obvious place to attach proof packets.
- Teams that follow the clean-repo approach need an out-of-band handoff.
- Reviewers may need to infer team ownership from scattered GitHub links.
- Duplicate registration attempts cannot be used to add the proof repo later.

## Proposed Fix

Add a separate optional proof link field:

```json
{
  "team": {
    "contact": "https://github.com/jumperz11",
    "proof_repo": "https://github.com/jumperz11/jumperz-spark-hunt"
  }
}
```

Validation should keep `contact` as a GitHub profile and validate `proof_repo` as a GitHub repository URL.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
