# Packet 014: Leaderboard Ignores API Rank

## Summary

The leaderboard API returns a `rank` field for every row, but the frontend ignores it and recalculates rank from the array index.

This is currently masked because the API happens to return rows in rank order. If the API adds filtering, pagination, tie handling, or non-rank sorting, the UI can show incorrect ranks.

## Surface

- Public leaderboard
- Ranking display
- Reviewer-verified point publishing

## Before Evidence

API rows include rank:

```json
{
  "team": {
    "name": "JUMPERZ"
  },
  "rank": 16,
  "public_points": 0,
  "public_score_band": "Registered"
}
```

Client mapping ignores API rank:

```js
function fromApiTeam(team, index) {
  return {
    rank: index + 1,
    team: team.team?.name || team.name || "Registered team",
    points: Number(team.public_points ?? team.points ?? 0)
  };
}
```

## Expected Behavior

Use API rank when present:

```js
rank: Number(team.rank ?? index + 1)
```

## Impact

- Rank display depends on transport order instead of the explicit ranking field.
- Future pagination/filtering can silently corrupt displayed rank.
- Tie-breaker or hidden adjudication ordering cannot be represented if the client overwrites rank.

## Proposed Fix

Preserve the API rank:

```js
function fromApiTeam(team, index) {
  return {
    rank: Number(team.rank ?? index + 1),
    team: team.team?.name || team.name || "Registered team",
    points: Number(team.public_points ?? team.points ?? 0),
    scoreBand: team.public_score_band || team.public_status || ""
  };
}
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
