# Packet 017: HEAD Requests Return 404 For Live Routes

## Summary

The live site serves core routes successfully with `GET`, but returns `404` for `HEAD` on the same routes.

This can make uptime checks, crawlers, link validators, and lightweight monitoring report the Spark Compete site or leaderboard API as missing even while browser traffic works.

## Surface

- `https://compete.sparkswarm.ai/`
- `https://compete.sparkswarm.ai/api/leaderboard`
- HTTP method handling / health checks

## Before Evidence

Checked on 2026-05-18 UTC:

```console
$ curl -sS -L -o /dev/null -w '%{http_code}\n' https://compete.sparkswarm.ai/
200

$ curl -sS -I -o /dev/null -w '%{http_code}\n' https://compete.sparkswarm.ai/
404

$ curl -sS -L -o /dev/null -w '%{http_code}\n' https://compete.sparkswarm.ai/api/leaderboard
200

$ curl -sS -I -o /dev/null -w '%{http_code}\n' https://compete.sparkswarm.ai/api/leaderboard
404
```

The `HEAD /api/leaderboard` response body is also the not-found JSON:

```json
{"error":"not_found"}
```

## Expected Behavior

For routable resources, `HEAD` should return the same status code and response headers as `GET`, without a body.

- `HEAD /` should return `200`.
- `HEAD /api/leaderboard` should return `200`.
- If an API intentionally disallows `HEAD`, it should return a method-aware response such as `405 Method Not Allowed` with an `Allow` header, not `404`.

## Impact

- Health monitors can mark the event site down.
- Link checkers can report the leaderboard API as missing.
- Reviewer or sponsor tooling that probes with `HEAD` can get false-negative availability.
- Agents validating the public proof route may conclude the route does not exist.

## Proposed Fix

Route `HEAD` through the same handler as `GET` for public pages and read-only API endpoints, then omit the response body:

```js
if (req.method === "HEAD") {
  return getHandler(req, { headOnly: true });
}
```

At minimum, return a method-aware `405` plus `Allow: GET, HEAD` or `Allow: GET` for routes where `HEAD` is intentionally unsupported.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
