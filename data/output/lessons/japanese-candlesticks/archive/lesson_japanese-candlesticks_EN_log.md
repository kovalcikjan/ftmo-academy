# Japanese Candlestick Patterns - Edit Log (V3)

**Article:** `lesson_japanese-candlesticks_EN_V3.md`
**Source:** https://academy.ftmo.com/lesson/japanese-candlesticks/
**Base:** `lesson_japanese-candlesticks_EN_V2.md`
**Date:** 2026-03-05

---

## Step 1 Log: Keywords

**Keywords file:** `japanese-candlesticks_keywords.xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | "There are hundreds of different candlestick patterns — you do not need to know all of them." | "There are hundreds of different candlestick chart patterns — you do not need to know all of them." | candlestick chart | 3500 | Intro | DONE |
| 2 | "This lesson covers the most common types of candlesticks you should know." | "This lesson covers the most common types of candlesticks used in candlestick trading." | candlestick trading | 800 | Intro | DONE |
| 3 | "Japanese candlesticks are among the most widely used tools in technical analysis." | "Japanese candlestick patterns are among the most widely used tools in technical analysis." | japanese candlestick patterns | 300 | H2 body | DONE |
| 4 | "The key advantages of candlestick patterns are simplicity and informational value." | "The key advantages of candlestick analysis are simplicity and informational value." | candlestick analysis | 100 | H2 body | DONE |
| 5 | "traders learn how to read candlesticks" already present in V2 | unchanged | how to read candlesticks | 1500 | H2 body | DONE |
| 6 | (no intro sentence before Two-candle H3s) | Added: "Engulfing candlestick patterns are the most common two-candle reversal signals in price action trading." | engulfing candlestick patterns | 50 | H2 intro | DONE |
| 7 | "Indecision patterns (doji, spinning top) carry the most weight at key support and resistance levels." | "Reversal candlestick patterns — especially doji and spinning top — carry the most weight at key support and resistance levels." | reversal candlestick patterns | 900 | Key Takeaways | DONE |
| 8 | hammer candlestick | — | hammer candlestick | 5800 | — | SKIP |
| 9 | bullish hammer | — | bullish hammer | 600 | — | SKIP |
| 10 | falling three methods | — | falling three methods | 150 | — | SKIP |

---

## Step 2 Log: ToV Rewrite

**Guide:** `ftmo_academy_tov_guide_EN.md`
**Topic classification:** BEGINNER

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "After a brief familiarization, traders learn how to read candlesticks and quickly determine what is happening in the market — whether buyers or sellers are in control, and whether a trend is likely to continue or reverse." | "Traders learn how to read candlesticks quickly — identifying whether buyers or sellers are in control, and whether a trend is likely to continue or reverse." | ToV: "After a brief familiarization" = academic preamble; "determine what is happening in the market" → specifics already follow in the dash clause |
| 2 | "A typical example can be seen in the candlestick chart below." | "The patterns covered in this lesson illustrate this directly." | ToV: passive "can be seen"; dangling "below" (no image in this section) |
| 3 | "The long day bullish candlestick consists of one candle with a long body and short wicks." | "The long day bullish candlestick has a long body with short wicks." | ToV: "consists of one candle with" redundant in single-candle section; tighter active construction |
| 4 | "It signals strength and is often seen as a breakout candle at the beginning of a trend." | "It signals market strength — often appearing as a breakout candle at the start of a new trend." | ToV: "is often seen as" passive → active participial; "at the beginning of" → "at the start of" (concise) |
| 5 | "There are two situations where you can make a trading decision with a bullish marubozu candlestick:" | "A bullish marubozu provides two clear trading signals:" | ToV: existential "There are... situations where you can" → direct active construction |
| 6 | "The short day candlestick indicates that price stayed within a range during the trading period, suggesting an expansion may follow." | "The short day candlestick indicates that price stayed within a range, with expansion likely to follow." | ToV: "during the trading period" redundant (candle = trading period); "suggesting... may" → "likely to" (confidence level 4) |
| 7 | "Compared to a regular doji, it is more dramatic — with long upper and lower wicks extending significantly in both directions." | "Compared to a regular doji, it is more pronounced — with upper and lower wicks extending well beyond the body in both directions." | ToV: "dramatic" subjective/casual → "pronounced" precise; "significantly" vague → "well beyond the body" specific |
| 8 | "Like the spinning top, it signals indecision and a possible reversal." | "Like the spinning top, it signals indecision and a potential reversal." | ToV: "possible" = weak hedging → "potential" standard professional framing |
| 9 | "The **bullish engulfing** is the first two-candle pattern in this lesson. It forms with a small bearish candle on the left and a larger bullish candle on the right." | "The **bullish engulfing** forms with a small bearish candle on the left and a larger bullish candle on the right." | ToV: "is the first two-candle pattern in this lesson" = lesson-meta reference, redundant after Step 1 intro sentence; two sentences merged |

---

## Step 3 Log: Structure & Formatting

**Paragraph audit:** All paragraphs under 100 words — no splits required.

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Prerequisites added | Blockquote after ToC: Introduction to Trading + Trader's Dictionary | Structure Guide: prerequisites always stated; BEGINNER lesson requires learning path context |
| 2 | Table repositioned | Pattern summary table moved from after Key Takeaways → before Key Takeaways | Structure: reference summary precedes takeaways (inverted pyramid at section level) |
| 3 | Internal link added | "uptrend" → /lesson/market-environment-range-vs-trend/ in Bullish marubozu section | Structure Guide: min. 3–5 internal links; brings total to 4 unique links |
| 4 | Author box updated | "Published: 2023-03-01" added alongside Last Updated | E-E-A-T: Trustworthiness — content freshness signals require both publish and update dates |

---

## Step 4 Log: HTML Conversion

| # | Change Type | Description |
|---|-------------|-------------|
| 1 | Template | v2_balanced applied |
| 2 | ToC | Styled block: #f5f5f7 bg, #123a83 text, nested H2-level |
| 3 | Prerequisites | Removed (CMS handles — markdown only) |
| 4 | Callouts | Warning (#fff8e1 + orange border), Tip (#e8f4fd + blue border), Keep in Mind (#f0f4e8 + olive border) |
| 5 | Table | #123a83 header, striped rows |
| 6 | Images | All 18 images at original positions with descriptive alt text |
| 7 | Author box | Published + Last Updated dates |
| 8 | Disclaimers | Educational Notice (gray bg) + Risk Warning (yellow bg, orange border) |
| 9 | Typo fix | Bearish engulfing: "small bullish candle on the right" → "on the left" |
| 10 | Branding | Poppins font, #0781fe / #123a83 / #c6c6c6, max-width 1160px, responsive |

---

## Step 5 Log: QA Review

**Date:** 2026-03-05
**Score:** 8/10

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | ToV fix | H2 opener: "**Japanese candlestick patterns** are among the most widely used tools in technical analysis. Candlestick pattern analysis originated in 18th-century Japan at the rice exchange..." → "**Japanese candlestick patterns** originated in 18th-century Japan at the rice exchange — the earliest known form of technical trading." | QA: "most widely used" repeated from intro paragraph (4 lines apart) |
| 2 | Content added | Added anatomy explanation (2 paragraphs) after candlestick anatomy image: body/wicks/open/close + bullish/bearish candle definitions | QA: critical BEGINNER gap — image existed but no text explanation of anatomy |
| 3 | ToV fix | "Always evaluate it within a larger context, considering what buyers and sellers are attempting to achieve." → "Always evaluate it within the surrounding price action — what it reveals about buyer and seller strength." | QA: "what buyers and sellers are attempting to achieve" is vague/subjective; anchored to observable evidence |
| 4 | Callout removed | Tip callout after Bearish marubozu converted to body text: "After identifying a marubozu candle, wait for confirmation from additional patterns, [support and resistance](/lesson/support-and-resistance/) levels, or indicators before entering a trade." | QA: 3 callouts for ~820-word article exceeds spec (1-2 for <1000 words); Tip was weakest |
| 5 | HTML fix | Title tag expanded: "Japanese Candlestick Patterns \| FTMO Academy" (46 chars) → "Japanese Candlestick Patterns: Complete Guide \| FTMO Academy" (58 chars) | QA: title below 50-60 char spec |

**Remaining (requires FTMO team):**
- Author attribution: replace "FTMO Academy" with named author + credentials

---

## Summary

| Step | Status | Changes |
|------|--------|---------|
| Step 1: Keywords | DONE | 7 applied, 3 skipped (hammer/bullish hammer/falling three methods — not in original article) |
| Step 2: ToV Rewrite | DONE | 9 sentence changes; classification: BEGINNER |
| Step 3: Structure | DONE | 4 structural changes; paragraph audit: all clear |
| Step 4: HTML | DONE | v2_balanced template; 18 images; 4 internal links |
| Step 5: QA | DONE | 5 fixes applied; 1 remaining (named author — requires FTMO team) |
