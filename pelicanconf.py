"""Development settings. Run commands from the project directory."""
AUTHOR = "Shobhit Bhatnagar"
SITENAME = "Integrals and Series"
SITESUBTITLE = "Notes on integrals, infinite series, and number theory"
SITEURL = ""
PATH = "content"
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"
THEME = "theme"
RELATIVE_URLS = True
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 45

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
AUTHOR_SAVE_AS = ""  # A single-author blog doesn't need duplicate author archives.
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = "archives.html"
DIRECT_TEMPLATES = ["index", "archives", "categories", "tags"]
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {"extra/legacy-posts.json": {"path": "legacy-posts.json"}}
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = False  # manage.py clears generated files; works with OneDrive folders.
TYPOGRIFY = False  # Never let typographic substitutions touch TeX.

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.meta": {},
        "markdown.extensions.extra": {},
        "pymdownx.arithmatex": {"generic": True, "smart_dollar": False},
    },
    "output_format": "html5",
}
