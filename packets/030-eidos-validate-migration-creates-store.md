# Packet 030: EIDOS Validate Migration Creates Store

## Summary

`spark eidos --validate-migration` creates `~/.spark/eidos.db` in a fresh home directory and reports `Tables exist: True`.

Validation should be a read-only check. In a clean environment with no EIDOS database, the command should report that EIDOS tables do not exist without creating them first.

## Mission Source

Spark Compete rewards agent-driven checks of real operational edges. Migration validation is exactly the kind of command an agent runs before changing state, so mutating the EIDOS store during validation is a high-signal CLI safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --validate-migration
============================================================
  EIDOS Migration Validation
============================================================

  Tables exist: True
  Distillations: 0
  Policies: 0
  Episodes: 0
  Steps: 0
  Backup exists: False
  Patterns archived: False

  [!!] Migration valid: False
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
Tables exist: True
```

`cmd_eidos()` constructs `get_store()` before the validation branch runs, and `validate_migration()` also calls `get_store()`. That initializes the EIDOS schema before the command checks whether migration artifacts exist.

## Expected Behavior

Validation should remain read-only:

```text
exit=0
Tables exist: False
Distillations: 0
Policies: 0
Episodes: 0
Steps: 0
Migration valid: False
no ~/.spark/eidos.db created
```

If an EIDOS store exists, validation should read it without modifying the database.

## Impact

- A validation command mutates local state before reporting results.
- Fresh environments get misleading validation output because the command creates the very tables it claims to check.
- Agents cannot safely validate migration state without creating persistent EIDOS files.

## Proposed Fix

Avoid constructing `EidosStore()` on the validation path:

```python
db_path = Path.home() / ".spark" / "eidos.db"
if not db_path.exists():
    return zero_counts_with_tables_exist_false()

with sqlite3.connect(readonly_uri(db_path), uri=True) as conn:
    tables_exist = required_tables_present(conn)
    counts = read_counts(conn) if tables_exist else zero_counts()
```

Move the eager `get_store()` call in `cmd_eidos()` below the `--validate-migration` branch so validation can execute before any store initialization.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-validate-readonly`
- Branch: `codex/fix-eidos-validate-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-validate-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-validate-readonly
- Commit: `e7f9517 Keep EIDOS migration validation read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_validate_migration_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --validate-migration` exits `0`, prints `Tables exist: False`, and creates no `~/.spark/eidos.db`.
- Control check: an existing EIDOS store is read without changing its database mtime.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
