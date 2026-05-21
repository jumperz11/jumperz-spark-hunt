# Packet 031: EIDOS List Views Create Store

## Summary

EIDOS list views create `~/.spark/eidos.db` in a fresh home directory:

- `spark eidos --episodes`
- `spark eidos --distillations`
- `spark eidos --policies`
- `spark eidos --steps`

These commands are read-only inspection surfaces. In a clean environment, they should show empty lists without initializing the EIDOS store.

## Mission Source

Spark Compete asks agents to inspect system state and report focused fixes. EIDOS list views are natural discovery commands for agents, so unexpected first-run writes make the hunt workflow noisier and less safe.

## Before Evidence

Read-only repro on upstream `main` with isolated homes:

```console
$ HOME="$(mktemp -d)" spark eidos --episodes
Recent Episodes (0)

$ HOME="$(mktemp -d)" spark eidos --distillations
Distillations (0)

$ HOME="$(mktemp -d)" spark eidos --policies
Policies (0)

$ HOME="$(mktemp -d)" spark eidos --steps
Steps (0)
```

Observed result for each command:

```text
exit=0
~/.spark/eidos.db is created
```

`cmd_eidos()` constructs `get_store()` before dispatching to these list-view branches. `EidosStore()` then creates `~/.spark/eidos.db` and initializes schema even though the command only needs to render an empty list.

## Expected Behavior

Fresh-home list views should remain read-only:

```text
exit=0
Recent Episodes (0) / Distillations (0) / Policies (0) / Steps (0)
no ~/.spark/eidos.db created
```

If an EIDOS store exists, the same commands should continue to list rows normally.

## Impact

- Agents cannot inspect EIDOS list surfaces without mutating local state.
- First-run discovery creates a persistent database even when there is nothing to list.
- Empty-list output looks read-only but performs hidden schema initialization.

## Proposed Fix

Check for the default EIDOS store before constructing it on list-view paths:

```python
def _eidos_store_exists():
    return (Path.home() / ".spark" / "eidos.db").exists()

store = get_store() if _eidos_store_exists() else None
episodes = store.get_recent_episodes(...) if store else []
```

Apply the same pattern to episodes, distillations, policies, and steps. Leave write-oriented and broader status paths unchanged for separate focused packets.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-eidos-list-readonly`
- Branch: `codex/fix-eidos-list-readonly`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-eidos-list-readonly
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-eidos-list-readonly
- Commit: `f157ea1 Keep EIDOS list views read-only`
- Verification: `PYTHONPATH=. python -m pytest tests/test_eidos_list_views_readonly.py tests/test_eidos.py::TestEidosStore -q` passed.
- Behavior check: `--episodes`, `--distillations`, `--distillations --type heuristic`, `--policies`, `--steps`, and `--episode missing-episode` each exit `0` in a fresh `HOME` and create no files.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
