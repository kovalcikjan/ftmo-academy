# Edit Log: Types of Trading Charts (v11)

**Source:** https://academy.ftmo.com/lesson/types-of-trading-charts/
**Base:** v10
**Date:** 2026-04-10
**Version:** v11

---

## Step 1 Log: Keywords

**Keywords file:** `data/output/keywords/types-of-trading-charts_keywords.xlsx`

### Applied Changes

| # | Original sentence (full) | New sentence (full) | Keyword | Volume | Position | Status |
|---|--------------------------|---------------------|---------|--------|----------|--------|
| 1 | "More advanced formats such as a **footprint chart** or **market profile** display volume at each price level, giving traders insight into where the most activity occurs." | "More advanced formats such as a **footprint chart**, **order flow chart**, or **market profile** display volume at each price level, giving traders insight into where the most activity occurs." | order flow chart | 250 | Body (Other Chart Types) | DONE |

### Already Present in v10 (no change needed)

| # | Keyword | Volume | Location in v10 | Status |
|---|---------|--------|-----------------|--------|
| 1 | heikin ashi | 2000 | H2 heading + body (multiple) | DONE |
| 2 | heikin ashi candles | 1400 | H2 heading "Heikin Ashi Candles" + body | DONE |
| 3 | candlestick charts | 1000 | H2 heading + intro + body (multiple) | DONE |
| 4 | tick chart | 700 | Body (line 36) | DONE |
| 5 | footprint chart | 700 | Body "Other Chart Types" (line 74) | DONE |
| 6 | market profile | 500 | Body "Other Chart Types" (line 74) | DONE |
| 7 | renko charts | 400 | H2 heading + body (multiple) | DONE |
| 8 | point and figure chart | 400 | Body "Other Chart Types" (line 72) | DONE |
| 9 | heikin ashi strategy | 250 | Body (line 66) | DONE |
| 10 | heikin-ashi | 250 | Covered by "Heikin Ashi" variant | DONE |
| 11 | japanese candlesticks | 200 | Body (lines 11, 50) + internal link | DONE |
| 12 | renko chart | 200 | Body (line 57) | DONE |
| 13 | heikin ashi candle formula | 150 | Body (line 62) | DONE |
| 14 | what is heikin ashi | 150 | Body question format (line 62) | DONE |
| 15 | tick charts | 100 | Body (line 34) + Key Takeaways | DONE |
| 16 | range charts | 100 | Body (lines 34, 40) + Key Takeaways | DONE |
| 17 | kagi chart | 90 | Body "Other Chart Types" (line 73) | DONE |
| 18 | ohlc charts | 40 | Body (line 50) | DONE |
| 19 | line break chart | 40 | Body "Other Chart Types" (line 73) | DONE |
| 20 | reading candlestick charts | 50 | Body (line 50) | DONE |

### Skipped (no natural placement without new content)

| # | Keyword | Volume | Reason | Status |
|---|---------|--------|--------|--------|
| 1 | heikin ashi candles explained | 250 | Would require restructuring H2 opening; "What is Heikin Ashi?" already serves same intent | SKIP |
| 2 | renko chart patterns | 200 | Article does not discuss specific Renko patterns; adding would introduce new content | SKIP |
| 3 | heikin ashi vs candles | 200 | No natural comparison paragraph exists; would need new section | SKIP |
| 4 | renko chart strategy | 150 | No strategy discussion in article; would need new content | SKIP |
| 5 | heikin ashi candle patterns | 150 | Article does not cover HA patterns specifically | SKIP |
| 6 | how to read heikin ashi candles | 150 | Would need new instructional paragraph | SKIP |
| 7 | renko chart free | 90 | Not relevant for educational content | SKIP |
| 8 | what is renko chart | 80 | Already answered by Renko section opening | SKIP |
| 9 | hollow candlestick | 50 | Niche variant not covered in article scope | SKIP |
| 10 | renko chart trading strategy | 50 | Same as "renko chart strategy" | SKIP |
| 11 | renko chart patterns pdf | 50 | Not relevant (PDF format reference) | SKIP |
| 12 | best renko chart settings | 40 | Would need new instructional content | SKIP |
| 13 | renko chart formula | 30 | Would need new technical content | SKIP |
| 14 | how renko chart works | 20 | Already explained in Renko body text | SKIP |

---

## Step 2 Log: ToV Rewrite

