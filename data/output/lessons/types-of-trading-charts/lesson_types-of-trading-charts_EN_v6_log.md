# Write Log: Types of Trading Charts (v6)

**Slug:** types-of-trading-charts
**Date:** 2026-03-06
**Workflow version:** 2.0

---

## INIT

| Item | Value |
|------|-------|
| Inventory position | Part 2: Trading Analysis > Technical Analysis, Lesson 2 of 19 |
| Status in inventory | DRAFT (v5) |
| Links to | Support/Resistance, Market Environment, Heikin Ashi, Renko |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions found | v4, v5 — new version written from scratch as v6 |


---

## STEP 1 — Competitor Research + Keyword Discovery

### Phase A — URL Discovery & Fetch

**EXA searches run:** 1 (rate limit hit after first search)
**Ahrefs SERP:** `types of trading charts` (US, top 10)

| # | URL | Source | DR | SERP pos | Fetch |
|---|-----|--------|----|----------|-------|
| 1 | https://www.babypips.com/learn/forex/types-of-charts | EXA | ~90 | — | ✓ |
| 2 | https://www.babypips.com/learn/forex/trading-chart-types-strengths-weaknesses | EXA | ~90 | — | ✓ |
| 3 | https://trendspider.com/learning-center/introduction-to-chart-types/ | Ahrefs | 65 | 6 | ✓ |
| 4 | https://zerodha.com/varsity/chapter/chart-types/ | Ahrefs | 77 | 8 | ✓ |
| 5 | https://www.ig.com/uk/ig-academy/the-basics-of-technical-analysis/types-of-charts | Ahrefs | 81 | 9 | ✓ |
| 6 | https://www.britannica.com/money/technical-analysis-chart-types | EXA | ~80 | — | ✓ |
| 7 | https://www.cmegroup.com/education/courses/technical-analysis/chart-types-candlestick-line-bar.html | Ahrefs | 85 | 5 | ✗ timeout |
| 8 | https://bullrush.com/types-of-charts-line-bar-candlestick/ | EXA | — | — | skip |
| 9 | https://blog.tradersunited.org/types-of-forex-charts-explained/ | EXA | — | — | skip |
| 10 | https://www.skyriss.com/guides/types-of-forex-charts-explained | EXA | — | — | skip |

**6 successful fetches** (above minimum of 3).

### Phase B — Keyword Discovery

**Seeds used:** `types of trading charts`, `candlestick chart`, `bar chart trading`, `line chart trading`, `forex chart types`, `trading chart types`

| # | Keyword | Volume | KD | Notes |
|---|---------|--------|----|-------|
| 1 | types of trading charts | 40 | 22 | PRIMARY — exact match |
| 2 | line chart | 8,200 | 20 | High vol, low KD — opportunity |
| 3 | candlestick | 7,900 | 38 | Core concept |
| 4 | technical analysis | 6,700 | 48 | Context keyword |
| 5 | candlestick chart | 3,500 | 47 | Core concept |
| 6 | price action | 2,400 | 26 | Low KD, relevant |
| 7 | trading charts | 2,700 | 84 | High KD, low priority |
| 8 | how to read a candlestick chart | 300 | 39 | Intent: practical |
| 9 | candlestick chart explained | 250 | 52 | Intent: educational |
| 10 | different types of trading charts | 10 | — | Long-tail variation |
| 11 | types of charts in trading | 10 | — | Long-tail variation |
| 12 | bar chart | 30,000 | 43 | High vol but generic |
| 13 | stock charts | 19,000 | 51 | Moderate relevance |
| 14 | chart patterns | 5,800 | 53 | Separate lesson — mention only |
| 15 | candlestick chart patterns | 1,000 | 52 | Separate lesson — mention only |
| 16 | how to read candlestick chart for day trading | 150 | 40 | Practical intent |
| 17 | types of charts in forex trading | 0 | — | Semantic variation |
| 18 | OHLC chart | — | — | Core concept (no vol data) |
| 19 | forex chart types | — | — | Semantic (EXA research) |
| 20 | bar chart trading | — | — | Semantic variation |

### Content Gap Summary

