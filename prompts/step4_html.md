# Step 4: HTML Conversion

Convert the final markdown article to styled HTML using the FTMO Academy v2_balanced template.

---

## CORE PRINCIPLE

> **RULE:** Images from original article must be placed EXACTLY where they were.
> Content meaning NEVER changes. Only presentation is applied.

---

## Page Structure (Mandatory Order)

```
1. <header>          Black background, FTMO logo + nav
2. <nav.breadcrumbs> Module > Lesson path
3. <header.lesson>   Module label + H1 + meta (date, author)
4. <nav.toc>         Table of Contents (always in HTML)
5. <article>         Full lesson content
6. <div.author-box>  Author + Published + Updated dates
7. <div.disclaimer>  Educational Notice
8. <div.disclaimer>  Risk Warning
9. <footer>          Black background, FTMO logo + links
```

> **NO Prerequisites inline block** — handled by FTMO CMS sidebar.
> **NO TL;DR or Overview section** — only Key Takeaways before conclusion.

---

## FTMO Brand Colors (Official)

| Color Name | Hex | Usage |
|------------|-----|-------|
| **Azure Radiance** | `#0781fe` | Links, buttons, Tip callout accent, highlights |
| **Torea Bay** | `#123a83` | H2/H3 headings, ToC text, table headers, ToC border |
| **Silver** | `#c6c6c6` | Borders, HR lines |
| **Black** | `#000000` | Header + footer background |
| **White** | `#ffffff` | Content background |
| **Light Gray** | `#f5f5f7` | ToC background, Key Takeaways bg, even table rows |

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| H1 | Poppins | 2rem | 700 | **`#2d2d2d`** (dark charcoal — NOT blue) |
| H2 | Poppins | 1.4rem | 700 | `#123a83` (Torea Bay) |
| H3 | Poppins | 1.1rem | 600 | `#123a83` (Torea Bay) |
| Body | Poppins | 16px | 400 | `#1a1a2e` |
| Small/meta | Poppins | 13px | 400 | `#555` |

**H1 rule:** Always `#2d2d2d`. Never Torea Bay blue. Large, bold, reads like a news/blog headline.

Load font via Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## Text Width

**Rule: Text width = image width = full content column width.**

- Content max-width: `1160px` (lesson-wrap)
- Paragraphs: NO `max-width` constraint — full column width
- List items: NO `max-width` constraint — full column width
- Callouts: NO `max-width` constraint — full column width
- Tables: `width: 100%`

> **Never** set `max-width: 72ch` or similar on paragraphs/lists. Text and images must align to the same width.

---

## Images

### Default (full width)
All lesson images display at full content column width:
```css
.lesson-content img {
    display: block;
    max-width: 100%;
    height: auto;
    margin: 24px 0;
    border-radius: 4px;
    border: 1px solid #c6c6c6;
}
```

### Sized images (intro / decorative)
Intro or decorative images that are too large at full width should be sized down using inline style. Determine appropriate size visually — typical range: 25%–50%.

```html
<!-- Example: intro image reduced to 30% -->
<img src="..." alt="..." style="width: 30%; height: auto;">
```

**Rule:** Judge each image individually. Full-width images = charts, comparisons, platform screenshots. Reduced images = decorative/intro visuals, logos, icons.

### Alt text
Every image requires descriptive alt text:
```html
<img src="..." alt="Renko chart example showing price bricks on EUR/USD">
```

### Captions (optional)
Add `<figcaption>` only when the image needs context not provided by surrounding text:
```html
<figure>
    <img src="..." alt="...">
    <figcaption>Time-based (left) vs. 100-range chart (right) — price rotations appear cleaner on the range chart.</figcaption>
</figure>
```

---

## Table of Contents

**Always include in HTML** (regardless of article word count).

Styling:
```css
background: #f5f5f7;
border-left: 4px solid #123a83;
text color: #123a83;
font: Poppins
```

Structure — nested (H2 = 1., H3 = 1.1., 1.2.):
```html
<nav class="toc">
    <div class="toc__title">Table of Contents</div>
    <ol>
        <li><a href="#section-1">Section 1</a>
            <ol>
                <li><a href="#subsection-1-1">Subsection 1.1</a></li>
                <li><a href="#subsection-1-2">Subsection 1.2</a></li>
            </ol>
        </li>
        <li><a href="#section-2">Section 2</a></li>
    </ol>
</nav>
```

