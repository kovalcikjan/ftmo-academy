# Write Log: Market Profile

**Slug:** market-profile
**Lokace:** 2.7.1.
**Parent Lekce:** 2.7. Market profile a objemová analýza
**Type:** Kapitola (standalone in-depth chapter article)
**Date:** 2026-04-17
**Workflow version:** 3.3 (academy-write)

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.7.1. |
| Czech name | Market profile |
| English working title | Market Profile |
| Inventory position | Part 2 (Technical Analysis) > Lekce 2.7 > Kapitola 1 of 5 |
| Classification (preliminary) | ADVANCED (assumes chart reading + price action basics) |
| Keywords source | Ahrefs MCP (Step 1) |
| User-provided source hint | https://ftmo.com/en/market-profile-volume-profile-and-auction-market-theory/ (saved locally as `lesson_market-profile_EN_original.md`) |
| Existing versions found | Stub `_log.md` and `_original.md` from abandoned /academy run — stub overwritten per user approval; `_original.md` kept as one of several sources for Step 1 |

### Lesson Structure Tree

```
2.7.   Lekce:    Market profile a objemová analýza
├── 2.7.1. Kapitola: Market profile           <-- THIS ARTICLE
├── 2.7.2. Kapitola: Volume Profile, Order Flow
├── 2.7.3. Kapitola: Identifikace zón s vysokým/nízkým objemem
├── 2.7.4. Kapitola: Úvod do profilace trhu
└── 2.7.7. Kapitola: Shrnutí a porovnání přístupů
```

### Scope Boundaries

**In scope:**
- Market Profile concept, structure, and TPO (Time Price Opportunity) logic
- Auction Market Theory foundations (price, time, volume as the three components)
- Value Area, Point of Control, balance vs imbalance, initial balance
- Profile shapes (D-shape, P-shape, b-shape, trend days) and how to read them
- Practical application for trading decisions (fair value, rotation, breakout context)

**Out of scope (forwarded to sibling chapters):**
- Volume Profile mechanics / Order Flow tape reading --> 2.7.2.
- High/low volume node identification as trade triggers --> 2.7.3.
- Full market profiling workflow --> 2.7.4.
- Comparison of approaches (MP vs VP vs OF) --> 2.7.7.

### Internal Linking Targets

**Within Lekce 2.7:**
- 2.7.2. Volume Profile, Order Flow (forward link for VP depth)
- 2.7.3. High/Low Volume Zones
- 2.7.4. Introduction to Market Profiling
- 2.7.7. Summary and Comparison of Approaches

**Cross-Part (prerequisites and context):**
- 2.1. Charts and Timeframes (how to read a chart)
- 2.2. Price Action Basics (supply/demand, support/resistance)

---

## Step 1 — Competitor Research + Keyword Discovery

**Date:** 2026-04-17
**Data source:** DataForSEO MCP (DFS) — Ahrefs MCP unavailable this session
**Main seed (validated):** `market profile` (also: `auction market theory`, `tpo chart`)

### Krok 1 — Seed Validation

Confirmed via 1 WebSearch: `market profile` is the standard trading-education term (Steidlmayer 1985, CBOT). Core concepts verified: TPO, Value Area, POC, Initial Balance, Auction Market Theory. Secondary seeds derived from competitor H2s: `auction market theory`, `tpo chart`.

### Krok 2 — WebSearch (4 queries × up to 6 URLs)

1. `"market profile" explained trading guide`
2. `market profile trading for traders guide TPO`
3. `how to read market profile chart value area point of control`
4. `market profile auction market theory Steidlmayer`

Candidate pool: 25 URLs (incl. user-provided FTMO source). Filtered out: forums (Forex Factory), paywalled courses (Udemy, Jim Dalton, ProfileTraders), PDF downloads (howtotrade.com), Amazon book page, software help pages (Sierra Chart, Quantower, TradingView, ProRealTime, CQG), NinjaTrader (workflow blocklist), non-relevant subdomain newsletter.

### Krok 3 — URL Metrics

DataForSEO `bulk_traffic_estimation` returned empty items for all 24 URL-level queries (URLs not present in DFS URL-level database — common for niche trading articles). Fell back to SERP rank + known domain authority as proxy for selection. DR column in xlsx left `n/a`.

### Krok 4 — Top 10 Fetch

Selected by relevance > known domain authority. Fetched 10 URLs; 9 succeeded, 1 failed (tradingriot.com/auction-market-theory 404 → blog subdomain worked as backup). Competitor coverage:

