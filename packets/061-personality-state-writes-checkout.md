# Packet 061: Personality State Writes Into Source Checkout

## Summary

Spark personality state uses the source checkout `.spark` directory instead of the user Spark directory.

Both `lib.spark_voice` and `lib.aha_tracker` define their state roots with `Path(__file__).parent.parent / ".spark"`, so voice state and surprise moments can be written into a cloned repo instead of isolated `HOME`.

## Mission Source

Spark Compete asks agents to run Spark CLI and learning flows inside clean worktrees. Personality and surprise state are runtime/user state; writing them into the source checkout creates proof noise and breaks isolated-home test runs.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python - <<'PY'
from lib.spark_voice import VOICE_FILE
from lib.aha_tracker import AHA_FILE
print(VOICE_FILE)
print(AHA_FILE)
PY
/path/to/vibeship-spark-intelligence/.spark/voice.json
/path/to/vibeship-spark-intelligence/.spark/aha_moments.json
```

Observed result:

```text
runtime personality state is anchored to the checkout, not $HOME
isolated HOME does not isolate these files
```

## Expected Behavior

Voice and surprise state should follow other Spark user state:

```text
$HOME/.spark/voice.json
$HOME/.spark/aha_moments.json
```

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python - <<'PY'
from pathlib import Path
from lib.spark_voice import SparkVoice, VOICE_FILE
from lib.aha_tracker import AhaTracker, AHA_FILE, SurpriseType
SparkVoice().record_interaction()
AhaTracker().capture_surprise(SurpriseType.UNEXPECTED_SUCCESS, "fail", "pass", 0.8, {"tool": "smoke"})
print(VOICE_FILE)
print(AHA_FILE)
print(Path.cwd() in VOICE_FILE.parents)
print(Path.cwd() in AHA_FILE.parents)
PY
$tmp/.spark/voice.json
$tmp/.spark/aha_moments.json
False
False
```

## Impact

- Runtime user state can dirty or pollute source checkouts.
- Isolated-home runs do not fully isolate Spark voice/surprise state.
- Review/proof worktrees can pick up unrelated `.spark` files from simple CLI usage.

## Proposed Fix

Move both module roots to the user Spark directory:

```python
SPARK_DIR = Path.home() / ".spark"
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-voice-aha-home-path`
- Branch: `codex/fix-voice-aha-home-path`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-voice-aha-home-path
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-voice-aha-home-path
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-voice-aha-home-path?expand=1
- Commit: `ab47fb4`
- Verification: `PYTHONPATH=. python -m pytest tests/test_personality_state_storage.py tests/test_validation_loop.py tests/test_convo_iq.py tests/test_niche_net.py -q` passed.
- Behavior check: isolated `HOME` writes `voice.json` and `aha_moments.json` under `$HOME/.spark`, not under the worktree.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
