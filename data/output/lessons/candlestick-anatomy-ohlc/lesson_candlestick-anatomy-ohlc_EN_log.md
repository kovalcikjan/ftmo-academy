# Write Log: Candlestick Anatomy (OHLC)

**Slug:** candlestick-anatomy-ohlc
**Lokace:** 2.1.2.
**Date:** 2026-04-16
**Workflow version:** 3.3

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.1.2. |
| Inventory position | Part 2: Trading Analysis > 2.1. Graf a timeframe, Chapter 2 of 5 |
| Internal linking targets | 2.1.1. Types of Trading Charts, 2.1.3. Choosing Timeframes by Trading Style, 2.3.1. Candlestick Patterns, 2.2.1. Support and Resistance, 2.2.3. Market Environment: Ranges vs Trends |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions found | None |

### Lesson Structure Tree

```
2.1.2. Anatomie svíčky (OHLC) — THIS IS THE ARTICLE (Kapitola)
       No sub-topics in Google Sheet — free structure based on Step 1 research
```

### Parent Lesson Context (2.1. Graf a timeframe)

```
2.1. Graf a timeframe
├── 2.1.1. Typy grafů: čárový, sloupcový, svíčkový
│   └── 2.1.1.1. Types of trading charts
├── 2.1.2. Anatomie svíčky (OHLC) ← THIS ARTICLE
├── 2.1.3. Volba časových rámců pro různé styly obchodování
│   ├── 2.1.3.1. Hierarchie timeframů
│   └── 2.1.3.2. Výběr timeframu podle stylu
├── 2.1.4. Multiple time frame analýza
└── 2.1.5. Forex trading hours and sessions
```

---

## Step 1 — Competitor Research + Keyword Discovery

**Date:** 2026-04-16
**Data source:** DataForSEO Labs (Ahrefs MCP unavailable — auth required, switched per workflow rules)
**Main seed:** `candlestick anatomy` (SV 260, KD 3, informational)
**Secondary seeds:** `how to read candlestick chart`, `ohlc candlestick`, `candlestick chart` (related)

### Process Summary

- 4 WebSearch queries × 6 URLs = 24 candidate URLs after dedup
- Domain rank overview (DFS Labs) for 11 priority domains → etv range 1,293 – 233M
- URL-level traffic unavailable (DFS Backlinks API not subscribed) — used domain etv as proxy
- 13 URLs selected for fetch → 10 successful, 3 failed (babypips 403, ig.com 403, cmegroup socket error)
- 2 Ahrefs-equivalent calls: `keyword_suggestions` (candlestick anatomy, how to read, ohlc candlestick) + `related_keywords` (candlestick chart, depth 2)

### Volume Cutoff Applied

Main KW SV 260 → 100–500 bucket → cutoff **10** (keep all keywords ≥10 SV).

### Final Keyword Set: 24 keywords across 5 intent clusters

| Cluster | Keywords | Volume range |
|---------|----------|--------------|
| C1 Anatomy/Structure | 8 | 10–260 |
| C2 How to Read | 3 | 170–2,400 |
| C3 OHLC Specific | 5 | 10–20 |
| C4 Chart/Types | 5 | 90–8,100 |
| C5 PDF/Download | 3 | 10 |

### Content Gap Summary

1. **Anatomy vs. patterns bleed.** Nearly every competitor article (Capital.com, Dukascopy, Litefinance, Pepperstone, StockCharts ChartSchool) collapses "candlestick anatomy" and "candlestick patterns" into one sprawling article. Our lesson is pure anatomy/OHLC — patterns live in 2.3.1. Explicit scope boundary = differentiation.

2. **OHLC as data abstraction is underdeveloped.** Most articles mention "open, high, low, close" as a bullet list. Only QuestDB explicitly frames OHLC as the underlying data structure that a candle renders visually. Academy can make this the intellectual anchor of the lesson.

