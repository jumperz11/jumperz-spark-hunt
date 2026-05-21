# Packet 021: OS Compile Missing Project Emits Traceback

## Summary

`spark os compile --json --project <missing-path>` crashes with a Python traceback and emits no JSON.

The command is specifically promoted by the Spark Compete missions as the safe discovery path, so missing or mistyped project paths should produce a bounded CLI error, not an internal stack trace.

## Mission Source

Spark Compete mission:

> Run `spark os compile --json` and ask Spark for a safe summary. It should use capability, authority, trace, memory, repo-board, and gaps views without publishing raw private maps.

Related site surface: first-run proof and public-track routing.

## Before Evidence

Read-only repro:

```console
$ spark os compile --json --project /tmp/spark-definitely-missing-project
Traceback (most recent call last):
  File ".../.venv/bin/spark", line 10, in <module>
    sys.exit(main())
  File ".../spark/cli.py", line 3333, in main
    commands[args.command](args)
  File ".../spark/cli.py", line 329, in cmd_os
    payload = _build_os_compile_snapshot(project_root)
  File ".../spark/cli.py", line 229, in _build_os_compile_snapshot
    repo_board = _repo_board_snapshot(project_root)
  File ".../spark/cli.py", line 192, in _repo_board_snapshot
    inside = _run_git(["rev-parse", "--is-inside-work-tree"], project_root)
...
FileNotFoundError: [Errno 2] No such file or directory: '/private/tmp/spark-definitely-missing-project'
```

Observed result:

```text
exit=1
stdout bytes=0
stderr contains Python traceback
```

Control check with an existing directory succeeds and emits valid JSON:

```console
$ spark os compile --json --project /tmp
json_valid yes
```

## Expected Behavior

For a missing `--project` path, Spark should return a clean, bounded error:

```console
$ spark os compile --json --project /tmp/spark-definitely-missing-project
{"error":{"code":"project_not_found","message":"Project path does not exist.","path":"/tmp/spark-definitely-missing-project"}}
```

or, for non-JSON mode:

```text
spark: project path does not exist: /tmp/spark-definitely-missing-project
```

## Impact

- Safe discovery fails noisily on a common user typo.
- Internal file paths and implementation details leak into user-facing output.
- Agents expecting JSON receive empty stdout and a traceback, making proof automation brittle.

## Proposed Fix

Validate `--project` before calling git:

```python
if not project_root.exists():
    return os_compile_error("project_not_found", project_root, json=args.json)
```

Also catch `FileNotFoundError` around repo-board collection and convert it into a structured warning or error.

## Fix Branch

Prepared locally, not pushed upstream:

- Worktree: `/Users/jumperz/Documents/spark-fix-os-missing-project`
- Branch: `codex/fix-os-compile-missing-project`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-os-compile-missing-project
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-os-compile-missing-project
- Commit: `0c2a743 Handle missing Spark OS project paths`
- Verification: `pytest tests/test_cli_os.py -q` passed.
- Behavior check: `spark os compile --json --project /tmp/spark-definitely-missing-project` now exits `1`, emits structured JSON on stdout, and emits no traceback on stderr.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