- **All 6 competitors cover only line / bar / candlestick** — opportunity to briefly cover Heikin Ashi, Renko, P&F with links to dedicated lessons (TrendSpider covers 7 types but too broadly)
- **No competitor offers a clear "which chart for which trader" decision framework** — opportunity for practical, trader-type-based guidance
- **Missing from competitors:** comparison table with quick-reference pros/cons per chart type
- **Missing from competitors:** connection between chart type choice and timeframe (e.g. Renko filters time, P&F filters noise)
- **Candlestick psychology depth lacking** — competitors mention color coding but don't connect to market sentiment reading

---

## STEP 3 — Draft Writing

**Word count:** ~1,850 words
**File:** `lesson_types-of-trading-charts_EN_v6.md`

### Keyword Integration Table

| # | Keyword | Vol | KD | Placement | Status |
|---|---------|-----|----|-----------|--------|
| 1 | types of trading charts | 40 | 22 | H1 title | ✓ |
| 2 | line chart | 8,200 | 20 | H2 heading + body | ✓ |
| 3 | candlestick chart | 3,500 | 47 | H2 heading + body | ✓ |
| 4 | candlestick | 7,900 | 38 | Throughout candlestick section | ✓ |
| 5 | bar chart | 30,000 | 43 | H2 heading + body | ✓ |
| 6 | OHLC chart | — | — | "also called an OHLC chart" in H2 | ✓ |
| 7 | price action | 2,400 | 26 | Body: "price action, support and resistance levels" | ✓ |
| 8 | how to read a candlestick chart | 300 | 39 | Addressed structurally (anatomy + reading sections) | ~ |
| 9 | technical analysis | 6,700 | 48 | Not placed — no natural opportunity without forcing | — |
| 10 | different types of trading charts | 10 | — | Semantic match via H1 + intro | ~ |

### Outline Deviations

| # | Outline item | Deviation | Reason |
|---|-------------|-----------|--------|
| 1 | H2: "What a Trading Chart Actually Shows" | Reworded to "What Does a Trading Chart Actually Show?" | Question framing more engaging for beginners |
| 2 | Closing links: Market Environment + Chart Patterns | Chart Patterns replaced with Support and Resistance; Chart Patterns still mentioned inline in candlestick section | More logical progression for lesson 2 of 19; S/R is closer in sequence |
| 3 | Comparison table in "Which Chart Type" section | Added as planned | No deviation |
| 4 | Tip callout about platform switching | Added to "Which Chart Type" section | Practical value; fits Tip callout type |

### Source Citations

| Claim | Source |
|-------|--------|
| Line chart plots only closing price, connects points with a line | https://www.babypips.com/learn/forex/types-of-charts |
| Line chart hides intraperiod price activity | https://www.babypips.com/learn/forex/trading-chart-types-strengths-weaknesses |
| Bar chart: left tick = open, right tick = close | https://www.ig.com/uk/ig-academy/the-basics-of-technical-analysis/types-of-charts |
| Bar charts preferred for longer timeframes | https://www.babypips.com/learn/forex/trading-chart-types-strengths-weaknesses |
| Bar charts harder to read for pattern analysis vs candlesticks | https://zerodha.com/varsity/chapter/chart-types/ |
| Candlestick: same OHLC data as bar, different visual encoding | https://www.britannica.com/money/technical-analysis-chart-types |
| Bullish candle = close higher than open; bearish = close lower | https://www.babypips.com/learn/forex/types-of-charts |
| Long body + short wicks = conviction; small body + long wicks = indecision | https://www.ig.com/uk/ig-academy/the-basics-of-technical-analysis/types-of-charts |
| Heikin Ashi uses averaged values from current and previous period | https://trendspider.com/learning-center/introduction-to-chart-types/ |
| Renko: new brick appears only when price moves fixed amount | https://trendspider.com/learning-center/introduction-to-chart-types/ |
| Candlestick as default recommendation for most traders | https://www.babypips.com/learn/forex/trading-chart-types-strengths-weaknesses |
| Keep in Mind callout (TA cognitive bias block) | FTMO Structure Guide — required for all TA lessons |

---

## STEP 4 — ToV Check

**Sentences reviewed:** ~85
**Issues found:** 2
**Result:** PASS (0-5 threshold)

