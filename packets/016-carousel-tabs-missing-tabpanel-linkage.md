# Packet 016: Carousel Tabs Missing Tabpanel Linkage

## Summary

The event explainer carousel uses ARIA `tablist` and `tab` roles, but the slide panels are plain `article` elements without `role="tabpanel"`, ids, or `aria-labelledby` linkage. The tabs also lack `aria-controls`.

This makes the tab relationship incomplete for assistive technologies and agent-based page interpretation.

## Surface

- Event explainer carousel
- Tablist semantics
- Accessibility / keyboard navigation

## Before Evidence

Tabs:

```html
<div class="event-controls" role="tablist" aria-label="Spark Compete event explainer">
  <button class="is-active" type="button" role="tab" aria-selected="true" data-event-slide="0">Team up</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="1">Hunt</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="2">Prove</button>
  <button type="button" role="tab" aria-selected="false" data-event-slide="3">Ship</button>
</div>
```

Panels:

```html
<article class="event-slide is-active" data-event-panel="0">...</article>
<article class="event-slide" data-event-panel="1" hidden>...</article>
```

There is no:

- `aria-controls` on each tab,
- panel `id`,
- `role="tabpanel"`,
- or `aria-labelledby` on each panel.

## Expected Behavior

Each tab should point to a corresponding tabpanel:

```html
<button id="event-tab-0" role="tab" aria-controls="event-panel-0" aria-selected="true">Team up</button>

<article id="event-panel-0" role="tabpanel" aria-labelledby="event-tab-0">...</article>
```

## Impact

- Screen-reader users may not understand which content each tab controls.
- Automated agents see selected tabs but cannot reliably connect tabs to panels.
- The page uses formal tab roles, so it should satisfy the tab/tabpanel contract.

## Proposed Fix

Add ids and ARIA linkage when rendering/static authoring the carousel:

```html
<button id="event-tab-0" role="tab" aria-controls="event-panel-0">Team up</button>
<article id="event-panel-0" role="tabpanel" aria-labelledby="event-tab-0">...</article>
```

Update the JS to keep `hidden`, `aria-selected`, and focus behavior in sync.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
