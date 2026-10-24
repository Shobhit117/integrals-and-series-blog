"""Import this WXR export without letting HTML/Markdown parsers modify LaTeX.

Install requirements-migration.txt first. Existing Markdown is never overwritten.
Use --destination content-reimport to review a fresh import alongside edited posts.
"""
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import parse_qs, unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[1]
NS = {"wp": "http://wordpress.org/export/1.2/", "content": "http://purl.org/rss/1.0/modules/content/"}
MATH = re.compile(r"(?<!\\)\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$(?!\$)", re.S)
FIGURES = {
    "contour.png": ("contour.webp", "Quarter-circle contour in the first quadrant, with indentations at 1 and i"),
    "contour1.png": ("contour1.webp", "Indented contour used for the second logarithmic integral"),
    "contour11.png": ("contour11.webp", "Upper-half-plane contour for the reciprocal beta integral"),
}
SUMMARIES = {
    1: "Two incomplete beta integrals, evaluated through substitutions and the addition formulas for the Weierstrass elliptic function.",
    21: "Eisenstein's trigonometric proof of quadratic reciprocity, starting with Euler's criterion and Gauss's lemma.",
    37: "Weyl's criterion connects uniform distribution modulo one with exponential sums and averages of Riemann-integrable functions.",
    94: "From the defining recursion for Bernoulli polynomials to their Fourier expansions and an associated integral.",
    210: "Derive Kummer's Fourier series for the logarithm of the gamma function, then use it to evaluate Vardi's integral.",
    286: "Use Ramanujan's master theorem to connect power-series coefficients with Mellin transforms of Bessel functions.",
    349: "An alternating Euler sum leads to harmonic-number generating functions, logarithmic integrals, and polylogarithms.",
    398: "A contour-integral approach to an infinite trigonometric series, with an application of equidistribution.",
    444: "Generating functions for squared harmonic numbers provide evaluations of Euler sums and logarithmic integrals.",
    476: "The first part of a series on logarithmic integrals: harmonic-number sums, polylogarithms, and residues.",
    532: "The second part develops further logarithmic integral evaluations through polylogarithmic identities.",
    679: "The third part uses complex contours to evaluate logarithmic integrals involving inverse trigonometric functions.",
    793: "A proof of the classification of integers whose multiplicative group of units is cyclic.",
    855: "Begin with Jacobi's theta series and derive their periodicity, zeros, and fundamental identities.",
    961: "Continue the study of theta functions with infinite products and connections to elliptic integrals.",
    1028: "A contour argument gives integral representations involving the reciprocal beta function and their logarithmic consequences.",
    1189: "A sequence of substitutions and a hypergeometric transformation proves integral 3.255 from Gradshteyn and Ryzhik.",
}


def field(item, key, default=""):
    return item.findtext(key, default=default, namespaces=NS) or default