**Topic classification:** BEGINNER (Part 2.1.1., basic charting)

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "[Japanese Candlesticks](/lesson/japanese-candlesticks/) are covered in the previous lesson." | "The previous lesson covers [Japanese Candlesticks](/lesson/japanese-candlesticks/)." | ToV: passive → active voice |
| 2 | "Wicks represent the highest and lowest points where the market traded." | "Wicks represent the highest and lowest prices reached during the period." | ToV: "points where the market traded" vague → "prices reached during the period" precise |
| 3 | "The image below shows two candlestick charts next to each other in the FTMO cTrader platform." | "The image below shows two candlestick charts next to each other in the cTrader platform." | Content focus: reduce FTMO brand mentions; cTrader is sufficient context |
| 4 | "the [candlestick patterns](/lesson/chart-patterns-trading/) on your chart may carry less relevance since fewer traders observe them." | "the [candlestick patterns](/lesson/chart-patterns-trading/) on your chart may carry less weight since fewer traders observe them." | ToV: "carry less relevance" non-standard English → "carry less weight" natural phrasing |
| 5 | "Traders can use **tick charts** and **range charts** in the FTMO cTrader platform." | "Traders can use **tick charts** and **range charts** in the cTrader platform." | Content focus: reduce FTMO brand mentions |
| 6 | "This means every bar has the same bar range and closes either at high or low." | "This means every bar covers the same price range and closes at either its high or its low." | ToV: "bar range" redundant with "range bar" → "price range" clearer; added "its" for precision |
| 7 | "Both the uptrend and downtrend appear cleaner on the range chart once the time factor is eliminated and the focus shifts to price rotations." | "Both the uptrend and downtrend appear cleaner on the range chart once you remove the time factor and focus on price rotations." | ToV: passive "is eliminated... shifts" → active "you remove... focus"; direct reader address |
| 8 | "**Bar charts**, often called **OHLC charts**, are represented as vertical bars with two notches that mark the open and close of the bar." | "**Bar charts**, often called **OHLC charts**, use vertical bars with two notches to mark the open and close of each bar." | ToV: passive "are represented as" → active "use"; "the bar" → "each bar" for precision |
| 9 | "bar charts are less intuitive for new traders reading candlestick charts." | "bar charts are less intuitive for new traders used to reading candlestick charts." | ToV: original ambiguous (reading what on bar charts?) → "used to reading" clarifies meaning |
| 10 | "The **Heikin Ashi candle formula** constructs candles the same way as a standard candlestick chart but applies a different calculation method." | "The **Heikin Ashi candle formula** uses the same visual structure as a standard candlestick chart but applies a different calculation method." | ToV: "constructs the same way" contradicts "different method" → "same visual structure" clarifies what is shared vs different |
| 11 | "Heikin Ashi candles filter out price movements and provide a smoother approach to trend following." | "Heikin Ashi candles smooth out price movements and provide a clearer approach to trend following." | ToV: "filter out" imprecise (HA does not remove data, it averages) → "smooth out" accurate; "smoother" → "clearer" avoids repetition with "smooth" |

---

## Step 3 Log: Structure & Formatting

### Phase 0: Paragraph Audit
All paragraphs within 40-100 word range. No splits required.

### Changes

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Bold audit | Line 11: 5 bold keyword fragments (**Candlestick charts**, **body**, **wick**, **bullish candlestick**, **bearish candlestick**) → 1 scanning anchor phrase (**Candlestick charts are the most popular format for technical analysis.**) + italic for term introductions (*body*, *wick*, *bullish candlestick*, *bearish candlestick*) | Bold rules: scanning anchors only, not single keywords; italic for term introductions |
| 2 | Image caption | Added caption above image 1: *Candlestick anatomy: body, wick, bullish vs bearish candle* | Image spacing: captions improve DOCX readability |
| 3 | Image caption + context | Added caption above image 2: *Two candlestick charts: time-based (left) vs non-time-based (right)*; moved image context into preceding paragraph | Image spacing + reduce standalone image reference paragraph |
| 4 | Paragraph merged | Lines 15+19: Merged image reference paragraph ("The image below shows...") with chart periodicity paragraph. Removed redundant "Although they look the same..." (now stated in caption + preceding text). | Structure: reduce thin paragraphs; image context folded into caption |
| 5 | Bold audit | Line 34: **tick charts** and **range charts** → *tick charts* and *range charts* (italic); **These are the two most popular non-time-based formats.** (scanning anchor) | Bold rules: term introductions → italic; one scanning anchor per paragraph |
| 6 | Bold audit | Line 36: **tick chart** → *tick chart*; Line 38: **range bar** → *range bar* | Bold rules: term introductions → italic |
| 7 | Image caption | Added caption above image 3: *Bar chart (OHLC): vertical bars with open and close notches* | Image spacing |
| 8 | Bold audit | Line 50: **Bar charts** → *Bar charts*; **OHLC charts** → *OHLC charts* | Bold rules: term introductions → italic |
| 9 | Bold + restructure | Line 54: **Renko charts** fragment → **Renko charts eliminate the time factor from trading entirely.** (scanning anchor phrase); sentence reordered for emphasis | Bold rules: keyword fragment → scanning anchor |
| 10 | Image caption | Added caption above image 4: *Renko chart: price bricks without a time axis* | Image spacing |
| 11 | Bold audit | Line 62: **Heikin Ashi candle formula** → *Heikin Ashi candle formula*; kept **What is Heikin Ashi?** as question lead | Bold rules: term intro → italic |
| 12 | Image caption | Added caption above image 5: *Heikin Ashi chart: smoothed candles for trend following* | Image spacing |
| 13 | Callout type | Warning → Keep in Mind; reworded: "A common mistake is switching chart formats looking for an edge." → "Switching chart formats does not create an edge. Every chart type displays the same underlying price data." | Structure Guide: TA lessons require 1 Keep in Mind callout for cognitive biases/limitations |
| 14 | Date updated | Last Updated: 2026-04-01 → 2026-04-10 | E-E-A-T: freshness signal |
