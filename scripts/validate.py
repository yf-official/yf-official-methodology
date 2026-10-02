#!/usr/bin/env python3
"""Validate publication metadata and local navigation using only the standard library."""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen


def markdown_body(text):
    """Ignore fenced examples when checking headings and links."""
    return re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$", "", text,
                  flags=re.MULTILINE | re.DOTALL)


def anchors(text):
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", markdown_body(text), re.MULTILINE):
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        slug = "".join(c for c in heading.lower()
                       if c in " _-" or unicodedata.category(c)[0] in "LNM")
        slug = slug.replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def validate(root, remote=False):
    root = root.resolve()
    errors = []
    try:
        catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"catalog.json: {exc}"]
    if not isinstance(catalog, dict) or type(catalog.get("schema_version")) is not int or catalog["schema_version"] != 1:
        return ["catalog.json: expected an object with schema_version 1"]
    repository = catalog.get("repository", "")
    if not isinstance(repository, str) or not re.fullmatch(r"[\w.-]+/[\w.-]+", repository):
        return ["catalog.json: invalid owner/repository"]
    papers = catalog.get("papers")
    if not isinstance(papers, list) or not papers:
        return ["catalog.json: papers must be a nonempty list"]

    base = f"https://github.com/{repository}/releases"
    markdown = {p: p.read_text(encoding="utf-8") for p in root.rglob("*.md")
                if ".git" not in p.relative_to(root).parts}
    bib_path = root / "references.bib"
    bib = bib_path.read_text(encoding="utf-8") if bib_path.is_file() else ""
    entries = re.findall(r"@misc\{([^,]+),\s*(.*?)^\}", bib, re.MULTILINE | re.DOTALL)
    citations = dict(entries)
    if len(citations) != len(entries):
        errors.append("references.bib: duplicate citation keys")
    seen_ids, seen_keys = set(), set()
    required_strings = ("id", "project", "title", "published", "language", "publication_type",
                        "release_tag", "asset", "pdf_url", "release_url", "citation_key", "rights")
    for index, paper in enumerate(papers):
        label = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{label}: expected an object")
            continue
        invalid = [k for k in required_strings
                   if not isinstance(paper.get(k), str) or not paper[k].strip()]
        if invalid:
            errors.append(f"{label}: missing/invalid fields: {', '.join(invalid)}")
            continue
        label = paper["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", label):
            errors.append(f"{label}: id must be a lowercase slug")
        for field, seen in (("id", seen_ids), ("citation_key", seen_keys)):
            if paper[field] in seen:
                errors.append(f"{label}: duplicate {field}")
            seen.add(paper[field])
        for field in ("authors", "topics"):
            values = paper.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                errors.append(f"{label}: {field} must contain nonempty strings")
        if type(paper.get("pages")) is not int or paper["pages"] <= 0:
            errors.append(f"{label}: pages must be a positive integer")
        try:
            dt.date.fromisoformat(paper["published"])
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", paper["published"]):
                raise ValueError("expected YYYY-MM-DD")
        except ValueError:
            errors.append(f"{label}: published must be a valid YYYY-MM-DD date")
        expected_pdf = f"{base}/download/{quote(paper['release_tag'], safe='')}/{quote(paper['asset'], safe='')}"
        expected_release = f"{base}/tag/{quote(paper['release_tag'], safe='')}"
        if not paper["asset"].endswith(".pdf") or "/" in paper["asset"]:
            errors.append(f"{label}: expected a PDF asset filename")
        if paper["pdf_url"] != expected_pdf or paper["release_url"] != expected_release:
            errors.append(f"{label}: URLs do not match repository, release tag and asset")
        if "project_url" in paper and (not isinstance(paper["project_url"], str) or not paper["project_url"].startswith("https://")):
            errors.append(f"{label}: project_url must use HTTPS")

        notes = paper.get("notes", {})
        if not isinstance(notes, dict) or set(notes) != {"en", "zh-CN"}:
            errors.append(f"{label}: notes must specify en and zh-CN")
        else:
            for language, filename in notes.items():
                if not isinstance(filename, str):
                    errors.append(f"{label}: invalid {language} note path")
                    continue
                path = (root / filename).resolve()
                content = markdown.get(path, "")
                if not path.is_relative_to(root) or not content:
                    errors.append(f"{label}: missing local note {filename}")
                    continue
                for value in (paper["title"], paper["release_tag"], paper["citation_key"], paper["pdf_url"]):
                    if value not in content:
                        errors.append(f"{filename}: missing catalog value {value}")
                other = notes["zh-CN" if language == "en" else "en"]
                if isinstance(other, str) and f"]({Path(other).name})" not in content:
                    errors.append(f"{filename}: missing language-switch link")
                readme = "README.md" if language == "en" else "README.zh-CN.md"
                overview = markdown.get(root / readme, "")
                if f"]({filename})" not in overview or paper["pdf_url"] not in overview:
                    errors.append(f"{readme}: missing {label} note or PDF link")

        entry = citations.get(paper["citation_key"], "")
        if not entry:
            errors.append(f"{label}: citation missing from references.bib")
        else:
            normalized = entry.replace("{", "").replace("}", "")
            authors = paper.get("authors", [])
            if not isinstance(authors, list):
                authors = []
            for value in (paper["title"], paper["published"][:4], paper["release_url"], *authors):
                if isinstance(value, str) and value not in normalized:
                    errors.append(f"{label}: citation does not contain {value}")

        if remote:
            api = f"https://api.github.com/repos/{repository}/releases/tags/{quote(paper['release_tag'], safe='')}"
            headers = {"Accept": "application/vnd.github+json", "User-Agent": "methodology-validator"}
            token = os.environ.get("GITHUB_TOKEN")
            if token:
                headers["Authorization"] = f"Bearer {token}"
            try:
                with urlopen(Request(api, headers=headers), timeout=20) as response:
                    release = json.load(response)
                if release.get("draft") or not release.get("published_at"):
                    errors.append(f"{label}: release is not published")
                elif release["published_at"][:10] != paper["published"]:
                    errors.append(f"{label}: published date differs from release (UTC)")
                assets = release.get("assets", [])
                if not any(a["name"] == paper["asset"] and a["size"] > 0 for a in assets):
                    errors.append(f"{label}: PDF asset absent or empty")
            except (OSError, ValueError, KeyError) as exc:
                errors.append(f"{label}: remote release check failed: {exc}")

    for path, text in markdown.items():
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", markdown_body(text)):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            label = f"{path.relative_to(root)}: {target}"
            if not local.is_relative_to(root) or not local.is_file():
                errors.append(f"{label}: missing file or path outside repository")
            elif parsed.fragment and local.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(markdown.get(local, "")):
                    errors.append(f"{label}: missing Markdown anchor")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", action="store_true", help="also verify release metadata through GitHub API")
    args = parser.parse_args()
    errors = validate(Path(__file__).resolve().parents[1], args.remote)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: catalog, citations, bilingual navigation and local links" +
          ("; published releases and PDF assets" if args.remote else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
