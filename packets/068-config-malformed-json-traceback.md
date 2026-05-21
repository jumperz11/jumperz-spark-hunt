# Packet 068: Config Malformed JSON Traceback

## Summary

`spark config show` and `spark config set` expose a raw Python traceback when `~/.spark/tuneables.json` contains malformed JSON.

Runtime config can be edited by users and automation, so Spark should report invalid config safely and avoid overwriting the file.

## Mission Source

Spark Compete asks agents to exercise configuration and setup paths. The tuneables file controls runtime behavior, so malformed config should produce a clear recovery diagnostic instead of a traceback.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ mkdir -p "$tmp/.spark"
$ printf '{bad json' > "$tmp/.spark/tuneables.json"

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config show
Traceback (most recent call last):
  ...
  File ".../spark/cli.py", line 680, in _load_json
    return json.loads(p.read_text(encoding="utf-8-sig"))
  ...
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
```

The same malformed runtime file also crashes `spark config set advisor.max_items 5` before the command can make a safe decision.

## Expected Behavior

- Malformed runtime config exits non-zero with a Spark-safe message.
- The diagnostic identifies the invalid config file and JSON location.
- `config set` must not overwrite malformed user config.
- Valid config files keep working.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config show
  Invalid JSON in config file: .../.spark/tuneables.json
  Expecting property name enclosed in double quotes at line 1, column 2

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config set advisor.max_items 5
  Invalid JSON in config file: .../.spark/tuneables.json
  Expecting property name enclosed in double quotes at line 1, column 2
```

Both commands exit with status `1`, and the malformed file remains unchanged.

## Impact

- Agents running config diagnostics see raw Python internals instead of actionable config feedback.
- Automation cannot distinguish bad config from an unexpected process crash.
- A state-changing command reaches the config load path without safe handling.

## Proposed Fix

Handle JSON decode failures in the shared config loader:

```python
try:
    return json.loads(p.read_text(encoding="utf-8-sig"))
except json.JSONDecodeError as exc:
    print(f"  Invalid JSON in config file: {p}")
    print(f"  {exc.msg} at line {exc.lineno}, column {exc.colno}")
    sys.exit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-config-json-errors`
- Branch: `codex/fix-config-json-errors`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-json-errors
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-config-json-errors
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-json-errors?expand=1
- Commit: `d1f44aa`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_config_json_errors.py -q` passed.
- Behavior check: isolated `HOME` reports malformed JSON safely for `config show` and `config set`, and `config set` leaves the malformed runtime file unchanged.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
