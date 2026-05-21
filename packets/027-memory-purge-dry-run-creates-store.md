# Packet 027: Memory Purge Dry Run Creates Store

## Summary

`spark memory-purge-telemetry --dry-run` creates `~/.spark/memory_store.sqlite` in a fresh home directory.

Dry-run commands should preview work without initializing durable stores or schemas.

## Mission Source

Spark Compete asks agents to inspect safe operational flows. A dry-run purge is explicitly a safe preview path, so durable writes from that path are high-signal.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark memory-purge-telemetry --dry-run
[SPARK] Memory Store Telemetry Purge (DRY RUN)
   Removed: 0
```

Observed result:

```text
exit=0
~/.spark/memory_store.sqlite is created
```

The dry-run path opens the memory store through `_connect()`, which creates the database and schema before the purge logic checks `dry_run`.

## Expected Behavior

Dry-run should remain read-only:

```text
exit=0
Removed: 0
no ~/.spark/memory_store.sqlite created
```

If an existing store is present, dry-run should read it without deleting rows.

## Impact

- Safe preview mode performs a durable write in fresh environments.
- Agents cannot use dry-run to inspect purge behavior without mutating local state.
- The command creates a SQLite store even when there is nothing to purge.

## Proposed Fix

Use a read-only SQLite connection for dry-run and return empty stats when the store is absent:

```python
conn = _connect_readonly_existing() if dry_run else _connect()
if conn is None:
    return {"removed": 0, "preview": [], "dry_run": dry_run}
```

Keep apply mode unchanged so actual purge operations still initialize and migrate the store when needed.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-memory-purge-dry-run`
- Branch: `codex/fix-memory-purge-dry-run`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-memory-purge-dry-run
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-memory-purge-dry-run
- Commit: `cb31a03 Keep memory purge dry run read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_memory_purge_telemetry.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark memory-purge-telemetry --dry-run` exits `0` and creates no `~/.spark` files.
- Control check: non-dry-run mode still creates/uses `~/.spark/memory_store.sqlite`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
