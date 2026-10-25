# Integrals and Series

A database-free Pelican blog by Shobhit Bhatnagar, with Markdown articles, MathJax, local figures, and a wide custom theme.

## Preview on this computer

The `.venv` environment is already prepared. In PowerShell, from this folder:

```powershell
.\.venv\Scripts\python.exe manage.py serve
```

Open [the local preview](http://localhost:8000). Stop it with Ctrl+C.

```powershell
.\.venv\Scripts\python.exe manage.py new "My next integral"
.\.venv\Scripts\python.exe manage.py new "Reading list" --page
.\.venv\Scripts\python.exe manage.py build
.\.venv\Scripts\python.exe scripts/check_site.py
.\.venv\Scripts\python.exe manage.py publish
```

New content starts as a draft. Edit its Markdown file and change `Status: draft` to `Status: published` when ready. `publish` generates the files in `output/`; it does not upload them. Build commands regenerate `output/`, so edit `content/` and `theme/` rather than generated files.

## A fresh installation

Use Python 3.11 or newer:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py serve
```

On macOS/Linux use `python3 -m venv .venv` and `.venv/bin/python` for the remaining commands. On this Windows machine, the system `python` alias is not working, so the explicit environment executable is the reliable choice.

## Project map

- `content/posts/`: the 17 imported, edited posts; edit these directly.
- `content/pages/`: standalone pages such as About.
- `content/images/`: the three matched contour figures.
- `pelicanconf.py` / `publishconf.py`: preview / production settings.
- `theme/`: templates, CSS, and MathJax setup.
- `manage.py`: build, preview, watch, and new-content commands.
- `MIGRATION_NOTES.md`: import decisions, corrections, and review scope.
- `migration-manifest.json`: original post IDs, dates/paths, and source equation counts/hashes.
- `pelican-tutorial.md`: your detailed private guide, excluded by `.gitignore`.

For a different production address, set `$env:BLOG_SITEURL = "https://example.com"` before running `manage.py publish`. Upload only the **contents of `output/`** to a static host. MathJax 3.2.2 loads from jsDelivr, so typesetting needs internet access; all articles and figures are local static files.

The importer is retained for recovery, not daily writing:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-migration.txt
.\.venv\Scripts\python.exe scripts/import_wordpress.py --destination content-reimport
```

It refuses to overwrite posts. A fresh import preserves the original wording; it does not replay the subsequent editorial work. The original WordPress XML stays untouched and is excluded from Git because it includes private export metadata and comments.

References: [Pelican settings](https://docs.getpelican.com/en/stable/settings.html), [Pelican writing guide](https://docs.getpelican.com/en/stable/content.html), [Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/).
