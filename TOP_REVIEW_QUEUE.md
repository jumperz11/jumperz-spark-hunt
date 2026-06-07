# Top Review Queue

This is the JUMPERZ conversion queue: the first fixes to route for reviewer scoring.

The goal is not more volume. The goal is to make the strongest existing work easy to review, accept, and credit.

Canonical start page: [START_HERE.md](START_HERE.md)

Reviewer first pass: [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051), [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058), [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059), and [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081).

## Current Allowed-Repo Queue

Last organized: 2026-06-07 13:25 UTC

Use this queue before opening or routing anything new. These are already-open `vibeforge1111/spark-cli` PRs in an allowed public repo. They have validated `spark-compete-hotfix-v1` packet JSON in the PR body, no draft state, no fresh maintainer request asking JUMPERZ for repair, and are based on current upstream `origin/master` `fc49c16` (`spark-cli-public-installer-2026-06-03-r24-v2`).

| Order | PR | Branch | Why this first | Validator state | Reviewer action |
| --- | --- | --- | --- | --- | --- |
| 1 | [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | `codex/ssh-host-port-validation` | Clean SSH validation fix; packet passes without warnings; current-base PR with no comments or reviews. | `pass` | Review as an input-validation lane. |
| 2 | [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | `codex/hosted-allowed-host-guard` | Clean hosted allowed-host validation fix; packet passes without warnings; current-base PR with no comments or reviews. | `pass` | Review as a public-host validation lane. |
| 3 | [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | `codex/ssh-doctor-path-redaction` | Clean diagnostic redaction fix; packet passes without warnings; current-base PR with no comments or reviews. | `pass` | Review as a safe-output diagnostic lane. |
| 4 | [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | `codex/system-map-path-redaction` | Clean Spark OS compile local-root redaction fix; packet passes without warnings; current-base PR with no comments or reviews. | `pass` | Review as a safe-output/redaction lane. |
| 5 | [#1069](https://github.com/vibeforge1111/spark-cli/pull/1069) | `codex/sandbox-output-local-path-redaction` | Sandbox output local-path redaction; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 6 | [#1052](https://github.com/vibeforge1111/spark-cli/pull/1052) | `codex/sandbox-authorization-token-redaction` | Higher-impact sandbox authorization-header redaction; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 7 | [#1086](https://github.com/vibeforge1111/spark-cli/pull/1086) | `codex/ssh-add-approval` | High-impact approval classifier lane for SSH agent mutation; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 8 | [#1215](https://github.com/vibeforge1111/spark-cli/pull/1215) | `codex/ssh-keygen-approval` | Private-key generation approval boundary; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 9 | [#1255](https://github.com/vibeforge1111/spark-cli/pull/1255) | `codex/ssh-tunnel-approval` | SSH tunnel/proxy approval boundary; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |
| 10 | [#1053](https://github.com/vibeforge1111/spark-cli/pull/1053) | `codex/git-approval-safety-hunt` | Destructive `git clean` approval boundary; current-base PR with expected security-owner warning. | `pass_with_warnings` | Security-owner/lab review expected before merge or points. |

## Behind But Still Packet-Clean

These PRs remain useful, but GitHub reports them `BEHIND` older base `f989fd0`. Do not rebase or force-push unless reviewers ask for focused rebase/repair.

| PR | Branch | Reason |
| --- | --- | --- |
| [#503](https://github.com/vibeforge1111/spark-cli/pull/503) | `codex/telegram-runtime-relay-status` | Clean Telegram status/reporting fix; packet passes without warnings but base is behind current r24-v2 master. |
| [#752](https://github.com/vibeforge1111/spark-cli/pull/752) | `codex/telegram-voice-starter-repair-guidance` | Clean Telegram guidance fix; packet passes without warnings but base is behind current r24-v2 master. |
| [#758](https://github.com/vibeforge1111/spark-cli/pull/758) | `codex/telegram-repair-route-fit` | Clean Telegram repair status fix; packet passes without warnings but base is behind current r24-v2 master. |
| [#440](https://github.com/vibeforge1111/spark-cli/pull/440) | `codex/healthcheck-summary-no-brace` | Healthcheck repair details fix; packet passes without warnings, has existing owner/security comments, and base is behind current r24-v2 master. |

## Live Queue Rule

- Do not open new PRs while this queue is waiting for review.
- Do not comment-bump these PRs.
- If a reviewer asks for proof, packet changes, rebase, scope split, security notes, account/team routing, or safety notes, repair that PR first.
- If a PR body needs another packet edit, validate through the official Spark packet endpoint before editing.
- Keep token/admin/private/local-path material out of packet text, tracker notes, screenshots, comments, and logs.

## Historical Context

Legacy fork-routing material was moved to [LEGACY_FORK_QUEUE.md](LEGACY_FORK_QUEUE.md). It is retained for audit only and is not the current reviewer-first queue.
