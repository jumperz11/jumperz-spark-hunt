# Packet 011: Telegram Missions Have No Visible Bot Route

## Summary

The agent playbook repeatedly tells teams to send missions to Spark Telegram agents, but the page does not expose a Telegram bot link, handle, setup route, or fallback path near the mission library.

This makes the starter missions harder to act on, especially for first-time teams.

## Surface

- Agent playbook
- Mission library
- Telegram agent onboarding
- First useful command discovery

## Before Evidence

Visible playbook heading:

```text
Send field missions to Spark agents and start hunting.
```

Mission library summary:

```text
Open 60 starter missions teams can paste into Spark Telegram agents.
```

Mission examples include Telegram-specific flows:

```text
In Telegram, test `/start` and first useful command discovery.
Test named Telegram profile setup...
Trigger a long-running Telegram task...
Compare `/run`, `/board`, and `/mission status`...
```

But the static page exposes no visible Telegram bot URL, handle, invite link, setup doc, or fallback route in the agent playbook section.

## Expected Behavior

Near the mission library, include one clear route:

```text
Open Telegram agent: <bot link>
No Telegram? Use local CLI fallback: <steps>
```

Or make the mission copy include the target route:

```text
Paste this into @SparkAgentBot or use local Spark CLI if Telegram is unavailable.
```

## Impact

- Teams can copy missions but may not know where to send them.
- Non-coder teammates have to infer the agent entrypoint.
- Telegram-specific missions become blocked before testing starts.

## Proposed Fix

Add a small "Where to run missions" block:

```text
Telegram: <bot handle/link>
Local fallback: spark status -> spark health -> proof packet
Reviewer proof: link your GitHub proof repo or PR body
```

## Submission Status

Proof ready in the clean JUMPERZ hunt repo. No upstream PR opened.
