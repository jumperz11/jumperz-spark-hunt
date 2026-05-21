# Hunt Proof Packet

## Summary

Team JUMPERZ found a Spark Compete onboarding mismatch: the hunt brief tells agents to run `spark os compile --json`, but the local Spark CLI did not expose an `os` command.

This proof packet records the bug, impact, fix shape, and validation without coupling this repository to the old Spark source tree.

## Before

Command from the hunt brief:

```bash
spark os compile --json
```

Observed behavior:

```text
spark: error: argument command: invalid choice: 'os'
```

## Why It Matters

The first agent-readable mission step fails before agents can inspect capability, authority, trace, memory, repo-board, or gap views.

That makes the hunt harder to enter and creates confusion for teams following the official instructions.

## Proposed Fix

Add a `spark os compile --json` command that emits a safe discovery snapshot with:

- capability summary
- authority and output boundary summary
- trace health
- memory aggregate counts
- repo-board status
- gap signals

The output should stay redacted and aggregate-only. It should not expose raw secrets, raw logs, raw conversations, raw memory rows, or absolute local paths.

## After

Expected successful shape:

```json
{
  "schema": "spark.os.compile.v1",
  "authority": {
    "output_boundary": "aggregates_only",
    "surface": "public_track"
  },
  "capability": {
    "cli": "spark"
  }
}
```

## Validation

Focused test result from the local fix branch:

```text
uv run --extra dev pytest tests/test_cli_os.py
3 passed
```

Manual smoke result:

```text
spark os compile --json
emits schema spark.os.compile.v1
```

## Fix Branch

Prepared on the `jumperz11` fork, not opened upstream yet:

- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/spark-os-compile-command
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/spark-os-compile-command?expand=1
- Commit: `00397b9 Add Spark OS compile command`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q` passed.
- Behavior check: `spark os compile --json` emits `spark.os.compile.v1` with the expected safe discovery sections.

## Submission Status

This clean repository is a proof hub only. It is not an upstream PR and does not push changes to any old repository.

Reviewer routing is pending.
