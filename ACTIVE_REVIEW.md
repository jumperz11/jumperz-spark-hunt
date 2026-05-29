# Active Review Control Room

Last checked: 2026-05-29 12:47 UTC

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
| [#23](https://github.com/vibeforge1111/spark-character/pull/23) | `spark-character` | Open, ready for review, mergeable clean, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Search adapter tests -> 14 passed; repo tests excluding external-chip baseline -> 88 passed, 9 deselected; redirect smoke confirmed three URL shapes | Watch for maintainer feedback. This is a focused live-search citation quality lane. |
| [#17](https://github.com/vibeforge1111/spark-personality-chip-labs/pull/17) | `spark-personality-chip-labs` | Open, ready for review, mergeable clean, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Spark hook tests -> 4 passed; full suite -> 255 passed; `py_compile` passed; missing-input and non-object-input smokes wrote structured output | Watch for maintainer feedback. This is a focused Spark hook input-boundary lane. |
| [#18](https://github.com/vibeforge1111/spark-personality-chip-labs/pull/18) | `spark-personality-chip-labs` | Open, ready for review, mergeable clean, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Validator script tests -> 2 passed; full suite -> 255 passed; `py_compile` passed; empty-dir and packaged-dir smokes confirmed corrected exits | Watch for maintainer feedback. This is a focused personality validation accuracy lane. |
| [#24](https://github.com/vibeforge1111/spark-domain-chip-labs/pull/24) | `spark-domain-chip-labs` | Open, ready for review, mergeable; GitHub shows unstable check state, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Targeted schema modules -> 6 skipped instead of collection errors; `PYTHONPATH=src python -m pytest -q` -> 1065 passed, 177 skipped, 1 unrelated saved-fixture mismatch; `py_compile` passed | Watch for maintainer feedback. This is a focused optional-dependency test collection lane; the saved-fixture mismatch is separate and outside this patch. |
| [#25](https://github.com/vibeforge1111/spark-domain-chip-labs/pull/25) | `spark-domain-chip-labs` | Open, ready for review, mergeable; GitHub shows unstable check state, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Exact saved-fixture test -> 1 passed; Startup YC operator-validation file -> 27 passed, 19 skipped; JSON validation passed; full suite still stops at unrelated #24 jsonschema blocker | Watch for maintainer feedback. This is a fixture-only provenance hash repair, split from #24. |
| [#106](https://github.com/vibeforge1111/spark-intelligence-builder/pull/106) | `spark-intelligence-builder` | Open, ready for review, mergeable; GitHub shows unstable check state, no comments | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Structured returncode regression -> 1 passed; attachment hook tests -> 16 passed; focused trio -> 3 passed; `py_compile` passed | Watch for maintainer feedback. This is a focused attachment hook success-classification lane; it treats process-0/output-returncode-1 as failure without changing normal hook execution. |
| [#441](https://github.com/vibeforge1111/spark-cli/pull/441) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Update repair tests -> 3 passed; `py_compile` passed; empty-home and installed-home smokes confirmed routing | Watch for maintainer feedback. This is a clean repair-guidance lane with no validator warnings. |
| [#440](https://github.com/vibeforge1111/spark-cli/pull/440) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | `summarize_command_output` tests -> 5 passed; `py_compile` passed; disposable `spark fix telegram --json` smoke shows after-fix detail | Watch for maintainer feedback. This is a clean repair-output quality lane with no validator warnings. |
| [#439](https://github.com/vibeforge1111/spark-cli/pull/439) | `spark-cli` | Open, ready for review, mergeable; GitHub shows blocked merge state | Valid: `packet_valid=true`, `can_continue_to_review=true`; validator warning `security_owner_review_expected` for sign-in readiness gate | Targeted provider-readiness tests -> 10 passed; `py_compile` passed; isolated onboarding smoke shows after-fix `llm_roles` failure | Watch for security/lab or maintainer feedback. Keep responses focused on redaction, sign-in readiness, and reproducible smoke. |
| [#438](https://github.com/vibeforge1111/spark-cli/pull/438) | `spark-cli` | Open, mergeable; Mac Lab failure comment answered with test-only fixture repair; GitHub now reports branch behind | Valid: `packet_valid=true`, `can_continue_to_review=true`, 0 errors/warnings | Focused live/external-ingress tests -> 5 passed after repair; previous full `tests/test_cli.py` -> 572 passed, 1 skipped | Await lab rerun/reviewer response. Do not update branch unless the reviewer asks or the behind state becomes the blocker. |
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
| Builder attachment hook execution | `spark-intelligence-builder` | PR #106 covers process-0/output-returncode-1 misclassification. | Avoid duplicating hook returncode; inspect other builder surfaces only if separate root cause. |
| Character live-search source handling | `spark-character` | PR #23 covers DuckDuckGo redirect URL decoding; adjacent parser/citation issues may still be useful. | Avoid duplicating redirect decoding; search open PRs before patching. |
| Personality hook host-output contract | `spark-personality-chip-labs` | PR #17 covers missing/non-object input in `spark_hook.py`; adjacent hook boundaries may still be worth checking. | Avoid overlapping PR #13 unsupported hook and PR #16 `hooks.py` stdin handling. |
| Personality validator CLI | `spark-personality-chip-labs` | PR #18 covers empty directories, template skipping, and current bridge summary keys. | Avoid overlapping directory validation behavior; look elsewhere unless reviewers ask. |
| Domain-chip local test collection | `spark-domain-chip-labs` | PR #24 covers optional `jsonschema` collection failures; PR #25 covers the Startup YC saved fixture hash mismatch. | Avoid duplicating importorskip or saved-hash work; move to another domain-chip lane only if it has a separate root cause. |
