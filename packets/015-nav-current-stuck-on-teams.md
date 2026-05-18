# Packet 015: Navigation Current State Is Stuck On Teams

## Summary

The primary navigation statically marks the `teams` link with `aria-current="page"`. When the user is on another hash section such as `#agent-playbook`, assistive technology still receives `teams` as the current page while `agents` has no current state.

## Surface

- Primary navigation
- Hash-section routing
- Accessibility / agent-readable page state

## Before Evidence

Static HTML:

```html
<a href="#register" aria-current="page">teams</a>
<a href="#agent-playbook">agents</a>
```

Browser state:

```text
URL: https://compete.sparkswarm.ai/#agent-playbook
teams aria-current: page
agents aria-current: null
```

## Expected Behavior

Only the active section should expose current state.

For example, when the URL is `#agent-playbook`:

```html
<a href="#register">teams</a>
<a href="#agent-playbook" aria-current="page">agents</a>
```

## Impact

- Screen-reader users get incorrect navigation state.
- Agent-based QA sees the wrong current section.
- Deep links to proof, board, and agents still announce teams as current.

## Proposed Fix

Update `aria-current` on hash change and initial load:

```js
function syncCurrentNav() {
  const hash = location.hash || "#register";
  document.querySelectorAll("nav a[href^='#']").forEach((link) => {
    link.toggleAttribute("aria-current", link.getAttribute("href") === hash);
    if (link.hasAttribute("aria-current")) link.setAttribute("aria-current", "page");
  });
}

window.addEventListener("hashchange", syncCurrentNav);
syncCurrentNav();
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
