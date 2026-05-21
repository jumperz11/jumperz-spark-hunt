# Packet 041: Capture List and Reject Are Ignored

## Summary

`spark capture --list` and `spark capture --reject <id>` are advertised CLI flags, but on upstream `main` they silently do nothing and exit `0`.

The backend already has `list_pending()` and `reject_suggestion()` helpers; the CLI handler simply never calls them.

## Mission Source

Spark Compete asks agents to inspect and exercise memory capture flows. A CLI that advertises accept/list/reject controls but ignores two of them makes the review loop unreliable for both humans and agents.

## Before Evidence

Read-only repro on upstream `main` with an isolated home:

```console
$ HOME="$(mktemp -d)" spark capture --list
```

Observed result:

```text
exit=0
stdout is empty
stderr is empty
```

Second repro:

```console
$ HOME="$(mktemp -d)" spark capture --reject missing
```

Observed result:

```text
exit=0
stdout is empty
stderr is empty
```

`cmd_capture()` handles scan and accept, then returns without checking `args.list` or `args.reject`.

## Expected Behavior

`--list` should show pending suggestions or an empty-state message:

```text
exit=0
No pending suggestions.
```

`--reject <id>` should call the reject helper and report the result:

```text
exit=0
[OK] Rejected
```

If the suggestion is missing, reject should be machine-detectable:

```text
exit=1
[MISS] Not found / not pending
```

## Impact

- The documented pending-memory review loop cannot be completed from the CLI.
- Agents can believe they listed or rejected suggestions even though no operation ran.
- Silent exit `0` makes failed capture review actions hard to detect in scripts.

## Proposed Fix

Wire the advertised flags to the existing helpers:

```python
if args.list:
    print(format_pending(capture_list_pending(limit=args.limit or 10)))

if args.reject:
    ok = capture_reject(args.reject)
    print("[OK] Rejected" if ok else "[MISS] Not found / not pending")
    if not ok:
        raise SystemExit(1)
```

Also use readable ASCII status markers for accept output and return non-zero when accept cannot find a pending suggestion.

## Fix Branch

Prepared locally, pushed only to the JUMPERZ fork:

- Worktree: `/Users/jumperz/Documents/spark-fix-capture-list-reject`
- Branch: `codex/fix-capture-list-reject`
- Fork branch: https://github.com/jumperz11/vibeship-spark-intelligence/tree/codex/fix-capture-list-reject
- PR link: https://github.com/jumperz11/vibeship-spark-intelligence/pull/new/codex/fix-capture-list-reject
- Upstream compare: https://github.com/vibeforge1111/vibeship-spark-intelligence/compare/main...jumperz11:vibeship-spark-intelligence:codex/fix-capture-list-reject?expand=1
- Commit: `1f55628 Wire capture list and reject actions`
- Verification: `PYTHONPATH=. python -m pytest tests/test_cli_capture_actions.py -q` passed.
- Behavior check: `HOME="$(mktemp -d)" spark capture --list` prints `No pending suggestions.`
- Behavior check: `HOME="$(mktemp -d)" spark capture --reject missing` exits `1` and prints `[MISS] Not found / not pending`.

## Submission Status

Proof and fix branch ready in the clean JUMPERZ hunt repo. No upstream PR opened.