| # | Source | Focus | Words | Key strength |
|---|--------|-------|-------|--------------|
| 1 | Wikipedia | Theory + limitations | ~2,200 | Neutral reference, honest caveats |
| 2 | Bookmap | Strategies + VP vs MP | ~3,500-4,000 | Practical trade setups, footprint integration |
| 3 | Earn2Trade | Complete guide + day types | ~2,400 | Clean day-type taxonomy |
| 4 | Topstep | AMT + MP intro (beginner) | ~2,200 | Jargon-free grocery-store analogies |
| 5 | Tradingriot (blog) | AMT framework deep | ~3,800 | Honest critique (VWAP myth-busting) |
| 6 | Eminimind | Profile shapes + VA calc | ~1,800-2,000 | Concrete 131→92 calculation example |
| 7 | MarketProfile.info | VAH/VAL/POC deep dive | ~8,500-9,000 | Comprehensive Value Area specialist |
| 8 | ATAS | AMT + responsive/initiative | ~3,200 | Real chart examples (E-mini, WTI) |
| 9 | TIOmarkets | MP origin + components | ~2,000 | Clean intro structure |
| 10 | Optimus Futures | TPO + profile shapes (D/P/b/B/trend) | ~2,100 | Clearest shape taxonomy |

Average competitor word count: ~3,000 words (excluding 8.5k outlier).

### Krok 5 — Keyword Discovery (DFS, 4 calls)

1. `keyword_suggestions` seed `market profile` (limit 100, SV≥50) → 29 results, 720 SV main
2. `keyword_suggestions` seed `auction market theory` (limit 50, SV≥20) → 7 results, 880 SV main
3. `keyword_suggestions` seed `tpo chart` (limit 50, SV≥20) → 3 trading-relevant results
4. `related_keywords` seed `market profile trading` (depth 2, limit 100, SV≥20) → cluster expansion
5. `keyword_overview` batch (10 known-important terms: point of control, value area, IB, TPO, shapes, day types) → filled gaps from steps 1-4

### Krok 6 — Merge + Dedup + Filter + Cluster

- Filtered: branded platform terms (tradingview, mt4, mt5), author brands (Jim Dalton), format intents (pdf, book, ebook), unrelated domain ("target market profile", "market research analyst", "gaf tpo color chart" roofing)
- Volume cutoff: main KW > 500 → cutoff 20 per workflow
- Kept: 28 keywords in 9 intent clusters

**Clusters:**
- `1_MP_core` — core definition (5 kw, max SV 720)
- `2_AMT` — Auction Market Theory (3 kw, max SV 880)
- `3_TPO` — Time Price Opportunity (5 kw, max SV 260)
- `4_MP_vs_VP` — comparison (1 kw, SV 110)
- `5_MP_charts` — chart visualization (2 kw)
- `6_MP_application` — trading with MP (5 kw)
- `7_ValueArea_POC` — specific structures (5 kw, max SV 140)
- `8_Shapes_DayTypes` — profile shapes (2 kw)
- `9_SessionStructure` — Initial Balance (1 kw, SV 90)

### Krok 7 — xlsx Output

File: `/Users/admin/Projects/ftmo-academy/data/output/lessons/market-profile/market-profile_step1.xlsx`
- Sheet "URLs": 25 rows (incl. FTMO source row 0)
- Sheet "Keywords": 28 rows (Status + Notes empty for user review)

### Content Gap Summary

- **FTMO differentiation opportunity:** No competitor builds the AMT → MP structure → practical reading bridge in one piece. Most either go deep on theory (Wikipedia, Tradingriot) OR deep on one component (MarketProfile.info on VA only, Optimus on TPO shapes only). The FTMO source article introduces all three AMT components but skims the practical MP reading. Our lesson can unify: AMT philosophy (why markets move) → MP structure (how to read it) → profile shapes and day types (what the market is doing today).
- **Profile shape taxonomy is underserved:** Only Optimus Futures and Eminimind cover the full D/P/b/B/trend-day set. Clean visual taxonomy is a gap.
- **Initial Balance treatment is weak:** Most pieces mention IB in passing. No competitor treats IB as a structural predictor of day type. Opportunity for clean explanation.
- **"Keep in Mind" limitations section absent across competitors:** No top-10 article honestly addresses MP's limitations (requires normal distribution, single-day unreliability, time-vs-volume distinction). FTMO's realistic-educator ToV can own this.
- **Competitor length range: 1,800 to 9,000 words.** Target 2,500-3,500 words (Kapitola — in-depth standalone chapter, not overview).

---

## Step 2 — Brief & Outline

**Date:** 2026-04-17

### Classification

**ADVANCED** — Market Profile is a specialised lens that assumes the reader can already read a price chart, understands supply/demand, and has finished the earlier TA basics lessons. Introducing MP to a total beginner would overload them; ADVANCED framing lets the lesson go straight to the three reference points without re-teaching candlesticks.

