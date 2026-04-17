# Lesson Brief & Outline: Candlestick Anatomy (OHLC)

## Brief

| Item | Value |
|------|-------|
| Topic | Candlestick Anatomy (OHLC) |
| Czech Title | Anatomie svíčky (OHLC) |
| Slug | candlestick-anatomy-ohlc |
| Lokace | 2.1.2. |
| Part | Part 2 — Trading Analysis |
| Module | 2.1. Graf a timeframe |
| Position | Kapitola 2 of 5 in the lesson (free structure — no sub-topics in Google Sheet) |
| Classification | BEGINNER — foundational TA lesson, assumes no prior knowledge; Part 2 early chapter |
| Word Count | 1,500–1,800 words — tighter than competitor average (2,200–5,500) by design: pure anatomy scope, patterns deferred to 2.3.1. |

---

## Differentiation

- **Strict anatomy-only scope.** Unlike Capital.com, Dukascopy, ChartSchool, and Pepperstone — which collapse anatomy and pattern recognition into a single sprawling article — this lesson stays focused on OHLC, body, and wicks. Patterns (Doji, Hammer, Engulfing, etc.) are deferred to Lesson 2.3.1.
- **OHLC as a data abstraction, not a bullet list.** Most competitors mention Open/High/Low/Close as four items. We frame OHLC as the underlying data model that a candlestick renders visually — the conceptual anchor of the lesson.
- **Explicit "what a candle does NOT tell you" section.** Only StockCharts ChartSchool does this honestly; we make it a standalone section with a Keep-in-Mind callout about TA interpretation bias.
- **Candlestick vs. OHLC bar chart comparison.** Short comparison table showing why candles became the retail default. Rarely done cleanly in competitor content.
- **Timeframe-awareness signposted forward.** We introduce the idea that a candle is meaningless without its timeframe context, then explicitly link forward to Lesson 2.1.3. on timeframe selection — instead of trying to cover it here.

**Topics deliberately excluded:**
- Specific candlestick patterns (doji, hammer, engulfing, marubozu, shooting star, etc.) — covered in 2.3.1.
- Pattern trading strategies or entry/exit rules — out of scope for anatomy.
- Timeframe selection guidance — mentioned only as a bridge to 2.1.3.
- Heikin-Ashi, Renko, or other derived chart types — out of scope (these are chart types, not candle anatomy).

---

## Keywords — Headings

Top 5 keywords by volume mapped to H1/H2. Remaining keywords integrate naturally into body text in Step 3.

| # | Keyword | Volume | Heading assignment |
|---|---------|--------|--------------------|
| 1 | candlestick anatomy | 260 | H1 (primary match for lesson title) |
| 2 | how to read a candlestick chart | 2,400 | H2 — "How to Read a Single Candle" |
| 3 | ohlc candlestick / ohlc vs candlestick | 20 each | H2 — "The Four OHLC Data Points" + "Candlestick vs. OHLC Bar" |
| 4 | candlestick chart | 8,100 | Body text (too broad for heading; covered in intro) |
| 5 | candlestick chart explained | 390 | Body text (intro) |
| — | remaining 19 keywords | — | Step 3 (body integration) |

**Note:** "candlestick types" (SV 2,400) is deliberately NOT used as a heading — in beginner search intent, "types" usually means patterns (Doji, Hammer, etc.), which are out of scope for this lesson.

---

## Outline

# Candlestick Anatomy: Understanding OHLC, Body, and Wicks (H1)

**Key point (reader takeaway):** A candlestick is a visual rendering of four data points — open, high, low, close — over a fixed time interval. By the end of this lesson, you can break any candle into its anatomy and read what the price did during that period.

Intro paragraph (150 words max):
- Hook: every chart in your trading platform is a wall of these shapes — reading them starts with anatomy
- Establish that a candle = OHLC made visible; a chart = a sequence of candles over time
- What this lesson covers (anatomy only) and what comes next (patterns in 2.3.1, timeframes in 2.1.3)

---

## What a Candlestick Represents (H2)

Target keyword: candlestick chart (body integration)

