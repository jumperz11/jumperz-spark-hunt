# Packet 032: EIDOS Metrics Creates Store

## Summary

`spark eidos --metrics` creates `~/.spark/eidos.db` in a fresh home directory.

The command prints an all-zero intelligence metrics report, which is a read-only discovery surface. It should not initialize EIDOS persistence just to report that no episodes, steps, or distillations exist.

## Mission Source

Spark Compete asks agents to run system-discovery missions and report focused fixes. Metrics are a natural first-run inspection command, so hidden persistence during metrics collection is a high-signal agent-safety issue.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark eidos --metrics
============================================================
  EIDOS Intelligence Metrics
============================================================

  [!!] COMPOUNDING RATE: 0.0% (target: 40.0%)

  Memory Effectiveness:
    With memory:    0.0% (0/0)
    Without memory: 0.0% (0/0)
    Advantage:      0.0%

  Loop Suppression:
    Avg retries: 0.0 (target: <3)
    Max retries: 0

  This Week:
    Episodes: 0 (0.0% success)
    New rules: 0 heuristics, 0 sharp edges
```

Observed result:

```text
exit=0
~/.spark/eidos.db is created
```

`cmd_eidos()` constructs `get_store()` before reaching the metrics branch. Without that eager store, `MetricsCalculator` would still connect to the default SQLite path and create an empty file.

## Expected Behavior

Fresh-home metrics should remain read-only:

```text
exit=0
COMPOUNDING RATE: 0.0%
This Week: Episodes: 0
no ~/.spark/eidos.db created
```

If an EIDOS store exists, metrics should continue to read its tables normally.

## Impact

- Agents cannot inspect EIDOS metrics without creating persistent local state.
- First-run metrics output appears read-only but performs hidden database initialization.
- Clean proof runs get extra filesystem noise from a command that only reports counts.

## Proposed Fix

Handle the missing-store case before opening SQLite:

```python
if not Path(self.db_path).exists():
    return zero_metrics_report()
```

Also dispatch `spark eidos --metrics` before constructing `get_store()` in `cmd_eidos()`.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-metrics-readonly`
- Branch: `codex/fix-eidos-metrics-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-metrics-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-metrics-readonly
- Commit: `b750cb4 Keep EIDOS metrics read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_metrics_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark eidos --metrics` exits `0`, prints the zero metrics report, and creates no files.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
