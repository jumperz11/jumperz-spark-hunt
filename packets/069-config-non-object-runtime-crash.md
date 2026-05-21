# Packet 069: Config Non-Object Runtime Crash

## Summary

A valid but non-object `~/.spark/tuneables.json` can crash Spark CLI startup before argument parsing.

For example, a runtime tuneables file containing `[]` reaches `lib.config_authority._section()`, which assumes the decoded JSON has `.get()`.

## Mission Source

Spark Compete asks agents to inspect configuration and agent-readiness surfaces. Runtime tuneables are loaded during import by several modules, so a malformed shape can disable otherwise unrelated commands.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ mkdir -p "$tmp/.spark"
$ printf '[]' > "$tmp/.spark/tuneables.json"

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config show
Traceback (most recent call last):
  ...
  File ".../lib/config_authority.py", line 131, in resolve_section
    runtime_section = _section(_read_json(runtime), section_name)
  File ".../lib/config_authority.py", line 49, in _section
    row = data.get(section_name, {})
AttributeError: 'list' object has no attribute 'get'
```

This occurs during CLI import through shared config resolution, before the requested command can handle the problem.

## Expected Behavior

- Shared config resolution should ignore non-object tuneables and fall back to baseline/defaults.
- `spark --help` should still start even when runtime tuneables has a JSON array or scalar.
- `spark config show` should reject non-object runtime config with a Spark-safe message.
- Valid object-shaped config should keep working.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli --help
usage: python -m spark.cli ...

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config show
  Config file must contain a JSON object: .../.spark/tuneables.json

$ printf '{"advisor":{"max_items":5}}' > "$tmp/.spark/tuneables.json"
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli config get advisor.max_items
5
```

## Impact

- A single valid JSON array in runtime tuneables can brick CLI startup paths.
- Agents and automation see an import-time Python traceback instead of a config diagnostic.
- The failure is broader than one command because `resolve_section()` is used across queue, advisory, memory, bridge, and learning modules.

## Proposed Fix

Guard decoded config shapes at both config boundaries:

```python
data = json.loads(path.read_text(encoding="utf-8-sig"))
return data if isinstance(data, dict) else {}
```

For `spark config`, reject non-object runtime config explicitly before reading `.keys()` or mutating the file.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-config-object-shape`
- Branch: `codex/fix-config-object-shape`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-config-object-shape
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-config-object-shape
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-config-object-shape?expand=1
- Commit: `695da92`
- Verification: `PYTHONPATH=. python -m pytest tests/test_config_object_shape.py -q` passed.
- Behavior check: isolated `HOME` with `[]` in runtime tuneables allows `spark --help`, makes `spark config show` exit `1` with a safe message, and still accepts object-shaped config.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
