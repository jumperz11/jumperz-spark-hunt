# Packet 047: Project Phase Accepts Invalid Values

## Summary

`spark project phase --set invalid` persists an unsupported project phase and exits `0`.

The command help advertises the valid phase set as `discovery/prototype/polish/launch`, but the implementation accepts arbitrary strings and writes them into the project profile and phase history.

## Mission Source

Spark Compete asks agents to exercise project-understanding flows. Project phase affects suggested questions and completion scoring, so invalid phase values should not become persisted project context.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project phase --set invalid
[SPARK] Phase set: invalid
```

Observed result:

```text
exit=0
~/.spark/projects/<project>.json contains "phase": "invalid"
phase_history contains "phase -> invalid"
```

`set_phase()` normalized any non-empty string and wrote it directly to the profile.

## Expected Behavior

Unsupported phase values should fail before writing:

```text
exit=1
[SPARK] Invalid phase. Use: discovery, prototype, polish, launch
```

Valid phases should continue to work:

```text
spark project phase --set prototype
```

## Impact

- Agents can accidentally persist invalid project state.
- Phase-specific question generation becomes inconsistent for unsupported phases.
- Completion scoring silently falls back while the profile reports an invalid phase.

## Proposed Fix

Define the supported phases from the phase-question map and validate before loading/writing profile state:

```python
VALID_PHASES = frozenset(PHASE_QUESTIONS.keys())

if (args.set_phase or "").strip().lower() not in VALID_PHASES:
    print("[SPARK] Invalid phase. Use: discovery, prototype, polish, launch")
    raise SystemExit(1)
```

Also make `set_phase()` return `False` for invalid values so non-CLI callers cannot write unsupported phases.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-project-phase-validation`
- Branch: `codex/fix-project-phase-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-phase-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-project-phase-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-phase-validation?expand=1
- Commit: `57531b1`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_project_phase_validation.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project phase --set invalid` exits `1`.
- Behavior check: invalid phase input creates no `.spark` files.
- Behavior check: `spark project phase --set prototype` still exits `0` and records the valid phase.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
