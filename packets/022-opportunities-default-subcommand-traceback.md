# Packet 022: Opportunities Default Subcommand Traceback

## Summary

`spark opportunities` crashes with an `AttributeError` when run without a subcommand.

The parser already treats a missing `opps_cmd` as `list`, but the list-only arguments live on the `list` subparser. When users run the shorter default command, those attributes are missing from the parent namespace.

## Mission Source

Spark Compete pushes agents to run mission-style CLI exploration and find rough edges in the agent workflow. The opportunity inbox is a natural self-improvement surface for that workflow, so its default entry point should be safe and readable.

## Before Evidence

Read-only repro on upstream `main`:

```console
$ spark opportunities
Traceback (most recent call last):
  File ".../spark/cli.py", line 3339, in <module>
    main()
  File ".../spark/cli.py", line 3333, in main
    commands[args.command](args)
  File ".../spark/cli.py", line 771, in cmd_opportunities
    limit=int(args.limit or 20),
AttributeError: 'Namespace' object has no attribute 'limit'
```

Observed result:

```text
exit=1
stderr contains Python traceback
```

## Expected Behavior

`spark opportunities` should behave like `spark opportunities list`, using default list filters and printing the opportunity inbox without a Python traceback.

## Impact

- A documented top-level CLI surface crashes on the simplest invocation.
- The crash exposes implementation details instead of actionable guidance.
- Agents exploring Spark's self-improvement loop hit a brittle default path before they can inspect opportunities.

## Proposed Fix

Read list-only options with safe defaults when `opps_cmd` is missing:

```python
limit=int(getattr(args, "limit", 20) or 20)
scope_type=getattr(args, "scope_type", None)
```

Add regression coverage for calling `cmd_opportunities` with only the parent command namespace.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-opportunities-default`
- Branch: `codex/fix-opportunities-default`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-opportunities-default
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-opportunities-default
- Commit: `ced1136 Fix opportunities default command`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_opportunities.py -q` passed.
- Behavior check: `PYTHONPATH=. python -m spark.cli opportunities` exits `0` and prints the opportunity inbox.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
