"""Production settings; override SITEURL with the BLOG_SITEURL environment variable."""
import os
from pelicanconf import *  # noqa: F403

SITEURL = os.environ.get("BLOG_SITEURL", "https://integralsandseries.in").rstrip("/")
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