| # | Location | Original | New | Reason |
|---|----------|----------|-----|--------|
| 1 | Intro, sentence 2 | "Before you can spot a trend, identify support and resistance, or recognize a pattern, you need to understand what the chart is telling you — and how different chart formats present that information." | "Before you can spot trends, read support and resistance, or recognize patterns, you need to understand what the chart is actually telling you. That starts with knowing how different formats present the same price data." | Sentence length: 34 words → split into 17+12 |
| 2 | "What Comes Next" | "You now understand what each chart type shows and when to use it." | "Chart type is the foundation." | Evaluative framing — reads cheerleading-adjacent; reframed as forward-looking |

---

## STEP 5 — Structure & Formatting

### Paragraph Audit
All paragraphs within 100 words. Longest: OHLC intro ~70 words. No splits required.

### Changes Applied

| Change | Detail |
|--------|--------|
| `---` separators | Reduced from 7 → 3 (Structure Guide max). Kept at: core→specialty break, specialty→decision break, footer |
| ToC added | `## In This Lesson` — 7 H2 links, placed after H1 before first H2 |
| Image placeholders | 4 added (see below) |
| CTA placeholders | 2 added (see below) |
| Callouts | Keep in Mind ✓, Note ✓, Tip ✓ — no additions; no section exceeds 2 callouts |
| Author block | Retained from draft |
| Risk Warning | Retained from draft |
| Educational Notice | Retained from draft |

### Image Placeholders

| # | Placement | Description |
|---|-----------|-------------|
| 1 | After H1 (hero) | Side-by-side comparison — same price period in line / bar / candlestick |
| 2 | End of Line Charts section | Line chart example on forex pair, daily timeframe |
| 3 | End of Bar Charts section | Annotated OHLC bar — open/high/low/close labeled, bullish + bearish side by side |
| 4 | End of Candlestick section | Candlestick anatomy — body, wicks, bullish vs bearish with OHLC labels |
| 5 | End of Which Chart Type section | Decision flowchart — trading goal → chart type recommendation |

### CTA Placeholders

| # | Placement | Description |
|---|-----------|-------------|
| 1 | End of "Beyond the Basics" section | Explore Heikin Ashi and Renko dedicated lessons |
| 2 | End of "What Comes Next" | Continue to Market Environment: Range vs. Trend |

---

## STEP 6 — HTML Conversion

| Item | Value |
|------|-------|
| Meta title | "Trading Chart Types: Line, Bar & Candlestick | FTMO Academy" — 59 chars |
| Meta description | "The three main trading chart types — line, bar, and candlestick — explained. Learn what each shows and how to choose the right format for your trading." — 152 chars |
| Canonical | `/lesson/types-of-trading-charts/` |
| Template | FTMO Academy v2_balanced |
| lesson HTML | `lesson_types-of-trading-charts_EN_v6.html` ✓ |
| log HTML | `lesson_types-of-trading-charts_EN_v6_log.html` ✓ |
| Callout classes | keep-in-mind, note, tip, risk-warning, edu-notice |
| Image placeholders | `<figure class="img-placeholder">` — 5 total |
| CTA placeholders | `<div class="cta-placeholder">` — 2 total |
| Internal links | 6 links with correct slugs preserved |

---

## STEP 7 — QA + Inventory Update

### Content Validation: PASS
- All OHLC definitions accurate
- Candlestick anatomy (body/wicks) correct
- Heikin Ashi / Renko / P&F descriptions accurate
- Didactic sequence: Line → Bar → Candlestick → Specialty → Decision ✓
- Scope clean: patterns/indicators deferred to correct lessons

### Source Citation Audit: PASS
- 12 claims — all sourced
- 0 [SOURCE NEEDED] flags

### QA Result: PASS
- E-E-A-T signals present ✓
- ToV compliant ✓
- Readability: avg ~18w sentences, no paragraph >100w ✓
- Keywords: primary + 7 secondary placed naturally ✓
- Formatting: callouts, table, image/CTA placeholders ✓
- Note: 8×H2 (guideline 3–7) — acceptable, "What Comes Next" is required template section

### Files Saved
- [x] lesson_types-of-trading-charts_EN_v6.md
- [x] lesson_types-of-trading-charts_EN_v6_log.md
- [x] lesson_types-of-trading-charts_EN_v6.html
- [x] lesson_types-of-trading-charts_EN_v6_log.html

### Inventory Updated
- Status: DRAFT (v5) → DRAFT (v6)
- Links To: updated to include all 6 internal links
- Last updated: 2026-03-06

