# Packet 025: Project Missing Path Writes Context

## Summary

`spark project status --project <missing-path>` exits successfully and writes Spark project context for a directory that does not exist.

The command is read-only from the user's perspective. With an explicit missing `--project` path, it should fail before loading project context or writing state.

## Mission Source

Spark Compete pushes agents to probe first-run and project-understanding flows. Project profile commands are a high-value agent surface because agents commonly pass explicit project paths.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark project status --project "$HOME/definitely-missing-project"
[SPARK] Project: definitely-missing-project
   Domain: general
   Phase: discovery
   Completion Score: 2/100
...
```

Observed result:

```text
exit=0
~/.spark/project_context.json is created
```

## Expected Behavior

Spark should reject explicit missing project paths before loading profile/context helpers:

```console
$ HOME="$(mktemp -d)" spark project status --project "$HOME/definitely-missing-project"
[SPARK] Project path not found: .../definitely-missing-project
```

Expected result:

```text
exit=1
no ~/.spark files are created
```

## Impact

- A read-only status probe writes state for a nonexistent project.
- Agents can accidentally pollute project context by passing a typo path.
- The success output makes a missing path look like a valid Spark project profile.

## Proposed Fix

Validate explicit `--project` paths before calling `load_profile()`:

```python
def _project_dir_arg(args):
    raw = getattr(args, "project", None)
    if not raw:
        return None
    project_dir = Path(raw).expanduser()
    if not project_dir.exists():
        print(f"[SPARK] Project path not found: {project_dir}")
        sys.exit(1)
    if not project_dir.is_dir():
        print(f"[SPARK] Project path is not a directory: {project_dir}")
        sys.exit(1)
    return project_dir
```

Reuse that helper across project subcommands so explicit typo paths are rejected consistently.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-project-missing-path`
- Branch: `codex/fix-project-missing-path`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-missing-path
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-project-missing-path
- Commit: `4492c40 Reject missing project paths in CLI`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_project.py -q` passed.
- Behavior check: missing explicit `--project` exits `1`, prints `Project path not found`, and writes no `~/.spark` files.
- Control check: existing explicit project paths and implicit current-directory status still work.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
