#!/usr/bin/env python3
"""
add_stable_anchors.py

Purpose
-------
This script adds stable HTML anchor tags to Markdown headings:

    ## Heading  →  ## Heading <a id="heading"></a>

These anchors are used for:
- stable internal linking
- multilingual content (anchors remain in English)
- avoiding broken links when headings are translated

Why we use this
---------------
Jupyter Book / MyST auto-generates heading anchors from text.
These break when:
- headings are renamed
- content is translated (e.g. English → Spanish)

By adding explicit HTML anchors (<a id="..."></a>), we:
- freeze anchor IDs
- keep links stable across languages
- allow automatic rewriting of file paths only

Usage
-----
1. Set the ROOT directory below
2. Run:
       python add_stable_anchors.py

3. The script will:
   - process all .md files recursively
   - add anchors to headings if missing
   - skip headings that already contain anchors

Important rules
---------------
- Only run this on SOURCE (English) files
- Do NOT run on translated files
- Anchors must remain unchanged across languages

Example
-------
Input:
    ## Installing QGIS

Output:
    ## Installing QGIS <a id="installing-qgis"></a>

After translation:
    ## Instalar QGIS <a id="installing-qgis"></a>

Notes
-----
- Anchors are unique per file
- Same anchor names can be reused across different files
- Script is safe to re-run (will not duplicate anchors)
"""

from pathlib import Path
import re
import unicodedata

# 🔧 CHANGE THIS to your target folder
ROOT = Path("content/Glossary")  # e.g. "content" or "content/module_1"

# Regex to detect markdown headings
heading_re = re.compile(r'^(#{1,6})\s+(.*)$')


def slugify(text: str) -> str:
    """Convert heading text into a URL-friendly anchor ID."""
    # Remove existing anchor if present
    text = re.sub(r'<a id=".*?"></a>', '', text)

    # Normalize unicode (remove accents)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = text.lower()
    text = text.replace("&", " and ")

    # Remove punctuation
    text = re.sub(r'[^a-z0-9\s-]', '', text)

    # Collapse whitespace and hyphens
    text = re.sub(r'[\s-]+', '-', text).strip('-')

    return text


def process_file(path: Path):
    """Process a single markdown file."""
    original_text = path.read_text(encoding="utf-8")
    lines = original_text.splitlines()

    used_ids = set()
    new_lines = []
    changes = 0

    for line in lines:
        match = heading_re.match(line)

        if not match:
            new_lines.append(line)
            continue

        hashes, title = match.groups()

        # Skip if anchor already exists
        if '<a id="' in line:
            existing = re.search(r'<a id="(.*?)"></a>', line)
            if existing:
                used_ids.add(existing.group(1))
            new_lines.append(line)
            continue

        clean_title = title.strip()
        slug = slugify(clean_title)

        if not slug:
            new_lines.append(line)
            continue

        # Ensure uniqueness within file
        base = slug
        i = 2
        while slug in used_ids:
            slug = f"{base}-{i}"
            i += 1

        used_ids.add(slug)

        new_line = f'{hashes} {clean_title} <a id="{slug}"></a>'
        new_lines.append(new_line)
        changes += 1

    new_text = "\n".join(new_lines) + "\n"

    if new_text != original_text:
        path.write_text(new_text, encoding="utf-8")
        print(f"CHANGED ({changes} headings): {path}")
    else:
        print(f"NO CHANGE: {path}")


def main():
    print(f"Processing folder: {ROOT.resolve()}")

    if not ROOT.exists():
        print("ERROR: Folder does not exist.")
        return

    for md_file in ROOT.rglob("*.md"):
        process_file(md_file)


if __name__ == "__main__":
    main()