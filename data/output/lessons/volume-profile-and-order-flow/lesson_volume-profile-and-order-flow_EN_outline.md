# Lesson Brief & Outline: Volume Profile and Order Flow

## Brief

| Item | Value |
|------|-------|
| Topic | Volume Profile and Order Flow |
| Czech Title | Volume Profile, Order Flow |
| Slug | volume-profile-and-order-flow |
| Lokace | 2.7.2. |
| Part | Part 2 — Technical Analysis |
| Module | 2.7. Market Profile and Volume Analysis |
| Position | Kapitola 2 of 5 (after 2.7.1. Market profile; before 2.7.3. High/low volume zones) |
| Classification | ADVANCED — requires candlestick, timeframe, and support/resistance foundations; volume profile and order flow are advanced volume-analysis tools typically introduced after standard TA |
| Word Count | 2,200–2,600 words — competitor average for dedicated VP+OF articles is 2,200–3,200 (Bookmap 3,200; Oanda 2,200; TradingView 2,300; TrendSpider 2,200; Trader-Dale 3,000; Atas 3,000). Target middle of that range, skipping platform/vendor deep dives |

## Differentiation

- **Integrate both tools.** Most competitor articles cover volume profile OR order flow in isolation. This lesson treats them as complementary: volume profile for historical levels, order flow for live confirmation at those levels.
- **Platform-neutral.** Top SERP results lean heavily on Bookmap, TradingView scripts, Atas, or NinjaTrader UIs. This lesson teaches the concepts so the reader can apply them in any platform.
- **Honest limitations.** Competitors rarely state that volume profile is reactive (not predictive) and that order flow requires centralised exchange data + low-latency infrastructure (which most retail forex traders do not have). We state this clearly.
- **Bridge to surrounding lessons.** Explicitly positions this chapter against 2.7.1. (Market Profile) and connects to 2.7.3. (High/low volume zones), avoiding duplication.
- **Deliberately excluded:** vendor-specific indicator setup, footprint chart tick settings, proprietary strategy recipes, order flow scalping for retail spot forex (infrastructure mismatch), full TPO methodology (lives in 2.7.1.).

## Keywords — Headings

| # | Keyword | Volume | Heading |
|---|---------|--------|---------|
| 1 | volume profile | 1,000 | H1 + H2 "Volume Profile: Reading Historical Activity at Price" |
| 2 | order flow trading | 1,000 | H2 "Order Flow: Reading Live Aggression in the Market" |
| 3 | volume profile indicator | 390 | Body (within VP section) |
| 4 | order flow chart | 480 | H3 within OF section |
| 5 | volume profile vs market profile | 110 | H2 "Volume Profile vs Market Profile vs Order Flow" |
| — | remaining 20 kw | — | Step 3 (body, naturally placed) |

## Outline

# Volume Profile and Order Flow (H1)

Key point: the reader leaves with (a) a clear mental model of volume profile as historical structure and order flow as live aggression, (b) the vocabulary to read both (POC, VA, HVN, LVN, delta, absorption, DOM), and (c) an honest view of when these tools add value and when they do not.

---

## Why Volume Analysis Changes What You See on a Chart (H2)

Key points:
- Price tells you *where* the market went. Volume analysis tells you *how much participation* drove it there and *at what prices*.
- Two complementary views: volume profile (a static record — where volume accumulated) and order flow (a live feed — who is aggressing right now).
- Positions this lesson against the previous chapter (2.7.1. Market Profile) and names the delta: Market Profile = time at price; Volume Profile = volume at price; Order Flow = executions in real time.

Callout: **Note** — Market Profile and Volume Profile share a visual format but measure different things (time vs. volume). The previous chapter covered Market Profile; this chapter adds the volume and execution dimension.

---

## Volume Profile: Reading Historical Activity at Price (H2)

Target keyword: `volume profile` (H2), `volume profile indicator` (body)

Key points:
- Definition: a horizontal histogram that distributes traded volume across price levels instead of across time.
- Core logic: prices with heavy volume represent areas of agreement (supply meeting demand); prices with little volume were rejected quickly.
- What this gives the trader: objective support/resistance zones based on where participation actually happened, not subjective trendlines.

### Point of Control (POC) (H3)

- The single price level with the highest traded volume in the measured range.
- Interpreted as the session's (or range's) fair-value anchor.
- Common use: revisits of POC act as natural decision points for entries or exits.

### Value Area (VA, VAH, VAL) (H3)

- The price range containing a defined share of total volume, typically 70%.
- VAH (value area high) and VAL (value area low) are the outer bounds.
- Use: price inside VA signals balance; price breaking out of VA signals a potential shift in perceived value.

### High Volume Nodes and Low Volume Nodes (H3)

- HVN (high volume node): price cluster with concentrated participation — acts as support/resistance and a likely reaction zone.
- LVN (low volume node): gap in the profile — price that moved through quickly, often revisited fast once re-entered.
- Keep in Mind: nodes describe the past, not the future. Reactions happen frequently but are not guaranteed.

### Volume Profile Types (H3)

Target keywords: `fixed range volume profile`, `visible range volume profile`, `session volume profile`, `anchored volume profile`

- **Session** — one trading session per profile. Useful for intraday structure.
- **Visible Range** — recalculates to whatever is on screen. Useful for swing-level zoom.
- **Fixed Range** — anchored between two manually chosen prices or times.
- **Anchored** — starts from a chosen event (earnings release, breakout bar) and builds forward.
- Choice depends on the question being asked (intraday pivot? weekly structure? post-event value?).

Table: compact comparison (type | when to use | typical timeframe).

---

## Order Flow: Reading Live Aggression in the Market (H2)

