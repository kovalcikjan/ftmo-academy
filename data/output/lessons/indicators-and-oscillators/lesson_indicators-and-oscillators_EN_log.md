# Write Log: Indicators and Oscillators

**Slug:** indicators-and-oscillators
**Lokace:** 2.5.
**Lesson type:** Lekce (X.Y.) — SHORT OVERVIEW ARTICLE (400–700 words)
**Date:** 2026-04-17
**Workflow version:** 3.3

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.5. |
| Czech lesson name | Indikátory a oscilátory |
| Lesson level | Lekce (X.Y.) — short overview / teaser article |
| Target word count | 400–700 words |
| Source sheet | `Kurz-technická_analýza` (Google Sheet 1Hdd9-8yQaQAJGLfM2R8bekI-tIRexQGNFOT7UwNeyXM) |
| Existing versions found | None |
| Keywords source | Ahrefs MCP (Step 1 — simplified for Lekce) |

### Lesson Structure Tree (from Google Sheet)

```
2.5. Indikátory a oscilátory — THIS IS THE OVERVIEW ARTICLE
├── 2.5.1. Základní pojmy: Perioda, Source, typy výpočtů
├── 2.5.2. Klíčové indikátory (Moving Average a jeho typy, Bollinger Bands, ...)
├── 2.5.3. Oscilátory (RSI, Stochastics, MACD)
├── 2.5.4. Správné použití indikátorů
└── 2.5.5. Rizika indikátorů
```

Podtemata (2.5.2.1.–2.5.2.6., 2.5.3.1.–2.5.3.5.) are ignored at Lekce level — they belong to their parent chapter articles.

---

## Step 1 — Competitor Research + Keyword Discovery (simplified for Lekce)

**Date:** 2026-04-17

### Seed validation
- Topic "Indikátory a oscilátory" → EN "indicators and oscillators" / "technical indicators and oscillators"
- Verified via 2 WebSearch queries — term is standard in trading education (StockCharts, Babypips, TradersAsset all use this framing)

### WebSearch queries (2 total, simplified for Lekce)
1. `technical indicators and oscillators trading guide`
2. `indicators vs oscillators difference trading education`

### URLs table
Up to 8 URLs in the candidate pool. 3 fetched (Lekce cap = top 3).

| Status | URL | Note |
|--------|-----|------|
| Fetched | chartschool.stockcharts.com/introduction-to-technical-indicators-and-oscillators | Pillar intro — 4,000 words |
| Fetched | tradersasset.com/education/oscillators-and-indicators | Classification focus — 2,800 words |
| Fetched | trendspider.com/learning-center/oscillator-essentials-for-traders | Short intro 850 words, risk angle |
| 403 | babypips.com/leading-indicators-oscillators | Blocked — listed as candidate only |
| Candidate | tradeciety.com, strike.money, groww.in, wikipedia | Over cap, not fetched |

### Ahrefs / DataForSEO keywords
- Ahrefs MCP is not authenticated in this session → used DataForSEO (functional equivalent) as fallback
- 1 call: `keyword_suggestions("indicators and oscillators", SV>=50)`
- 1 call: `keyword_overview` for manual variant verification (broader trading-indicator terms + leading/lagging)

Final keyword set: 15 keywords across 4 clusters. Saved to `indicators-and-oscillators_step1.xlsx`.

### Content Gap Summary (3–5 bullets)

- **Competitors frame the topic as a pillar/taxonomy article.** StockCharts (4,000 words) and TradersAsset (2,800 words) attempt to teach the full classification in one place — leading vs lagging, centered vs banded, plus individual tools. At Lekce level we do the opposite: introduce + signpost, let the chapter articles (2.5.1–2.5.5) do the teaching.
- **The clearest visual distinction traders remember: indicators overlay the chart, oscillators sit in a separate window below price.** TradersAsset leads with this. Worth preserving in the Lekce intro — it is intuitive and immediately useful.
- **Trendspider's honest caveat is underused elsewhere: mix indicator *categories*, do not stack multiple oscillators.** Good angle for the "Správné použití / Rizika" framing (chapters 2.5.4 and 2.5.5) — supports no-false-certainty positioning without being preachy in the Lekce itself.
- **No competitor we fetched separates calculation basics (period, source, price type) from the indicator catalogue.** That is a structural advantage for the course: chapter 2.5.1 earns its spot by giving traders the vocabulary they need before meeting RSI or MACD. Worth hinting at in the Lekce "What you will learn" list.
- **All competitors acknowledge OB/OS signals fail in trending markets.** For a Lekce, this context belongs as a one-line framing note, not a section.

### Main keyword placement plan (for Step 2)

| Keyword | Placement |
|---------|-----------|
| indicators and oscillators | H1 |
| technical indicators | H2 (What you will learn) |
| oscillators in trading | H2 (What you will learn) |
| remaining 12 keywords | Step 3 body (natural integration, many may be left out — Lekce is short) |

**Output file:** `/Users/admin/Projects/ftmo-academy/data/output/lessons/indicators-and-oscillators/indicators-and-oscillators_step1.xlsx`


### Chapters — Summary for Lekce outline

| Lokace | Chapter name | One-line value |
|--------|--------------|----------------|
| 2.5.1. | Základní pojmy: Perioda, Source, typy výpočtů | Foundation — how every indicator is actually calculated |
| 2.5.2. | Klíčové indikátory (MA, Bollinger Bands, ...) | Trend-following tools overlaid directly on price |
| 2.5.3. | Oscilátory (RSI, Stochastics, MACD) | Momentum tools plotted below price for overbought / oversold reads |
| 2.5.4. | Správné použití indikátorů | Practical rules for combining and interpreting indicators |
| 2.5.5. | Rizika indikátorů | Common mistakes and cognitive traps in indicator-based trading |

---

## Step 2 — Brief & Outline

**Date:** 2026-04-17
**Lesson type:** Lekce (overview article)
**Classification:** BEGINNER
**Word count target:** 450–550 words (Lekce range 400–700)

### Structure (mandatory Lekce skeleton)
- H1: Indicators and Oscillators
- Intro (2 short paragraphs, AIO-friendly opening definition)
- H2: What you will learn in this lesson — bullet list with 1 item per chapter (2.5.1–2.5.5)
- H2: Why indicators and oscillators matter for traders (with 1 "Keep in Mind" callout)
- H2: How to approach this lesson (prerequisites)
- Closing paragraph + CTA to Chapter 2.5.1

### Keyword mapping (3 to headings, rest to body)
| Keyword | SV | Heading |
|---------|-----|---------|
| indicators and oscillators | 70 | H1 |
| technical indicators | 590 | H2 (What you will learn) |
| oscillators in trading | 140 | H2 (Why ... matter for traders) |

### Internal links (7 total, 5-minimum exceeded)
- 5 chapter links (2.5.1–2.5.5, future slugs)
- 2 prerequisite links (charts-and-timeframes, candlestick-patterns)

### Content validation
All 10 checks pass. No false certainty, no deep concept teaching in the Lekce, Podtemata correctly excluded.

**Validation: PASS**

### Outputs
- `.md` (LLM working file): `/Users/admin/Projects/ftmo-academy/data/output/lessons/indicators-and-oscillators/lesson_indicators-and-oscillators_EN_outline.md`
- `.docx` (human review): `/Users/admin/Projects/ftmo-academy/data/output/lessons/indicators-and-oscillators/lesson_indicators-and-oscillators_EN_outline.docx`
