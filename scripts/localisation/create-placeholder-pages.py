#!/usr/bin/env python3
"""Create placeholder pages for English pages that aren't translated yet.

Links in the translated books point at the translated page even before it exists (see
rewrite-translated-links.py). Until then the link renders as plain text, and cards lead
nowhere. This script creates a small page in its place, for example
`content/fr/Module_5/fr_qgis_spatial_tools.md`, that says the page isn't translated yet and
links to the English page.

It creates a placeholder for every page in the English table of contents and for every
missing page that a translated page links to. Placeholders aren't added to the translated
table of contents (`orphan: true`), so the menu only shows translated pages.

Placeholders are marked with `translation_placeholder: true` in the front matter. The script
only ever writes or deletes files with that marker, so it never touches a real translation.
When Crowdin delivers the translation, the merge replaces the placeholder. A placeholder whose
English page no longer exists is deleted. Running it twice changes nothing.

usage: python scripts/localisation/create-placeholder-pages.py --lang fr [--content-root content]
"""

from pathlib import Path
import argparse
import os
import posixpath
import re
import sys


MARKER = "translation_placeholder: true"

MESSAGES = {
    "fr": {
        "note": "Cette page n'est pas encore disponible en français.",
        "button": "Lire la version anglaise",
    },
    "es": {
        "note": "Esta página aún no está disponible en español.",
        "button": "Leer la versión en inglés",
    },
}

TEXT_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)")
CARD_LINK = re.compile(r"^\s*:link:[ \t]*(\S+)[ \t]*$", re.M)
TOC_FILE = re.compile(r"^\s*-?\s*(?:file|root):\s*(\S+)", re.M)

TEMPLATE = """---
orphan: true
{marker}
---

# {title}

:::{{note}}
{note}
:::

:::{{button-link}} {english_url}
:color: primary

{button}
:::
"""


def is_placeholder(page: Path) -> bool:
    if not page.exists():
        return False
    text = page.read_text(encoding="utf-8")
    return text.startswith("---") and MARKER in text.split("\n---", 1)[0]


def stem_of(name: str) -> str:
    return name[len("en_"):] if name.startswith("en_") else name


class Placeholders:
    def __init__(self, content_root: Path, lang: str):
        self.content_root = content_root.resolve()
        self.en_root = self.content_root / "en"
        self.book_root = self.content_root / lang
        self.lang = lang

    def book_page(self, english: Path) -> Path:
        """content/en/Module_5/en_x.md -> content/fr/Module_5/fr_x.md"""
        rel = english.relative_to(self.en_root)
        return self.book_root / rel.parent / f"{self.lang}_{stem_of(rel.name)}"

    def english_page(self, page: Path):
        """content/fr/Module_5/fr_x.md -> content/en/Module_5/en_x.md, if it exists"""
        rel = page.relative_to(self.book_root)
        stem = rel.name[len(f"{self.lang}_"):] if rel.name.startswith(f"{self.lang}_") else rel.name
        for name in (f"en_{stem}", stem):
            if (self.en_root / rel.parent / name).exists():
                return self.en_root / rel.parent / name
        return None

    def toc_pages(self):
        toc = (self.en_root / "_toc.yml").read_text(encoding="utf-8")
        for f in TOC_FILE.findall(toc):
            page = self.en_root / (f if f.endswith(".md") else f"{f}.md")
            if page.exists():
                yield page

    def linked_pages(self):
        """English pages behind links in the translated book that point at a missing page."""
        for md in sorted(self.book_root.rglob("*.md")):
            if is_placeholder(md):
                continue
            text = md.read_text(encoding="utf-8")
            for url in TEXT_LINK.findall(text) + CARD_LINK.findall(text):
                path = url.partition("#")[0]
                if not path or re.match(r"^[a-z][a-z0-9+.-]*:", path, re.I):
                    continue
                target = Path(os.path.normpath(md.parent / path))
                if target.suffix != ".md":
                    if target.suffix == ".html" or (target.suffix and not re.search(r"\.\d", target.name)):
                        continue  # a page on the live site, a download or an image
                    target = target.parent / f"{target.name}.md"
                try:
                    target.relative_to(self.book_root)
                except ValueError:
                    continue
                if target.name.startswith(f"{self.lang}_") and (not target.exists() or is_placeholder(target)):
                    english = self.english_page(target)
                    if english is not None:
                        yield english

    def render(self, english: Path, page: Path) -> str:
        text = english.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else stem_of(english.stem).replace("_", " ")
        here = page.parent.relative_to(self.content_root).as_posix()
        target = english.relative_to(self.content_root).with_suffix(".html").as_posix()
        return TEMPLATE.format(
            marker=MARKER,
            title=title,
            english_url=posixpath.relpath(target, here),
            **MESSAGES[self.lang],
        )

    def run(self):
        created, updated, removed, kept = [], [], [], 0
        wanted = {}
        for english in list(self.toc_pages()) + list(self.linked_pages()):
            wanted.setdefault(self.book_page(english), english)

        for page, english in sorted(wanted.items()):
            if page.exists() and not is_placeholder(page):
                continue  # translated
            content = self.render(english, page)
            if page.exists():
                if page.read_text(encoding="utf-8") == content:
                    kept += 1
                    continue
                updated.append(page)
            else:
                created.append(page)
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(content, encoding="utf-8", newline="\n")

        for page in sorted(self.book_root.rglob("*.md")):
            if is_placeholder(page) and self.english_page(page) is None:
                page.unlink()
                removed.append(page)
        return created, updated, removed, kept


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--lang", required=True, choices=sorted(MESSAGES), help="Target language code.")
    parser.add_argument("--content-root", default="content", help="Content root folder. Default: content")
    args = parser.parse_args()

    placeholders = Placeholders(Path(args.content_root), args.lang)
    if not placeholders.book_root.exists():
        print(f"Translated content folder does not exist: {placeholders.book_root}", file=sys.stderr)
        return 1

    created, updated, removed, kept = placeholders.run()
    root = placeholders.content_root
    print(f"Placeholder pages created: {len(created)}")
    for page in created:
        print(f"  {page.relative_to(root).as_posix()}")
    print(f"Placeholder pages updated: {len(updated)}")
    for page in updated:
        print(f"  {page.relative_to(root).as_posix()}")
    print(f"Placeholder pages removed (English page no longer exists): {len(removed)}")
    for page in removed:
        print(f"  {page.relative_to(root).as_posix()}")
    print(f"Placeholder pages unchanged: {kept}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
