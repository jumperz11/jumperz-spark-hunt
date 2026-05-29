# Packet 088: Voice Install Kokoro Structured Runtime Error

## Summary

`voice.install` for Kokoro raises a raw `RuntimeError` on Python 3.14 before returning the structured hook result used by Spark operator and Telegram flows. The combined local install path can also complete the faster-whisper half, then abort on Kokoro without preserving partial status.

## Impact

Spark voice setup loses a reviewer- and user-readable recovery path when the active Python runtime cannot support `kokoro-onnx`. Operators should receive a safe non-zero result that explains the runtime constraint and keeps any successful STT install state visible.

## Before

On current `vibeforge1111/spark-voice-comms` main at `75277a7` with Python 3.14:

```bash
python -m pytest -q
```

Result:

```text
4 failed, 36 passed
RuntimeError: kokoro-onnx currently requires Python <3.14. Use a Python 3.10-3.13 runtime.
```

The failing tests cover direct Kokoro install, already-installed Kokoro, Kokoro model assets from process env, and combined local voice install.

## After

PR #19 returns a structured unsupported-runtime result from Kokoro install and preserves the combined local install partial result when faster-whisper succeeds but Kokoro is blocked by the Python runtime.

Verification:

```bash
python -m pytest -q
```

Result:

```text
42 passed
```

## Fix

- Public PR: https://github.com/vibeforge1111/spark-voice-comms/pull/19
- Fork branch: https://github.com/jumperz11/spark-voice-comms/tree/codex/voice-install-kokoro-python314-structured-error
- Scope:
  - `src/voice_comms_chip/spark_hook.py`
  - `tests/test_spark_hook.py`
- Packet validation: `packet_valid=true`, `can_continue_to_review=true`, no errors, no warnings.
- Risk: small hook-path change; no provider keys, model paths, audio payloads, or supported-runtime install commands are exposed or changed.

## Duplicate Notes

Searched upstream GitHub issues and PRs for Kokoro, Python 3.14, RuntimeError, structured voice install, and local partial install terms. No matching duplicate was returned.
