# Packet 018: Carousel Tabs Missing Keyboard Navigation

## Summary

The event explainer carousel exposes its controls as an ARIA `tablist` with `role="tab"` buttons, but the JavaScript only handles mouse/click activation.

ARIA tabs are expected to support keyboard navigation with arrow keys, Home, and End. Without that behavior, keyboard and assistive-technology users get a tab widget that does not behave like a tab widget.

## Surface

- Event explainer carousel
- `role="tablist"` / `role="tab"`
- Keyboard accessibility

## Before Evidence

HTML declares a tablist:

```html
<div class="event-controls" role="tablist" aria-label="Spark Compete event explainer">
  <button class="is-active" type="button" role="tab" aria-selected="true" data-event-slide="0">Team up</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="1">Hunt</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="2">Prove</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="3">Ship</button>
</div>
```

The carousel binding only registers click handlers:

```js
els.eventSlideButtons.forEach((button) => {
  button.addEventListener("click", () => {
    selectSlide(Number(button.dataset.eventSlide || 0));
  });
});
```

There is no `keydown` handler for:

- `ArrowLeft`
- `ArrowRight`
- `Home`
- `End`

## Expected Behavior

If the carousel uses ARIA tab semantics, keyboard behavior should match the tab pattern:

- Right/Down arrow moves to the next tab.
- Left/Up arrow moves to the previous tab.
- Home moves to the first tab.
- End moves to the last tab.
- Focus and `aria-selected` stay in sync.

## Impact

- Keyboard users cannot operate the carousel as a proper tab interface.
- Screen-reader users receive tab semantics but not the expected controls.
- Agents and accessibility tooling will flag a mismatch between declared role and behavior.

## Proposed Fix

Add roving tabindex and key handling:

```js
function activateTab(index) {
  selectSlide(index);
  els.eventSlideButtons[index]?.focus();
}

button.addEventListener("keydown", (event) => {
  const keys = ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End"];
  if (!keys.includes(event.key)) return;
  event.preventDefault();

  if (event.key === "Home") return activateTab(0);
  if (event.key === "End") return activateTab(els.eventSlideButtons.length - 1);

  const delta = event.key === "ArrowLeft" || event.key === "ArrowUp" ? -1 : 1;
  activateTab(activeIndex + delta);
});
```

Also set inactive tabs to `tabindex="-1"` and the active tab to `tabindex="0"`.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
