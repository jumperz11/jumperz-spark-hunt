# Packet 075: Outcome Unlinked Limit Ignored

## Summary

`spark outcome-unlinked --limit 0` lists all unlinked outcomes, and `spark outcome-unlinked --limit -1` exits successfully with a sliced subset.

The command is an outcome-validation evidence surface, so display bounds should be respected exactly.

## Mission Source

Spark Compete asks agents to inspect learning and outcome-validation loops. Outcome lists can become proof for validation coverage, so malformed display limits should not expose more outcome data than requested or return false success.

## Before Evidence

Repro on upstream `main` with an isolated home and two unlinked outcomes:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit 0
[SPARK] Unlinked Outcomes (2):
   [  pos  ] o1... first
   [  neg  ] o2... second

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit -1
[SPARK] Unlinked Outcomes (1):
   [  neg  ] o2... second

$ echo $?
0
```

Observed result: zero becomes unlimited, and negative limits return successful output.

## Expected Behavior

- `--limit 0` should display zero unlinked outcomes.
- Negative limits should exit non-zero before reading links/outcomes.
- Positive limits should keep showing the requested number of newest unlinked outcomes.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit -1
[SPARK] Outcome unlinked failed: limit must be zero or greater

$ echo $?
1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit 0
[SPARK] No unlinked outcomes found.

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli outcome-unlinked --limit 1
[SPARK] Unlinked Outcomes (1):
   [  neg  ] o2... second
```

## Impact

- Agents cannot safely request a zero-row outcome coverage probe.
- Negative limits produce successful but misleading output.
- Reviewer proof can accidentally expose more outcome rows than requested.

## Proposed Fix

Preserve explicit zero in the CLI and validate bounds in `get_unlinked_outcomes()`:

```python
limit = int(limit)
if limit < 0:
    raise ValueError("limit must be zero or greater")
if limit == 0:
    return []
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-outcome-unlinked-limit`
- Branch: `codex/fix-outcome-unlinked-limit`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-outcome-unlinked-limit
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-outcome-unlinked-limit
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-outcome-unlinked-limit?expand=1
- Commit: `8153a5a`
- Verification: `PYTHONPATH=. python -m pytest tests/test_outcome_log_full_stats.py -q` passed.
- Behavior check: isolated `HOME` rejects `--limit -1`, shows no rows for `--limit 0`, and shows one newest unlinked outcome for `--limit 1`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
