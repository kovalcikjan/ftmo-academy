"""Step 4: Markdown → HTML converter using v2_balanced FTMO template."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import markdown
from bs4 import BeautifulSoup, Tag

# ---------------------------------------------------------------------------
# CSS — v2_balanced template (FTMO brand colors)
# ---------------------------------------------------------------------------

CSS = """
:root {
    --ftmo-blue: #0781fe;
    --ftmo-dark: #123a83;
    --ftmo-navy: #0a1628;
    --ftmo-silver: #c6c6c6;
    --ftmo-gray: #6b7280;
    --ftmo-light: #f8f9fa;
    --ftmo-border: #e1e5eb;
    --max-width: 1160px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 16px; line-height: 1.7; color: #1f2937; background: #fff;
}
.header {
    background: #000; padding: 1rem 2rem; position: sticky; top: 0; z-index: 100;
}
.header-inner {
    max-width: 1200px; margin: 0 auto;
    display: flex; justify-content: space-between; align-items: center;
}
.logo { color: #fff; font-size: 1.25rem; font-weight: 700; text-decoration: none; }
.nav { display: flex; gap: 2rem; }
.nav a { color: #ccc; text-decoration: none; font-size: 0.875rem; font-weight: 500; }
.nav a:hover { color: #fff; }
.header-cta {
    background: var(--ftmo-blue); color: #fff; padding: 0.5rem 1rem;
    border-radius: 4px; text-decoration: none; font-size: 0.875rem; font-weight: 600;
}
.breadcrumb {
    background: var(--ftmo-light); padding: 0.75rem 2rem;
    font-size: 0.875rem; border-bottom: 1px solid var(--ftmo-border);
}
.breadcrumb-inner { max-width: var(--max-width); margin: 0 auto; }
.breadcrumb a { color: var(--ftmo-gray); text-decoration: none; }
.breadcrumb span { color: var(--ftmo-gray); margin: 0 0.5rem; }
.main { max-width: var(--max-width); margin: 0 auto; padding: 2rem; }
h1 { font-size: 2.25rem; font-weight: 700; line-height: 1.2; margin-bottom: 1.5rem; }
h2 {
    font-size: 1.5rem; font-weight: 600; margin: 2.5rem 0 1rem;
    padding-top: 1rem; border-top: 1px solid var(--ftmo-border);
}
h3 { font-size: 1.25rem; font-weight: 600; margin: 1.5rem 0 0.75rem; }
h4 { font-size: 1rem; font-weight: 600; margin: 1.25rem 0 0.5rem; }
p { margin-bottom: 1rem; color: var(--ftmo-gray); }
.intro-text { font-size: 1.125rem; color: #1f2937; line-height: 1.8; }
strong { color: #1f2937; }
a { color: var(--ftmo-blue); }
ul, ol { margin: 1rem 0 1rem 1.5rem; color: var(--ftmo-gray); }
li { margin-bottom: 0.5rem; }
table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9375rem; }
th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--ftmo-border); }
th { background: var(--ftmo-light); font-weight: 600; color: var(--ftmo-dark); }
td { color: var(--ftmo-gray); }
.toc {
    background: var(--ftmo-light); padding: 1.5rem; border-radius: 8px; margin: 2rem 0;
}
.toc-title { font-size: 0.875rem; font-weight: 600; color: var(--ftmo-gray);
    text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
.toc ul { list-style: none; margin: 0; padding: 0; }
.toc li { margin-bottom: 0.4rem; }
.toc a {
    color: var(--ftmo-dark); text-decoration: none; font-size: 0.9375rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.toc a::before {
    content: ""; display: inline-block; width: 6px; height: 6px;
    background: var(--ftmo-blue); border-radius: 50%; flex-shrink: 0;
}
.toc a:hover { color: var(--ftmo-blue); }
.toc .toc-h3 { padding-left: 1.25rem; font-size: 0.875rem; }
.callout {
    padding: 1rem 1.25rem; margin: 1.5rem 0;
    border-radius: 0 4px 4px 0; font-size: 0.9375rem;
}
.callout-tip    { background: #e8f4fd; border-left: 4px solid var(--ftmo-blue); }
.callout-warning { background: #fff3cd; border-left: 4px solid #ffc107; }
.callout-important { background: #fde8e8; border-left: 4px solid #e53e3e; }
.callout-note   { background: var(--ftmo-light); border-left: 4px solid var(--ftmo-gray); }
.callout-keep-in-mind { background: #f0f7ee; border-left: 4px solid #5a8a4a; }
.callout-example { background: #f5f5f5; border-left: 4px solid #999; }
.callout strong { display: block; margin-bottom: 0.25rem; }
figure.lesson-image { margin: 1.5rem 0; }
figure.lesson-image img {
    width: 100%; height: auto; border-radius: 8px;
    border: 1px solid var(--ftmo-border); display: block;
}
figure.lesson-image figcaption {
    margin-top: 0.5rem; font-size: 0.875rem;
    color: var(--ftmo-gray); text-align: center; font-style: italic;
}
.video-container {
    position: relative; padding-bottom: 56.25%; height: 0;
    overflow: hidden; margin: 2rem 0; border-radius: 8px; background: #000;
}
.video-container iframe {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;
}
.takeaways {
    background: linear-gradient(135deg, var(--ftmo-navy) 0%, var(--ftmo-dark) 100%);
    color: #fff; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;
}
.takeaways h2 { color: #fff; border: none; margin-top: 0; padding-top: 0; }
.takeaways ul { color: #ccc; }
.author-box {
    background: var(--ftmo-light); border-radius: 12px; padding: 1.5rem; margin: 2rem 0;
}
.author-box-header {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid var(--ftmo-border);
}
.author-box-title { font-weight: 600; font-size: 1rem; }
.author-dates { font-size: 0.8125rem; color: var(--ftmo-gray); display: flex; gap: 1.5rem; }
.author-card { display: flex; align-items: center; gap: 0.875rem; }
.author-avatar {
    width: 48px; height: 48px; border-radius: 50%; background: var(--ftmo-dark);
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-weight: 600; font-size: 1rem; flex-shrink: 0;
}
.author-role {
    font-size: 0.6875rem; text-transform: uppercase; letter-spacing: 0.05em;
    color: var(--ftmo-blue); font-weight: 600; margin-bottom: 0.125rem;
}
.author-name { font-weight: 600; color: var(--ftmo-dark); font-size: 0.9375rem; }
.disclaimer {
    background: var(--ftmo-light); padding: 1rem 1.25rem; border-radius: 4px;
    font-size: 0.875rem; color: var(--ftmo-gray); margin: 1rem 0;
}
.risk-warning {
    background: #fff3cd; border-left: 4px solid #ffc107;
    padding: 1rem 1.25rem; font-size: 0.875rem; border-radius: 0 4px 4px 0; margin: 1rem 0;
}
.risk-warning strong { color: #856404; }
.footer { background: #000; color: #fff; padding: 3rem 2rem; margin-top: 4rem; }
.footer-inner {
    max-width: 1200px; margin: 0 auto;
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;
}
.footer-logo { font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 1rem; }
.footer-desc { color: #888; font-size: 0.875rem; line-height: 1.6; }
.footer h4 {
    font-size: 0.875rem; text-transform: uppercase;
    letter-spacing: 0.05em; margin-bottom: 1rem; color: #888;
}
.footer ul { list-style: none; margin: 0; padding: 0; }
.footer li { margin-bottom: 0.5rem; }
.footer a { color: #ccc; text-decoration: none; font-size: 0.9375rem; }
.footer a:hover { color: #fff; }
"""

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

CALLOUT_MAP = {
    "tip": "callout-tip",
    "warning": "callout-warning",
    "important": "callout-important",
    "note": "callout-note",
    "keep in mind": "callout-keep-in-mind",
    "example": "callout-example",
}


def _slugify(text: str) -> str:
    """Convert heading text to URL-safe anchor ID."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text)


def _strip_log(markdown_text: str) -> str:
    """Remove Step 3 log section from markdown (everything after the log separator)."""
    # Split on the log marker — keep only article content
    marker = "\n---\n\n## Step 3 Log:"
    if marker in markdown_text:
        return markdown_text.split(marker)[0].strip()
    # Fallback: split on horizontal rule before log
    parts = re.split(r"\n---\n+## Step \d+ Log:", markdown_text)
    return parts[0].strip()


def _extract_headings(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Extract H2/H3 headings for ToC generation."""
    headings = []
    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)
        slug = _slugify(text)
        tag["id"] = slug
        headings.append({"level": tag.name, "text": text, "id": slug})
    return headings


def _build_toc(headings: list[dict[str, str]]) -> str:
    """Build HTML Table of Contents from heading list."""
    if not headings:
        return ""
    items = []
    for h in headings:
        css = "toc-h3" if h["level"] == "h3" else ""
        items.append(
            f'<li class="{css}"><a href="#{h["id"]}">{h["text"]}</a></li>'
        )
    return (
        '<div class="toc">'
        '<p class="toc-title">Table of Contents</p>'
        f'<ul>{"".join(items)}</ul>'
        "</div>"
    )


def _process_callouts(soup: BeautifulSoup) -> None:
    """Convert blockquotes with **Label:** markers to styled callout divs."""
    for bq in soup.find_all("blockquote"):
        text = bq.get_text(strip=True)
        callout_class = None
        for label, cls in CALLOUT_MAP.items():
            if text.lower().startswith(label + ":") or text.lower().startswith(f"**{label}:**"):
                callout_class = cls
                break
        if callout_class:
            div = soup.new_tag("div", attrs={"class": f"callout {callout_class}"})
            div.extend(bq.contents)
            bq.replace_with(div)


def _process_images(soup: BeautifulSoup) -> None:
    """Wrap bare <img> tags in <figure class="lesson-image">."""
    for img in list(soup.find_all("img")):
        # Skip if already inside a figure
        if img.parent and img.parent.name == "figure":
            continue
        alt = img.get("alt", "")
        figure = soup.new_tag("figure", attrs={"class": "lesson-image"})
        # Replace img in-place with figure, then move img inside figure
        img.replace_with(figure)
        figure.append(img)
        if alt:
            cap = soup.new_tag("figcaption")
            cap.string = alt
            figure.append(cap)
        # If parent paragraph is now empty (only contained the image), unwrap it
        parent = figure.parent
        if parent and parent.name == "p" and not parent.get_text(strip=True):
            parent.replace_with(figure)


def _add_intro_class(soup: BeautifulSoup) -> None:
    """Add intro-text class to first paragraph after H1."""
    h1 = soup.find("h1")
    if h1:
        first_p = h1.find_next_sibling("p")
        if first_p:
            first_p["class"] = first_p.get("class", []) + ["intro-text"]


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

def _html_template(
    title: str,
    slug: str,
    body_html: str,
    toc_html: str,
    today: str,
) -> str:
    """Wrap article content in full v2_balanced HTML page."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | FTMO Academy</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>{CSS}</style>
</head>
<body>

<header class="header">
    <div class="header-inner">
        <a class="logo" href="https://academy.ftmo.com">FTMO Academy</a>
        <nav class="nav">
            <a href="https://academy.ftmo.com">Lessons</a>
            <a href="https://ftmo.com">FTMO.com</a>
        </nav>
        <a class="header-cta" href="https://trader.ftmo.com/#sign-up">Start Challenge</a>
    </div>
</header>

<div class="breadcrumb">
    <div class="breadcrumb-inner">
        <a href="https://academy.ftmo.com">Academy</a>
        <span>›</span>
        <a href="https://academy.ftmo.com/lesson/{slug}/">{title}</a>
    </div>
</div>

<main class="main">

{toc_html}

{body_html}

<div class="author-box">
    <div class="author-box-header">
        <span class="author-box-title">About this lesson</span>
        <div class="author-dates">
            <span>Updated: {today}</span>
        </div>
    </div>
    <div class="author-card">
        <div class="author-avatar">FA</div>
        <div>
            <div class="author-role">Content Lead</div>
            <div class="author-name">FTMO Academy</div>
        </div>
    </div>
</div>

<div class="disclaimer">
    <strong>Educational Content Notice:</strong> This material is for educational purposes only
    and does not constitute financial advice. Trading decisions should be based on your own
    analysis and risk tolerance.
</div>

<div class="risk-warning">
    <strong>Risk Warning:</strong> Trading involves significant risk of loss.
    Past performance is not indicative of future results.
    Only trade with capital you can afford to lose.
</div>

</main>

<footer class="footer">
    <div class="footer-inner">
        <div>
            <div class="footer-logo">FTMO Academy</div>
            <p class="footer-desc">Professional trading education for aspiring funded traders.</p>
        </div>
        <div>
            <h4>Academy</h4>
            <ul>
                <li><a href="https://academy.ftmo.com">All Lessons</a></li>
                <li><a href="https://ftmo.com">FTMO Challenge</a></li>
            </ul>
        </div>
    </div>
</footer>

</body>
</html>"""


# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def convert_to_html(markdown_text: str, slug: str, output_path: Path) -> Path:
    """
    Convert Step 3 markdown to styled HTML using v2_balanced template.

    Strips the Step 3 log, converts markdown to HTML, applies FTMO branding,
    generates ToC, and saves the result.

    Args:
        markdown_text: Full content of step3_structure.md (including log).
        slug: URL slug used for breadcrumb and filename.
        output_path: Directory where the HTML file will be saved.

    Returns:
        Path to the generated HTML file.
    """
    article_md = _strip_log(markdown_text)

    # Extract title from H1
    title_match = re.search(r"^#\s+(.+)$", article_md, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else slug.replace("-", " ").title()

    # Convert markdown → HTML
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "nl2br"],
        output_format="html",
    )
    raw_html = md.convert(article_md)

    # Post-process with BeautifulSoup
    soup = BeautifulSoup(raw_html, "html.parser")
    _add_intro_class(soup)
    headings = _extract_headings(soup)
    _process_callouts(soup)
    _process_images(soup)

    body_html = str(soup)
    toc_html = _build_toc(headings)
    today = date.today().isoformat()

    html = _html_template(title, slug, body_html, toc_html, today)

    output_path.mkdir(parents=True, exist_ok=True)
    html_file = output_path / f"{slug}_v2_balanced.html"
    html_file.write_text(html, encoding="utf-8")
    return html_file
