# Packet 059: Sync Context Negative Gates Export Low-Quality Memory

## Summary

`spark sync-context` accepts negative quality gates and exports a low-reliability, zero-validation insight into agent bootstrap context files.

The command is meant to write high-confidence learnings to platform targets. Negative `--min-reliability` and `--min-validations` values invert that safety gate and let weak memory into `gpt_instructions.md`, `gemini_system.md`, `SPARK_ADVISORY_PAYLOAD.json`, and exposure logs.

## Mission Source

Spark Compete asks agents to exercise Spark’s learning and context workflows. Bootstrap context is especially high impact because it can steer later agent behavior; invalid gates should fail before writing prompt/context artifacts.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli learn wisdom "Always validate payload contracts before rollout" --reliability 0.1

âœ“ Learned [wisdom]: Always validate payload contracts before rollout
  Reliability: 10%

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-reliability -1 --min-validations -1 --limit 1
{
  "selected": 1,
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

Observed exported content:

```text
~/.spark/exports/gpt_instructions.md:
- [wisdom] Always validate payload contracts before rollout (10% reliable, 0 validations)

~/.spark/exports/SPARK_ADVISORY_PAYLOAD.json:
"text": "Always validate payload contracts before rollout"

~/.spark/exposures.jsonl includes the same insight from sync_context
```

## Expected Behavior

Invalid gates should fail before context files or exposure rows are written:

```text
[SPARK] Min reliability must be between 0 and 1
exit=1
```

Negative validation requirements should also fail:

```text
[SPARK] Min validations must be zero or greater
exit=1
```

## Impact

- Explicitly low-quality memory can be exported into agent instructions.
- Exposure logs can record a weak insight as presented to the agent.
- Automation cannot trust `sync-context` gates to protect bootstrap context quality.

## Proposed Fix

Validate the CLI gates before calling `sync_context()`:

```python
min_reliability = float(args.min_reliability)
min_validations = int(args.min_validations)
if min_reliability < 0.0 or min_reliability > 1.0:
    print("[SPARK] Min reliability must be between 0 and 1")
    raise SystemExit(1)
if min_validations < 0:
    print("[SPARK] Min validations must be zero or greater")
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-sync-context-threshold-validation`
- Branch: `codex/fix-sync-context-threshold-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-sync-context-threshold-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-sync-context-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-sync-context-threshold-validation?expand=1
- Commit: `8a009cd`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_sync_context_validation.py -q` passed.
- Behavior checks:
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-reliability -1 --min-validations -1 --limit 1` exits `1` before creating exports.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-reliability 1.1 --limit 1` exits `1` before creating exports.
  - `HOME="$tmp" PYTHONPATH=. python -m spark.cli sync-context --min-validations -1 --limit 1` exits `1` before creating exports.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
