# Top Review Queue

This is the JUMPERZ conversion queue: the first fixes to route for reviewer scoring.

The goal is not more volume. The goal is to make the strongest existing work easy to review, accept, and credit.

## Routing Rule

- These are fork branches on `jumperz11/vibeship-spark-intelligence`.
- No upstream PR is open for these branches unless reviewers ask for direct PR submission.
- If reviewers approve direct PRs, open them in this order.
- If reviewers prefer owner routing first, use the compare links from [PR_READY.md](PR_READY.md).

## First 10 To Route

| Order | Packet | Branch | Why this first | Verification |
| --- | --- | --- | --- | --- |
| 1 | [001](HUNT_PROOF.md) | `codex/spark-os-compile-command` | Foundational command promoted by the site's agent-readable brief. Lets agents safely inspect capability, authority, trace, memory, repo-board, and gaps. | `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q` |
| 2 | [021](packets/021-os-compile-missing-project-traceback.md) | `codex/fix-os-compile-missing-project` | Stacked hardening for the same site-promoted discovery command: missing project paths become structured failure instead of traceback. | `PYTHONPATH=. python -m pytest tests/test_cli_os.py -q` |
| 3 | [009](packets/009-starter-missions-reference-missing-cli-commands.md) | `codex/fix-mission-command-compat` | Directly tied to the 60 starter missions. Missing mission commands become read-only compatibility guidance instead of argparse invalid-choice failures. | `PYTHONPATH=. python -m pytest tests/test_cli_mission_compat.py -q` |
| 4 | [022](packets/022-opportunities-default-subcommand-traceback.md) | `codex/fix-opportunities-default` | Low-risk CLI traceback fix on an opportunity/mission workflow. `spark opportunities` becomes a safe default inbox view. | `PYTHONPATH=. python -m pytest tests/test_cli_opportunities.py -q` |
| 5 | [040](packets/040-advice-feedback-failure-exits-zero.md) | `codex/fix-advice-feedback-failure-exit` | False-success exit codes are bad for agents and scoring. Failed advice feedback now exits non-zero. | `PYTHONPATH=. python -m pytest tests/test_cli_advice_feedback_exit.py -q` |
| 6 | [041](packets/041-capture-list-reject-ignored.md) | `codex/fix-capture-list-reject` | Wires advertised capture review controls. Good user-facing reliability fix with focused scope. | `PYTHONPATH=. python -m pytest tests/test_cli_capture_actions.py -q` |
| 7 | [042](packets/042-opportunities-missing-exits-zero.md) | `codex/fix-opportunities-missing-exit` | Another false-success automation fix: missing accept/dismiss targets now return failure. | `PYTHONPATH=. python -m pytest tests/test_cli_opportunities_missing_exit.py -q` |
| 8 | [043](packets/043-outcome-link-invalid-targets.md) | `codex/fix-outcome-link-validation` | Protects validation evidence from invalid outcome IDs/confidence values. Strong proof-loop value. | `PYTHONPATH=. python -m pytest tests/test_cli_outcome_link_validation.py tests/test_outcome_log_full_stats.py -q` |
| 9 | [048](packets/048-hypotheses-outcome-missing-target.md) | `codex/fix-hypotheses-outcome-validation` | Prediction-loop validation should not claim success for missing or malformed targets. Clear learning-system bug. | `PYTHONPATH=. python -m pytest tests/test_cli_hypotheses_outcome_validation.py tests/test_project_context.py -q` |
| 10 | [049](packets/049-contradictions-resolve-missing-index.md) | `codex/fix-contradictions-resolve-validation` | Contradiction resolution should not report success unless a real contradiction was resolved. Clear validation-loop fix. | `PYTHONPATH=. python -m pytest tests/test_cli_contradictions_resolve.py tests/test_project_context.py -q` |

## Next Batch

After the first 10, route these as the next clean group:

| Packet | Branch | Reason |
| --- | --- | --- |
| [063](packets/063-process-runtime-limits.md) | `codex/fix-process-runtime-validation` | Prevents invalid runtime limits from starting mutation-heavy bridge work. |
| [065](packets/065-validate-ingest-negative-limit.md) | `codex/fix-validate-ingest-limit` | Replaces traceback with safe ingest-validation failure. |
| [081](packets/081-surprises-persisted-row-crash.md) | `codex/fix-surprises-row-format` | Stored surprise evidence should render instead of crashing. |
| [078](packets/078-sync-context-negative-limit.md) | `codex/fix-sync-context-limit-validation` | Invalid context sync bounds should fail before writing exports. |
| [080](packets/080-eidos-list-limit-ignored.md) | `codex/fix-eidos-list-limit-validation` | EIDOS decision-memory views should respect display bounds. |

## Reviewer Copy

Suggested short note:

```text
JUMPERZ has a larger proof set, but this is the first review queue. These branches are selected for clear user value, focused scope, existing tests, and direct alignment with Spark Compete's "safe proof + focused hotfix PR" loop.
```
