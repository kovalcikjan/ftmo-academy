# Write Log: Charts and Timeframes (Lesson Overview)

**Slug:** charts-and-timeframes
**Lokace:** 2.1.
**Date:** 2026-04-17
**Workflow version:** 3.3

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.1. |
| Level | Lekce (hub/overview article) |
| Inventory position | Part 2: Trading Analysis > Technical Analysis > Lesson 2.1. "Graf a timeframe" |
| Article type | SHORT overview — references chapters, not comprehensive |
| User directive | "vytvoř článek pro zastřešující téma. nemusí být tak rozsáhlé, stačí aby jen odkazoval na ty kapitoly a byl kratší obecně" |
| Target word count | 600–900 words (short hub article) |
| Internal linking targets (children) | 2.1.1. Types of charts, 2.1.2. Candlestick anatomy (OHLC), 2.1.3. Timeframes for trading styles, 2.1.4. Multiple timeframe analysis, 2.1.5. Forex hours and sessions |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions found | None |

### Lesson Structure Tree (from Google Sheet `Kurz-technická_analýza`)

```
2.1. Graf a timeframe — THIS ARTICLE (overview hub)
├── 2.1.1. Typy grafů: čárový, sloupcový, svíčkový → H2 link-out
│   └── 2.1.1.1. Types of trading charts
├── 2.1.2. Anatomie svíčky (OHLC) → H2 link-out
├── 2.1.3. Volba časových rámců pro různé styly obchodování → H2 link-out
│   ├── 2.1.3.1. Hierarchie timeframů
│   └── 2.1.3.2. Výběr timeframu podle stylu
├── 2.1.4. Multiple time frame analýza → H2 link-out
└── 2.1.5. Forex trading hours and sessions → H2 link-out
```

### Child slug mapping (for internal links)

| Lokace | Slug | Status on disk |
|--------|------|----------------|
| 2.1.1. | types-of-trading-charts | exists |
| 2.1.2. | candlestick-anatomy-ohlc | exists |
| 2.1.3. | trading-timeframes | exists (outline stage) |
| 2.1.4. | multiple-timeframe-analysis | exists |
| 2.1.5. | forex-trading-hours-and-sessions | exists |

---

## Step 1 — Competitor Research + Keyword Discovery

### Krok 1: Seed Validation

Topic (CZ): Graf a timeframe (Lekce 2.1., hub/overview article)
Seeds (EN): `trading charts and timeframes`, `how to read trading charts`, `trading timeframes` — verified via WebSearch (cityindex, cmcmarkets, heygotrade, britannica, cmegroup all frame topic consistently)

### Krok 2: WebSearch — 4 queries

| Query # | Query | URLs returned |
|---------|-------|---------------|
| Q1 | "trading charts and timeframes" basics beginner guide | 10 |
| Q2 | how to read trading charts and timeframes introduction | 10 |
| Q3 | trading chart types and timeframes explained | 10 |
| Q4 | understanding charts candlesticks timeframes technical analysis | 10 |

After dedup + filter (removed Wikipedia, forums): **26 unique URLs**

### Krok 3: Ahrefs Metrics

**SKIPPED** — User requested DFS MCP instead of Ahrefs. DFS does not offer comparable URL-level DR / organic traffic endpoints. DR + organic traffic columns left empty in xlsx. For a short hub article (600–900 words), URL-level metrics are lower priority than content structure comparison.

### Krok 4: Top Fetches

Fetched 5 of 26 (minimum 3 required): newtrading.io, cmcmarkets.com, heygotrade.com, bullrush.com, britannica.com.

Failed: cityindex.com (403), cmegroup.com (timeout), ninjatrader.com (blocklist — skipped per workflow).

### Krok 5: Keyword Discovery (DFS)

Calls:
1. `dataforseo_labs_google_keyword_ideas` — seeds `trading charts`, `trading timeframes`, `chart timeframes` (broad seeds produced mostly non-trading noise — e.g. Gantt/Bristol stool/waterfall charts)
2. `dataforseo_labs_google_keyword_suggestions` — seed `candlestick chart` (strong candlestick-specific set)
3. `dataforseo_labs_google_keyword_suggestions` — seed `trading timeframe` (strong TF set)
4. `dataforseo_labs_google_keyword_suggestions` — seed `how to read trading charts` (strong reading-charts set)

### Krok 6: Merge + Dedup + Filter + Cluster

**Final keyword set: 28 keywords, 5 clusters**
- A: Reading charts (hub primary — 8 kws)
- B: Timeframes (6 kws)
- C: Multi-timeframe analysis — routes to 2.1.4. (4 kws)
- D: Candlestick — routes to 2.1.2. (6 kws)
- E: Chart types — routes to 2.1.1. (2 kws)

Main KW: "how to read trading charts" (320 vol, KD 5, MEDIUM). Low/medium cutoff 30 given niche topic.

### Content Gap Summary

- **No competitor presents charts + timeframes as a unified module hub** — they cover timeframes OR charts, rarely both at introductory gateway level
- **Educational progression (chart type → candlestick anatomy → timeframe choice → MTA → sessions)** is not shown elsewhere as a linked navigation path
- **Hub-style summary articles with explicit chapter link-outs** are rare in trading academies (Britannica, CMC, HeyGoTrade all go deep in one direction)
- **Opportunity for Academy:** concise gateway article (~600-900 words) that routes readers to detailed chapters — no competitor fills that niche
- **Keyword strategy:** primary KW "how to read trading charts" (320 vol, KD 5) is low-competition and fits the hub intent; candlestick/chart-type high-volume terms (8100 vol) belong in their dedicated chapters, not the hub

### xlsx output

`charts-and-timeframes_step1.xlsx` — Sheet "URLs" (26 rows) + Sheet "Keywords" (28 rows, Status + Notes empty for user review)

---

## Step 2 — Brief & Outline

**Date:** 2026-04-17
**Classification:** BEGINNER
**Target word count:** 600–900 words (short hub per user directive)
**Article type:** Module hub / gateway — not a standalone deep-dive

### Structure (7 H2 sections)

1. Types of Trading Charts → link-out to 2.1.1.
2. Anatomy of a Candlestick (OHLC) → link-out to 2.1.2.
3. Choosing a Timeframe for Your Trading Style → link-out to 2.1.3.
4. Multiple Timeframe Analysis → link-out to 2.1.4.
5. Trading Sessions and Hours → link-out to 2.1.5.
6. Next Steps (reading order guidance)
7. (Final section, no link-out)

### Keyword assignments to headings

- H1: `how to read trading charts` (primary, 320 vol, KD 5)
- H2 (Timeframes): `best timeframe for day trading` (260 vol, KD 1)
- H2 (Multi-TF): `multiple timeframe analysis` (150 vol)
- Remaining body keywords: woven naturally in Step 3

### Callouts planned

- Note (top): "Each section below is a summary. Use the link to open the full chapter."
- Keep in Mind (end): "Charts and timeframes are descriptive, not predictive."

Total: 2 callouts — within short-article limits.

### Internal links

5 mandatory link-outs (one per child chapter). Meets and exceeds the 3-5 minimum naturally, since the hub's core purpose is chapter routing.

### Validation

- Structure logical + didactic
- BEGINNER classification appropriate
- Word budget within target
- All 5 child chapters represented
- No deep-dive content duplicated (scope strictly kept to overview)
- **Validation: PASS**

### Output files

- `lesson_charts-and-timeframes_EN_outline.md` (LLM working file)
- `lesson_charts-and-timeframes_EN_outline.docx` (trading expert review copy)
