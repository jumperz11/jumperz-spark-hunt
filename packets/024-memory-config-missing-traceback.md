# Packet 024: Memory Config Missing Traceback

## Summary

`spark memory --show` and `spark memory --set off --no-restart` crash when `~/.clawdbot/clawdbot.json` does not exist.

The memory command is a setup/configuration surface. A fresh install is exactly when the config may be absent, so the command should report an unset state or create the config path instead of exposing a Python traceback.

## Mission Source

Spark Compete encourages agents to inspect first-run and configuration flows. Memory setup is a high-value agent-readiness surface because it determines whether semantic memory search is available.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark memory --show
Traceback (most recent call last):
  File ".../spark/cli.py", line 3770, in main
    commands[args.command](args)
  File ".../spark/cli.py", line 2796, in cmd_memory
    ms = get_current_memory_search()
  File ".../lib/clawdbot_memory_setup.py", line 63, in get_current_memory_search
    cfg = cfg or _load_config()
  File ".../lib/clawdbot_memory_setup.py", line 35, in _load_config
    raise FileNotFoundError(f"Missing config: {CONFIG_PATH}")
FileNotFoundError: Missing config: .../.clawdbot/clawdbot.json
```

Second repro:

```console
$ HOME="$(mktemp -d)" spark memory --set off --no-restart
FileNotFoundError: Missing config: .../.clawdbot/clawdbot.json
```

## Expected Behavior

Fresh environments should be handled cleanly:

```console
$ HOME="$(mktemp -d)" spark memory --show
Current Clawdbot agents.defaults.memorySearch:
(not set)
```

and:

```console
$ HOME="$(mktemp -d)" spark memory --set off --no-restart
Applied memorySearch:
{'enabled': False, 'provider': 'none'}
```

## Impact

- First-run memory configuration fails before users can disable or inspect memory search.
- Agents receive a traceback instead of a setup-ready state.
- `--set off`, the safest privacy-preserving mode, is unavailable unless a config already exists.

## Proposed Fix

Treat a missing Clawdbot config as an empty config for read/setup helpers, and create the parent directory before saving:

```python
def _load_config():
    if not CONFIG_PATH.exists():
        return {}
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

def _save_config(cfg):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
```

Add regression coverage for `get_current_memory_search()` with no config and `apply_memory_mode("off")` creating the missing config path.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-memory-config-missing`
- Branch: `codex/fix-memory-config-missing`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-memory-config-missing
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-memory-config-missing
- Commit: `8173558 Handle missing Clawdbot memory config`
- Verification: `PYTHONPATH=. python -m pytest tests/test_clawdbot_memory_setup.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark memory --show` prints `(not set)`.
- Behavior check: `HOME="$(mktemp -d)" spark memory --set off --no-restart` creates `~/.clawdbot/clawdbot.json` with disabled memory search.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
