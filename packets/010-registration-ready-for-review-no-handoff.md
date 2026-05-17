# Packet 010: Registration Says Ready For Review With No Handoff

## Summary

After a successful team registration, the frontend success message says the team registration packet is ready for review. The site then resets the form, but does not show a stable team ID, proof submission link, reviewer route, or "what next" action.

This creates a gap between "ready for review" messaging and actual reviewer visibility.

## Surface

- Team registration
- Post-registration next step
- Reviewer routing
- Competition onboarding

## Before Evidence

Frontend success message logic:

```js
const savedMessage = saved.persisted
  ? "Saved to database. Team registration packet is ready for review."
  : "Saved locally for this preview. Team registration packet is ready.";
```

After the success message, the form is reset:

```js
els.form.reset();
updateDeviceOptions();
await loadAndRenderLeaderboard();
```

There is no visible code path that renders:

- team ID,
- proof repository field,
- reviewer handoff link,
- update-registration route,
- or submission URL.

## Expected Behavior

After successful registration, show one concrete next action:

```text
Team registered.
Your team id: <stable id or slug>
Submit proof here: <submission route>
Reviewer handoff: <instructions>
```

Or if no submission route exists yet:

```text
Team registered. Keep your GitHub profile link current and include your team name in proof PRs.
```

## Impact

- Teams may think the site has sent something to reviewers when it has only registered the team.
- Teams have no canonical ID to include in proof packets.
- Clean proof repos are not visible to reviewers unless shared out of band.

## Proposed Fix

Return and display a stable public team slug/id after registration, and add a clear post-registration CTA:

```json
{
  "team": {
    "name": "JUMPERZ",
    "slug": "jumperz",
    "submission_url": "/teams/jumperz/submit"
  }
}
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
