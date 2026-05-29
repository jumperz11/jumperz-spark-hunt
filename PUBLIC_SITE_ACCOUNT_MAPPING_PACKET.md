# Reviewer-Routed Public Site Account Mapping Packet

Status: posted as reviewer-routed candidate, not counted in the 86 documented Spark Compete findings/fix packets unless reviewers accept it for routing.

Posted intake comment:

https://github.com/vibeforge1111/Spark-Agent-Site/issues/46#issuecomment-4573182952

Validator result:

- `packet_valid: true`
- `status: pass`
- `error_count: 0`
- `warning_count: 0`
- `next_step: continue_to_review_gates`

## Why This Matters

The public Spark Compete form requires a device-holder GitHub identity, but the Team PR GitHub accounts field is optional. Public point gates later require the PR author to map to a registered team GitHub account or reviewer verification.

That mismatch can create a successful team registration that still fails the account mapping gate later. This is close to the current JUMPERZ blocker, but the packet is framed as a public-site UX/data-shape issue for future teams, not as a request to bypass review gates.

## Suggested Intake

Post as a comment to:

https://github.com/vibeforge1111/Spark-Agent-Site/issues/46

Suggested heading:

```text
[spark-compete] Reviewer-routed public-site account mapping registration packet
```

## Packet

```json
{
  "schema": "spark-compete-hotfix-v1",
  "event": "spark-compete-first-event",
  "submission_mode": "reviewer_routed_packet",
  "submission_target_url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/46",
  "team": {
    "name": "JUMPERZ",
    "members": ["JUMPERZ", "Basjee01", "acexqt"],
    "llm_device_holder": "JUMPERZ",
    "device_holder_github": "https://github.com/jumperz11",
    "github_accounts": ["jumperz11"]
  },
  "target_repo": {
    "id": "reviewer-routed/spark-compete-public-site",
    "source": "https://compete.sparkswarm.ai",
    "owner_surface": "spark-compete-public-site"
  },
  "issue": {
    "type": "usage_friction",
    "severity": "medium",
    "title": "Team form allows registration without mapping required device-holder GitHub into team PR accounts",
    "actual_behavior": "The public Spark Compete registration form requires a Device holder GitHub value, but the Team PR GitHub accounts field is optional and is not automatically populated with that required device-holder account. A team can therefore register successfully while leaving the account list empty or incomplete, then later hit the public-points gate where the PR author must map to a registered team GitHub account.",
    "expected_behavior": "A required device-holder GitHub identity should either be automatically included in github_accounts or the form should require at least one team PR GitHub account before registration, so the registration success state does not create a later account-mapping dead end.",
    "repro_steps": [
      "Open https://compete.sparkswarm.ai/ and inspect the registration form behavior.",
      "The required Device holder GitHub field is separate from the optional Team PR GitHub accounts field.",
      "Bounded public-site script inspection shows buildTeamPayload includes required contact separately while github_accounts comes only from the optional accounts input.",
      "Bounded public-site script inspection shows validatePayload validates contact and validates github_accounts entries only when present; it does not require at least one github_accounts entry and does not copy contact into github_accounts.",
      "Compare with docs/scoring-gates.md, which says public points require the PR author to map to a registered team GitHub account or reviewer verification."
    ],
    "affected_workflow": "Spark Compete team registration, PR author mapping, and public points gate clarity"
  },
  "evidence": {
    "safe_links_only": true,
    "before_after_proof": "Before: the required Device holder GitHub can be valid while Team PR GitHub accounts remains empty, leaving no guaranteed account mapping for later PR credit. After: proposed public-site behavior would include the required device-holder GitHub in github_accounts or block registration until at least one team PR GitHub account is present.",
    "links": [
      "https://compete.sparkswarm.ai/",
      "https://compete.sparkswarm.ai/docs/scoring-gates.md",
      "https://github.com/vibeforge1111/Spark-Agent-Site/issues/46"
    ],
    "forbidden": ["pdf", "zip", "exe", "unknown downloads", "shortened links", "archives", "binaries", "tokens", "browser cookies", "wallet material", "raw logs", "raw conversations", "raw memory", "raw patches", "private repo maps", "private scoring details"]
  },
  "proposed_fix": {
    "approach": "In the public-site team registration handler, normalize the required device-holder GitHub identity and include it in github_accounts when building the registration payload, or require the Team PR GitHub accounts field to contain at least one valid GitHub identity before POST /api/teams. The UI copy should make clear that these accounts are used for PR author mapping.",
    "files_expected": ["teams.js"],
    "tests_or_smoke": "Static smoke: inspect the public registration form script behavior. Expected post-fix smoke: submitting a team with a valid Device holder GitHub and blank Team PR GitHub accounts either sends github_accounts containing the normalized device-holder account or blocks submission with a clear message."
  },
  "pr": {
    "branch": "spark-compete/reviewer-routed-account-mapping-registration",
    "title_prefix": "[spark-compete]",
    "author_github": "jumperz11",
    "body_must_include": ["packet", "team", "pr_author", "repo", "actual_behavior", "expected_behavior", "repro_steps", "before_after_proof", "tests_or_smoke", "duplicate_notes", "risk_notes", "review_claim"],
    "url": "https://github.com/vibeforge1111/Spark-Agent-Site/issues/46"
  },
  "review_claim": {
    "impact_claim": "medium",
    "evidence_types": ["redacted_terminal_excerpt", "smoke_test"],
    "duplicate_notes": "Searched Spark-Agent-Site issues/PRs for github_accounts, device holder, and team_account_unverified; no existing public issue or PR was found for this registration-to-account-gate mismatch. This is distinct from JUMPERZ's team-specific account mapping request because it addresses the public registration UX/root cause for future teams.",
    "risk_notes": "Reviewer-routed public-site UX/data-shape fix only. No secrets, auth bypass, scoring internals, private admin data, raw logs, private repo maps, or account verification claims are included. Maintainers should route to the private/public site owner and verify the exact database migration or backfill behavior if needed.",
    "review_state_requested": "pr_review"
  }
}
```
