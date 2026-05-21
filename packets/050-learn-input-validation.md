# Packet 050: Learn Command Accepts Invalid Input And Crashes On Filtered Insights

## Summary

`spark learn` does not consistently reject invalid user input.

Invalid categories print an error but exit `0`, out-of-range reliability values are persisted as raw confidence, and filtered/empty insights crash with an `AttributeError`.

## Mission Source

Spark Compete asks agents to exercise learning and validation loops. Manual learning is a core mutation command, so invalid learning input needs a clear non-zero failure instead of false success, corrupt confidence, or tracebacks.

## Before Evidence

Repro on upstream `main` with isolated homes:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn invalid "x"
Unknown category: invalid
Valid: self, self_awareness, user, user_understanding, reasoning, context, wisdom, meta, meta_learning, communication, creativity
```

Observed result:

```text
exit=0
```

Filtered or empty insight text crashes:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom ""
AttributeError: 'NoneType' object has no attribute 'insight'
```

Out-of-range reliability is accepted and written:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom "When preparing a focused fix, reproduce the failing command first and add a narrow regression test before changing the implementation." --reliability 1.2
Learned [wisdom]: When preparing a focused fix, reproduce the failing command first and add a narrow regression test before changing the implementation.
Reliability: 99%
```

Persisted state includes:

```json
"confidence": 1.2
```

## Expected Behavior

Invalid learning input should fail clearly before writing state:

```text
exit=1
Unknown category: invalid
```

```text
exit=1
Reliability must be between 0 and 1.
```

```text
exit=1
Insight text cannot be empty.
```

If the learner filters an insight, the CLI should report that no insight was stored instead of dereferencing `None`.

## Impact

- Automation can treat invalid category submissions as successful learning.
- Manual learning can persist confidence values outside the documented `0-1` range.
- Filtered insights produce raw tracebacks instead of actionable CLI output.
- Learning workflows receive noisy or corrupt evidence from invalid commands.

## Proposed Fix

Validate `spark learn` inputs before calling the learner, and handle a filtered `None` result:

```python
if cat_key not in category_map:
    raise SystemExit(1)
if not 0.0 <= args.reliability <= 1.0:
    raise SystemExit(1)
if not args.insight.strip():
    raise SystemExit(1)
if insight is None:
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-learn-input-validation`
- Branch: `codex/fix-learn-input-validation`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-learn-input-validation
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-learn-input-validation
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-learn-input-validation?expand=1
- Commit: `83d8aac`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_learn_validation.py tests/test_cognitive_noise_filter.py -q` passed.
- Behavior checks:
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn invalid "x"` exits `1`.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom "x" --reliability 1.2` exits `1`.
  - `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli learn wisdom ""` exits `1`.
  - Valid actionable learning input still stores successfully.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
