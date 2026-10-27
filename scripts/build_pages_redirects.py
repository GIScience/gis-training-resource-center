#!/usr/bin/env python3
"""
build_pages_redirects.py

Purpose
-------
The site moved from GitHub Pages
(https://giscience.github.io/gis-training-resource-center/) to
https://gis-training.heigit.org. This script builds a small redirect-only site
that replaces the old GitHub Pages site, so old links and search results lead
to the matching page on the new domain.

What it generates
-----------------
- One redirect page for every book page (.md / .ipynb in content/en|es|fr),
  under the current URLs and under the older URLs from before the language
  split:

      /en/Module_1/x.html            → https://gis-training.heigit.org/en/Module_1/x.html
      /content/Module_1/x.html       → https://gis-training.heigit.org/en/Module_1/x.html
      /content/es/Module_1/x.html    → https://gis-training.heigit.org/es/Module_1/x.html
      /content/fr/Module_1/x.html    → https://gis-training.heigit.org/fr/Module_1/x.html

  Each page has a canonical link and a meta refresh (search engines treat this
  as a permanent redirect) and keeps the #anchor and ?query of the old link.
- A 404.html that applies the same mapping in JavaScript for any other old URL
  (pages that no longer exist, images, downloads).
- A .nojekyll file.

Usage
-----
    python scripts/build_pages_redirects.py [--out _redirect_site]

Then deploy the output folder to GitHub Pages (see
.github/workflows/deploy-pages-redirects.yml).
"""

import argparse
import html
import shutil
from pathlib import Path

NEW_BASE = "https://gis-training.heigit.org"
REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT = REPO_ROOT / "content"
LANGS = ["en", "es", "fr"]

# Old URL prefix for each language, from before the language split
LEGACY_PREFIX = {"en": "content", "es": "content/es", "fr": "content/fr"}

PAGE_TEMPLATE = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>This page has moved</title>
  <link rel="canonical" href="{target}">
  <script>location.replace("{target}" + location.search + location.hash);</script>
  <meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
  <p>The GIS Training Resource Center has moved to
  <a href="{target}">{target}</a>.</p>
</body>
</html>
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>This page has moved</title>
  <meta name="robots" content="noindex">
  <script>
    (function () {
      var base = "__NEW_BASE__";
      var path = location.pathname.replace(/^\\/gis-training-resource-center/, "");
      path = path
        .replace(/^\\/content\\/(es|fr)\\//, "/$1/")
        .replace(/^\\/content\\//, "/en/");
      location.replace(base + path + location.search + location.hash);
    })();
  </script>
</head>
<body>
  <p>The GIS Training Resource Center has moved to
  <a href="__NEW_BASE__/">__NEW_BASE__</a>.</p>
</body>
</html>
""".replace("__NEW_BASE__", NEW_BASE)


def book_pages(lang):
    """Yield page paths (relative, ending in .html) for one language book."""
    root = CONTENT / lang
    for src in sorted(root.rglob("*")):
        if src.suffix not in (".md", ".ipynb"):
            continue
        rel = src.relative_to(root)
        if any(part.startswith(("_", ".")) or part in ("venv",) for part in rel.parts):
            continue
        yield rel.with_suffix(".html").as_posix()
    # Pages Jupyter Book adds on its own
    yield from ("index.html", "search.html", "genindex.html")


def write_redirect(out, old_path, target, lang):
    dest = out / old_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        PAGE_TEMPLATE.format(lang=lang, target=html.escape(target, quote=True)),
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", default=str(REPO_ROOT / "_redirect_site"))
    args = parser.parse_args()

    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    count = 0
    for lang in LANGS:
        for page in book_pages(lang):
            target = f"{NEW_BASE}/{lang}/{page}"
            write_redirect(out, f"{lang}/{page}", target, lang)
            write_redirect(out, f"{LEGACY_PREFIX[lang]}/{page}", target, lang)
            count += 2

    write_redirect(out, "index.html", f"{NEW_BASE}/", "en")
    (out / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    (out / ".nojekyll").touch()

    print(f"Wrote {count + 1} redirect pages and 404.html to {out}")


if __name__ == "__main__":
    main()
