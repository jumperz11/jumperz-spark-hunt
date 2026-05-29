from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "ACTIVE_REVIEW.md"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "jumperz-review-comment-check",
}


def fetch_json(url: str) -> Any:
    api_path = url.replace("https://api.github.com", "")
    try:
        output = subprocess.check_output(["gh", "api", api_path], text=True, stderr=subprocess.DEVNULL)
        return json.loads(output)
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def compact(text: str, limit: int = 320) -> str:
    value = " ".join(str(text or "").split())
    return value if len(value) <= limit else value[: limit - 3].rstrip() + "..."


def pull_urls() -> list[tuple[str, int]]:
    text = TRACKER.read_text(encoding="utf-8")
    seen: set[tuple[str, int]] = set()
    urls: list[tuple[str, int]] = []
    for match in re.finditer(r"https://github\.com/([^/\s]+/[^/\s]+)/pull/(\d+)", text):
        item = (match.group(1), int(match.group(2)))
        if item not in seen:
            seen.add(item)
            urls.append(item)
    return urls


def main() -> int:
    for repo, number in pull_urls():
        print(f"== {repo}#{number}")
        try:
            pull = fetch_json(f"https://api.github.com/repos/{repo}/pulls/{number}")
        except urllib.error.HTTPError as exc:
            print(f"error: GitHub API returned HTTP {exc.code}; rerun after gh auth login if rate-limited")
            print()
            continue
        head = pull.get("head") or {}
        print(
            "state:",
            pull.get("state"),
            "head:",
            (head.get("repo") or {}).get("full_name"),
            head.get("ref"),
            str(head.get("sha") or "")[:7],
        )
        try:
            comments = fetch_json(f"https://api.github.com/repos/{repo}/issues/{number}/comments?per_page=20")
            reviews = fetch_json(f"https://api.github.com/repos/{repo}/pulls/{number}/reviews?per_page=20")
        except urllib.error.HTTPError as exc:
            print(f"error: GitHub API returned HTTP {exc.code} while reading comments/reviews")
            print()
            continue
        if comments:
            for comment in comments[-2:]:
                user = (comment.get("user") or {}).get("login")
                print("comment:", comment.get("updated_at"), user, compact(comment.get("body") or ""))
        else:
            print("comment: none")
        if reviews:
            for review in reviews[-2:]:
                user = (review.get("user") or {}).get("login")
                print("review:", review.get("submitted_at"), user, review.get("state"), compact(review.get("body") or ""))
        else:
            print("review: none")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