Key points:
- A single candlestick represents price action across one fixed time interval (1 minute, 1 hour, 1 day — whatever the chart is set to)
- Each candle packs four data points (open, high, low, close) into one shape
- Candlestick charts originated in 18th-century Japan (Munehisa Homma, rice markets); they displaced OHLC bar charts as the retail default in the 1990s
- Brief historical note kept to 1–2 sentences — this is not a history lesson

Transition: Before looking at the shape, understand the data it is encoding.

---

## The Four OHLC Data Points (H2)

Target keyword: ohlc candlestick / ohlc vs candlestick (body mentions)

Key points:
- OHLC is the data model every candle renders: Open, High, Low, Close
- Each point corresponds to a specific moment or extreme within the interval
- These four values are what trading platforms store for every bar in the database

Table:

| Data point | Definition | Where it sits on the candle |
|------------|-----------|----------------------------|
| Open | Price at the start of the interval | Top or bottom of the body (depends on direction) |
| High | Highest price traded during the interval | Top of the upper wick |
| Low | Lowest price traded during the interval | Bottom of the lower wick |
| Close | Price at the end of the interval | Opposite end of the body from open |

[IMAGE: labelled diagram of a bullish candle showing open, high, low, close positions; same diagram for a bearish candle]

Callout (Note): OHLC is the data. The candle is one way to visualise it. You can render the same four numbers as a bar, a line, or a candle — candles won because the coloured body makes direction readable at a glance.

---

## Body and Wicks: The Visual Anatomy (H2)

Target keyword: candlestick anatomy (primary)

Key points:
- Body = the thick rectangle between open and close (the net move for the interval)
- Wicks (also called shadows or tails) = thin lines extending above and below the body, reaching the high and low
- Upper wick = distance from body top to the high
- Lower wick = distance from body bottom to the low
- A candle with no wicks (marubozu) means open/close equalled high/low — rare and signals decisive action
- A candle with no body (open = close) is a doji — indecision

**Important:** avoid naming specific patterns here. Mention marubozu and doji only as "edge cases of the anatomy" — the full pattern treatment belongs in 2.3.1.

[IMAGE: annotated candle diagram showing body, upper wick, lower wick with labels]

---

## Bullish vs. Bearish Candles (H2)

Target keyword: (body integration — "bullish candle", "bearish candle")

Key points:
- Green / hollow / white body = close above open (buyers won the interval) → bullish candle
- Red / filled / black body = close below open (sellers won the interval) → bearish candle
- Colour is a platform convention, not a universal standard — always check what your chart is set to
- The relationship between open and close determines direction; the body colour is just a visual shortcut

Callout (Tip): Most platforms let you customise candle colours. If you cannot immediately tell direction on a new chart, check the colour settings before reading the market.

---

## How to Read a Single Candle (H2)

Target keyword: how to read a candlestick chart (H2 match)

Key points:
- Body size tells you conviction: long body = strong directional pressure; small body = balance / indecision
- Wick length tells you rejection: long upper wick = price pushed up then got pushed back down; long lower wick = price pushed down then bought back up
- The body-to-wick ratio is the fastest sentiment read
- No single candle is a signal on its own — it is one data point in a sequence

Table (quick-read guide):

| Candle shape | What it suggests |
|-------------|-----------------|
| Long body, small wicks | Strong directional move, conviction |
| Small body, long wicks on both sides | Indecision, buyers and sellers balanced |
| Small body, long upper wick | Sellers rejected higher prices |
| Small body, long lower wick | Buyers rejected lower prices |
| No body (open ≈ close) | Market undecided |

Callout (Keep in Mind): One common mistake is to read a single candle as a trade signal. A candle is a summary of one interval; its meaning changes depending on where it sits in the broader trend and which timeframe you are looking at. Context decides the interpretation, not the candle shape alone.

---

## Candlestick vs. OHLC Bar Chart (H2)

Target keyword: ohlc vs candlestick

Key points:
- The OHLC bar chart is the older visualisation of the same four data points — a vertical line (high to low) with two short horizontal ticks (open on the left, close on the right)
- Both display identical information
- Candles replaced bars as the retail standard because the coloured body makes direction readable without comparing two ticks
- Bars are still used where visual density matters (institutional charts, long-term monthly/yearly views)

