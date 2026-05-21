# Packet 080: EIDOS List Limit Ignored

## Summary

`spark eidos --episodes --limit 0` and `spark eidos --episodes --limit -1` both list all seeded EIDOS episodes and exit successfully.

The same list-limit pattern affects EIDOS distillation and step list views. These are evidence surfaces for decision packets, so malformed list bounds should not produce successful output.

## Mission Source

Spark Compete asks agents to inspect Spark's decision, memory, and validation loops. EIDOS list views expose the decision-packet memory surface, so invalid bounds should be handled before rows are queried or displayed.

## Before Evidence

Repro on upstream `main` with an isolated home and two seeded EIDOS episodes:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit 0
============================================================
  Recent Episodes (2)
============================================================

  [OK] two
      ID: e2
      Phase: explore | Outcome: success
      Steps: 0/25

  [OK] one
      ID: e1
      Phase: explore | Outcome: success
      Steps: 0/25

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit -1
============================================================
  Recent Episodes (2)
============================================================

  [OK] two
      ID: e2
      Phase: explore | Outcome: success
      Steps: 0/25

  [OK] one
      ID: e1
      Phase: explore | Outcome: success
      Steps: 0/25

$ echo $?
0
```

Observed result: zero is converted to the default limit, and SQLite treats `LIMIT -1` like an unbounded query.

## Expected Behavior

- `--limit 0` should display zero EIDOS list rows.
- Negative limits should exit non-zero.
- Positive limits should keep showing the requested newest rows.
- Store list helpers should reject negative limits for direct callers too.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit -1
[SPARK] EIDOS list failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit 0
============================================================
  Recent Episodes (0)
============================================================

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eidos --episodes --limit 1
============================================================
  Recent Episodes (1)
============================================================

  [OK] two
      ID: e2
      Phase: explore | Outcome: success
      Steps: 0/25
```

## Impact

- Agents cannot safely request a zero-row EIDOS evidence probe.
- Negative limits look like successful complete list reads.
- Reviewer proof can expose more EIDOS rows than requested.

## Proposed Fix

Validate EIDOS list limits before query execution:

```python
def _validate_limit(limit, default):
    value = default if limit is None else int(limit)
    if value < 0:
        raise ValueError("limit must be zero or greater")
    return value
```

Use that helper in episode, step, and distillation list methods. Also preserve explicit zero in the CLI instead of converting it to a default.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-list-limit-validation`
- Branch: `codex/fix-eidos-list-limit-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-list-limit-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-list-limit-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eidos-list-limit-validation?expand=1
- Commit: `9bdf052`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_list_limits.py tests/test_eidos_store_distillation_dedupe.py -q` passed.
- Behavior check: isolated `HOME` rejects negative limits for `--episodes`, `--distillations`, and `--steps`; zero shows zero rows; positive episode limit shows one newest row.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
