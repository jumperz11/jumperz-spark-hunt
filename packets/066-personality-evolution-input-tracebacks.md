# Packet 066: Personality Evolution Input Tracebacks

## Summary

`spark personality-evolution apply` exposes Python tracebacks for malformed signal input.

The command is meant to apply bounded user-guided personality signals. Invalid JSON, non-object JSON, and missing `--signals-file` paths should fail with Spark-safe diagnostics before calling the evolver.

## Mission Source

Spark Compete asks agents to exercise Spark learning and personality surfaces. Personality evolution is a state-changing control path, so malformed input should not expose raw JSON, file, or type errors.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '{bad json'
Traceback (most recent call last):
  ...
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '[1]'
Traceback (most recent call last):
  ...
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals-file "$tmp/missing.json"
Traceback (most recent call last):
  ...
FileNotFoundError: [Errno 2] No such file or directory
```

Observed result:

```text
malformed JSON reaches json.loads without CLI handling
non-object JSON reaches ingest_signals and raises TypeError
missing file paths raise FileNotFoundError
```

## Expected Behavior

- Invalid inline JSON exits non-zero with a Spark-safe message.
- Non-object JSON exits non-zero before `ingest_signals()`.
- Missing signal files exit non-zero without a Python traceback.
- Valid JSON objects keep working.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '{bad json'
[SPARK] Signals payload must be valid JSON

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals '[1]'
[SPARK] Signals payload must be a JSON object

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli personality-evolution apply --signals-file "$tmp/missing.json"
[SPARK] Signals file not found
```

All invalid invocations exit with status `1` and do not create a personality evolution state file.

## Impact

- Agents probing personality evolution get raw Python tracebacks for simple input mistakes.
- Non-object payloads can reach the state-changing evolver path.
- Reviewer proof for bounded personality controls becomes brittle and noisy.

## Proposed Fix

Handle signal loading at the CLI boundary:

```python
try:
    signals = json.loads(...)
except FileNotFoundError:
    raise SystemExit(1)
except json.JSONDecodeError:
    raise SystemExit(1)

if not isinstance(signals, dict):
    raise SystemExit(1)
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-personality-evolution-input`
- Branch: `codex/fix-personality-evolution-input`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-personality-evolution-input
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-personality-evolution-input
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-personality-evolution-input?expand=1
- Commit: `c1e84b1`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_personality_evolution_input.py tests/test_personality_evolver.py -q` passed.
- Behavior check: isolated `HOME` rejects malformed JSON, non-object JSON, and missing signal files without tracebacks or state-file writes.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
