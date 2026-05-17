# Packet 012: Public Practice Repo Name Is Not Linked

## Summary

The site names `spark-personality-chip-labs` as an optional public practice repo, but renders it as plain text instead of a clickable GitHub link.

The repo exists publicly, so the site can link directly to it and save teams from manual search.

## Surface

- Agent playbook
- System surface list
- Public practice repo onboarding

## Before Evidence

Site data:

```js
{
  label: "spark-personality-chip-labs",
  kind: "public repo",
  detail: "Optional public practice repo for persona consistency, response boundaries, and voice QA."
}
```

Rendered surfaces use plain cards:

```js
els.surfaceGrid.innerHTML = systemSurfaces.map((surface) => `
  <article class="surface-card">
    <span>${escapeHtml(surface.kind)}</span>
    <strong>${escapeHtml(surface.label)}</strong>
    <small>${escapeHtml(surface.detail)}</small>
  </article>
`).join("");
```

Public GitHub search confirms the repo exists:

```text
vibeforge1111/spark-personality-chip-labs
https://github.com/vibeforge1111/spark-personality-chip-labs
```

## Expected Behavior

Public repo surfaces should include a direct link:

```html
<a href="https://github.com/vibeforge1111/spark-personality-chip-labs">
  spark-personality-chip-labs
</a>
```

## Impact

- Teams must manually search for a repo the site already knows by name.
- Search results can be noisy or confused with unrelated Spark projects.
- Non-coder teammates may not know which GitHub owner/repo is correct.

## Proposed Fix

Add an optional `href` field to `systemSurfaces`:

```js
{
  label: "spark-personality-chip-labs",
  kind: "public repo",
  href: "https://github.com/vibeforge1111/spark-personality-chip-labs",
  detail: "Optional public practice repo..."
}
```

Then render linked labels when `href` is present.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
