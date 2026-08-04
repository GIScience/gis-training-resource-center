from pathlib import Path
import os
import re

BOOK_ROOT = Path("content/en").resolve()

# Skip cross-language links so we do not accidentally rewrite /content/es/... or /content/fr/...
SKIP_PREFIXES = ("es/", "fr/")

# Matches Markdown links/images like:
# [text](/content/Module_2/page.md)
# ![alt](/content/Module_2/image.md)
markdown_link_pattern = re.compile(
    r'(?P<prefix>!?\[[^\]]*?\]\()'
    r'(?P<url>/content/[^)\s]+|content/[^)\s]+)'
    r'(?P<suffix>\))'
)

# Matches basic HTML href/src links like:
# href="/content/Module_2/page.md"
# src="/content/Module_2/page.md"
html_attr_pattern = re.compile(
    r'(?P<prefix>\b(?:href|src)=["\'])'
    r'(?P<url>/content/[^"\']+|content/[^"\']+)'
    r'(?P<suffix>["\'])'
)


def split_url(url: str):
    """Split URL into path and anchor/query suffix."""
    for separator in ("#", "?"):
        if separator in url:
            path, suffix = url.split(separator, 1)
            return path, separator + suffix
    return url, ""


def convert_url(url: str, current_file: Path) -> str:
    path_part, suffix = split_url(url)

    # Normalize leading slash
    if path_part.startswith("/content/"):
        rest = path_part[len("/content/"):]
    elif path_part.startswith("content/"):
        rest = path_part[len("content/"):]
    else:
        return url

    # If the link already contains /content/en/..., normalize it.
    if rest.startswith("en/"):
        rest = rest[len("en/"):]

    # Avoid rewriting cross-language links.
    if rest.startswith(SKIP_PREFIXES):
        return url

    # Only rewrite source-page links, not figures/videos/data.
    if not rest.endswith((".md", ".ipynb", ".rst")):
        return url

    target_file = BOOK_ROOT / rest

    if not target_file.exists():
        print(f"Skipped missing target: {url} in {current_file}")
        return url

    relative_path = os.path.relpath(target_file, start=current_file.parent)
    relative_path = relative_path.replace("\\", "/")

    return relative_path + suffix


def process_file(path: Path):
    text = path.read_text(encoding="utf-8")

    def replace_markdown(match):
        new_url = convert_url(match.group("url"), path)
        return f'{match.group("prefix")}{new_url}{match.group("suffix")}'

    def replace_html(match):
        new_url = convert_url(match.group("url"), path)
        return f'{match.group("prefix")}{new_url}{match.group("suffix")}'

    new_text = markdown_link_pattern.sub(replace_markdown, text)
    new_text = html_attr_pattern.sub(replace_html, new_text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8", newline="")
        print(f"Updated {path}")


for md_file in BOOK_ROOT.rglob("*.md"):
    process_file(md_file)