Table:

| Feature | OHLC Bar | Candlestick |
|---------|----------|-------------|
| Data encoded | OHLC | OHLC |
| Direction indicator | Open/close tick position | Body colour |
| Readability at glance | Slower (compare ticks) | Faster (colour + body) |
| Visual density on a chart | Higher (thinner) | Lower (wider bodies) |
| Common use | Institutional, long-term | Retail, short-to-mid term |

---

## What a Candle Does NOT Tell You (H2)

Key points (honesty about limitations — required for TA lesson per Structure Guide):
- No information about the **order** of events within the interval — you see the high and low but not whether the high came before the low
- No **volume** data by default — candles show price only
- The candle is **timeframe-dependent** — the same visual shape means different things on a 1-minute chart versus a 1-day chart
- Interpretation relies on context (trend, support/resistance, broader market conditions) — the shape alone is not a signal

Callout (Keep in Mind): Technical analysis tends to make traders see patterns where none exist. A single candle is a compressed summary of many trades; it does not predict the next move. Treat candle readings as one input among several, not as standalone signals.

---

## Next Steps in Your Technical Analysis Learning (H2)

Key points:
- Anatomy is the foundation; everything else in chart analysis builds on it
- The next logical steps: learn how to choose a timeframe (so your candle reads match your trading style), and then learn specific multi-candle patterns

Internal links summary list:
- Chart types (line, bar, candle) — 2.1.1.1.
- Choosing timeframes — 2.1.3.
- Candlestick patterns — 2.3.1.
- Support and resistance — 2.2.1.

---

## Internal Links Plan

| # | Link Text | Target Lesson | Slug | Placement |
|---|-----------|---------------|------|-----------|
| 1 | types of trading charts | 2.1.1.1. Types of Trading Charts | types-of-trading-charts | Intro or "Candlestick vs. OHLC Bar" section |
| 2 | choosing the right timeframe | 2.1.3. Choosing Timeframes by Trading Style | choosing-timeframe-by-trading-style | "What a Candle Does NOT Tell You" (timeframe limitation) |
| 3 | candlestick patterns | 2.3.1. Candlestick Patterns | japanese-candlesticks | "Next Steps" + "Body and Wicks" (marubozu/doji mention) |
| 4 | support and resistance | 2.2.1. Support and Resistance | support-and-resistance | "Next Steps" (context use) |
| 5 | ranges vs trends | 2.2.3. Market Environment: Ranges vs Trends | ranges-vs-trends | "Next Steps" (market context) |

Minimum 3 links will appear naturally in body; target 4–5 total for the lesson.

---

## Content Validation

**Trading-expert review (self-check):**

- Structure follows beginner didactic order: what a candle represents → data (OHLC) → visual anatomy (body/wicks) → direction (colour) → reading → comparison (bar vs candle) → honest limitations → next steps
- All foundational concepts for OHLC/anatomy are covered; nothing advanced assumed
- Specific pattern names (doji, hammer, engulfing) deliberately excluded — clean handoff to 2.3.1.
- Timeframe dependency mentioned as a limitation, not a separate chapter — clean handoff to 2.1.3.
- Comparison to OHLC bar chart is genuinely useful context (not filler) — many traders first saw bar charts
- Keep-in-Mind callout on pattern overfitting aligns with Structure Guide YMYL requirement for TA content
- Word count target (1,500–1,800) sits below competitor average (2,200–5,500) — justified by strict scope

**Potential concerns:**
- Risk that "What a Candle Does NOT Tell You" feels negative for a beginner. Mitigation: frame as "honest foundation" not "warnings" — this is Academy ToV (realistic educator, not cheerleader).
- Marubozu and doji are named in "Body and Wicks". This is minimal pattern mention needed to describe anatomy edge cases (no-wick, no-body). Kept to single-word references without pattern interpretation. If trading expert prefers zero pattern names, remove and describe structurally only.

**Validation: PASS** (pending trading-expert review of .docx)
