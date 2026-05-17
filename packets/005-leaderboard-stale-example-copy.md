# Packet 005: Leaderboard Copy Says Real Teams Are Example Rows

## Summary

The Bounty Board renders live registered teams, including JUMPERZ, but the visible copy still says the rows are example standings "until competing teams arrive."

This makes the live board feel like placeholder data even after real teams have registered.

## Surface

- Competition leaderboard
- Registration confirmation confidence
- Team standings visibility

## Before Evidence

Visible leaderboard copy:

```text
Live database ready once teams register.
This board refreshes periodically with approved-PR points. The rows below are example standings until competing teams arrive.
```

Visible rows include real registered teams:

```text
1  Bugman  0 pts
2  Giwa  0 pts
...
16 JUMPERZ 0 pts
```

API confirms JUMPERZ is a real registered row:

```json
{
  "schema": "spark-compete-leaderboard-row-v1",
  "event": "spark-compete-first-event",
  "registered_at": "2026-05-17T21:47:08.168Z",
  "updated_at": "2026-05-17T21:47:08.168Z",
  "team": {
    "name": "JUMPERZ"
  },
  "public_points": 0,
  "public_score_band": "Registered",
  "rank": 16
}
```

## Expected Behavior

Once the API returns real leaderboard rows, copy should switch away from placeholder wording.

Example:

```text
Live team standings
This board refreshes periodically with approved-PR points. Registered teams appear here while reviewer-approved value is counted.
```

If there are no real teams, then placeholder copy can remain:

```text
Example standings will be replaced once teams register.
```

## Impact

- Teams may think their registration did not create a real public board row.
- Reviewers and participants may treat current standings as mock data.
- The "live database ready" badge conflicts with "example standings" wording.

## Proposed Fix

Use API row state to choose the leaderboard note:

```js
const hasLiveTeams = rows.some((row) => !row.isPreview);
```

Then render:

- live-copy when `hasLiveTeams` is true,
- preview-copy only when all rows are mock rows.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
