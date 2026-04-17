# Write Log: Chart Patterns

**Slug:** chart-patterns
**Lokace:** 2.4.
**Type:** Lekce (lesson overview — short article, 400–700 words)
**Date:** 2026-04-17
**Workflow version:** 3.4

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.4. |
| Czech title | Patterny na grafu |
| English title | Chart Patterns |
| Part | Part 2 — Technical Analysis |
| Module | 2.4. Patterny na grafu |
| Position | Lesson 4 of 6 in Technical Analysis module |
| Existing versions found | None — first version |
| Keywords source | Ahrefs MCP (Step 1) — simplified for Lekce |

### Lesson Structure Tree (from Google Sheet "Kurz-technická_analýza")

```
2.4. Patterny na grafu — THIS IS THE LEKCE (short overview article)
├── 2.4.1. Cenové formace (Price Formations) → item in "What you will learn"
├── 2.4.2. Pivot points → item in "What you will learn"
├── 2.4.3. Harmonic patterns → item in "What you will learn"
└── 2.4.4. Wyckoff metodologie (Wyckoff Method) → item in "What you will learn"
```

Podtemata (2.4.1.1.–2.4.1.5., 2.4.3.1.–2.4.3.4., 2.4.4.1.–2.4.4.3.) are ignored at Lekce level — they belong to chapter articles.

### Internal Linking Targets (from Content Inventory)

- 2.3. Svíčkové formace (Candlestick Formations) — prior lesson, smaller single-candle/cluster patterns
- 2.2. Základní price action (Price Action Basics) — foundation (support/resistance, trend)
- 2.5. Indikátory a oscilátory (Indicators and Oscillators) — next lesson
- 2.6. Fibonacci a Elliottovy vlny (Fibonacci and Elliott Waves) — related pattern-based framework
- Chapter articles under 2.4. will be linked once their slugs are defined

---

## Step 1 — Competitor Research + Keyword Discovery

**Branch:** DataForSEO (DFS) — Ahrefs MCP unavailable (OAuth required). DR score replaced by qualitative domain-ETV proxy; URL-level organic traffic not available on DFS branch.

**Scope (simplified for Lekce):**
- 2 WebSearch queries, 8 unique candidate URLs after dedup + filter (PDFs, off-topic removed)
- 3 competitor pages successfully fetched (minimum met)
- 1 DFS keyword suggestion call on main seed "chart patterns"
- Domain-level ETV collected for 6 candidate domains

**Fetches:**
| # | Domain | Status | Notes |
|---|--------|--------|-------|
| 1 | ig.com | 403 | Blocked — not fetched |
| 2 | forex.com | 403 | Blocked — not fetched |
| 3 | vtmarkets.com | fetched | ~4,500 words, comprehensive overview |
| 4 | oanda.com | fetched | ~3,000 words, conceptual guide |
| 5 | elearnmarkets.com | fetched | ~8,500 words, detailed formation catalogue |
| 6 | schwab.com | 403 | Auth error page — not real content |

**Keywords:** 12 trading-relevant keywords retained (off-topic results like curl/hair, knitting, crochet, lug patterns filtered out). Main seed "chart patterns" = 6,600 SV, KD 27. Formation-specific keywords (head & shoulders, double top/bottom) flagged as chapter-level — will be used by chapter articles, not by this Lekce overview.

### Content Gap Summary

- **None of the three fetched competitors cover all four pattern-based frameworks** that lesson 2.4. bundles together. Every fetched article covers price formations (head & shoulders, double tops, triangles, flags, cup and handle); none cover harmonic patterns, pivot points, or Wyckoff methodology. This is a strong differentiation angle for the Lekce overview.
- Competitors treat "chart patterns" as synonymous with classical price formations. FTMO Academy's lesson broadens the scope to four analytical lenses: price formations (2.4.1), pivot points (2.4.2), harmonic patterns (2.4.3), Wyckoff methodology (2.4.4). The overview article's job is to map the territory.
- Market psychology and self-fulfilling prophecy are common framing across competitors — this belongs in the Lekce intro.
- Volume confirmation and breakout discipline come up in every source as the most commonly missed step. Worth mentioning in the overview.
- Reliability / statistical performance is rarely quantified. FTMO Academy can acknowledge honest uncertainty (different traders use different frameworks) without pretending patterns are deterministic.

### xlsx output

`/Users/admin/Projects/ftmo-academy/data/output/lessons/chart-patterns/chart-patterns_step1.xlsx`

- Sheet "URLs": 8 rows (3 fetched, 3 blocked, 2 skipped)
- Sheet "Keywords": 12 rows — Status + Notes columns left empty for user review

---

## Step 2 — Brief & Outline

**Classification:** BEGINNER — overview/teaser, assumes only lessons 2.1–2.3 as prerequisites
**Word count target:** 500–650 words (Lekce band 400–700)

**Structure:**
- H1: Chart Patterns
- Intro: 2–3 short paragraphs (AIO-friendly opening definition)
- H2: What You Will Learn in This Lesson — bullet per chapter (2.4.1–2.4.4)
- H2: Why Chart Patterns Matter for Traders — benefit framing
- Closing: forward-moving CTA to first chapter

**Callouts:** 1 × Keep in Mind (TA bias framing) — Lekce limit.
**Tables:** none — Lekce is too short.
**Internal links:** 7 planned, 5 point to chapters under 2.4. (placeholders until chapter slugs exist).

**Keyword placement:**
| # | Keyword | Volume | Heading |
|---|---------|--------|---------|
| 1 | chart patterns | 6,600 | H1 |
| 2 | chart patterns trading | 1,600 | Body |
| 3 | trading chart patterns | 1,600 | Body |

Formation-specific keywords (head and shoulders, double top/bottom) deliberately left for chapter 2.4.1.

**Content validation:** PASS
- Lekce skeleton followed exactly
- All four chapters from the Google Sheet structure tree represented
- Podtemata correctly excluded
- Honest framing about method variety present (no false certainty)

**Output files:**
- `/Users/admin/Projects/ftmo-academy/data/output/lessons/chart-patterns/lesson_chart-patterns_EN_outline.md`
- `/Users/admin/Projects/ftmo-academy/data/output/lessons/chart-patterns/lesson_chart-patterns_EN_outline.docx`

---
