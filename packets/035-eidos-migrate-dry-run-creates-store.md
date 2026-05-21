# Packet 035: EIDOS Migrate Dry Run Creates Store

## Summary

`spark eidos --migrate --dry-run` creates `~/.spark/eidos.db` in a fresh home directory.

Dry-run migration should preview migration counts and errors without initializing EIDOS persistence.

## Mission Source

Spark Compete asks agents to probe operational flows safely. Migration dry-runs are specifically meant to preview changes before making them, so a hidden database write is a high-signal dry-run safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --migrate --dry-run
============================================================
  EIDOS Migration
============================================================

  [DRY RUN] No changes will be made.

  Insights migrated: 0
  Insights skipped:  0
  Patterns archived: 0
  Policies created:  0

  Errors:
    - Insights file not found: .../.spark/cognitive_insights.json
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
```

`cmd_eidos()` constructs `get_store()` before reaching the migrate branch. The migration helpers already avoid `get_store()` when `dry_run=True`, but the CLI has initialized the store before they run.

## Expected Behavior

Dry-run migration should remain read-only:

```text
exit=0
[DRY RUN] No changes will be made.
Insights migrated: 0
Policies created: 0
no ~/.spark/eidos.db created
```

Non-dry-run migration should continue to create/use the EIDOS store.

## Impact

- A dry-run command mutates local state before previewing migration results.
- Agents cannot safely check migration impact in a clean environment.
- The command contradicts its own dry-run guarantee by creating durable EIDOS schema.

## Proposed Fix

Handle `args.migrate and args.dry_run` before constructing the EIDOS store:

```python
if args.migrate and args.dry_run:
    results = run_full_migration(dry_run=True)
    print_migration_results(results)
    return

store = get_store()
```

Keep apply mode unchanged so real migration still initializes the store.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-migrate-dry-run`
- Branch: `codex/fix-eidos-migrate-dry-run`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-migrate-dry-run
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-migrate-dry-run
- Commit: `d6d14f7 Keep EIDOS migration dry run read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_migrate_dry_run_readonly.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --migrate --dry-run` exits `0` and creates no files.
- Control check: `HOME="$(mktemp -d)" spark eidos --migrate` still creates/uses `~/.spark/eidos.db`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
