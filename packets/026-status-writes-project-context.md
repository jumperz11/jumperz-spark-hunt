# Packet 026: Status Writes Project Context

## Summary

`spark status` writes `~/.spark/project_context.json` in a fresh home directory.

Status is an observational command. It should report current Spark state without initializing project-context cache files.

## Mission Source

Spark Compete asks agents to inspect first-run and operational surfaces. `spark status` is one of the first commands an agent will run, so accidental state writes from this read-only probe are high-signal.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark status
============================================================
  SPARK - Self-Evolving Intelligence Layer
============================================================
...
```

Observed result:

```text
exit=0
~/.spark/project_context.json is created
```

The write comes from project intelligence display: `spark status` calls `load_profile(Path.cwd())`, which infers domain through cached project-context detection.

## Expected Behavior

`spark status` should remain read-only:

```text
exit=0
no ~/.spark/project_context.json created
```

Project-context cache writes should still occur when callers explicitly ask for cached project context.

## Impact

- A status probe creates state in a fresh environment.
- Agents cannot safely distinguish read-only inspection from initialization.
- The project-context cache can be polluted by incidental working directories.

## Proposed Fix

Make `use_cache=False` genuinely read-only in `get_project_context()`, thread that option through domain/profile loading, and have `spark status` use the read-only path:

```python
profile = load_profile(Path.cwd(), use_cache=False)
```

Keep the default cached behavior unchanged for explicit project-context workflows.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-status-readonly-context`
- Branch: `codex/fix-status-readonly-context`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-status-readonly-context
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-status-readonly-context
- Commit: `f6123d2 Keep status project context read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark status` exits `0` and creates no `~/.spark` files.
- Control check: direct cached `get_project_context()` still writes `~/.spark/project_context.json`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
