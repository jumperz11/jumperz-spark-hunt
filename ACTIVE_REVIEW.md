# Active Review Control Room

Last checked: 2026-05-29 12:45 UTC

This page tracks public Spark Compete PRs that need fast, calm reviewer follow-up. It is intentionally about review readiness, not volume.

## Review SLA

- Check active PRs before opening new work.
- If a reviewer comments, reply with either a fix, a clarification, or a clean close/adoption note.
- Keep each response short, specific, and tied to tests or packet validation.
- Do not add unsafe evidence, private maps, raw logs, account material, or unrelated scoring discussion.

## Active PRs

| PR | Repo | Status | Packet | Verification | Next action |
| --- | --- | --- | --- | --- | --- |
| [#19](https://github.com/vibeforge1111/spark-voice-comms/pull/19) | `spark-voice-comms` | Open, mergeable, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | `python -m pytest -q` -> 42 passed | Watch for reviewer comments. This is the strongest current public PR lane. |
| [#20](https://github.com/vibeforge1111/spark-voice-comms/pull/20) | `spark-voice-comms` | Open, ready for review, mergeable; GitHub shows unstable check state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Hook CLI tests -> 4 passed; `py_compile` passed; invalid JSON and non-object smokes confirmed structured output | Watch for maintainer feedback. This is separate from #19 and keeps attachment hook failures structured. |
| [#441](https://github.com/vibeforge1111/spark-cli/pull/441) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Update repair tests -> 3 passed; `py_compile` passed; empty-home and installed-home smokes confirmed routing | Watch for maintainer feedback. This is a clean repair-guidance lane with no validator warnings. |
| [#440](https://github.com/vibeforge1111/spark-cli/pull/440) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | `summarize_command_output` tests -> 5 passed; `py_compile` passed; disposable `spark fix telegram --json` smoke shows after-fix detail | Watch for maintainer feedback. This is a clean repair-output quality lane with no validator warnings. |
| [#439](https://github.com/vibeforge1111/spark-cli/pull/439) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`; validator warning `security_owner_review_expected` for sign-in readiness gate | Targeted provider-readiness tests -> 10 passed; `py_compile` passed; isolated onboarding smoke shows after-fix `llm_roles` failure | Watch for security/lab or maintainer feedback. Keep responses focused on redaction, sign-in readiness, and reproducible smoke. |
| [#438](https://github.com/vibeforge1111/spark-cli/pull/438) | `spark-cli` | Open, mergeable, no comments; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Full `tests/test_cli.py` -> 572 passed, 1 skipped | Watch for comments. If blocked state becomes actionable, inspect branch protection/check requirements before changing code. |
| [#224](https://github.com/vibeforge1111/spark-telegram-bot/pull/224) | `spark-telegram-bot` | Open; maintainer requested reshape/split; reply posted | Older packet status not used as next lane | Maintainer/lab previously reported Mac Lab passed; upstream now has patch-equivalent commit `014f17f` | Do not force-push unless reviewer asks. Treat as adopted/overtaken and keep the public note concise. |

## Ready Replies

### Packet Or Format Issue

Thanks, fixed. I repaired the packet in the PR body and re-ran the Spark Compete validator. Current result: `packet_valid=true`, `can_continue_to_review=true`, with 0 errors and 0 warnings.

### Tests Or Repro Question

Thanks, confirmed. The before state reproduces with the command listed in the packet, and the current branch verifies with the listed test command. I kept the patch scoped to the files named in the packet.

### Split Or Scope Concern

Thanks, agreed. I will keep this to one root cause and one owner surface. If this PR is too broad, I can close it and open a smaller focused replacement rather than force-pushing unrelated changes.

### Overtaken Or Duplicate

Thanks, confirmed. I checked current upstream before changing the branch. If the fix is already patch-equivalent upstream, I will not force-push noise; please treat this as adopted/overtaken or tell me if you prefer a clean replacement PR.

## Next Work Gate

Open another PR only when all are true:

- It is in an allowed public repo.
- The issue is reproducible without private evidence.
- The patch is one root cause and one owner surface.
- Tests pass locally.
- The PR body includes a validator-clean `spark-compete-hotfix-v1` packet.
- Existing review comments are already answered.

## Candidate Queue

| Candidate | Repo | Why it may be worth checking | Gate before work |
| --- | --- | --- | --- |
| Research URL/evidence handling | `spark-researcher` | Safety and proof quality are high-value if reproducible. | Run tests with `PYTHONPATH=src`; find a real failure, not just env setup noise. |
| Voice install/onboard edge cases | `spark-voice-comms` | PR #19 showed real operator friction in a small code surface. | Avoid overlapping #19; pick a separate runtime or config path. |
| Builder feedback/error formatting | `spark-intelligence-builder` | Useful if a public flow throws or loses reviewer-readable context. | Install missing deps or isolate a single test target first. |
