# Packet 013: Leaderboard Hides Public Score Band

## Summary

The leaderboard API returns `public_score_band`, but the frontend drops it and renders only numeric points.

For newly registered teams, this hides the useful public state `Registered` and leaves rows looking like plain `0 pts` entries.

## Surface

- Public leaderboard
- Team registration confidence
- Rank/status visibility

## Before Evidence

API response fields include:

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

Frontend mapping drops `public_score_band`:

```js
function fromApiTeam(team, index) {
  return {
    rank: index + 1,
    team: team.team?.name || team.name || "Registered team",
    points: Number(team.public_points ?? team.points ?? 0)
  };
}
```

Rendered row:

```text
16  JUMPERZ  0 pts
```

The visible row does not show `Registered`.

## Expected Behavior

The leaderboard should show the public score band when present:

```text
16  JUMPERZ  Registered  0 pts
```

Or:

```text
JUMPERZ
Registered · 0 pts
```

## Impact

- Teams cannot tell from the UI whether they are merely listed or actually registered.
- The public API has useful state that is not surfaced.
- This increases support/reviewer noise because teams ask whether the board sees them.

## Proposed Fix

Preserve score/status fields in `fromApiTeam`:

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

Then render `scoreBand` in the row when present.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
