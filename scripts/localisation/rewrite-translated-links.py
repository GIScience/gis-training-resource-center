#!/usr/bin/env python3

from pathlib import Path
import argparse
import os
import re
import sys


PAGE_EXTENSIONS = (".md", ".ipynb", ".rst")
KNOWN_LANGUAGE_PREFIXES = {"en", "fr", "es"}


markdown_link_pattern = re.compile(
    r'(?P<prefix>!?\[[^\]]*?\]\()'
    r'(?P<url>/content/[^)\s]+|content/[^)\s]+)'
    r'(?P<suffix>\))'
)

html_attr_pattern = re.compile(
    r'(?P<prefix>\b(?:href|src)=["\'])'
    r'(?P<url>/content/[^"\']+|content/[^"\']+)'
    r'(?P<suffix>["\'])'
)


def split_url(url: str):
    match = re.match(r"^(?P<path>[^?#]*)(?P<suffix>[?#].*)?$", url)
    if not match:
        return url, ""

    return match.group("path"), match.group("suffix") or ""


def strip_content_prefix(path_part: str):
    if path_part.startswith("/content/"):
        return path_part[len("/content/"):]
    if path_part.startswith("content/"):
        return path_part[len("content/"):]
    return None


def normalise_content_path(rest: str, target_lang: str):
    parts = rest.split("/", 1)

    if len(parts) == 2 and parts[0] in KNOWN_LANGUAGE_PREFIXES:
        lang_prefix, remainder = parts

        # Keep links that explicitly point to another translated language.
        if lang_prefix not in {"en", target_lang}:
            return None

        return remainder

    return rest


def translated_filename_candidates(filename: str, target_lang: str):
    candidates = []

    if filename.startswith("en_"):
        candidates.append(f"{target_lang}_{filename[len('en_'):]}")
        candidates.append(filename)
    elif filename.startswith(f"{target_lang}_"):
        candidates.append(filename)
    else:
        candidates.append(filename)

    return candidates


def find_translated_target(book_root: Path, rest: str, target_lang: str):
    rest_path = Path(rest)
    parent = rest_path.parent
    filename = rest_path.name

    for candidate_name in translated_filename_candidates(filename, target_lang):
        candidate = book_root / parent / candidate_name
        if candidate.exists():
            return candidate

    return None


def convert_url(url: str, current_file: Path, book_root: Path, target_lang: str) -> str:
    path_part, suffix = split_url(url)

    rest = strip_content_prefix(path_part)
    if rest is None:
        return url

    rest = normalise_content_path(rest, target_lang)
    if rest is None:
        return url

    # Only rewrite source-page links, not figures, videos, data, etc.
    if not rest.endswith(PAGE_EXTENSIONS):
        return url

    target_file = find_translated_target(book_root, rest, target_lang)

    if target_file is None:
        print(f"Skipped missing translated target: {url} in {current_file}")
        return url

    relative_path = os.path.relpath(target_file, start=current_file.parent)
    relative_path = relative_path.replace("\\", "/")

    return relative_path + suffix


def process_file(path: Path, book_root: Path, target_lang: str) -> bool:
    text = path.read_text(encoding="utf-8")

    def replace_markdown(match):
        new_url = convert_url(match.group("url"), path, book_root, target_lang)
        return f'{match.group("prefix")}{new_url}{match.group("suffix")}'

    def replace_html(match):
        new_url = convert_url(match.group("url"), path, book_root, target_lang)
        return f'{match.group("prefix")}{new_url}{match.group("suffix")}'

    new_text = markdown_link_pattern.sub(replace_markdown, text)
    new_text = html_attr_pattern.sub(replace_html, new_text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8", newline="")
        print(f"Updated {path}")
        return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Rewrite /content/... links in translated Markdown files."
    )
    parser.add_argument(
        "--lang",
        required=True,
        help="Target language code, for example fr or es.",
    )
    parser.add_argument(
        "--content-root",
        default="content",
        help="Content root folder. Default: content",
    )

    args = parser.parse_args()

    target_lang = args.lang
    content_root = Path(args.content_root)
    book_root = (content_root / target_lang).resolve()

    if not book_root.exists():
        print(f"Translated content folder does not exist: {book_root}", file=sys.stderr)
        return 1

    updated_count = 0

    for md_file in book_root.rglob("*.md"):
        if process_file(md_file, book_root, target_lang):
            updated_count += 1

    print(f"Updated files: {updated_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())