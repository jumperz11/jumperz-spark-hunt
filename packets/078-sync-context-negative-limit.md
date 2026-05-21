# Packet 078: Sync Context Negative Limit Writes Exports

## Summary

`spark sync-context --limit -1` exits successfully and writes context/export files even though the scan bound is invalid.

The command writes agent bootstrap context to multiple targets, so malformed limits should fail before any export or telemetry write happens.

## Mission Source

Spark Compete asks agents to run Spark discovery and context-sync workflows. `sync-context` is a high-impact surface because it writes the context that agents consume, so invalid bounds should not produce fresh bootstrap artifacts.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --limit -1
{
  "selected": 0,
  "promoted_selected": 0,
  "targets": {
    "claude_code": "written",
    "cursor": "written",
    "windsurf": "written",
    "clawdbot": "written",
    "openclaw": "written",
    "codex": "written",
    "exports": "written"
  }
}

$ echo $?
0

$ find "$tmp" -maxdepth 3 -type f | sort
$tmp/.openclaw/workspace/SPARK_ADVISORY_PAYLOAD.json
$tmp/.openclaw/workspace/SPARK_CONTEXT.md
$tmp/.spark/exports/SPARK_ADVISORY_PAYLOAD.json
$tmp/.spark/exports/gemini_system.md
$tmp/.spark/exports/gpt_instructions.md
$tmp/.spark/project_context.json
$tmp/.spark/sync_stats.json
$tmp/clawd/SPARK_ADVISORY_PAYLOAD.json
$tmp/clawd/SPARK_CONTEXT.md
$tmp/clawd/USER.md
```

Observed result: a negative limit looks like a successful zero-selection sync while still writing adapter outputs.

## Expected Behavior

- Negative limits should exit non-zero before sync work begins.
- `--limit 0` should remain a valid zero-insight sync.
- Positive limits should keep selecting and writing bounded context normally.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --limit -1
[SPARK] Sync context failed: limit must be zero or greater

$ echo $?
1

$ find "$tmp" -maxdepth 3 -type f | sort

$ HOME="$tmp2" PYTHONPATH=. python -m spark.cli sync-context --limit 0
{
  "selected": 0,
  "promoted_selected": 0,
  "targets": {
    "claude_code": "written",
    "cursor": "written",
    "windsurf": "written",
    "clawdbot": "written",
    "openclaw": "written",
    "codex": "written",
    "exports": "written"
  }
}
```

## Impact

- Agents can accidentally refresh bootstrap context with an invalid scan bound.
- Reviewers see successful output even though the requested bound is malformed.
- Invalid runs write multiple files under isolated homes, making proof and local state noisy.

## Proposed Fix

Validate sync limits before `sync_context()` initializes learners, loads project context, records exposures, or writes adapter outputs:

```python
def _validate_limit(limit):
    value = DEFAULT_MAX_ITEMS if limit is None else int(limit)
    if value < 0:
        raise ValueError("limit must be zero or greater")
    return value
```

Also short-circuit `_select_insights(limit=0)` so zero does not select one item after the append-before-cap check.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-sync-context-limit-validation`
- Branch: `codex/fix-sync-context-limit-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-context-limit-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-sync-context-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-context-limit-validation?expand=1
- Commit: `5490e05`
- Verification: `PYTHONPATH=. python -m pytest tests/test_context_sync_limit_validation.py tests/test_context_sync_mind.py tests/test_production_hardening.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1` with no files written and preserves `--limit 0` as a zero-selection sync.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
