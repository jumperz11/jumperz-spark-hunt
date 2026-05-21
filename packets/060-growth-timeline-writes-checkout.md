# Packet 060: Growth Timeline Writes State Into Source Checkout

## Summary

`spark timeline` stores growth state under the source checkout at `.spark/growth.json` instead of the user Spark directory.

The CLI command is presented as a growth timeline view, but its tracker path is anchored to `Path(__file__).parent.parent`, so running it from a clean checkout can create or update a repo-local `.spark/growth.json`.

## Mission Source

Spark Compete asks agents to exercise Spark CLI workflows in clean repos. Commands that mutate the source checkout are high-signal because they create local noise, confuse proof diffs, and make view-style commands unsafe in review worktrees.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ tmp="$(mktemp -d)"
$ HOME="$tmp" PYTHONPATH=. python - <<'PY'
from lib.growth_tracker import GrowthTracker
print(GrowthTracker.GROWTH_FILE)
PY
/path/to/vibeship-spark-intelligence/.spark/growth.json
```

Running the CLI creates or updates that checkout-local file:

```console
$ HOME="$tmp" PYTHONPATH=. python -m spark.cli timeline --limit 0
🌱 **Day 1** — Just getting started

**0** insights learned
**0%** average reliability
**0** promoted to docs
```

Observed result:

```text
repo checkout: .spark/growth.json exists/updates
isolated HOME: no ~/.spark/growth.json
```

## Expected Behavior

Growth state should follow the rest of Spark user state and write to `Path.home() / ".spark" / "growth.json"`.

After the fix:

```console
$ HOME="$tmp" PYTHONPATH=. python - <<'PY'
from lib.growth_tracker import GrowthTracker
print(GrowthTracker.GROWTH_FILE)
PY
$tmp/.spark/growth.json

$ HOME="$tmp" PYTHONPATH=. python -m spark.cli timeline --limit 0
...
$ find "$tmp/.spark" -maxdepth 2 -type f
$tmp/.spark/growth.json
```

The worktree does not receive `.spark/growth.json`.

## Impact

- A CLI timeline command mutates the source checkout instead of user state.
- Review and proof worktrees can pick up unrelated local files from simple inspection.
- Isolated `HOME` runs do not isolate growth tracker state.

## Proposed Fix

Change the growth tracker storage path:

```python
GROWTH_FILE = Path.home() / ".spark" / "growth.json"
```

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-growth-tracker-home-path`
- Branch: `codex/fix-growth-tracker-home-path`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-growth-tracker-home-path
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-growth-tracker-home-path
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-growth-tracker-home-path?expand=1
- Commit: `683bf28`
- Verification: `PYTHONPATH=. python -m pytest tests/test_growth_tracker_storage.py -q` passed.
- Behavior check: `HOME="$tmp" PYTHONPATH=. python -m spark.cli timeline --limit 0` writes `$tmp/.spark/growth.json` and does not create `.spark/growth.json` in the worktree.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