---

## Table Styling

```css
table     { width: 100%; border-collapse: collapse; font-size: 14px; }
th        { background: #123a83; color: #ffffff; font-weight: 600; text-align: left; padding: 12px 16px; }
td        { padding: 10px 16px; border-bottom: 1px solid #c6c6c6; vertical-align: top; }
tr:nth-child(even) td { background: #f5f5f7; }
```

---

## Callout Styling

| Type | Background | Left border | Label color |
|------|------------|-------------|-------------|
| **Tip** | `#e8f4ff` | `#0781fe` | `#0781fe` |
| **Note** | `#eef2fa` | `#123a83` | `#123a83` |
| **Warning** | `#fff8e6` | `#e6a817` | `#a06b00` |
| **Important** | `#fef0f0` | `#e05050` | `#c03030` |
| **Keep in Mind** | `#f0f7f0` | `#4a7c59` | `#2e5c3a` |

```html
<div class="callout callout--tip">
    <span class="callout__label">Tip</span>
    <p>...</p>
</div>
```

---

## Key Takeaways

Place **before** Next Steps, **after** Conclusion content.

```html
<section class="key-takeaways">
    <h2 id="key-takeaways">Key Takeaways</h2>
    <ul>
        <li><strong>Term</strong> — explanation</li>
    </ul>
</section>
```

Styling: `background: #f5f5f7; border-radius: 6px; padding: 24px 28px;`

---

## Author Box

```html
<div class="author-box">
    <div class="author-box__avatar">FA</div>
    <div>
        <div class="author-box__name">FTMO Academy Content Team</div>
        <div class="author-box__meta">Published: [Date] &bull; Last Updated: [Date]</div>
    </div>
</div>
```

---

## Disclaimers

```html
<!-- Educational Notice -->
<div class="disclaimer disclaimer--educational">
    <strong>Educational Content Notice:</strong> This material is for educational purposes only
    and does not constitute financial advice. Trading decisions should be based on your own
    analysis and risk tolerance.
</div>

<!-- Risk Warning -->
<div class="disclaimer disclaimer--risk">
    <strong>Risk Warning:</strong> Trading involves significant risk of loss. Past performance
    is not indicative of future results. Only trade with capital you can afford to lose.
</div>
```

Styling:
- Educational: `background: #f5f5f7; border-left: 3px solid #c6c6c6; color: #555;`
- Risk: `background: #fff8e6; border-left: 3px solid #e6a817; color: #6b4c00;`

---

## HTML Checklist

**Structure:**
- [ ] H1 title: `#2d2d2d`, font-weight 700, Poppins
- [ ] Intro text immediately below H1 (before ToC)
- [ ] Table of Contents present (nested, styled)
- [ ] NO Prerequisites inline block
- [ ] NO TL;DR or Overview section
- [ ] Key Takeaways present (before Next Steps)
- [ ] Next Steps with internal links

**Images:**
- [ ] All original images included at exact original positions
- [ ] Full-width images: charts, screenshots, comparisons
- [ ] Reduced images: decorative/intro — sized with inline `style="width: X%; height: auto;"`
- [ ] Every image has descriptive alt text
- [ ] Captions only where additional context needed

**Text width:**
- [ ] Paragraphs: no max-width constraint
- [ ] Lists: no max-width constraint
- [ ] Callouts: no max-width constraint
- [ ] Text and images align to same column width

**Branding:**
- [ ] Poppins font loaded
- [ ] H1 color `#2d2d2d`
- [ ] H2/H3 color `#123a83`
- [ ] Links color `#0781fe`
- [ ] Table headers `#123a83`
- [ ] ToC: gray bg `#f5f5f7`, dark blue text `#123a83`, left border `#123a83`

**Required elements:**
- [ ] Author box with dates
- [ ] Educational Content Notice
- [ ] Risk Warning
- [ ] Black header + footer

**Technical:**
- [ ] Responsive design (max-width 1160px)
- [ ] Meta title: `[Lesson Title] | FTMO Academy` (50-60 chars)
- [ ] Meta description (150-160 chars)
- [ ] Canonical URL

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-05 | Initial creation |
| 1.1 | 2026-03-05 | H1 color rule (#2d2d2d not blue); text width = image width (no max-width on paragraphs/lists/callouts); image sizing rules (full-width vs. reduced) |
