# Lesson Brief & Outline: Timeframe Hierarchy

## Brief

| Item | Value |
|------|-------|
| Topic | Timeframe Hierarchy |
| Czech Title | Hierarchie timeframu |
| Slug | timeframe-hierarchy |
| Lokace | 2.1.3.1. |
| Part | Part 2: Trading Analysis |
| Module | 2.1. Graf a timeframe |
| Position | Podtema under 2.1.3. Volba casovych ramcu pro ruzne styly obchodovani |
| Classification | BEGINNER: foundational concept, no prior TA knowledge required beyond chart basics |
| Word Count | 1,800-2,200 words (competitors avg ~1,800; topic is conceptual but needs practical demonstration) |

## Prerequisites

- Types of Trading Charts: reader must understand what a chart displays
- Japanese Candlesticks: each candle = one timeframe unit (OHLC)

## Differentiation

- Hierarchy as standalone concept: no competitor dedicates an article to WHY higher timeframes carry more weight. All bury this inside MTF analysis or "best timeframe" guides. Academy owns the foundational layer.
- Information layering: explicit breakdown of what each timeframe tier reveals (monthly = macro trend, daily = swing context, H1 = intraday momentum). Competitors only list TFs by trading style.
- Same-instrument demonstration: show the SAME price action across 4 timeframes to illustrate how the picture changes. No competitor does this.
- FTMO connection: how timeframe awareness prevents impulsive entries and supports drawdown management.
- Deliberately excluded: timeframe selection by trading style (separate subtopic 2.1.3.2.), multiple timeframe analysis strategy (separate lesson 2.1.4.), platform-specific setup, exotic chart types (Renko, range bars).

## Keywords: Headings

| # | Keyword | Volume | Heading |
|---|---------|--------|---------|
| 1 | trading time frames | 90 | H1 |
| 2 | what are timeframes in trading | 20 | H2: What Is a Timeframe |
| 3 | different time frames | 60 | H2: Types of Trading Timeframes |
| 4 | higher time frame trading | 50 | H2: Why Higher Timeframes Carry More Weight |
| 5 | trading timeframes explained | 10 | Body (Step 3) |
| - | remaining 16 kw | - | Step 3 (body) |

## Outline

# Trading Timeframes: Understanding the Hierarchy (H1)

Key point: Timeframes determine how you see the market. Understanding their hierarchy, how they nest inside each other and why higher timeframes dominate, is the foundation for every analytical decision. This concept is also known as top-down analysis: reading the market from the highest timeframe down to the lowest, building context before precision. [expert comment a]

---

## What Is a Timeframe (H2)

Target keyword: what are timeframes in trading

Key points:
- A timeframe defines the period each candlestick or bar represents, from 1 minute to 1 month
- The underlying price data is identical; only the resolution changes (zoom in/out analogy)
- Standard timeframe notation: M1, M5, M15, M30, H1, H4, D1, W1, MN
- Each candle compresses all price action within that period into four data points: open, high, low, close

Callout [Note]: "Changing the timeframe does not change the market. It changes how much detail you see."

---

## Types of Trading Timeframes (H2)

Target keyword: different time frames

Key points:
- Three tiers: short-term (M1-M15), medium-term (M30-H4), long-term (D1-MN)
- Short-term: high detail, more noise, more candles per session. Used for entries and intraday decisions
- Medium-term: balance of detail and context. Used for pattern identification and setup confirmation
- Long-term: smooth, low noise, shows dominant trend and major levels. Used for directional bias
- The dividing line is roughly H1: below = short-term, above = medium/long-term

Table: Timeframe Tiers
| Tier | Timeframes | What It Shows | Noise Level | Typical Use |

---

## How Timeframes Nest Inside Each Other (H2)

Key points:
- Every higher timeframe candle contains multiple lower timeframe candles (1 daily = 24x H1 = 96x M15)
- This nesting creates a natural hierarchy: information from higher TFs encompasses all lower TF data
- The 4x-6x ratio: adjacent timeframes in a useful analysis chain are typically 4-6x apart (M15 to H1 to H4 to D1)
- Too close (M5 to M15) = redundant information; too far apart (M5 to D1) = gaps in the picture
- Practical application: traders typically combine 2-3 timeframes. For example, D1 for identifying support and resistance levels, M30 for confirming activity at those levels (such as a candlestick formation), and M1 for refining the final entry (such as a trendline breakout). If the D1 chart shows an uptrend, the trader looks for bullish setups on M30 and then times the entry on M1. [expert comment a]

Callout [Tip]: "A useful rule: multiply your timeframe by 4-6 to find the next meaningful level up. M15 x 4 = H1. H1 x 4 = H4. H4 x 6 = D1."

Table: Nesting Ratios
| From TF | To TF | Candles Contained | Ratio |

---

## Why Higher Timeframes Carry More Weight (H2)

Target keyword: higher time frame trading

Key points:
- Higher TF candles represent more market participants, more volume, more data. Each candle is a summary of thousands of decisions
- A support level on the daily chart reflects weeks of price interaction; a support level on M15 reflects minutes
- Higher TF trends take longer to develop AND longer to reverse. They are structurally more stable
- Institutional traders operate on higher timeframes. Their order flow creates the dominant moves that lower TF traders react to
- When higher and lower TFs disagree, the higher TF wins the bias (preview of MTF analysis concept)

