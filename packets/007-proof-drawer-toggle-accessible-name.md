# Packet 007: Proof Drawer Toggle Exposes Confusing Close/Open Text

## Summary

The proof kit drawer is open by default and visually shows a `Close` control, but the accessibility/DOM snapshot exposes the summary control as `CloseOpen`.

This creates a confusing toggle name for assistive technology and automated agents trying to understand whether the drawer is open or closed.

## Surface

- Proof kit drawer
- Keyboard/screen-reader navigation
- Agent-readable page state

## Before Evidence

Visible page state:

```text
BUG PROOF KIT
Open the proof kit for PR screenshots and smoke evidence.
[CLOSE]
```

Agent/DOM snapshot:

```text
generic "bug proof kit Open the proof kit for PR screenshots and smoke evidence. CloseOpen"
```

The static HTML includes:

```html
<details class="panel proof-drawer" id="proof-kit" open>
  <summary>
    ...
    <b>Open</b>
  </summary>
</details>
```

## Expected Behavior

The toggle should expose one state-appropriate action:

- when open: `Close proof kit`
- when closed: `Open proof kit`

It should not expose both `Close` and `Open` at once.

## Impact

- Screen-reader users get contradictory action text.
- Agent-based QA sees ambiguous state.
- The proof section is a core competition workflow, so proof instructions should be especially clear.

## Proposed Fix

Use state-specific text and hide decorative duplicate labels from assistive tech.

Example:

```html
<summary aria-label="Close proof kit">
  ...
  <b aria-hidden="true">Close</b>
</summary>
```

Or update text based on `[open]` state without leaving both labels in the accessible tree.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
