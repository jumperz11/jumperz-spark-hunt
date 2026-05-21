# Packet 038: CLI View Commands Emit Mojibake

## Summary

Packet 002 fixes mojibake in `spark status` and `spark health`, but several other read-only CLI views still print corrupted glyphs.

Examples include `spark events`, `spark learnings`, `spark surprises`, `spark voice`, `spark timeline`, and `spark bridge --status`.

## Mission Source

Spark Compete asks agents to inspect Spark surfaces and report proof. These view commands are common first-run probes, so corrupted headings and status markers reduce readability for both humans and LLM agents.

## Before Evidence

Read-only repro on upstream `main`:

```console
$ spark events

ðŸ“‹ Recent Events (showing 0 of 0)
```

```console
$ spark learnings

ðŸ“š Recent Cognitive Insights (showing 0 of 0)
```

```console
$ spark surprises

ðŸ’¡ Recent Surprises (showing 0)
```

```console
$ spark voice

ðŸŽ­ Spark Voice Status
```

```console
$ spark bridge --status

  Bridge Status
  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  Context file: âœ—
  Memory file: âœ—
```

## Expected Behavior

View commands should use readable, ASCII-safe section and status markers:

```text
[INFO] Recent Events
[INFO] Recent Cognitive Insights
[INFO] Recent Surprises
[INFO] Spark Voice Status
Context file: [MISS]
```

## Impact

- CLI output looks corrupted on normal UTF-8 terminals.
- Agents reading command output get noisy tokens instead of meaningful section labels.
- Packet 002 improves the main status surfaces, but adjacent view commands still carry the same user-visible encoding bug.

## Proposed Fix

Replace corrupted headings/status markers in the scoped view commands with ASCII markers, matching the Packet 002 style:

```text
[INFO]
[OK]
[MISS]
```

Add a regression test that runs the read-only views and rejects common mojibake fragments.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-cli-view-mojibake`
- Branch: `codex/fix-cli-view-mojibake`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-cli-view-mojibake
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-cli-view-mojibake
- Stacked base: `codex/fix-cli-status-mojibake`
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-cli-status-mojibake...codex/fix-cli-view-mojibake?expand=1
- Commit: `1e8207e Fix mojibake in CLI view commands`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_status_health_output.py tests/test_cli_view_output_mojibake.py -q` passed.
- Behavior check: `events`, `learnings`, `surprises`, `voice`, `voice --growth`, `timeline`, and `bridge --status` emit no `ðŸ`, `âœ`, `Ã¢`, `â†`, `âš`, or `â”` markers.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
