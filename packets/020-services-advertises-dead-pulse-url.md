# Packet 020: Services Advertises Dead Pulse URL

## Summary

`spark services` reports Spark Pulse as stopped and says the Pulse app file is missing, but still prints a local Spark Pulse URL as if it is available.

This creates a false-ready state for agents and users checking local service readiness.

## Mission Source

Spark Compete mission:

> Ask Spark to compare `spark live status`, Telegram readiness, and local CLI readiness. Report confusing differences or false ready states.

Related site surface: service/readiness checks and first-run recovery.

## Before Evidence

Read-only command:

```console
$ spark services
[spark] mind: RUNNING (healthy)
[spark] sparkd: RUNNING (healthy)
[spark] pulse: STOPPED
[spark] bridge_worker: RUNNING
[spark] scheduler: RUNNING
[spark] watchdog: RUNNING
[spark] logs: /Users/jumperz/.spark/logs
[spark] pulse_dir: /path/to/vibeship-spark-pulse (app.py missing)
Spark Pulse: http://127.0.0.1:8765
```

The advertised URL is not reachable:

```console
$ curl -m 3 http://127.0.0.1:8765/
curl: (7) Failed to connect to 127.0.0.1 port 8765
```

## Expected Behavior

When Pulse is stopped and the app file is missing, the service report should not advertise the URL as an available app endpoint.

Better output:

```text
[spark] pulse: STOPPED
[spark] pulse_dir: /path/to/vibeship-spark-pulse (app.py missing)
[spark] pulse_url: unavailable until Pulse starts successfully
```

## Impact

- Agents can incorrectly send users to a dead local URL.
- First-run troubleshooting becomes confusing because the same command reports both a missing app and a clickable endpoint.
- Readiness checks cannot distinguish configured, stopped, missing, and reachable states.

## Proposed Fix

Gate URL display on actual service reachability or label it clearly:

- If Pulse is running and HTTP responds, show `Spark Pulse: http://127.0.0.1:8765`.
- If Pulse is stopped, show `Spark Pulse: stopped`.
- If `app.py` is missing, show `Spark Pulse: unavailable (app.py missing)`.

## Fix Branch

Prepared locally, not pushed upstream:

- Worktree: `/Users/jumperz/Documents/spark-fix-pulse-status`
- Branch: `codex/fix-pulse-service-status`
- Commit: `05b8eab Fix Pulse service status URL reporting`
- Verification: `pytest tests/test_service_status_formatting.py -q` passed.
- Behavior check: `spark services` now prints `Spark Pulse: unavailable (app.py missing)` when Pulse is stopped and the app file is missing.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
