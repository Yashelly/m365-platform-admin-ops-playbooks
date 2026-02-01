#!/usr/bin/env python3
"""Repo consistency checker (portfolio-friendly).

- Validates that local markdown links/images resolve to existing files.
- Skips external links (http/https/mailto).
- Adds lightweight guardrails (optional but helpful for portfolio repos):
  - STATUS.md must exist (evidence maturity tracking).
  - 99-evidence/placeholders/.keep must exist (keeps structure reviewable).
"""

from __future__ import annotations
from pathlib import Path
import re

LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')

SKIP_DIRS = {
    ".git",
    ".github",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
}

def iter_markdown_files(root: Path):
    for p in root.rglob("*.md"):
        # Skip vendor folders if any
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p

def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:"))

def normalize(link: str) -> str:
    # Strip anchors and query
    link = link.split("#", 1)[0].split("?", 1)[0].strip()
    return link

def check_guardrails(root: Path, errors: list[str]) -> None:
    status = root / "STATUS.md"
    if not status.exists():
        errors.append("STATUS.md is missing (track evidence maturity: Captured / Partial / Planned).")

    keep = root / "99-evidence" / "placeholders" / ".keep"
    if not keep.exists():
        errors.append("99-evidence/placeholders/.keep is missing (placeholders keep folder structure reviewable).")

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    # Guardrails first
    check_guardrails(root, errors)

    # Markdown link checks
    for md in iter_markdown_files(root):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for raw in LINK_RE.findall(text):
            link = normalize(raw)
            if not link or is_external(link):
                continue
            # Ignore pure anchors
            if link.startswith("#"):
                continue

            target = (md.parent / link).resolve()

            # Avoid escaping repo root
            try:
                target.relative_to(root.resolve())
            except Exception:
                errors.append(f"{md}: link escapes repo root: {raw}")
                continue

            if not target.exists():
                errors.append(f"{md}: missing target: {raw}")

    if errors:
        print("Repo consistency check FAILED:\n")
        for e in errors:
            print("-", e)
        return 1

    print("Repo consistency check OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
