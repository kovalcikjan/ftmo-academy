# Write Log: Basic Price Action

**Slug:** basic-price-action
**Lokace:** 2.2.
**Date:** 2026-04-17
**Workflow version:** 3.4
**Article type:** Lekce (X.Y.) — SHORT OVERVIEW (400–700 words)

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.2. |
| Lekce (Czech) | Základní price action |
| Lekce (English) | Basic Price Action |
| Article type | Lekce — short overview / teaser (400–700 words) |
| Part | Part 2 — Technical Analysis |
| Position | Lesson 2 of module (follows 2.1. Charts and timeframes) |
| Keywords source | Ahrefs MCP (Step 1 — reduced for Lekce) |
| Existing versions found | None |

### Lesson Structure Tree (from Google Sheet `Kurz-technická_analýza`)

```
2.2. Základní price action  [THIS LEKCE — overview article]
├── 2.2.1. Support a resistance
│   ├── 2.2.1.1. Flip zóny (resistance → support a naopak)
│   ├── 2.2.1.2. Dynamic S/R (MA jako podpora/odpor)
│   ├── 2.2.1.3. Round numbers jako S/R
│   └── 2.2.1.4. Horizontální úrovně (price levels)
├── 2.2.2. Supply & Demand zóny (Supply and demand trading)
├── 2.2.3. Trendové linie a definice trendu
├── 2.2.4. Market environment – ranges and trends
└── 2.2.5. Aktivita na levelech
    ├── 2.2.5.1. Pullback
    ├── 2.2.5.2. Breakout
    └── 2.2.5.3. False breakout (fakeout)
```

**Rule:** Lekce article lists chapters (X.Y.Z.) only. Podtemata (X.Y.Z.N.) belong to chapter articles — not included here.

### Chapters to introduce in the Lekce article (5 items)

1. **Support and resistance** — the foundational price-level concept
2. **Supply and demand zones** — zone-based interpretation of S/R
3. **Trendlines and trend definition** — how to read market direction
4. **Market environment: ranges and trends** — recognising which state the market is in
5. **Activity at levels (pullback, breakout, fakeout)** — how price behaves when it meets a level

### Internal linking targets

- Preceding Lekce: `2.1.` Charts and timeframes (`/lesson/charts-and-timeframes/`)
- Each chapter item → placeholder link to its future standalone chapter article under `/lesson/[chapter-slug]/`

---

## Step 1 — Competitor Research + Keyword Discovery (reduced for Lekce)

**Provider:** Ahrefs MCP unavailable (requires OAuth) — fell back to DataForSEO MCP. DR score replaced by qualitative domain authority proxy; organic traffic is qualitative only.

### Krok 1 — Seed validation

- Czech title: "Základní price action"
- Translated / canonical seed: **price action trading** (confirmed via WebSearch — standard term across trading academies)

### Krok 2 — WebSearch

2 queries, 14 unique candidate URLs after dedup and filter (removed TradingView indicator scripts, FTMO's own lesson as internal link target):
1. `"basic price action trading explained for beginners"`
2. `"price action trading fundamentals support resistance trendlines"`

### Krok 4 — Top competitor fetches (3 of 4 attempted)

| # | URL | Status | Word count | Key finding |
|---|-----|--------|------------|-------------|
| 1 | pepperstone.com/.../price-action-trading/ | OK | 1,200–1,400 | Covers S/R, candlestick patterns, multi-timeframe. Misses supply/demand, pullbacks, breakouts, fakeouts. |
| 2 | priceaction.com/.../what-is-price-action/ | OK | ~2,200 | Strongest on patterns (pin bar, inside bar, fakey) and confluence. S/R well covered. Supply/demand absent. |
| 3 | forex.com/.../price-action-trading/ | 403 blocked | — | Skipped — replaced by #4. |
| 4 | learntotradethemarket.com/price-action-trading-forex | OK | 2,200–2,500 | Best on trend definition (HH/HL, LH/LL) + ranges vs trends distinction. Fakeouts and pullbacks both mentioned. No supply/demand. |

### Krok 5 — Keyword discovery (1 DFS call — reduced)

- `dataforseo_labs_google_keyword_suggestions` for seed `price action trading`, limit 50, SV ≥ 100, EN only
- 32 EN keywords returned. After dedup (word-order variants of the main term collapsed) and scope filter (removed book/course/indicator/brand variants like "Al Brooks"): **10 keywords kept**

### Content Gap Summary (for the Lekce framing)

- **Supply and demand zones** are consistently absent from top competitor overview pages — a clear differentiation point for FTMO's Lekce.
- **Ranges vs trends as a distinct concept** appears fragmented across competitors (usually bundled inside "trends"). Treating it as its own chapter (2.2.4) is a structural edge.
- Most competitor overviews jump straight to candlestick patterns; FTMO's Lekce treats **the market context (S/R, zones, structure) as the foundation first**, then layers pattern-level behaviour (pullback / breakout / fakeout) on top. This is the right didactic order.
- Competitors mix "naked chart" philosophy with specific setups; FTMO Lekce keeps philosophy light and focuses on the building blocks that subsequent chapters will expand.
- Primary keyword `price action trading` (1,600 vol, KD 13) is a broad fit; `what is price action trading` (590 vol) is ideal for an H2 definition; remaining keywords (strategy, patterns, trends, forex) map naturally to body mentions of chapter topics.

---

## Step 2 — Brief & Outline

| Item | Value |
|------|-------|
| Classification | BEGINNER |
| Word count target | 450–650 (Lekce rule) |
| H1 | Basic Price Action Trading |
| H2 count | 4 (What is / What you will learn / Why it matters / How to approach) |
| Chapter items listed | 5 of 5 (2.2.1 → 2.2.5) |
| Internal links planned | 6 |
| Callouts planned | 1 (Keep in Mind) |
| Validation | PASS |

### Keyword → Heading Map

| # | Keyword | Volume | KD | Assignment |
|---|---------|--------|----|-----------|
| 1 | price action trading | 1,600 | 13 | H1 |
| 2 | what is price action trading | 590 | 25 | H2 (first) |

All remaining keywords placed via body prose in Step 3 where natural.

### Files saved

- Markdown (LLM working file): `/Users/admin/Projects/ftmo-academy/data/output/lessons/basic-price-action/lesson_basic-price-action_EN_outline.md`
- DOCX (expert review): `/Users/admin/Projects/ftmo-academy/data/output/lessons/basic-price-action/lesson_basic-price-action_EN_outline.docx`
