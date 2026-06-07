# Top Review Queue

This is the JUMPERZ conversion queue: the first fixes to route for reviewer scoring.

The goal is not more volume. The goal is to make the strongest existing work easy to review, accept, and credit.

## Current Allowed-Repo Queue

Last organized: 2026-06-07 12:34 UTC

Use this queue before opening or routing anything new. These are already-open `vibeforge1111/spark-cli` PRs in an allowed public repo. They have validated `spark-compete-hotfix-v1` packet JSON in the PR body, no draft state, and no fresh maintainer request asking JUMPERZ for repair.

| Order | PR | Branch | Why this first | Validator state | Reviewer action |
| --- | --- | --- | --- | --- | --- |
| 1 | [#503](https://github.com/vibeforge1111/spark-cli/pull/503) | `codex/telegram-runtime-relay-status` | Clean Telegram status/reporting fix; packet passes without warnings; no comments or reviews. | `pass` | Review as a low-noise Telegram reliability lane. |
| 2 | [#752](https://github.com/vibeforge1111/spark-cli/pull/752) | `codex/telegram-voice-starter-repair-guidance` | Clean Telegram guidance fix; packet passes without warnings; no comments or reviews. | `pass` | Review as a low-risk onboarding/repair guidance lane. |
| 3 | [#758](https://github.com/vibeforge1111/spark-cli/pull/758) | `codex/telegram-repair-route-fit` | Clean Telegram repair status fix; packet now passes after wording was made path/status-specific. | `pass` | Review as a small Telegram repair-status lane. |
| 4 | [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | `codex/ssh-host-port-validation` | Clean SSH validation fix; packet passes without warnings; no comments or reviews. | `pass` | Review as an input-validation lane. |
| 5 | [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | `codex/hosted-allowed-host-guard` | Clean hosted allowed-host validation fix; packet passes without warnings; no comments or reviews. | `pass` | Review as a public-host validation lane. |
| 6 | [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | `codex/ssh-doctor-path-redaction` | Clean diagnostic redaction fix; packet passes without warnings; no comments or reviews. | `pass` | Review as a safe-output diagnostic lane. |
| 7 | [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | `codex/system-map-path-redaction` | Clean Spark OS compile local-root redaction fix; packet passes without warnings; no comments or reviews. | `pass` | Review as a safe-output/redaction lane. |
| 8 | [#440](https://github.com/vibeforge1111/spark-cli/pull/440) | `codex/healthcheck-summary-no-brace` | Healthcheck repair details fix; packet passes without warnings; already has owner/security comments, so do not bump. | `pass` | Review only if owner/security queue is ready; no contributor comment needed. |
| 9 | [#1052](https://github.com/vibeforge1111/spark-cli/pull/1052) | `codex/sandbox-authorization-token-redaction` | Higher-impact sandbox redaction fix; packet validates with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 10 | [#1086](https://github.com/vibeforge1111/spark-cli/pull/1086) | `codex/ssh-add-approval` | High-impact approval classifier lane for SSH agent mutation; packet validates with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |

## Next Security-Control Batch

These are strong, but they should trail the clean-pass queue because they naturally require security-owner review:

| PR | Branch | Reason |
| --- | --- | --- |
| [#1215](https://github.com/vibeforge1111/spark-cli/pull/1215) | `codex/ssh-keygen-approval` | Private-key generation approval boundary. |
| [#1255](https://github.com/vibeforge1111/spark-cli/pull/1255) | `codex/ssh-tunnel-approval` | SSH tunnel approval boundary. |
| [#1053](https://github.com/vibeforge1111/spark-cli/pull/1053) | `codex/git-approval-safety-hunt` | `git clean` destructive working-tree approval boundary. |
| [#1054](https://github.com/vibeforge1111/spark-cli/pull/1054) | `codex/git-discard-approval` | Worktree discard approval boundary. |
| [#1055](https://github.com/vibeforge1111/spark-cli/pull/1055) | `codex/git-stash-approval` | Stash deletion approval boundary. |

## Live Queue Rule

- Do not open new PRs while this queue is waiting for review.
- Do not comment-bump these PRs.
- If a reviewer asks for proof, packet changes, rebase, scope split, security notes, account/team routing, or safety notes, repair that PR first.
- If a PR body needs another packet edit, validate through the official Spark packet endpoint before editing.
- Keep token/admin/private/local-path material out of packet text, tracker notes, screenshots, comments, and logs.

## Legacy Fork Routing Rule

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
