# Reviewer Start Here

Last organized: 2026-06-07 13:25 UTC

This is the shortest reviewer path for current JUMPERZ Spark Compete work.

## First Four

Start with these four existing `vibeforge1111/spark-cli` PRs. They are already open, non-draft, packet-ready, based on current public upstream `fc49c16` / `spark-cli-public-installer-2026-06-03-r24-v2`, and have `pass` validator status.

| Order | PR | Validator | Why this is first |
| --- | --- | --- | --- |
| 1 | [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | `pass` | SSH host port validation; clean current-base input-validation lane. |
| 2 | [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | `pass` | Hosted allowed-host guard; clean current-base validation lane. |
| 3 | [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | `pass` | SSH doctor path redaction; clean current-base diagnostic lane. |
| 4 | [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | `pass` | Spark OS compile local-root redaction; clean current-base proof-safety lane. |

Each body starts with `Reviewer Fast Path` so the reviewer sees current base, change summary, proof location, and remaining gate before reading packet JSON.

## Full Current-Base Top 10

Use this only after the first four, or when a reviewer wants security-owner/lab routing for the higher-impact lanes.

| Order | PR | Validator | Why this is first |
| --- | --- | --- | --- |
| 1 | [#1051](https://github.com/vibeforge1111/spark-cli/pull/1051) | `pass` | SSH host port validation; clean current-base input-validation lane. |
| 2 | [#1058](https://github.com/vibeforge1111/spark-cli/pull/1058) | `pass` | Hosted allowed-host guard; clean current-base validation lane. |
| 3 | [#1059](https://github.com/vibeforge1111/spark-cli/pull/1059) | `pass` | SSH doctor path redaction; clean current-base diagnostic lane. |
| 4 | [#1081](https://github.com/vibeforge1111/spark-cli/pull/1081) | `pass` | Spark OS compile local-root redaction; clean current-base proof-safety lane. |
| 5 | [#1069](https://github.com/vibeforge1111/spark-cli/pull/1069) | `pass_with_warnings` | Sandbox local-path redaction; security-owner review expected. |
| 6 | [#1052](https://github.com/vibeforge1111/spark-cli/pull/1052) | `pass_with_warnings` | Sandbox authorization-header redaction; security-owner review expected. |
| 7 | [#1086](https://github.com/vibeforge1111/spark-cli/pull/1086) | `pass_with_warnings` | `ssh-add` approval boundary; security-owner review expected. |
| 8 | [#1215](https://github.com/vibeforge1111/spark-cli/pull/1215) | `pass_with_warnings` | `ssh-keygen` private-key approval boundary; security-owner review expected. |
| 9 | [#1255](https://github.com/vibeforge1111/spark-cli/pull/1255) | `pass_with_warnings` | SSH tunnel/proxy approval boundary; security-owner review expected. |
| 10 | [#1053](https://github.com/vibeforge1111/spark-cli/pull/1053) | `pass_with_warnings` | `git clean` destructive-action approval boundary; security-owner review expected. |

Each of these PR bodies now starts with `Reviewer Fast Path`.

## What Not To Review First

- Do not start with raw open PR volume.
- Do not start with legacy fork packet IDs.
- Do not start with older-base but packet-clean PRs [#503](https://github.com/vibeforge1111/spark-cli/pull/503), [#752](https://github.com/vibeforge1111/spark-cli/pull/752), [#758](https://github.com/vibeforge1111/spark-cli/pull/758), or [#440](https://github.com/vibeforge1111/spark-cli/pull/440) unless a reviewer wants focused rebase/repair.
- Do not treat `pass_with_warnings` as approval. It means the packet is valid but a security-owner/lab gate can still block merge or points.

## Current Blocking Conditions

These are the real remaining gates from a reviewer perspective:

| Blocker | Current handling |
| --- | --- |
| Too many open PRs | Canonical `START_HERE.md` leads with the clean first four, then the full top 10. |
| Long PR bodies | Top 10 PR bodies now include `Reviewer Fast Path`. |
| Packet completeness | 127 of 128 open `spark-cli` PRs have packet JSON; the sole missing one is non-competition [#756](https://github.com/vibeforge1111/spark-cli/pull/756). |
| Security-control warnings | Expected for sandbox/approval PRs; route to security-owner/lab. |
| Older-base PRs | Moved behind current-base queue; do not rebase unless asked. |
| Account/team mapping | Still needs reviewer/admin verification for `jumperz11` -> `JUMPERZ`; public form cannot self-edit existing team. |

## Safety State

No token/admin/private/local-path material should be copied into comments, tracker notes, packet text, logs, or screenshots. The current top queue uses redacted public summaries and safe proof references only.
