"""Post (or update) a single schema-diff comment on the current GitLab MR.

Combines the branch report (blocking) and last-tag report (running list)
into one note. The note carries a hidden marker so later pipeline runs edit
it in place instead of adding a new comment each time.

Runs only inside a GitLab merge-request pipeline. Needs a project access
token with `api` scope in the masked CI variable SCHEMA_DIFF_TOKEN; without
it the script prints a notice and exits 0 so the pipeline isn't blocked.

Usage:
  python util/post_mr_note.py BRANCH_REPORT.md TAG_REPORT.md
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path

MARKER = "<!-- basalt-schema-diff -->"


def api(method: str, url: str, token: str, data: dict | None = None):
    req = urllib.request.Request(
        url,
        method=method,
        headers={"PRIVATE-TOKEN": token, "Content-Type": "application/json"},
        data=json.dumps(data).encode() if data is not None else None,
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def find_note(base: str, token: str) -> int | None:
    page = 1
    while True:
        notes = api("GET", f"{base}?per_page=100&page={page}", token)
        for note in notes:
            if MARKER in note.get("body", ""):
                return note["id"]
        if len(notes) < 100:
            return None
        page += 1


def main() -> int:
    branch_md, tag_md = (Path(p).read_text(encoding="utf-8") for p in sys.argv[1:3])
    token = os.environ.get("SCHEMA_DIFF_TOKEN")
    iid = os.environ.get("CI_MERGE_REQUEST_IID")
    if not token or not iid:
        print("SCHEMA_DIFF_TOKEN or CI_MERGE_REQUEST_IID not set; skipping MR comment.")
        return 0

    tag_title = tag_md.splitlines()[0].lstrip("# ").strip()
    tag_body = "\n".join(tag_md.splitlines()[1:]).strip()
    body = (
        f"{MARKER}\n"
        f"{branch_md.strip()}\n\n"
        f"<details><summary><b>{tag_title}</b> (running list, informational)</summary>\n\n"
        f"{tag_body}\n\n</details>\n\n"
        f"<sub>Updated by pipeline [#{os.environ.get('CI_PIPELINE_ID', '?')}]"
        f"({os.environ.get('CI_PIPELINE_URL', '')}) for `{os.environ.get('CI_COMMIT_SHORT_SHA', '')}`.</sub>"
    )

    base = (
        f"{os.environ['CI_API_V4_URL']}/projects/{os.environ['CI_PROJECT_ID']}"
        f"/merge_requests/{iid}/notes"
    )
    note_id = find_note(base, token)
    if note_id:
        api("PUT", f"{base}/{note_id}", token, {"body": body})
        print(f"Updated MR note {note_id}.")
    else:
        note = api("POST", base, token, {"body": body})
        print(f"Created MR note {note['id']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