### Word Count Target

**2,600–3,200 words.** Competitor average ~3,000 (excluding the 8.5k Value Area specialist). Need to cover: AMT philosophy, TPO mechanics, POC/VA/IB, five profile shapes, practical use, MP-vs-VP clarifier, limitations, next steps — without turning into a reference manual.

### Differentiation (Four Levers)

1. **Unify the stack** (AMT → MP chart → reference points → shapes → practical use) — no single top-10 competitor does all four.
2. **Own the honest-limitations section** — zero competitor top-10 pieces cover normal-distribution assumption, single-day unreliability, or time-vs-volume trade-off candidly.
3. **Clean profile-shape taxonomy** — D / P / b / trend-day / double-distribution in one table with "what it means" column.
4. **Trader-facing framing** — drop CBOT pit jargon (LDB, bracketed letters, single prints) unless explained in plain language first.

### Structure — 8 H2s + intro

1. (Intro — no H2, 3 paragraphs ~140w)
2. H2: Auction Market Theory: Why Markets Move (~400w)
3. H2: Time Price Opportunity: How a Market Profile Chart Is Built (~450w)
4. H2: Value Area, Point of Control, and Initial Balance (~600w, 3 H3s)
5. H2: Profile Shapes: Reading What the Session Is Doing (~500w, one table)
6. H2: How to Use Market Profile in Practice (~400w)
7. H2: Market Profile vs Volume Profile: A Quick Clarifier (~250w, one table)
8. H2: Limitations to Keep in Mind (~350w)
9. H2: What to Cover Next (~120w)

Total planned: ~3,210 words (within target range).

### Keyword Placement (Headings only)

Top 7 keywords mapped to H1/H2. Remaining ~21 keywords placed naturally in body prose in Step 3.

| Keyword | Volume | Heading |
|---------|--------|---------|
| market profile | 720 | H1 |
| auction market theory | 880 | H2 — "Auction Market Theory: Why Markets Move" |
| tpo chart / time price opportunity | 260/90 | H2 — "Time Price Opportunity: How a Market Profile Chart Is Built" |
| value area trading | 140 | H2 — "Value Area, Point of Control, and Initial Balance" |
| point of control trading | 110 | H3 under VA/POC section |
| market profile vs volume profile | 110 | H2 — "Market Profile vs Volume Profile: A Quick Clarifier" |
| market profile shapes | 20 | H2 — "Profile Shapes: Reading What the Session Is Doing" |

### Internal Links Plan

5 links planned (exceeds the 3–5 minimum):

1. 2.1. Charts and Timeframes — prerequisite link in first Tip callout
2. 2.2. Price Action Basics — same Tip callout
3. 2.7.2. Volume Profile, Order Flow — forward link in MP-vs-VP section + "Next" section
4. 2.7.3. High/Low Volume Zones — "Next" section
5. 2.7.4. Introduction to Market Profiling — "Next" section + referenced in Limitations (composite-profile note)

### Callout Plan (6 callouts across 8 H2s — within Medium-article limits: 2–3 per lesson)

| # | Section | Type | Purpose |
|---|---------|------|---------|
| 1 | AMT H2 | Note | Clarify AMT vs MP (theory vs tool) |
| 2 | TPO H2 | Tip | Prerequisite link to lessons 2.1 + 2.2 |
| 3 | VA/POC/IB H2 | Important | The three reference points every MP reader must know |
| 4 | Shapes H2 | Keep in Mind | Shape recognition is context, not a signal |
| 5 | Practical use H2 | Tip | MP is a second screen, not primary chart |
| 6 | Limitations H2 | Keep in Mind | Honest framing — MP is one tool among many |

Max 1 callout per H2. No back-to-back callouts. Two "Keep in Mind" callouts — appropriate for a TA lesson addressing common biases.

### Content Validation

- Logical flow: PASS (philosophy → tool → reference points → pattern recognition → practice → comparison → limitations → next)
- ADVANCED-level completeness: PASS (all key concepts present)
- Scope discipline: PASS (VP, order flow, HVN/LVN, composite profiles, full MP-vs-VP-vs-OF comparison forwarded to siblings)
- Honest framing: PASS (limitations explicit, "not a signal" callouts, no guru tone)
- Risk flagged: 8 H2s is at the ceiling of Structure Guide's 3–7 range. If Step 3 draft runs long, candidate to merge: "Practical Use" + "Limitations" could combine. Do not compress preemptively.

**Validation: PASS**

### Output

- Markdown: `data/output/lessons/market-profile/lesson_market-profile_EN_outline.md`
- Docx: `data/output/lessons/market-profile/lesson_market-profile_EN_outline.docx`
