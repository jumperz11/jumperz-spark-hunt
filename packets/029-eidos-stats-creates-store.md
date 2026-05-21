# Packet 029: EIDOS Stats Creates Store

## Summary

`spark eidos --stats` creates `~/.spark/eidos.db` in a fresh home directory.

Stats commands should be safe for agents to run as read-only discovery probes. Creating a new EIDOS store just to report zero counts makes the command mutate local state before the user has opted into EIDOS persistence.

## Mission Source

Spark Compete asks agents to run missions and report focused proof. EIDOS is Spark's decision/memory substrate, so first-run read-only telemetry that writes a store is a high-signal CLI safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --stats
============================================================
  EIDOS Intelligence Store
============================================================

  Episodes: 0
  Steps: 0
  Distillations: 0
  Policies: 0
  Success Rate: 0.0%
  High-Confidence Distillations: 0
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
```

`cmd_eidos()` constructs `get_store()` before dispatching to the `--stats` branch. `EidosStore()` creates `~/.spark/eidos.db` and initializes schema even when the command only needs to report counts.

## Expected Behavior

Stats should remain read-only when no EIDOS store exists:

```text
exit=0
Episodes: 0
Steps: 0
Distillations: 0
Policies: 0
no ~/.spark/eidos.db created
```

If an existing EIDOS store is present, stats should read it without mutating rows.

## Impact

- Agents cannot inspect EIDOS state in a clean environment without creating persistent local state.
- First-run status/proof commands become noisy because they leave behind durable files.
- The CLI reports a read-only view but performs an implicit schema initialization.

## Proposed Fix

Add a stats helper that can report empty counts without constructing `EidosStore()`:

```python
def get_stats_readonly(db_path=None):
    path = Path(db_path) if db_path else default_store_path()
    if not path.exists():
        return empty_zero_stats(path)
    with sqlite3.connect(readonly_uri(path), uri=True) as conn:
        return collect_stats(conn, str(path))
```

Then use that helper for `spark eidos --stats` and the default `spark eidos` overview, while keeping write/list paths on `get_store()`.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-stats-readonly`
- Branch: `codex/fix-eidos-stats-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-stats-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-stats-readonly
- Commit: `d68c846 Keep EIDOS stats read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_stats_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --stats` exits `0` and creates no `~/.spark/eidos.db`.
- Control check: an existing EIDOS store is still readable by the stats helper.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
