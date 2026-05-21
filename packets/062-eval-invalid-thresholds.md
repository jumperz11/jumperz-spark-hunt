# Packet 062: Eval Accepts Invalid Thresholds

## Summary

`spark eval` accepts invalid evaluation bounds even though the CLI help documents `--sim` as a `0-1` similarity threshold.

Passing `--sim -1` makes unrelated prediction/outcome rows match, which can report false contradictions and 100% outcome coverage.

## Mission Source

Spark Compete asks agents to trap bad behavior with before/after proof. Evaluation metrics are reviewer-facing signal; invalid thresholds should not turn unrelated outcomes into scored matches.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ now="$(python - <<'PY'
import time
print(time.time())
PY
)"
$ mkdir -p "$tmp/.spark"
$ cat > "$tmp/.spark/predictions.jsonl" <<EOF
{"prediction_id":"p1","text":"alpha prediction unrelated","expected_polarity":"pos","type":"general","created_at":$now}
EOF
$ cat > "$tmp/.spark/outcomes.jsonl" <<EOF
{"outcome_id":"o1","text":"omega outcome unrelated","polarity":"neg","created_at":$now}
EOF
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eval --days 7 --sim -1
[SPARK] Evaluation
   Predictions: 1
   Outcomes: 1
   Matched: 1
   Validated: 0
   Contradicted: 1
   Precision: 0%
   Outcome Coverage: 100%
```

Observed result:

```text
invalid similarity threshold is accepted
unrelated prediction/outcome rows are treated as matched
command exits successfully with misleading evaluation metrics
```

`--days -1` is also accepted as an invalid lookback and returns a successful empty evaluation.

## Expected Behavior

- Reject `--sim` values below `0` or above `1`.
- Reject negative `--days` values.
- Exit non-zero before running evaluation when bounds are invalid.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eval --days 7 --sim -1
[SPARK] Similarity threshold must be between 0 and 1

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli eval --days -1 --sim 0.72
[SPARK] Evaluation days must be zero or greater
```

Both invalid invocations exit with status `1`.

## Impact

- Evaluation output can over-report matches and contradictions.
- Agents can produce misleading proof from bad threshold inputs.
- Automation sees success even though the requested evaluation window is invalid.

## Proposed Fix

Validate the CLI arguments in `cmd_eval` before calling `evaluate_predictions`:

```python
if days < 0:
    raise SystemExit(1)
if sim_threshold < 0.0 or sim_threshold > 1.0:
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eval-threshold-validation`
- Branch: `codex/fix-eval-threshold-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eval-threshold-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eval-threshold-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-eval-threshold-validation?expand=1
- Commit: `55969b1`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_eval_validation.py -q` passed.
- Behavior check: isolated `HOME` rejects `--sim -1` and `--days -1` before producing evaluation metrics.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
