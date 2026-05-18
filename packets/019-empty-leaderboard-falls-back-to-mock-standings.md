# Packet 019: Empty Leaderboard Falls Back To Mock Standings

## Summary

The leaderboard loader falls back to mock preview standings whenever the live API returns an empty `leaderboard` array.

That means a valid live response of "no teams yet" is rendered as fake/example teams instead of an empty registered-team state. This can mislead teams, reviewers, and agents during event resets, new events, outages, or database migrations.

## Surface

- Leaderboard rendering
- Live API to preview fallback
- Event launch/reset state

## Before Evidence

The live loader only accepts API data when the array is non-empty:

```js
const response = await fetch("/api/leaderboard", { headers: { Accept: "application/json" } });
if (response.ok) {
  const body = await response.json();
  if (Array.isArray(body.leaderboard) && body.leaderboard.length) {
    return body.leaderboard.map(fromApiTeam);
  }
}
```

If the API returns:

```json
{"leaderboard":[]}
```

the code falls through to local preview/mock standings:

```js
const localTeams = loadLocalTeams();
if (localTeams.length) return localTeams.map(fromApiTeam);
return previewLeaderboard.map((team) => ({ ...team, isPreview: true }));
```

## Expected Behavior

An empty live leaderboard response should be treated as successful live state:

```js
if (Array.isArray(body.leaderboard)) {
  return body.leaderboard.map(fromApiTeam);
}
```

The UI should then render an explicit empty state such as:

```text
No registered teams yet.
```

Preview standings should only appear in a static local demo mode or when the page is intentionally opened from `file:`.

## Impact

- A healthy empty event can look like it has fake teams.
- Event resets or database migrations can show stale mock rankings.
- Reviewers and participants may not trust whether the board is live.
- Agents reading the page can incorrectly report registered competitors that do not exist.

## Proposed Fix

Treat `[]` as a valid live response and render an empty state:

```js
if (Array.isArray(body.leaderboard)) {
  return body.leaderboard.map(fromApiTeam);
}
```

Then update `renderLeaderboard` to handle zero rows without falling back to `previewLeaderboard`.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