Callout [Important]: "A support level on the daily chart is not the same as a support level on the 15-minute chart. The daily level represents days of price memory. The M15 level represents minutes."

---

## What Each Timeframe Reveals (H2)

Key points:
- Monthly/Weekly: macro trend direction, long-term support/resistance, overall market regime (trending vs ranging)
- Daily: swing-level trend, key price levels for the current cycle, overnight gaps
- H4/H1: intraday momentum, session-level structure, short-term patterns
- M15/M5: entry precision, micro-structure, immediate supply/demand
- The same instrument looks different on each timeframe. A downtrend on H1 can be a pullback on D1
- Practical demonstration: describe the same price scenario across MN to D1 to H1 to M15

Callout [Keep in Mind]: "What looks like a reversal on the 15-minute chart may be a minor pullback on the daily chart. Context depends entirely on which timeframe you are reading."

---

## The Signal-to-Noise Problem (H2)

Key points:
- Lower timeframes contain more noise: random price fluctuations that do not reflect meaningful market moves
- Higher timeframes filter noise by averaging over larger samples of data
- This is why strategies tend to produce cleaner signals on higher timeframes
- Session-dependent noise: noise on lower timeframes increases significantly outside main trading hours. For example, an M15 candle during the Asian session (low liquidity, small volume) does not carry the same informational value as an M15 candle during the London or New York open, where order volume within a single M15 period can be several times higher. [expert comment b]
- Noise does not mean "useless." Lower TFs are valuable for entry timing, but only within the context of a higher TF bias. The main reason traders step down to a lower timeframe for entries is risk management: a tighter stop loss improves the risk-to-reward ratio (RRR). However, this comes at the cost of win rate, because more noise on the lower timeframe generates more false signals. The trade-off must be understood before applying it. [expert comment c]
- Beginners often start on low TFs because "more action" feels productive, but more candles = more false signals

Callout [Warning]: "More candles does not mean more opportunities. On lower timeframes, the majority of price movements are noise: random fluctuations that trigger false signals and erode capital."

---

## Key Takeaways

Key points:
- 5 bullet points summarising the hierarchy concept
- Actionable next step: open any instrument on three timeframes (D1, H1, M15) and observe how the same price action looks different at each level
- Bridge to next lessons: timeframe selection by style (2.1.3.2.) and multiple timeframe analysis (2.1.4.)

---

## Internal Links Plan

| # | Link Text | Target Lesson | Slug | Placement |
|---|-----------|---------------|------|-----------|
| 1 | Japanese candlesticks | Japanese Candlesticks | japanese-candlesticks | What Is a Timeframe (OHLC reference) |
| 2 | support and resistance | Support and Resistance | support-and-resistance | Why Higher TFs Carry More Weight (level significance) |
| 3 | market environment | Market Environment | market-environment-range-vs-trend | What Each TF Reveals (trending vs ranging) |
| 4 | types of trading charts | Types of Trading Charts | types-of-trading-charts | What Is a Timeframe (chart types reference) |
| 5 | trading hours and sessions | Trading Hours and Sessions | forex-trading-hours-and-sessions | Signal-to-Noise (session-dependent noise) |
| 6 | risk and money management | Risk Management | risk-and-money-management | Signal-to-Noise (RRR vs win rate trade-off) |

## Content Validation

- Structure follows logical progression: definition, types, nesting, hierarchy principle, practical revelation, noise problem, takeaways
- BEGINNER classification correct: explains foundational concepts, defines every term, assumes only basic chart knowledge
- Didactic sequence: each section builds on the previous. Understanding nesting (section 3) is required before understanding why higher TFs dominate (section 4)
- No gaps: covers what a TF is, how they relate, why hierarchy matters, and what information each provides
- Nothing out of scope: no MTF strategy, no style-based selection, no platform guides
- All 3 expert comments implemented (see changelog below)
- Internal links: 6 planned (added trading hours + risk management per expert comments)
- **Validation: PASS**

## Expert Comments: Resolution Log

| # | Location | Expert Feedback | Resolution |
|---|----------|----------------|------------|
| [a] | H1 + Nesting section | Also called top-down analysis. Practical example: D1 for S/R, M30 for confirmation (candlestick formation), M1 for final entry (trendline breakout). If D1 uptrend, look for bullish setups on M30, refine on M1. | Added "top-down analysis" to H1 intro. Added full practical 3-TF example in "How Timeframes Nest Inside Each Other" section. |
| [b] | Signal-to-Noise section | Noise increases outside main trading hours. M15 during Asian session has less informational value than M15 during London/NY open (order volume several times higher). | Added dedicated bullet point with Asian vs London/NY example. Added link to Trading Hours and Sessions lesson. |
| [c] | Signal-to-Noise (entry timing note) | Lower TF entries are mainly about risk management: tighter SL = better RRR, BUT at cost of win rate (more noise). | Expanded entry timing bullet to include RRR vs win rate trade-off explicitly. Added link to Risk Management lesson. |
