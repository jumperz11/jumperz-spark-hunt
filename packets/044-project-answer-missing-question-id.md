# Packet 044: Project Answer Accepts Missing Question ID

## Summary

`spark project answer missing --text hello` reports success and stores an answer for a question ID that was never suggested.

This creates false project-context evidence. The user sees “Answer recorded,” the command exits `0`, and the profile contains an answer row with `question_id: missing`.

## Mission Source

Spark Compete asks agents to exercise project-understanding flows and report focused fixes. Project answers are explicit evidence, so typo or nonexistent question IDs should not become stored project memory.

## Before Evidence

Repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project answer missing --text hello
[SPARK] Answer recorded.
```

Observed result:

```text
exit=0
~/.spark/projects/<project>.json contains {"question_id": "missing", "answer": "hello"}
~/.spark/banks/global_user.jsonl contains a project_answer:general memory for "hello"
```

`cmd_project_answer()` generated the question pool, then called `record_answer()` directly. `record_answer()` falls back to category `general` when the ID is not found, so the CLI accepted unknown IDs as valid answers.

## Expected Behavior

Unknown question IDs should fail before answer/memory writes:

```text
exit=1
[SPARK] Project question not found for id: missing
```

Valid project question IDs should still work:

```text
spark project answer eng_arch --text "..."
```

Suggested IDs surfaced by `spark project questions`, such as `proj_goal`, should remain accepted.

## Impact

- Agents can accidentally create project evidence for typo IDs.
- Reviewers and later automation may treat false project answers as intentional context.
- The answer path can pollute memory with generic text that is not tied to an actual question.

## Proposed Fix

Validate the requested ID against the generated question set before recording:

```python
ensure_questions(profile)
if args.id not in _project_question_ids(profile):
    print(f"[SPARK] Project question not found for id: {args.id}")
    raise SystemExit(1)
```

The validation includes persisted profile questions and currently suggested synthetic questions so legitimate surfaced IDs keep working.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-project-answer-missing-id`
- Branch: `codex/fix-project-answer-missing-id`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-project-answer-missing-id
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-project-answer-missing-id
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-project-answer-missing-id?expand=1
- Commit: `1e080ec`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_project_answer_validation.py tests/test_project_context.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" PYTHONPATH=. python -m spark.cli project answer missing --text hello` exits `1`.
- Behavior check: no `"question_id": "missing"` or `hello` answer text is persisted after the rejected command.
- Behavior check: valid known and suggested question IDs still record successfully.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
