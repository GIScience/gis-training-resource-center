#!/usr/bin/env python3
"""
check_site_links.py

Check every internal link, image and #anchor in the built books.

Why check the built HTML?
-------------------------
MyST's own link check doesn't recognise the stable <a id="..."> anchors that
scripts/add_stable_anchors.py adds to headings, so the build log is full of false
alarms (those warnings are switched off in the book configs). Checking the HTML
catches what readers actually hit: missing pages, missing images, anchors that
don't exist, and links that only work on GitHub Pages.

The three books are checked together, laid out like the published site:
    /en -> english/_build/html    /es -> spanish/_build/html    /fr -> french/_build/html

Usage
-----
Build the books first (build_preview_book.bat, or the jupyter-book commands in the
README), then from the repository root:

    python scripts/check_site_links.py                # all languages
    python scripts/check_site_links.py --lang en      # English only
    python scripts/check_site_links.py --orphans      # also check pages not in the TOC
    python scripts/check_site_links.py --external     # also check external URLs (slow)

Exit code is 1 when problems are found on pages in the table of contents.
"""
import argparse
import os
import posixpath
import sys
from collections import defaultdict
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = {
    "en": ("english", "content/en/_toc.yml"),
    "es": ("spanish", "content/es/es_toc.yml"),
    "fr": ("french", "content/fr/fr_toc.yml"),
}
SITE_PREFIX = "/gis-training-resource-center/"
SKIP_DIRS = {"_static", "_sources", "_images", "_sphinx_design_static", "_panels_static"}
SKIP_PAGES = {"genindex.html", "search.html", "py-modindex.html"}


def book_dir(lang):
    return os.path.join(ROOT, BOOKS[lang][0], "_build", "html")


