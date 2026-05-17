# Packet 006: Mission Copy Buttons Are Indistinguishable

## Summary

The agent mission grid renders 60 mission cards, each with a button whose visible/accessibility text is only `Copy`. This creates indistinguishable controls for keyboard and screen-reader users.

## Surface

- Agent playbook
- Mission copy controls
- Accessibility / non-coder workflow

## Before Evidence

Source render:

```html
<span>mission ${String(index + 1).padStart(2, "0")}</span>
<button class="ghost-button mini-button" type="button" data-copy-prompt="${index}">Copy</button>
```

DOM check:

```text
data-copy-prompt count: 60
```

All 60 buttons are rendered from the same button text:

```text
Copy
```

## Expected Behavior

Each mission copy button should expose a unique accessible name.

Examples:

```html
<button aria-label="Copy mission 01">Copy</button>
```

or:

```html
<button>
  <span aria-hidden="true">Copy</span>
  <span class="sr-only">mission 01</span>
</button>
```

## Impact

- Screen-reader users hear many repeated `Copy` buttons with no mission context.
- Keyboard users cannot easily tell which mission they are copying.
- The hunt explicitly targets non-coder/team workflows, so mission controls should be easy to navigate and verify.

## Proposed Fix

Include the mission number in the accessible name while keeping the compact visual label:

```js
const missionNumber = String(index + 1).padStart(2, "0");

`<button
  class="ghost-button mini-button"
  type="button"
  data-copy-prompt="${index}"
  aria-label="Copy mission ${missionNumber}"
>Copy</button>`
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
