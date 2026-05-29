# Packet 087: Spark CLI Live Tests Inherit Operator Config

## Summary

`spark live run` and `spark live restart` tests read the operator's real Spark setup file. When that setup uses external Telegram ingress, the tests fail on a clean checkout because `live_runtime_target()` resolves to `spawner-ui` instead of the local `telegram-starter` target those tests are trying to verify.

## Impact

Spark Live release testing becomes environment-dependent. A contributor with `~/.spark/state/setup.json` set to external Telegram ingress sees unrelated failures in the live command tests, while another contributor may see the same commit pass.

## Before

On current `vibeforge1111/spark-cli` master at `f2ae903`, with operator setup containing `telegram_ingress_mode=external`:

```bash
TMPDIR=/Users/jumperz/tmp/spark-cli-pytest PYTHONPATH=src python -m pytest \
  tests/test_cli.py::SparkCliTests::test_live_restart_targets_starter_bundle_with_cascade \
  tests/test_cli.py::SparkCliTests::test_live_run_starts_stack_and_follows_logs -q
```

Result:

```text
2 failed
expected 'telegram-starter', got 'spawner-ui'
```

## After

PR #438 isolates the local-mode tests with a temporary `CONFIG_PATH` and adds explicit external-ingress coverage for the `spawner-ui` target.

Focused verification:

```bash
TMPDIR=/Users/jumperz/tmp/spark-cli-pytest PYTHONPATH=src python -m pytest \
  tests/test_cli.py::SparkCliTests::test_live_restart_targets_starter_bundle_with_cascade \
  tests/test_cli.py::SparkCliTests::test_live_run_starts_stack_and_follows_logs \
  tests/test_cli.py::SparkCliTests::test_live_run_external_ingress_targets_spawner_only \
  tests/test_cli.py::SparkCliTests::test_live_restart_external_ingress_targets_spawner_only -q
```

Result:

```text
4 passed
```

Full file verification:

```bash
TMPDIR=/Users/jumperz/tmp/spark-cli-pytest PYTHONPATH=src python -m pytest tests/test_cli.py -q
```

Result:

```text
572 passed, 1 skipped, 137 subtests passed
```

## Fix

- Public PR: https://github.com/vibeforge1111/spark-cli/pull/438
- Fork branch: https://github.com/jumperz11/spark-cli/tree/codex/isolate-live-command-config-tests
- Scope: `tests/test_cli.py`
- Risk: test-only; no runtime Spark Live behavior changes.

## Duplicate Notes

Searched upstream GitHub issues and PRs for the live command, external ingress, `CONFIG_PATH`, `telegram_ingress_mode`, `telegram-starter`, and `spawner-ui` terms used in this packet. No matching duplicate was returned.
