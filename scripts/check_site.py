"""Check generated links, figures, and preservation of every Markdown math fragment.

Run after a build: python scripts/check_site.py
Only runtime requirements are needed. This checks the generated HTML before
MathJax runs; browser rendering should also be checked when changing math setup.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pelicanconf import MARKDOWN  # noqa: E402


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.math = []
        self.stack = []
        self.math_depth = None
        self.fragment = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in {"a", "link", "script", "img"}:
            url = attrs.get("href") or attrs.get("src")
            if url:
                self.links.append(url)
        if tag == "img" and not attrs.get("alt"):
            raise ValueError("Image missing descriptive alternative text")
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(tag)
            if "arithmatex" in attrs.get("class", "").split():
                self.math_depth = len(self.stack)
                self.fragment = []

    def handle_endtag(self, tag):
        if self.math_depth == len(self.stack):
            self.math.append("".join(self.fragment).strip())
            self.math_depth = None
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, value):
        if self.math_depth is not None:
            self.fragment.append(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output")
    parser.add_argument("--site-url", default="https://integralsandseries.in")
    args = parser.parse_args()
    output = args.output.resolve()
    origin = urlsplit(args.site_url)
    documents = {p.resolve(): Document(p.read_text(encoding="utf-8")) for p in output.rglob("*.html")}
    failures = []
    links = 0
    for path, doc in documents.items():
        page_url = "https://preview.invalid/" + path.relative_to(output).as_posix()
        for link in doc.links:
            url = urlsplit(link)
            if url.scheme in {"mailto", "tel", "data"}:
                continue
            if url.netloc and url.netloc != origin.netloc:
                continue
            if url.netloc == origin.netloc:
                if not url.path.startswith(origin.path.rstrip("/") + "/"):
                    failures.append(f"Unexpected same-site URL: {link}")
                    continue
                link = url.path[len(origin.path.rstrip('/')):] + ("#" + url.fragment if url.fragment else "")
            resolved = urlsplit(urljoin(page_url, link))
            target = (output / unquote(resolved.path).lstrip("/")).resolve()
            if target.is_dir():
                target /= "index.html"
            links += 1
            if not target.is_relative_to(output) or not target.exists():
                failures.append(f"{path.relative_to(output)}: missing target {link}")
            elif resolved.fragment and target in documents and unquote(resolved.fragment) not in documents[target].ids:
                failures.append(f"{path.relative_to(output)}: missing fragment {link}")
    manifest = json.loads((ROOT / "migration-manifest.json").read_text(encoding="utf-8"))
    equation_count = 0
    for post in manifest["posts"]:
        text = (ROOT / "content" / post["file"]).read_text(encoding="utf-8")
        source = Document(markdown.markdown(text, extensions=list(MARKDOWN["extension_configs"]), extension_configs=MARKDOWN["extension_configs"]))
        target = (output / post["url"] / "index.html").resolve()
        if target not in documents:
            failures.append(f"Missing migrated article {post['url']}")
            continue
        if not source.math or Counter(source.math) != Counter(documents[target].math):
            failures.append(f"Math changed or disappeared in {post['file']}")
        equation_count += len(source.math)
        if "wp-content/uploads" in target.read_text(encoding="utf-8"):
            failures.append(f"WordPress image dependency in {post['file']}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {len(documents)} HTML pages, {links} local links/assets, {len(manifest['posts'])} migrated posts, {equation_count} intact math fragments.")


if __name__ == "__main__":
    main()