def convert(body, posts):
    # Exclude WordPress block markers and deliberately unpublished HTML comments
    # before collecting equations (one source post includes a commented draft).
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    equations = []

    def protect(match):
        display = match.group(1) is not None
        tex = html.unescape(match.group(1) if display else match.group(2)).strip()
        # Bernoulli's opening system was single-dollar math inside <center>.
        display = display or ("\\begin{aligned}" in tex and "\n" in tex)
        token = f"MATHTOKEN{len(equations):05d}END"
        equations.append((token, display, tex))
        return ("\n\n" + token + "\n\n") if display else token

    protected = MATH.sub(protect, body)
    soup = BeautifulSoup(protected, "html.parser")
    for comment in soup.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()
    for center in soup.find_all("center"):
        center.unwrap()
    for paragraph in soup.find_all("p"):
        children = [c for c in paragraph.contents if str(c).strip()]
        if len(children) == 1 and getattr(children[0], "name", None) in {"b", "strong"}:
            paragraph.name = "h2"
            children[0].unwrap()
    for image in soup.find_all("img"):
        name = Path(unquote(urlsplit(image["src"]).path)).name
        if name not in FIGURES:
            raise ValueError(f"Unmapped image: {image['src']}")
        filename, alt = FIGURES[name]
        image.attrs = {"src": "{static}/images/" + filename, "alt": alt}
    for anchor in soup.find_all("a", href=True):
        url = urlsplit(anchor["href"])
        if url.netloc in {"integralsandseries.in", "www.integralsandseries.in"}:
            post_id = parse_qs(url.query).get("p", [None])[0]
            target = posts.get(post_id)
            if target:
                anchor["href"] = "{filename}/posts/" + target + ".md" + ("#" + url.fragment if url.fragment else "")
    text = markdownify(str(soup), heading_style="ATX", bullets="-", escape_underscores=False, escape_asterisks=False, escape_misc=False, wrap=False)
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    for token, display, tex in equations:
        if text.count(token) != 1:
            raise ValueError(f"Lost or duplicated equation: {token}")
        if display:
            tex = re.sub(r"\n\s*\n", "\n", tex)
            # Python-Markdown requires four spaces for a block within a list.
            line = re.search(r"(?m)^([ \t]*)" + token + r"[ \t]*$", text)
            indent = "    " if line and line.group(1) else ""
            replacement = "\n\n" + indent + "$$\n" + "\n".join(indent + row for row in tex.splitlines()) + "\n" + indent + "$$\n\n"
            if line:
                text = text[:line.start()] + replacement + text[line.end():]
                continue
        else:
            replacement = "$" + re.sub(r"\s*\n\s*", " ", tex) + "$"
        text = text.replace(token, replacement)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text, equations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default=str(ROOT / "integralsandseries.WordPress.2026-10-24.xml"))
    parser.add_argument("--destination", type=Path, default=ROOT / "content")
    args = parser.parse_args()
    destination = args.destination.resolve()
    items = ET.parse(args.source).findall("./channel/item")
    articles = [i for i in items if field(i, "wp:post_type") == "post" and field(i, "wp:status") == "publish"]
    posts = {field(i, "wp:post_id"): unquote(field(i, "wp:post_name")) for i in articles}
    for slug in posts.values():
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            parser.error(f"Unsafe slug: {slug}")
        if (destination / "posts" / f"{slug}.md").exists():
            parser.error("Destination already contains posts. Use --destination content-reimport; existing edits will not be overwritten.")
    (destination / "posts").mkdir(parents=True, exist_ok=True)
    (destination / "images").mkdir(exist_ok=True)
    (destination / "extra").mkdir(exist_ok=True)
    for filename, _ in FIGURES.values():
        shutil.copy2(ROOT / filename, destination / "images" / filename)
    legacy = {}
    manifest = []
    # Convert everything first, so a conversion failure cannot leave half an import.
    converted = {field(i, "wp:post_id"): convert(field(i, "content:encoded"), posts) for i in articles}
    for item in articles:
        post_id = field(item, "wp:post_id")
        slug = posts[post_id]
        text, equations = converted[post_id]
        categories = [c.text for c in item.findall("category") if c.get("domain") == "category"]
        tags = [c.text for c in item.findall("category") if c.get("domain") == "post_tag"]
        # Pelican has one primary category. Retain additional WP categories as tags.
        tags = list(dict.fromkeys(tags + categories[1:]))
        date = field(item, "wp:post_date_gmt", field(item, "wp:post_date"))
        modified = field(item, "wp:post_modified_gmt", date)
        metadata = {"Title": field(item, "title"), "Date": date + " +0000", "Modified": modified + " +0000", "Slug": slug, "Author": "Shobhit Bhatnagar", "Category": categories[0] if categories else "Mathematics", "Tags": ", ".join(tags), "Summary": SUMMARIES[int(post_id)], "Status": "published", "WordPress_ID": post_id}
        (destination / "posts" / f"{slug}.md").write_text("\n".join(f"{k}: {v}" for k, v in metadata.items()) + "\n\n" + text, encoding="utf-8")
        url = date[:10].replace("-", "/") + "/" + slug + "/"
        legacy[post_id] = url
        manifest.append({"id": int(post_id), "title": metadata["Title"], "file": f"posts/{slug}.md", "url": url, "source_math_count": len(equations), "source_math_sha256": hashlib.sha256("\n".join(tex for _, _, tex in equations).encode()).hexdigest(), "categories": categories})
    (destination / "extra" / "legacy-posts.json").write_text(json.dumps(legacy, indent=2) + "\n", encoding="utf-8")
    report = {"source": Path(args.source).name, "counts": dict(Counter(field(i, "wp:post_type") + ":" + field(i, "wp:status") for i in items)), "comments_preserved_in_xml": sum(len(i.findall("wp:comment", NS)) for i in items), "posts": manifest}
    (destination.parent / ("migration-manifest.json" if destination.name == "content" else destination.name + "-manifest.json")).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Imported {len(articles)} posts and {len(FIGURES)} figures into {destination}")


if __name__ == "__main__":
    main()
