# Packet 039: Bridge Preview Writes Project State

## Summary

Bare `spark bridge` prints an active context preview, but it also creates first-run project state in a fresh home directory.

The explicit write path is `spark bridge --update`, which writes `SPARK_CONTEXT.md`. The default preview path should render context without persisting project context or generated profile data.

## Mission Source

Spark Compete asks agents to inspect operational context and first-run flows. `spark bridge` is a natural read-only probe for active context, so hidden first-run writes make agent discovery less safe.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark bridge
==================================================
  SPARK ACTIVE CONTEXT
  Learnings that should influence behavior
==================================================

## Project Focus
- Phase: discovery

## Project Questions
- What architecture decision matters most?
- What will cause problems later if ignored?
- What signals completion beyond tests passing?
```

Observed result:

```text
exit=0
~/.spark/project_context.json is created
~/.spark/projects/<project>.json is created
```

The preview path calls `load_profile(Path.cwd())` and then `get_suggested_questions(project_profile)`, which infer/cache project context and persist generated questions.

## Expected Behavior

Bare `spark bridge` should be a preview:

```text
exit=0
SPARK ACTIVE CONTEXT is printed
no ~/.spark/project_context.json created
no ~/.spark/projects directory or profile file created
```

Explicit write behavior should remain on the explicit write path:

```text
spark bridge --update
```

## Impact

- A context preview initializes project state without user intent.
- Agents cannot safely inspect bridge context in clean environments.
- Generated project questions become indistinguishable from intentionally initialized project profiles.

## Proposed Fix

Use the read-only project profile/question path when generating preview context:

```python
project_profile = load_profile(Path.cwd(), use_cache=False)
questions = get_suggested_questions(project_profile, limit=3, persist_questions=False)
```

Keep `spark bridge --update` as the explicit persistence path.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-bridge-readonly-context`
- Branch: `codex/fix-bridge-readonly-context`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-bridge-readonly-context
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-bridge-readonly-context
- Stacked base: `codex/fix-project-readonly-views`
- Stacked compare: https://github.com/jumperz11/vibeship-spark-intelligence/compare/codex/fix-project-readonly-views...codex/fix-bridge-readonly-context?expand=1
- Commit: `00f7568 Keep bridge context preview read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_bridge_readonly_context.py tests/test_cli_project_readonly_views.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark bridge` exits `0`, prints active context, and creates no files or directories under `HOME`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
