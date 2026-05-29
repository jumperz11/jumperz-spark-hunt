# Packet 008: Mission Library Toggle Exposes Close/Open Text

## Summary

When the mission library drawer is expanded, its summary control exposes both `Close` and `Open` text in the accessible/agent-readable tree.

This is confusing on the same page where teams are expected to copy missions into agents and coordinate work.

## Surface

- Agent playbook
- Mission library drawer
- Keyboard/screen-reader navigation
- Agent-readable page state

## Before Evidence

After opening the mission library drawer, the DOM/agent snapshot reports:

```text
generic "mission library Open 60 starter missions teams can paste into Spark Telegram agents. ... Close Open"
```

Inside the expanded drawer:

```text
button "Copy all 60 missions"
generic "Telegram agent QA missions"
mission 01
button "Copy"
mission 02
button "Copy"
...
```

## Expected Behavior

The drawer toggle should expose one clear action based on current state:

- closed: `Open mission library`
- open: `Close mission library`

It should not expose both labels together.

## Impact

- Agent-based QA sees contradictory drawer state.
- Screen-reader users get noisy state/action text before a dense list of 60 missions.
- The mission library is a core mission review workflow, so navigation clarity affects every team using it.

## Proposed Fix

Use a single state-aware label for the summary:

```html
<summary aria-label="Close mission library">
  ...
  <b aria-hidden="true">Close</b>
</summary>
```

Or use CSS/JS to update one visible label and keep inactive decorative text out of the accessible tree.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
