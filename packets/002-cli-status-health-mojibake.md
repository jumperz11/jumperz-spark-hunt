# Packet 002: CLI Status And Health Mojibake

## Summary

`spark status` and `spark health` show corrupted mojibake for several user-facing icons and checkmarks. This makes first-run health output look broken even when services are OK.

## Surface

- Spark CLI status output
- Spark CLI health output
- First-run / setup verification flow

## Before Evidence

Command:

```bash
spark status
```

Observed excerpt:

```text
ðŸ“š Cognitive Insights
ðŸ§  Mind Bridge
ðŸ“‹ Event Queue
ðŸŽ¯ Project Intelligence
Ã¢Å¡â„¢ Workers
âœ… Validation Loop
ðŸ§­ Prediction Loop
ðŸ“ Markdown Output
ðŸ“¤ Promotions
ðŸ’¡ Surprises (Aha Moments)
ðŸŽ­ Personality
```

Command:

```bash
spark health
```

Observed excerpt:

```text
ðŸ¥ Health Check

âœ“ Cognitive Learner: OK
âœ“ Mind API: OK
âœ“ Event Queue: OK (0 events)
Ã¢Å“â€œ bridge_worker: heartbeat 40s ago
âœ“ Learnings Dir: OK
```

## Expected Behavior

Health/status output should render readable symbols or plain ASCII fallback text, for example:

```text
Health Check

✓ Cognitive Learner: OK
✓ Mind API: OK
✓ Event Queue: OK
✓ bridge_worker: heartbeat 40s ago
✓ Learnings Dir: OK
```

If terminal encoding is uncertain, plain ASCII is safer:

```text
[OK] Cognitive Learner
[OK] Mind API
```

## Impact

- First-run users may think Spark is broken even when health checks pass.
- Non-coder teammates cannot confidently capture proof because the output looks corrupted.
- The hunt mission asks teams to verify first-run and status flows; this directly affects that surface.

## Proposed Fix

- Replace mojibake string literals in CLI status/health output with valid Unicode or ASCII-safe labels.
- Prefer a single output helper for status symbols so Windows, macOS, Linux, and redirected logs behave consistently.
- Add a snapshot-style CLI test that asserts common mojibake fragments such as `ðŸ`, `âœ`, and `Ã¢` do not appear in status/health text.

## Validation Shape

After the fix:

```bash
spark status
spark health
```

Both commands should show readable headings and OK markers with no mojibake fragments.

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.

## Recheck

Rechecked on 2026-05-21: `spark status` still contains mojibake markers such as `ðŸ`, `âœ`, and `Ã¢` in section headings and checkmark output.

Current bounded examples:

```text
ðŸ“š Cognitive Insights
ðŸ§  Mind Bridge
Mind Available: âœ“ Yes
Ã¢Å¡â„¢ Workers
âœ… Validation Loop
```
