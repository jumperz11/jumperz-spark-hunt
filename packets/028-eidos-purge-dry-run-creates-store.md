# Packet 028: EIDOS Purge Dry Run Creates Store

## Summary

`spark eidos-purge-telemetry --dry-run` creates `~/.spark/eidos.db` in a fresh home directory.

Dry-run purge commands should preview work without initializing durable stores or schemas.

## Mission Source

Spark Compete asks agents to inspect safe operational and cleanup flows. EIDOS is Spark's decision/memory substrate, so dry-run behavior that mutates local state is a high-signal agent-safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos-purge-telemetry --dry-run
[SPARK] EIDOS Distillation Telemetry Purge (DRY RUN)
   Scanned: 0
   Removed: 0
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
```

The top-level purge helper constructs `EidosStore()`, and `EidosStore` initializes the SQLite database before the dry-run purge logic runs.

## Expected Behavior

Dry-run should remain read-only:

```text
exit=0
Scanned: 0
Removed: 0
no ~/.spark/eidos.db created
```

If an existing EIDOS store is present, dry-run should scan it without deleting rows.

## Impact

- Safe preview mode performs a durable write in fresh environments.
- Agents cannot inspect EIDOS purge behavior without mutating local state.
- The command creates an EIDOS database even when there is nothing to purge.

## Proposed Fix

Guard the top-level dry-run helper before constructing the default store:

```python
if dry_run and _store is None:
    default_db = Path.home() / ".spark" / "eidos.db"
    if not default_db.exists():
        return {"scanned": 0, "removed": 0, "preview": [], "dry_run": dry_run}
```

Keep apply mode unchanged so actual purge operations still initialize and migrate the store when needed.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-purge-dry-run`
- Branch: `codex/fix-eidos-purge-dry-run`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-purge-dry-run
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-purge-dry-run
- Commit: `3af6e4d Keep EIDOS purge dry run read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_purge_telemetry.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos-purge-telemetry --dry-run` exits `0` and creates no `~/.spark` files.
- Control check: non-dry-run mode still creates/uses `~/.spark/eidos.db`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