3. **"What candlesticks don't tell you" is missing from most guides.** Only StockCharts ChartSchool covers this honestly. Good fit for a Keep-in-Mind callout (aligns with Structure Guide's TA cognitive-bias disclaimer).

4. **Timeframe context is often buried.** Pepperstone and DayTradingToolkit touch on "a candle means nothing alone" / timeframe dependency, but it is not a headline point. Strong bridge opportunity to 2.1.3. (Choosing timeframes).

5. **Candlestick vs. bar chart comparison.** LiteFinance and StoneX lean on this framing. Useful table for our lesson — short comparison showing why candlesticks won over OHLC bars for retail trading.

### Output Files

- xlsx: `/Users/admin/Projects/ftmo-academy/data/output/lessons/candlestick-anatomy-ohlc/candlestick-anatomy-ohlc_step1.xlsx`
  - Sheet "URLs" — 24 rows (DR~, domain etv, fetch status, H1, key topics, notable gap, word count, data source column = "dfs")
  - Sheet "Keywords" — 24 rows (Volume, KD, Cluster, Status + Notes empty for user review)

### Notes for User Review

- Babypips source unavailable (403) — premier trading academy reference lost. Alternative: Litefinance + DayTradingToolkit + StockCharts ChartSchool cover comparable depth.
- Wikipedia OHLC bar chart article (entry #19) was intentionally not fetched — bar-chart focused, marginal value for candle-anatomy lesson.
- Intent data from DFS shows "commercial" for many keywords — misleading (these are informational for trader education). Treat with judgement.

---

## Step 2 — Brief & Outline

**Date:** 2026-04-16
**Classification:** BEGINNER
**Word Count Target:** 1,500–1,800 words (below competitor average 2,200–5,500 — strict anatomy scope)

### Structure Summary

- H1 + 8 H2 sections (intro → what a candlestick represents → OHLC data → body/wicks → colour → reading → bar vs candle → limitations → next steps)
- 3 tables (OHLC data points, candle shape quick-read, bar vs candle comparison)
- 3 callouts (Note on OHLC as data; Tip on platform colour settings; 2x Keep-in-Mind on pattern overfitting / context)
- 2 image placeholders (labelled OHLC candle diagram, annotated body/wicks diagram)

### Keywords Mapped to Headings

| Keyword | Volume | Heading assignment |
|---------|--------|--------------------|
| candlestick anatomy | 260 | H1 |
| how to read a candlestick chart | 2,400 | H2 — "How to Read a Single Candle" |
| ohlc candlestick / ohlc vs candlestick | 20 each | H2 — "The Four OHLC Data Points" + "Candlestick vs. OHLC Bar" |
| candlestick chart | 8,100 | body (intro) |
| candlestick chart explained | 390 | body (intro) |
| remaining 19 | — | Step 3 body integration |

### Internal Links Plan

5 targets identified (3–5 will appear in final article):
- 2.1.1.1. Types of Trading Charts → `types-of-trading-charts`
- 2.1.3. Choosing Timeframes by Trading Style → `choosing-timeframe-by-trading-style`
- 2.3.1. Candlestick Patterns → `japanese-candlesticks`
- 2.2.1. Support and Resistance → `support-and-resistance`
- 2.2.3. Ranges vs Trends → `ranges-vs-trends`

### Differentiation (summary)

1. Strict anatomy-only scope (patterns deferred to 2.3.1.)
2. OHLC framed as data abstraction, not just a bullet list
3. Explicit "What a Candle Does NOT Tell You" section with Keep-in-Mind callout
4. Candlestick vs. OHLC bar comparison table
5. Timeframe dependency signposted forward to 2.1.3. (not covered here)

### Content Validation

- Beginner didactic order: concept → data → visual → direction → reading → comparison → limitations → next steps
- Marubozu and doji mentioned once each as anatomy edge cases (no-wick, no-body) — no pattern interpretation; flagged for trading-expert review in case stricter exclusion is preferred
- Pattern overfitting acknowledged per Structure Guide YMYL requirement for TA content
- **Validation: PASS** (pending trading-expert review)

### Output Files

- Working outline (LLM): `/Users/admin/Projects/ftmo-academy/data/output/lessons/candlestick-anatomy-ohlc/lesson_candlestick-anatomy-ohlc_EN_outline.md`
- Reviewable docx: `/Users/admin/Projects/ftmo-academy/data/output/lessons/candlestick-anatomy-ohlc/lesson_candlestick-anatomy-ohlc_EN_outline.docx`
