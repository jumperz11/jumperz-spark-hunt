# Packet 037: Project View Commands Write Context

## Summary

`spark project status` and `spark project questions` create first-run project state in a fresh home directory.

Both commands are view/inspection surfaces. They should infer enough project data to print their report, but should not persist `~/.spark/project_context.json` or generated project profiles unless the user runs an explicit write command.

## Mission Source

Spark Compete asks agents to inspect project-understanding flows. Project status and question previews are natural agent probes, so hidden first-run writes on read-only views are a high-signal CLI safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark project status
[SPARK] Project: spark-audit-cli-edges
   Domain: engineering
   Phase: discovery
   Completion Score: 2/100
   Goals: 0
   Done: not set
```

Observed result:

```text
exit=0
~/.spark/project_context.json is created
~/.spark/projects/ is created
```

`spark project questions` is more visible:

```console
$ HOME="$(mktemp -d)" spark project questions
[SPARK] Suggested questions:
   - [decision] eng_arch: What architecture decision matters most?
   - [risk] eng_risk: What will cause problems later if ignored?
   - [done] eng_done: What signals completion beyond tests passing?
```

Observed result:

```text
exit=0
~/.spark/project_context.json is created
~/.spark/projects/<project>.json is created
```

## Expected Behavior

Read-only project views should remain read-only:

```text
exit=0
project status/questions are printed
no ~/.spark/project_context.json created
no ~/.spark/projects directory or profile file created
```

Explicit write commands should continue to persist state:

```text
spark project init
spark project answer
spark project capture
spark project phase --set-phase ...
```

## Impact

- Agents probing project context create local Spark state unintentionally.
- Generated question profiles can be persisted before the user answers or initializes the project.
- It becomes difficult to tell whether a project was intentionally initialized or merely inspected.

## Proposed Fix

Use the read-only profile/context path for view commands, and allow generated questions to stay in memory:

```python
profile = load_profile(project_dir, use_cache=False)
ensure_questions(profile, persist=False)
_print_project_questions(profile, limit, persist_questions=False)
```

Also avoid creating `~/.spark/projects` when loading a missing profile for inspection.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-project-readonly-views`
- Branch: `codex/fix-project-readonly-views`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-readonly-views
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-project-readonly-views
- Stacked base: `codex/fix-status-readonly-context`
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-status-readonly-context...codex/fix-project-readonly-views?expand=1
- Commit: `e58d6ec Keep project view commands read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_project_readonly_views.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark project status` exits `0` and creates no files or directories under `HOME`.
- Behavior check: `HOME="$(mktemp -d)" spark project questions` exits `0` and creates no files or directories under `HOME`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
