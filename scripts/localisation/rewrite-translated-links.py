#!/usr/bin/env python3
"""Rewrite links in translated Markdown so they work in the translated book.

Crowdin translations keep the links of the English source, for example
`../Wiki/en_qgis_digitisation_wiki.md#adding-geometries-to-a-layer`. Inside the French or
Spanish book that file doesn't exist, and links to another book (`../../en/...md`) render
as plain text. For every text link and card link to an English page, this script points it
at the translated page (`fr_...md` / `es_...md`), in the same folder as the English page.
If that page isn't translated yet, the link starts working as soon as it is.

Language switch links ("English version" on a translated page) stay English. On cards they
become relative links to the English HTML page (`../../en/...html`); text links point at the
English page on the live site (full URL).

Images, downloads and external links are left alone. Running it twice changes nothing.

usage: python scripts/localisation/rewrite-translated-links.py --lang fr [--content-root content]
"""

from pathlib import Path
import argparse
import os
import posixpath
import re
import sys


SITE_URL = "https://giscience.github.io/gis-training-resource-center"

# [text](target) or [text](target "title"), but not images ![alt](...)
TEXT_LINK = re.compile(r'(?<!!)(\[[^\]\n]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
# :link: target on a card, with an optional :link-type: line in the same option block
CARD_LINK = re.compile(r"^(\s*):link:[ \t]*(\S+)[ \t]*$", re.M)
LINK_TYPE_DOC = re.compile(r"^\s*:link-type:\s*doc\s*$")


def stem_of(name: str) -> str:
    """Page name without the language prefix: en_qgis_x.md -> qgis_x.md"""
    return name[len("en_"):] if name.startswith("en_") else name


class Rewriter:
    def __init__(self, content_root: Path, lang: str, site_url: str):
        self.content_root = content_root.resolve()
        self.en_root = self.content_root / "en"
        self.book_root = self.content_root / lang
        self.lang = lang
        self.site_url = site_url.rstrip("/")
        self.counts = {"translated": 0, "untranslated": 0, "english": 0, "card": 0}
        self.untranslated = []
        self.unresolved = []
        self.missing_anchors = []
        self._anchors = {}

    def has_anchor(self, page: Path, anchor: str) -> bool:
        """Whether the page defines the anchor (<a id>, a MyST label, or a heading slug)."""
        if page not in self._anchors:
            text = page.read_text(encoding="utf-8")
            ids = set(re.findall(r'\bid="([^"]+)"', text))
            ids |= set(re.findall(r"^\(([^)]+)\)=\s*$", text, re.M))
            for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M):
                heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
                ids.add(re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", heading)))
            self._anchors[page] = ids
        return anchor in self._anchors[page]

    def check_anchor(self, current: Path, page: Path, anchor: str, url: str):
        if anchor and not self.has_anchor(page, anchor):
            self.missing_anchors.append((current, url))

    def resolve(self, current: Path, path: str):
        """Return ("book", page) for an existing page in the translated book,
        ("en", path inside content/en) for a link written into the English book,
        ("source", path inside content/en) for an English source link that Crowdin left
        unchanged (it points into the translated book, where the page doesn't exist),
        or None."""
        if path.startswith("/content/"):
            path = path[len("/"):]
        if path.startswith("content/"):
            target = self.content_root.parent / path
        else:
            target = Path(os.path.normpath(current.parent / path))

        if target.suffix != ".md":
            # Card doc links leave out .md (and page names can contain dots, e.g. 3.44)
            target = target.parent / f"{target.name}.md"

        for root in (self.en_root, self.book_root):
            try:
                rel = target.relative_to(root)
            except ValueError:
                continue
            if root == self.en_root:
                return "en", rel
            if target.exists():
                return "book", target
            return "source", rel
        return None

    def translated_page(self, rel: Path):
        name = rel.name
        for candidate in (f"{self.lang}_{stem_of(name)}", name):
            page = self.book_root / rel.parent / candidate
            if page.exists():
                return page
        return None

    def rewrite(self, current: Path, url: str, card_doc: bool, url_card: bool = False):
        """Return (new_url, kind) or None to leave the link alone.

        kind is "translated", "english", or "card" (a url-type card pointing at a page
        in the translated book, which only works as a doc link).
        """
        if re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith(("#", "//")):
            return None
        path, _, anchor = url.partition("#")
        suffix = f"#{anchor}" if anchor else ""
        if not path or (not card_doc and not path.endswith(".md")):
            return None

        resolved = self.resolve(current, path)
        if resolved is None:
            return None
        where, rel = resolved
        if where == "book":
            if not url_card:
                return None  # already points at an existing translated page
            self.check_anchor(current, rel, anchor, url)
            new = os.path.relpath(rel, start=current.parent).replace("\\", "/")
            return new[: -len(".md")] + suffix, "card"

        page = self.translated_page(rel)
        # A link written into the English book that leads back to this very page, without a
        # section anchor, is a language switch ("also available in English"): keep it English.
        switch = where == "en" and not anchor and page is not None and page.resolve() == current.resolve()
        if page is not None and not switch:
            self.check_anchor(current, page, anchor, url)
            new = os.path.relpath(page, start=current.parent).replace("\\", "/")
            if card_doc:
                new = new[: -len(".md")]
            return new + suffix, "translated"

        if switch:
            html = rel.with_suffix(".html").as_posix()
            if card_doc:
                # The books are published side by side (/en, /es, /fr), so a relative
                # url-type link works on any domain.
                here = current.parent.relative_to(self.content_root).as_posix()
                return posixpath.relpath(f"en/{html}", here) + suffix, "english"
            return f"{self.site_url}/en/{html}{suffix}", "english"

        if where == "source" and rel.name.startswith(f"{self.lang}_"):
            return None  # already points at a page that isn't translated yet

        if (self.en_root / rel).exists():
            # Not translated yet: point at the page it will become, so the link works
            # as soon as the translation is merged.
            page = self.book_root / rel.parent / f"{self.lang}_{stem_of(rel.name)}"
            self.untranslated.append((current, page))
            new = os.path.relpath(page, start=current.parent).replace("\\", "/")
            if card_doc:
                new = new[: -len(".md")]
            return new + suffix, "untranslated"

        self.unresolved.append((current, url))
        return None

    def process(self, current: Path) -> bool:
        text = current.read_text(encoding="utf-8")

        def text_link(m):
            result = self.rewrite(current, m.group(2), card_doc=False)
            if result is None:
                return m.group(0)
            new, kind = result
            self.counts[kind] += 1
            return f"{m.group(1)}{new}{m.group(3)}"

        new_text = TEXT_LINK.sub(text_link, text)

        # Card links. First decide what each line becomes, then rebuild the file.
        lines = new_text.splitlines(keepends=True)
        replace = {}  # line index -> list of new lines ([] removes the line)
        option = re.compile(r"^\s*:[\w-]+:")
        for i, line in enumerate(lines):
            m = CARD_LINK.match(line.rstrip("\r\n"))
            if not m:
                continue

            # Option lines (":key: value") directly around :link: belong to the same card.
            start, end = i, i + 1
            while start > 0 and option.match(lines[start - 1]):
                start -= 1
            while end < len(lines) and option.match(lines[end]):
                end += 1
            type_lines = [j for j in range(start, end) if LINK_TYPE_DOC.match(lines[j])]

            url = m.group(2)
            url_card = not type_lines
            if url_card:
                path = url.partition("#")[0]
                if Path(path).suffix not in ("", ".md") and not re.search(r"\.\d", Path(path).name):
                    continue  # a plain url-type card link, e.g. a download or .html page
                if path.endswith(".md"):
                    url = path[: -len(".md")] + url[len(path):]
            result = self.rewrite(current, url, card_doc=True, url_card=url_card)
            if result is None:
                continue

            new, kind = result
            self.counts[kind] += 1
            newline = line[len(line.rstrip("\r\n")):]
            indent = m.group(1)
            replace[i] = [f"{indent}:link: {new}{newline}"]
            if kind in ("translated", "untranslated", "card") and not type_lines:
                replace[i].append(f"{indent}:link-type: doc{newline}")
            if kind == "english":
                # A full URL is a url-type link, so the card must not say :link-type: doc.
                for j in type_lines:
                    replace[j] = []

        new_text = "".join(
            "".join(replace[i]) if i in replace else line for i, line in enumerate(lines)
        )
        if new_text != text:
            current.write_text(new_text, encoding="utf-8", newline="")
            return True
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--lang", required=True, help="Target language code, for example fr or es.")
    parser.add_argument("--content-root", default="content", help="Content root folder. Default: content")
    parser.add_argument("--site-url", default=SITE_URL, help=f"Live site for untranslated pages. Default: {SITE_URL}")
    args = parser.parse_args()

    rewriter = Rewriter(Path(args.content_root), args.lang, args.site_url)
    if not rewriter.book_root.exists():
        print(f"Translated content folder does not exist: {rewriter.book_root}", file=sys.stderr)
        return 1

    updated = sum(rewriter.process(md) for md in sorted(rewriter.book_root.rglob("*.md")))

    print(f"Updated files: {updated}")
    print(f"Links to translated pages: {rewriter.counts['translated']}")
    print(f"Links to pages that aren't translated yet: {rewriter.counts['untranslated']}")
    if rewriter.untranslated:
        pages = sorted({page.relative_to(rewriter.content_root).as_posix() for _, page in rewriter.untranslated})
        print(f"  They work once these pages are translated ({len(pages)}):")
        for page in pages:
            print(f"  {page}")
    print(f"Language switch links to the English page: {rewriter.counts['english']}")
    print(f"Card links changed to doc links: {rewriter.counts['card']}")
    if rewriter.unresolved:
        print(f"Links left unchanged because the English page doesn't exist: {len(rewriter.unresolved)}")
        for page, url in rewriter.unresolved:
            print(f"  {page.relative_to(rewriter.content_root)}: {url}")
    if rewriter.missing_anchors:
        print(
            f"Links rewritten, but the #anchor isn't on the target page "
            f"(the link opens the top of the page): {len(rewriter.missing_anchors)}"
        )
        for page, url in rewriter.missing_anchors:
            print(f"  {page.relative_to(rewriter.content_root)}: {url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
