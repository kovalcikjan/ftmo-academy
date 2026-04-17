# Write Log: Candlestick Patterns (Lekce 2.3.)

**Slug:** candlestick-patterns
**Lokace:** 2.3.
**Level:** Lekce (overview article — 400–700 words)
**Date:** 2026-04-17
**Workflow version:** 3.4

---

## INIT

| Item | Value |
|------|-------|
| Lokace | 2.3. |
| Lesson name (EN) | Candlestick Patterns |
| Lesson name (CZ) | Svíčkové formace |
| Level | Lekce (short overview article) |
| Target word count | 400–700 words |
| Inventory position | Part 2: Trading Analysis > 2.3. Svíčkové formace |
| Chapters under this Lekce | 1 chapter (2.3.1. Candlestick patterns/formations) |
| Subtopics under 2.3.1. | 13 (Doji, Hammer, Hanging Man, Engulfing, Shooting Star, Evening Star, Morning Star, Harami, Tweezer Top/Bottom, Marubozu, Spinning Top, Three White Soldiers, Inside Bar — plus "Interpretace svíček v kontextu trendu") |
| Internal linking targets | 2.1.1. Types of Trading Charts, 2.1.2. Candlestick Anatomy (OHLC), 2.3.1. Candlestick Patterns (chapter), individual pattern pages |
| Keywords source | Ahrefs MCP (Step 1) — reduced scope for Lekce |
| Existing versions found | None |

### Lesson Structure Tree (from Google Sheet)

```
2.3. Candlestick patterns (Lekce) — THIS ARTICLE
└── 2.3.1. Candlestick patterns/formations (Kapitola)
    ├── 2.3.1.1. Doji (Dragonfly, Gravestone)
    ├── 2.3.1.2. Hammer
    ├── 2.3.1.3. Hanging Man
    ├── 2.3.1.4. Engulfing
    ├── 2.3.1.5. Shooting Star
    ├── 2.3.1.6. Evening Star
    ├── 2.3.1.7. Morning Star
    ├── 2.3.1.8. Harami (bullish/bearish)
    ├── 2.3.1.9. Tweezer Top/Bottom
    ├── 2.3.1.9. Interpretace svíček v kontextu trendu (duplicate numbering in sheet)
    ├── 2.3.1.10. Marubozu
    ├── 2.3.1.11. Spinning Top
    ├── 2.3.1.12. Three White Soldiers
    └── 2.3.1.13. Inside Bar
```

### Structural Note

This Lekce contains only ONE Kapitola (2.3.1.). The standard Lekce template assumes multiple chapters to introduce. For this lesson, the "What you will learn" section will focus on the chapter (2.3.1. Candlestick Patterns) and reference the individual pattern categories (reversal vs. continuation, single-candle vs. multi-candle) that will be covered inside the chapter.

---

## Step 1 — Competitor Research + Keyword Discovery

**Provider:** Ahrefs MCP unavailable — fell back to DataForSEO MCP. DR score replaced by qualitative ETV-based proxy; organic traffic is domain-level only.

**Scope:** Reduced Lekce scope — 2 WebSearch queries, 3 successful competitor fetches, 1 keyword_suggestions call, max 10–12 keywords.

### Krok 1 — Seed Validation

Main seed confirmed: `candlestick patterns`. All searched sources use this exact phrasing; categorisations use "reversal / continuation / indecision" or "bullish / bearish / continuation" frameworks consistently.

### Krok 2 — WebSearch

- Query 1: `"candlestick patterns" explained trading guide` → 10 URLs
- Query 2: `types of candlestick patterns for traders` → 10 URLs
- After dedup + filter: 8 unique high-signal candidate URLs retained

### Krok 3B — DFS domain_rank_overview

ETV-based DR proxy applied. ig.com + britannica.com = very high; forex.com + stockcharts.com = high; strike.money, morpher.com, quantinsti.com, tradenation.com = medium.

### Krok 4 — Fetches

3 fetched successfully (britannica.com, morpher.com, quantinsti.com, tradenation.com — note: 4 fetches completed after retries; 2 blocked with 403: ig.com, forex.com). Minimum of 3 met.

### Krok 5B — DFS keyword_suggestions

1 call, seed `candlestick patterns`, limit 50, volume ≥ 100. Response auto-saved (92 KB), parsed with Python.

### Krok 6 — Merge / Filter / Cluster

Dynamic cutoff = 20 (main KW > 500). After dedup and filtering PDF / stock-specific / strong-variant noise, final set = 12 keywords across 7 clusters (main, bullish, bearish, reversal, trading, resource, specific patterns for internal linking).

### Content Gap Summary (Lekce angle)

- Competitor Lekce-style pages are rare — most URLs are deep dives (3,500–9,000 words) listing every pattern. Academy's Lekce can differentiate as a concise, navigational overview (400–700 words) that routes readers to in-depth chapter + pattern pages.
- Three competing categorisations exist: (a) reversal / continuation / indecision (IG, britannica), (b) bullish / bearish / continuation (tradenation), (c) bullish / bearish only (morpher). The Lekce should pick one explicitly and stick with it.
- Morpher and quantinsti cover drawbacks / limitations explicitly — Academy's "Keep in Mind" callout can do this in one line, aligning with the ToV "realistic educator" principle.
- Context-sensitivity is undersold elsewhere: same candle has different meaning based on trend placement (britannica). This is a natural Academy angle for the overview.
- Almost no competitor links out to structured follow-up lessons — Academy's routing "what you'll learn next" section is a genuine differentiator.

---

## Step 2 — Brief & Outline

**Classification:** BEGINNER
**Target word count:** 400–700 words (Lekce band)
**Category framework chosen:** reversal / continuation / indecision (bullish/bearish treated as an attribute inside each category)
**Internal links planned:** 4 structural + 12 pattern-level links (one per bulleted pattern in "What you will learn")
**Structural adaptation:** Lokace 2.3. has only one Kapitola (2.3.1.). "What you will learn" items are pattern *categories* (not chapters), each routing to 2.3.1. and individual 2.3.1.x pattern pages. This preserves the Lekce-as-map role without inventing chapters that do not exist.

**Content validation:** PASS — structure, scope, and keyword placement reviewed as trading educator; no issues flagged.

