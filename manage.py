"""Small, cross-platform command runner for this Pelican blog."""
import argparse
from datetime import datetime
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from zoneinfo import ZoneInfo

from pelicanconf import TIMEZONE

ROOT = Path(__file__).resolve().parent


def preferred_python() -> str:
    """Use the current interpreter if it has Pelican + Arithmatex installed, else fall back to .venv."""
    if importlib.util.find_spec("pelican") and importlib.util.find_spec("pymdownx"):
        return sys.executable
    for candidate in (ROOT / ".venv" / "Scripts" / "python.exe", ROOT / ".venv" / "bin" / "python"):
        if candidate.exists():
            return str(candidate)
    return sys.executable


def build_figures():
    figures_dir = ROOT / "figures"
    images_dir = ROOT / "content" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    latex = shutil.which("latex") or r"C:\texlive\2025\bin\windows\latex.exe"
    dvisvgm = shutil.which("dvisvgm") or r"C:\texlive\2025\bin\windows\dvisvgm.exe"
    for tex_file in sorted(figures_dir.glob("*.tex")):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(
                [latex, "-interaction=nonstopmode", f"-output-directory={tmp}", str(tex_file)],
                cwd=ROOT, check=True,
            )
            dvi_file = Path(tmp) / f"{tex_file.stem}.dvi"
            svg_file = images_dir / f"{tex_file.stem}.svg"
            subprocess.run(
                [dvisvgm, "--no-fonts", "--exact-bbox", "-o", str(svg_file), str(dvi_file)],
                cwd=ROOT, check=True,
            )
            print(f"Compiled {tex_file.relative_to(ROOT)} -> {svg_file.relative_to(ROOT)}")


def build(publish=False):
    # OneDrive may mark directories read-only. Clear files rather than trying
    # to remove those directories; empty folders do not retain stale articles.
    output = ROOT / "output"
    if output.resolve() != ROOT.resolve() / "output":
        raise RuntimeError("Refusing to clear an output directory outside this project")
    if output.exists():
        for path in output.rglob("*"):
            if not path.resolve().is_relative_to(output.resolve()):
                raise RuntimeError(f"Output contains a link outside the output directory: {path}")
            if path.is_file():
                path.unlink()
    subprocess.run(
        [preferred_python(), "-m", "pelican", "content", "-s",
         "publishconf.py" if publish else "pelicanconf.py", "--fatal", "warnings"],
        cwd=ROOT, check=True,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build", help="Generate output/ for local preview")
    commands.add_parser("publish", help="Generate output/ with production URLs and feeds")
    commands.add_parser("figures", help="Compile TikZ figures/*.tex into content/images/*.svg")
    serve = commands.add_parser("serve", help="Build and serve at http://localhost:8000")
    serve.add_argument("--port", type=int, default=8000)
    commands.add_parser("watch", help="Regenerate output/ when content or templates change")
    new = commands.add_parser("new", help="Create a draft post (or --page)")
    new.add_argument("title")
    new.add_argument("--slug", help="URL slug; defaults to a slug made from the title")
    new.add_argument("--page", action="store_true")
    args = parser.parse_args()
    if args.command in {"build", "publish"}:
        build(args.command == "publish")
    elif args.command == "figures":
        build_figures()
    elif args.command == "serve":
        build()
        handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT / "output"))
        print(f"Preview: http://localhost:{args.port} (Ctrl+C to stop)", flush=True)
        try:
            with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
                server.serve_forever()
        except KeyboardInterrupt:
            pass
    elif args.command == "watch":
        build()
        subprocess.run([preferred_python(), "-m", "pelican", "content", "-s", "pelicanconf.py", "--autoreload"], cwd=ROOT, check=True)
    elif args.command == "new":
        slug = args.slug or re.sub(r"[^a-z0-9]+", "-", args.title.lower()).strip("-")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or any(c in args.title for c in "\n\r"):
            parser.error("Use a single-line title and a slug containing lowercase letters, digits, and hyphens.")
        folder = ROOT / "content" / ("pages" if args.page else "posts")
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{slug}.md"
        with path.open("x", encoding="utf-8") as f:
            f.write(f"Title: {args.title}\nDate: {datetime.now(ZoneInfo(TIMEZONE)):%Y-%m-%d %H:%M %z}\nSlug: {slug}\nStatus: draft\n")
            if not args.page:
                f.write("Category: Mathematics\nTags: \nSummary: Write a short plain-text introduction here.\n")
            f.write("\nWrite your introduction here.\n\n## The idea\n\n$$\n\\int_0^1 x^2\\,dx = \\frac{1}{3}.\n$$\n")
        print(f"Created {path.relative_to(ROOT)}. Change Status to published when ready.")


if __name__ == "__main__":
    main()