def toc_docs(lang):
    """Document names (without extension) listed in a book's table of contents."""
    with open(os.path.join(ROOT, BOOKS[lang][1]), encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    docs = set()

    def walk(node):
        if isinstance(node, dict):
            for key in ("root", "file"):
                if isinstance(node.get(key), str):
                    docs.add(posixpath.splitext(node[key])[0])
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(data)
    return docs


def site_to_fs(site_path):
    """'fr/Module_1/x.html' -> file path, or None if outside the three books."""
    lang, _, rest = site_path.partition("/")
    if lang not in BOOKS:
        return None
    return os.path.join(book_dir(lang), *rest.split("/")) if rest else book_dir(lang)


_ids = {}


def page_ids(path):
    if path not in _ids:
        with open(path, encoding="utf-8", errors="replace") as fh:
            soup = BeautifulSoup(fh.read(), "html.parser")
        _ids[path] = {t["id"] for t in soup.find_all(id=True)} | {
            t["name"] for t in soup.find_all("a", attrs={"name": True})
        }
    return _ids[path]


def check(langs, include_orphans):
    problems = []  # (page, in_toc, kind, href, reason)
    external = defaultdict(set)
    pages = 0
    for lang in langs:
        base = book_dir(lang)
        if not os.path.isdir(base):
            sys.exit(f"No build found for '{lang}' at {base}. Build the books first.")
        in_toc = toc_docs(lang)
        for dirpath, dirnames, filenames in os.walk(base):
            rel_dir = os.path.relpath(dirpath, base).replace("\\", "/")
            if rel_dir.split("/")[0] in SKIP_DIRS:
                dirnames[:] = []
                continue
            for fn in filenames:
                if not fn.endswith(".html") or fn in SKIP_PAGES:
                    continue
                doc = posixpath.normpath(posixpath.join(rel_dir, fn[:-5]))
                page_in_toc = doc in in_toc
                if not page_in_toc and not include_orphans:
                    continue
                with open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace") as fh:
                    html = fh.read()
                if 'http-equiv="refresh"' in html and len(html) < 2000:
                    continue  # redirect stub
                pages += 1
                page = posixpath.normpath(posixpath.join(lang, rel_dir, fn))
                soup = BeautifulSoup(html, "html.parser")
                article = soup.find("article", class_="bd-article") or soup.find("main") or soup
                targets = [("link", a["href"]) for a in article.find_all("a", href=True)]
                targets += [
                    ("image" if t.name == "img" else t.name, t["src"])
                    for t in article.find_all(["img", "source", "video", "iframe"], src=True)
                ]
                for kind, href in targets:
                    reason = check_target(page, href.strip(), external)
                    if reason:
                        problems.append((page, page_in_toc, kind, href.strip(), reason))
    return problems, external, pages


def check_target(page, href, external):
    """Return a reason string if the target is broken, else None."""
    if not href or href.startswith(("mailto:", "javascript:", "tel:", "data:")):
        return None
    sp = urlsplit(href)
    if sp.scheme in ("http", "https") or href.startswith("//"):
        external[href].add(page)
        return None
    if sp.scheme:
        return f"unknown link type '{sp.scheme}:'"
    path, frag = unquote(sp.path), sp.fragment
    if path == "":
        target = page
    elif path.startswith("/"):
        if not path.startswith(SITE_PREFIX):
            return "absolute path outside the site (breaks on GitHub Pages)"
        target = posixpath.normpath(path[len(SITE_PREFIX):])
    else:
        target = posixpath.normpath(posixpath.join(posixpath.dirname(page), path))
    if target.startswith(".."):
        return "points above the site root"
    fs = site_to_fs(target)
    if fs is None:
        return "points outside the en/es/fr books"
    if os.path.isdir(fs):
        fs = os.path.join(fs, "index.html")
    if not os.path.exists(fs):
        if not os.path.splitext(fs)[1] and os.path.exists(fs + ".html"):
            return "missing .html (only works on GitHub Pages)"
        return "target does not exist"
    if frag and fs.endswith(".html") and frag not in page_ids(fs):
        return f"anchor #{frag} not found on target page"
    return None


def check_external(external):
    import requests  # installed with Sphinx
    from concurrent.futures import ThreadPoolExecutor

    headers = {"User-Agent": "Mozilla/5.0 (link check for the IFRC GIS Training Platform)"}
    skip = ("https://github.com/GIScience/gis-training-resource-center/edit/",
            "https://github.com/GIScience/gis-training-resource-center/issues/new")

    def one(url):
        u = ("https:" + url if url.startswith("//") else url).split("#")[0]
        for method in ("head", "get"):
            try:
                r = getattr(requests, method)(u, headers=headers, timeout=20, allow_redirects=True, stream=True)
                if method == "head" and r.status_code >= 400:
                    continue
                return url, (None if r.status_code < 400 else f"HTTP {r.status_code}")
            except Exception as exc:  # noqa: BLE001 - report any network error
                err = type(exc).__name__
        return url, err

    todo = [u for u in external if not u.startswith(skip)]
    with ThreadPoolExecutor(max_workers=16) as pool:
        return {u: e for u, e in pool.map(one, todo) if e}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", choices=sorted(BOOKS), action="append", help="language(s) to check (default: all)")
    ap.add_argument("--orphans", action="store_true", help="also check pages that are not in the table of contents")
    ap.add_argument("--external", action="store_true", help="also check external URLs (slow)")
    args = ap.parse_args()
    langs = args.lang or list(BOOKS)

    problems, external, pages = check(langs, args.orphans)
    by_page = defaultdict(list)
    for page, in_toc, kind, href, reason in problems:
        by_page[(page, in_toc)].append((kind, href, reason))

    print(f"Checked {pages} pages ({', '.join(langs)}).\n")
    for (page, in_toc), items in sorted(by_page.items()):
        print(f"{page}{'' if in_toc else '   (not in TOC)'}")
        for kind, href, reason in sorted(set(items)):
            print(f"    {kind:5s} {href}\n          -> {reason}")
    toc_problems = sum(1 for p in problems if p[1])
    print(f"\n{len(problems)} problems ({toc_problems} on pages in the table of contents).")

    if args.external:
        print(f"\nChecking {len(external)} external URLs ...")
        bad = check_external(external)
        for url, err in sorted(bad.items()):
            print(f"    {err:14s} {url}\n          on {', '.join(sorted(external[url])[:3])}")
        print(f"{len(bad)} external URLs failed (403/400 often just means the site blocks automated checks).")

    return 1 if toc_problems else 0


if __name__ == "__main__":
    sys.exit(main())
