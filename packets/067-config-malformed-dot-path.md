# Packet 067: Config Malformed Dot-Path Writes Empty Keys

## Summary

`spark config set` accepts malformed dot-path keys and writes invalid runtime config shapes into `~/.spark/tuneables.json`.

Empty keys and doubled separators should be rejected before the command mutates user config.

## Mission Source

Spark Compete asks agents to inspect setup, configuration, and automation surfaces. Runtime tuneables are a high-impact control path because bad values can change agent behavior across later commands.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set "" 1
   = 1
  Saved to .../.spark/tuneables.json

$ cat "$tmp/.spark/tuneables.json"
{
  "": 1
}

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor..max_items 5
  advisor..max_items = 5
  Saved to .../.spark/tuneables.json

$ cat "$tmp/.spark/tuneables.json"
{
  "": 1,
  "advisor": {
    "": {
      "max_items": 5
    }
  }
}
```

Observed result: the command exits `0` and persists malformed empty-key sections.

## Expected Behavior

- Empty config keys exit non-zero before writing.
- Dot paths with blank segments, leading dots, trailing dots, or doubled dots exit non-zero.
- Whitespace-padded segments exit non-zero instead of creating surprising keys.
- Valid dot paths keep working.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set "" 1
  Config key must be a non-empty dot path without blank segments

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor..max_items 5
  Config key must be a non-empty dot path without blank segments

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor.max_items 5
  advisor.max_items = 5
  Saved to .../.spark/tuneables.json
```

Invalid invocations exit with status `1` and do not create `~/.spark/tuneables.json`.

## Impact

- Agents can poison runtime tuneables with empty config sections.
- Later config validation only checks top-level known sections, so nested malformed keys can persist quietly.
- Automation sees a successful exit code even though the requested config path is not meaningful.

## Proposed Fix

Validate config dot-path keys at the CLI boundary before `get`, `set`, or `unset`:

```python
def _normalize_dot_key(key):
    key = str(key or "")
    parts = key.split(".")
    if not key or any(not part or part.strip() != part for part in parts):
        print("  Config key must be a non-empty dot path without blank segments")
        sys.exit(1)
    return key
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-config-key-validation`
- Branch: `codex/fix-config-key-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-key-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-config-key-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-key-validation?expand=1
- Commit: `a7ac2e8`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_config_key_validation.py -q` passed.
- Behavior check: isolated `HOME` rejects empty and doubled dot-path keys with exit `1`, creates no runtime config, and still accepts `advisor.max_items`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
