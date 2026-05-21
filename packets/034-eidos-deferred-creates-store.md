# Packet 034: EIDOS Deferred Creates Store

## Summary

`spark eidos --deferred` creates `~/.spark/eidos.db` in a fresh home directory.

The command prints an all-zero deferred validation report. It should be a read-only inspection surface, not a first-run persistence initializer.

## Mission Source

Spark Compete asks agents to inspect operational edges and produce focused fixes. Deferred validation status is exactly the kind of safety/status command an agent checks before acting, so hidden store creation makes proof runs noisier and less trustworthy.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --deferred
============================================================
  Deferred Validations
============================================================

  Total: 0
  Resolved: 0
  Pending: 0
  Overdue: 0
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
```

`cmd_eidos()` constructs `get_store()` before reaching the deferred branch. The branch also calls `get_deferred_tracker()`, whose constructor initializes the deferred validation table.

## Expected Behavior

Fresh-home deferred status should remain read-only:

```text
exit=0
Total: 0
Resolved: 0
Pending: 0
Overdue: 0
no ~/.spark/eidos.db created
```

If deferred validations exist, the command should still read and report them.

## Impact

- Agents cannot inspect deferred validation status without creating persistent EIDOS state.
- A status command initializes schema even when no deferred validations exist.
- First-run proof output appears read-only while performing hidden database writes.

## Proposed Fix

Add read-only helpers for deferred validation stats and overdue rows:

```python
if not eidos_db.exists():
    return zero_deferred_stats()
with sqlite3.connect(readonly_uri, uri=True) as conn:
    return collect_deferred_stats(conn)
```

Dispatch `spark eidos --deferred` before constructing the EIDOS store in `cmd_eidos()`.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-deferred-readonly`
- Branch: `codex/fix-eidos-deferred-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-deferred-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-deferred-readonly
- Commit: `ecf1f34 Keep EIDOS deferred stats read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_deferred_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --deferred` exits `0`, prints the zero deferred report, and creates no files.
- Control check: an existing EIDOS database with an overdue deferred validation is still read and reported.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
