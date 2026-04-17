# Write Log: Volume Profile and Order Flow

**Slug:** volume-profile-and-order-flow
**Lokace:** 2.7.2.
**Date:** 2026-04-17
**Workflow version:** 3.3

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.7.2. |
| Hierarchy level | Kapitola (X.Y.Z.) — standalone in-depth article |
| Czech name | Volume Profile, Order Flow |
| English name | Volume Profile and Order Flow |
| Parent Lekce | 2.7. Market profile a objemová analýza (Market Profile and Volume Analysis) |
| Position in Lekce | Kapitola 2 of 5 (2.7.1, 2.7.2, 2.7.3, 2.7.4, 2.7.7) |
| Target search volume | 2,550 (from inventory) |
| Sub-topics (X.Y.Z.N.) | None — free structure based on Step 1 research |
| User-provided reference | https://ftmo.com/en/market-profile-volume-profile-and-auction-market-theory/ (partial info on volume profile) |
| Internal linking targets | 2.7.1. Market profile; 2.7.3. High/low volume zones; 2.7.4. Introduction to market profiling; 2.7.7. Approach comparison |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions (this slug) | None |
| Related existing folder | `market-profile-volume-profile-and-auction-market-theory/` — separate `/academy` (edit) run on legacy FTMO article covering the same Lokace; kept as-is |

---

## Lesson Structure Tree

```
2.7. Market profile a objemová analýza [LEKCE]
├── 2.7.1. Market profile [KAPITOLA]
├── 2.7.2. Volume Profile, Order Flow [KAPITOLA] ← THIS ARTICLE
├── 2.7.3. Identifikace zón s vysokým/nízkým objemem [KAPITOLA]
├── 2.7.4. Úvod do profilace trhu [KAPITOLA]
└── 2.7.7. Shrnutí a porovnání přístupů [KAPITOLA]
```

No sub-topics (X.Y.Z.N.) under 2.7.2. — article structure will be derived from Step 1 competitor research.

---

## Step 1 — Competitor Research + Keyword Discovery

**Date:** 2026-04-17
**Data source:** DataForSEO MCP (Ahrefs MCP unavailable)

### Seed Validation
- Topic (CZ): Volume Profile, Order Flow
- Primary EN seeds: `volume profile`, `order flow trading`
- Validated via WebSearch — terminology used verbatim across trading academies (TradingView, Bookmap, Oanda, Schwab, Topstep, Atas)
- No translation ambiguity

### URL Discovery — 4 WebSearch Queries
1. "volume profile order flow trading explained"
2. "volume profile indicator guide for traders"
3. "how to read order flow trading"
4. "volume profile vs order flow difference"

**Result:** 24 candidate URLs after dedup + filter (removed Quora, ForexFactory, Reddit, NinjaTrader per blocklist, course/marketing pages).

### URL Enrichment — DataForSEO Labs `domain_rank_overview`
- Organic traffic (ETV) collected for 17 unique domains.
- DR proxy scored qualitatively (very high/high/medium/low/very low) based on ETV magnitude — direct DR unavailable without Ahrefs.
- medium.com, dowidth.com omitted from metric calls (known high traffic / empty result respectively).

### Top 10 WebFetch
- 9 successful fetches + 1 FTMO reference article (user-provided).
- 1 failure: Schwab (authorization error — skipped, replaced with Topstep and Trendspider already in top 10).
- Extracted: H1, H2/H3 structure, topics covered, unique angle, word count estimate per URL.

### Keyword Discovery — DataForSEO Labs (2 calls)
- Call 1: `keyword_suggestions` for seed `volume profile` — 53 results, filtered SV ≥ 50.
- Call 2: `related_keywords` for seed `order flow trading`, depth 2 — 12 results, filtered SV ≥ 30.

### Merge + Dedup + Filter + Cluster
- Removed branded/platform keywords (thinkorswim, tradingview, ninjatrader, webull, sierra chart, tradestation, trader-dale, jigsaw, atas, gocharting, MT4/MT5) — out of scope for a platform-neutral educational article.
- Removed transactional/product queries ("order flow trading software", "volume profile books").
- Removed near-duplicates (profile volume ≈ volume profile; volume profile indicator/indicators).
- 25 keywords retained across 5 intent clusters:
  - **Cluster 1 — VP core** (definition, indicator, trading basics)
  - **Cluster 2 — VP how-to** (how to read, use, trade with VP + strategies)
  - **Cluster 3 — VP types** (fixed range, visible range, session, anchored, shapes, p-shape)
  - **Cluster 4 — VP vs Market Profile / TPO**
  - **Cluster 5 — OF core** (order flow trading, chart, indicator, data, strategy)
- Main KW "volume profile" (1,000) and "order flow trading" (1,000) → cutoff SV ≥ 20 (applied ≥ 50 de facto).

### Output
- xlsx: `volume-profile-and-order-flow_step1.xlsx` (2 sheets: URLs 24 rows + Keywords 25 rows)
- Status + Notes columns empty for user review.

### Content Gap Summary
1. **VP + OF integration is rare.** Most competitor pages cover volume profile OR order flow in isolation. Only Trader-Dale and Bookmap treat them as a combined system — strong differentiation opportunity.
2. **Platform-neutral framing missing.** Top-ranking pages lean heavily on specific platforms (Bookmap, TradingView, Atas, NinjaTrader). An educational lesson explaining the concepts platform-agnostically fills a clear gap.
3. **Beginner-friendly entry is weak.** Pages jump into POC/VA jargon or assume footprint-chart familiarity. A clear "what is this and why use it" opening separates educational content from tool documentation.
4. **No honest discussion of limitations.** Competitors rarely acknowledge that VP is reactive (not predictive) or that order flow requires expensive data feeds + low-latency infrastructure. An FTMO-aligned "realistic educator" angle adds trust.
5. **Comparison framing underused.** "Volume profile vs market profile / TPO" has 110 SV and no deep competitor answer — a short clarifying section serves both search intent and didactic clarity.

### Files
- xlsx: `/Users/admin/Projects/ftmo-academy/data/output/lessons/volume-profile-and-order-flow/volume-profile-and-order-flow_step1.xlsx`

---

## Step 2 — Brief & Outline

**Date:** 2026-04-17

| Item | Value |
|------|-------|
| Classification | ADVANCED |
| Target word count | 2,200–2,600 |
| Competitor avg (fetched) | ~2,300 (range 700–3,200) |
| H2 sections | 7 |
| H3 sections | 12 |
| Keywords mapped to headings | 5 (top by volume) |
| Internal links planned | 5 (2.7.1, 2.7.3, 2.7.4, 2.7.7, 2.1.1.1.) |
| Callouts planned | 4 (Note, Keep in Mind ×2, Tip) |
| Tables planned | 2 (profile types; VP vs MP vs OF comparison) |
| Content validation | PASS |

### Differentiation (from Content Gap Summary)
- Integrate VP + OF as complementary tools (rare in SERP).
- Platform-neutral presentation (SERP is vendor-dominated).
- Honest limitations section (VP = reactive; OF = infrastructure-gated on retail forex).
- Explicit bridging to sibling chapters 2.7.1 and 2.7.3 to avoid overlap.

### Files
- outline .md: `/Users/admin/Projects/ftmo-academy/data/output/lessons/volume-profile-and-order-flow/lesson_volume-profile-and-order-flow_EN_outline.md`
- outline .docx: `/Users/admin/Projects/ftmo-academy/data/output/lessons/volume-profile-and-order-flow/lesson_volume-profile-and-order-flow_EN_outline.docx`

