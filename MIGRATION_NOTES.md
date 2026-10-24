# WordPress → Pelican migration

Source: `integralsandseries.WordPress.2026-10-24.xml`. The source XML and all three supplied WebP files remain intact.

## What was migrated

- All **17 published articles**, from January 2020 through November 2025, now live in `content/posts/` as Markdown.
- Original titles, slugs, author, publication timestamps, modification timestamps, categories, and tags were imported. Two titles received grammatical/capitalization edits; their slugs remain unchanged.
- The export's local and GMT timestamps agree. Imported metadata includes `+0000` to preserve those instants explicitly; new articles use the configured India timezone.
- Pelican accepts one primary category. Additional categories were kept as tags. Uncategorized entries remain available for later categorization.
- All post-to-post WordPress query links were converted to Pelican source-file links.
- Published HTML comments and WordPress editor wrappers were stripped. A deliberately commented-out derivation in Theta Functions I stays unpublished in the original XML.
- Five attachment records were present, but only three images were referenced in published article bodies. Those three were all supplied locally. No missing article figures were detected.
- Two WordPress comments remain in the XML. They are not published or sent to a comment service. There were no exported standalone pages or drafts. The About page was added for this site.

The original-wording import contains **798 math fragments**. The edited articles contain **827**, including the explanatory notation added in the revisions below. The importer protects TeX before HTML parsing, decodes HTML entities once, and verifies that each protected equation is restored. Source counts and hashes are recorded in `migration-manifest.json`; these describe the original export, not the subsequently edited articles.

## Figure matches

| Original image in the export | Local asset | Article |
| --- | --- | --- |
| `2020/09/contour.png` (attachment 682) | `content/images/contour.webp` | Logarithmic integrals, part III, integral 5 |
| `2020/09/contour1.png` (attachment 757) | `content/images/contour1.webp` | Logarithmic integrals, part III, integral 6 |
| `2023/11/contour11.png` (attachment 1043) | `content/images/contour11.webp` | Reciprocal beta function |

The mappings come from the image URLs and attachment IDs in the export. The figures were also visually inspected, and descriptive alternative text was added. In part III, the straight segment down the imaginary axis is now correctly labeled `gamma_5`, matching the first diagram.

## Exposition and mathematical edits

Introductions now explain the goal and route of the argument. Section headings, summaries, whitespace, grammar, and cross-links were cleaned up throughout. Original references and the author's mathematical voice were retained. General prose replacements deliberately excluded TeX.

Specific changes worth reviewing:

1. **Quadratic reciprocity:** clarified the zero case of the Legendre symbol. After division by the leading coefficient, the coefficients of the monic sine polynomial are described as rational, rather than necessarily integral. The even-polynomial argument now says that the coefficients of **odd powers** vanish; the original wording incorrectly appeared to eliminate every intermediate coefficient.
2. **Weyl's criterion:** restored the missing `1/N` in the displayed average of a linear combination. Reworked `(2) ⇒ (3)` to approximate **continuous periodic** functions first and then sandwich interval indicators. The original claim of uniform trigonometric approximation for every continuous function on `[0,1]` needed the endpoint-periodicity condition. The revised argument also explains why endpoint visits have density zero. The numbered statements retain their numbering around display equations.
3. **Ramanujan's master theorem:** replaced the unrestricted theorem claim with an explicitly qualified master-theorem principle. Added an explanation of why analytic continuation, growth conditions, and a convergence strip matter. The Bessel calculations remain, with a link to [González, Moll, and Schmidt's discussion](https://www.math.tulane.edu/~vhm/papers_html/ram-feynman.pdf). This article presents the method, rather than a full theorem with verified hypotheses for every application.
4. **Unit groups modulo n:** corrected the totient definition's modulus from `p` to `n` and the divisibility condition to `p` not dividing `s`. Added the missing necessity argument using multiple square roots of unity and the Chinese remainder theorem.
5. **Theta functions:** stated the consistent nome convention `q = exp(i*pi*tau)`, with positive imaginary part of `tau`. Corrected the zeros in part II to `(2n+1)*pi*tau/2 + m*pi`; the source had extra factors of `i`.
6. **GR 3.255:** retained the target evaluation, added the real-parameter condition `c > 0`, and replaced the derivation. The original Möbius argument asserted the existence of a positive root without adequate conditions, used an inconsistent transformed endpoint, and contained errors in the Pfaff argument and gamma duplication factor. The new proof uses `t=(1-x)/x`, an inversion symmetry, and a beta integral. It works under the displayed positivity and convergence assumptions without choosing a quadratic root. Five real-parameter cases and one complex-`mu` case were checked by high-precision numerical quadrature; the relative discrepancies were below `1e-18`.

These are targeted corrections and exposition improvements, not a complete independent verification of every identity, convergence claim, or branch choice in all 17 articles. The untouched XML provides the original text for comparison. Reimporting does **not** replay the editorial revisions.

## URLs and hosting

Articles use `/YYYY/MM/DD/slug/`. The unusual `hello-world` slug of the first article is preserved intentionally. The export identifies article links as `/?p=ID`; the generated homepage resolves these old query links using `legacy-posts.json` and a small script. This preserves visits when JavaScript is enabled but is not a server-side 301 redirect. Configure host-level redirects if you need HTTP redirects; the JSON file supplies the exact ID-to-path mapping. Other historical URL patterns were not included in the export and were not guessed.

`manage.py publish` builds production files with the existing domain by default, and supports `BLOG_SITEURL` for another domain or path prefix. It does not upload files, alter DNS, or replace the WordPress installation. Upload only the contents of `output/`. Production Atom feeds are generated locally. MathJax 3.2.2 is pinned and loaded from jsDelivr; the article text, theme, and figures are local files.

## Validation

- Development and production builds run with warnings treated as failures.
- `scripts/check_site.py` validates local links, assets, migrated article presence, and exact preservation of every current math fragment through Markdown-to-HTML generation.
- Browser checks covered MathJax rendering in all 17 articles: **827 fragments rendered, with no MathJax errors**. All three article images loaded.
- All 17 articles were checked on desktop and at a 390px viewport with no document-level horizontal overflow. Wide displays scroll within their containers; three long inline formulas also receive contained scrolling when they exceed the available width.
- The importer was checked independently against all **798** original published math fragments, allowing only whitespace normalization.
- Both the development and production site builds passed link validation. The production build includes Atom feeds.
- A production build under a `/my-blog` path prefix also passed. New draft posts and standalone pages were exercised, including draft exclusion from the index and stale-file removal on the next full build.
- An old `/?p=679` link was opened in the browser and resolved to the migrated article.

The helper clears generated files before each build to prevent stale articles from surviving. It leaves empty directories in place because this OneDrive workspace rejects Python's ordinary recursive directory removal for some folders. Source content is never cleared. The watcher is convenient for editing; always run a full `publish` before deploying.