Target keyword: `order flow trading` (H2)

Key points:
- Definition: the real-time stream of executed trades and resting orders.
- Where volume profile shows *where* volume happened, order flow shows *who was aggressing* — buyers hitting the ask or sellers hitting the bid.
- Practical prerequisite: meaningful order flow requires a centralised exchange and tick-level data. Works well on futures (ES, NQ, CL); works less reliably on retail spot forex because there is no central order book.

### Footprint Charts (H3)

Target keyword: `order flow chart`

- Visual representation of a candle broken down by executed buy and sell volume at each price inside the candle.
- Numbers on the left = volume executed at the bid (sellers aggressing); numbers on the right = volume at the ask (buyers aggressing).
- Reading: look for imbalance patterns — one side dominating at a level suggests conviction.

### Delta and Cumulative Delta (H3)

- Delta = (buy-initiated volume) − (sell-initiated volume) for a bar.
- Cumulative delta = running sum across bars — reveals sustained aggression beyond any single candle.
- Use: divergence between price and cumulative delta (e.g., price makes a new high, cumulative delta does not) suggests weakening aggression and a possible reversal.

### Absorption and Imbalance (H3)

- Absorption: large volume hits a price level repeatedly but price barely moves — resting orders are absorbing the aggression. Often marks where an institutional participant is defending a level.
- Imbalance: one side's executed volume dominates meaningfully at a level (commonly 3× or more). Points to conviction and often precedes continuation.
- Callout: **Keep in Mind** — absorption and delta divergence are signals of possibility, not certainty. Many divergences resolve by price simply continuing.

### Depth of Market (DOM) (H3)

- The live order book: resting bids and offers at each price.
- Useful for short-term execution context, but prone to spoofing (fake orders placed to mislead and cancelled before fill).
- Treat DOM as one input, not a trading signal in isolation.

---

## Volume Profile vs. Market Profile vs. Order Flow (H2)

Target keyword: `volume profile vs market profile`

Key points:
- Market Profile = time spent at price (TPO).
- Volume Profile = volume traded at price.
- Order Flow = individual executions and resting orders in real time.
- Each answers a different question: Market Profile asks "where did the market spend time?"; Volume Profile asks "where did the volume actually occur?"; Order Flow asks "who is aggressing right now?".

Table: three-way comparison (dimension | measures | timeframe | primary use).

---

## Using Volume Profile and Order Flow Together (H2)

Key points:
- A practical workflow: use higher-timeframe volume profile to map where meaningful levels sit (POC, HVN, VAH/VAL), then switch to order flow at those levels for execution context.
- At an HVN on a revisit: look at delta and absorption to judge whether the level is being defended or broken.
- At an LVN: expect fast price movement — order flow can confirm whether aggression is strong enough to push through.
- This is a *framework*, not a recipe. Any of several valid approaches exists.

Callout: **Tip** — the two tools answer different questions. Profile narrows where to look; flow tells you what is happening when you get there.

---

## Limitations and Honest Caveats (H2)

Key points:
- Volume profile is reactive — it describes the past. It does not predict the next move; it tells you where previous participants placed their orders.
- Historical levels fail. Regularly. A POC from three sessions ago may carry no weight today.
- Order flow needs tick-level data and a centralised exchange. On retail spot forex, what is sold as "order flow" is usually a broker-aggregated approximation, not the real market.
- Both tools reward screen time. Reading them accurately is a skill that develops over months of deliberate observation.

Callout: **Keep in Mind** — pattern recognition in volume analysis is vulnerable to confirmation bias. Traders see the levels that worked and discount the ones that did not. Track outcomes honestly before relying on any single approach.

---

## What to Review Next (H2)

- If you want the auction-theory foundation that sits behind both tools, revisit [Market profile](/lesson/market-profile/) (2.7.1.).
- To translate these concepts into concrete zone identification, continue to [Identifying high and low volume zones](/lesson/high-low-volume-zones/) (2.7.3.).
- For the broader framing of market profiling as a methodology, see [Introduction to market profiling](/lesson/introduction-to-market-profiling/) (2.7.4.).
- For a comparison of how these approaches fit together in practice, see [Comparison of volume-based approaches](/lesson/comparison-of-approaches/) (2.7.7.).

---

## Internal Links Plan

| # | Link Text | Target Lesson | Slug | Placement |
|---|-----------|---------------|------|-----------|
| 1 | Market profile | 2.7.1. Market profile | market-profile | Intro callout + Review section |
| 2 | Identifying high and low volume zones | 2.7.3. | high-low-volume-zones | HVN/LVN section + Review |
| 3 | Introduction to market profiling | 2.7.4. | introduction-to-market-profiling | Review section |
| 4 | Comparison of volume-based approaches | 2.7.7. | comparison-of-approaches | Review section |
| 5 | Types of trading charts | 2.1.1.1. | types-of-trading-charts | Footprint chart intro (chart-type prerequisite) |

## Content Validation

- Structure follows classical progression: framing → volume profile (static structure) → order flow (live confirmation) → comparison → combined use → limitations → next steps. Didactically sound.
- All standard concepts competitors cover are present (POC, VA, HVN, LVN, profile types, footprint, delta, absorption, DOM).
- ADVANCED classification appropriate: the lesson assumes prior familiarity with candlesticks, timeframes, and support/resistance.
- Limitations section addresses a real gap in SERP — most competitors oversell these tools. Aligns with FTMO Academy "realistic educator" positioning.
- Retail-forex caveat for order flow is important and rarely stated elsewhere.
- Two callouts per H2 limit respected; 2 tables planned (profile types, three-way comparison).
- **Validation: PASS**
