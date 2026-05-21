# Packet 033: EIDOS Evidence Creates Stores

## Summary

`spark eidos --evidence` creates both `~/.spark/eidos.db` and `~/.spark/evidence.db` in a fresh home directory.

The command prints an all-zero evidence store report. It should be a read-only inspection surface, not a first-run persistence initializer.

## Mission Source

Spark Compete asks agents to gather proof safely. Evidence inspection is a natural proof/debug command, so hidden store creation during `--evidence` makes agent-driven review noisier and less trustworthy.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --evidence
============================================================
  EIDOS Evidence Store
============================================================

  Total Items: 0
  Total Size: 0.0 KB
  Expiring in 24h: 0
  Permanent: 0
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
~/.spark/evidence.db is created
```

`cmd_eidos()` constructs `get_store()` before reaching the evidence branch, creating `eidos.db`. The evidence branch then calls `get_evidence_store()`, which initializes `evidence.db` before reading stats.

## Expected Behavior

Fresh-home evidence stats should remain read-only:

```text
exit=0
Total Items: 0
Total Size: 0.0 KB
Expiring in 24h: 0
Permanent: 0
no ~/.spark/eidos.db created
no ~/.spark/evidence.db created
```

If an evidence store exists, stats should continue to read its tables normally.

## Impact

- Agents cannot inspect EIDOS evidence state without creating persistent local state.
- A proof/debug command creates two databases even when there is no evidence to report.
- First-run evidence output appears read-only while performing hidden schema initialization.

## Proposed Fix

Add a read-only stats helper for the evidence store:

```python
if not evidence_db.exists():
    return zero_evidence_stats()
with sqlite3.connect(readonly_uri, uri=True) as conn:
    return collect_evidence_stats(conn)
```

Dispatch `spark eidos --evidence` before constructing the EIDOS store in `cmd_eidos()`.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-evidence-readonly`
- Branch: `codex/fix-eidos-evidence-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-evidence-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-evidence-readonly
- Commit: `93fb1ef Keep EIDOS evidence stats read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_evidence_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --evidence` exits `0`, prints the zero evidence report, and creates no files.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
