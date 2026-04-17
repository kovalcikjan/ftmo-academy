# Lesson Brief & Outline: Market Profile

## Brief

| Item | Value |
|------|-------|
| Topic | Market Profile |
| Czech Title | Market profile |
| Slug | market-profile |
| Lokace | 2.7.1. |
| Part | Part 2 — Technical Analysis |
| Lekce (parent) | 2.7. Market profile a objemová analýza |
| Type | Kapitola (standalone in-depth chapter article) |
| Position | Kapitola 1 of 5 under Lekce 2.7. |
| Classification | ADVANCED — assumes reader understands chart reading, candles, supply/demand, and basic TA. Market Profile is a specialised lens; introducing it to a total beginner would overload them. |
| Word Count | 2,600–3,200 words — based on competitor average (~3,000 excluding the 8.5k Value Area specialist); needs to cover AMT + MP structure + shapes + limitations without becoming a reference manual. |

---

## Differentiation

Step 1 gap analysis surfaced four clear differentiation levers. This lesson will combine them; no single competitor in the top 10 does all four.

- **Unify the stack, not silo it.** Most competitors pick one angle: theory only (Wikipedia, Tradingriot), Value Area only (MarketProfile.info), profile shapes only (Optimus Futures), or strategies only (Bookmap). This lesson walks from AMT philosophy → MP chart construction → three reference points (POC, Value Area, Initial Balance) → profile shapes / day types → practical reading.
- **Own the honest-limitations section.** None of the top 10 competitor pieces addresses Market Profile's limitations candidly (normal-distribution assumption, single-day unreliability, session-dependence, time-vs-volume distinction). Academy's realistic-educator ToV makes this natural ground — a dedicated "Keep in Mind" block and a short limitations section.
- **Clean profile shape taxonomy.** Only Optimus and Eminimind cover the full D / P / b / B / trend-day set. This lesson will table them with visual cues and what each implies about the session.
- **Trader-facing framing, not futures-desk jargon.** Market Profile was born at CBOT, but most retail MP content still reads like a pit-trader memo. Write it for the FTMO trader reading a chart in a platform — no "bracketed letters", no "LDB", no "single-print tails" without plain-language explanation first.

**Deliberately excluded (forwarded to sibling chapters):**

| Topic | Forwarded to |
|-------|--------------|
| Volume Profile mechanics (POC on volume, not time; VPOC, HVN/LVN) | 2.7.2. Volume Profile, Order Flow |
| Order flow, footprint charts, DOM tape reading | 2.7.2. Volume Profile, Order Flow |
| High Volume Nodes / Low Volume Nodes as trade triggers | 2.7.3. Identifikace zón s vysokým/nízkým objemem |
| Full profiling workflow (multi-day composites, weekly/monthly profile) | 2.7.4. Úvod do profilace trhu |
| Head-to-head comparison of MP vs VP vs Order Flow | 2.7.7. Shrnutí a porovnání přístupů |

This lesson touches MP vs VP briefly (single short section with forward link) because the distinction is needed to understand what MP is not — but the comparison deep-dive lives in 2.7.7.

**FTMO-specific context to include (minimal):**

- Brief note in the "How to use Market Profile in practice" section: Market Profile was designed for session-based markets (futures). Applying it in 24-hour FX requires defining a session (e.g. London open to NY close) — relevant for FTMO traders who run FX strategies.
- One risk-framed mention: MP is a context tool, not a signal generator — should be combined with the trader's existing strategy, not used in isolation.

No other FTMO product placement.

---

## Keywords — Headings

Top keywords from `market-profile_step1.xlsx`, mapped to H1/H2 only. Remaining keywords placed naturally in body prose in Step 3.

| # | Keyword | Volume | KD | Heading placement |
|---|---------|--------|----|-------------------|
| 1 | market profile | 720 | 1 | H1 (core term) |
| 2 | auction market theory | 880 | 6 | H2 — "Auction Market Theory: Why Markets Move" |
| 3 | tpo chart / time price opportunity | 260 / 90 | — | H2 — "Time Price Opportunity: How a Market Profile Chart Is Built" |
| 4 | value area trading | 140 | — | H2/H3 — "Value Area, Point of Control, and Initial Balance" |
| 5 | point of control trading | 110 | 1 | H3 under VA/POC section |
| 6 | market profile vs volume profile | 110 | — | H2 — "Market Profile vs Volume Profile: A Quick Clarifier" |
| 7 | market profile shapes | 20 | — | H2 — "Profile Shapes: Reading What the Session Is Doing" |
| — | remaining ~21 keywords | — | — | Step 3 — body text (natural integration only) |

---

## Outline

# Market Profile (H1)

Key point: The reader should leave able to (a) explain what MP represents and why it was invented, (b) read a Market Profile chart (POC, Value Area, Initial Balance, profile shape, day type), and (c) know what MP can and cannot do.

---

## Intro (no H2 — lead paragraphs)

Key points:
- Open with the principle, not a preamble. A Market Profile is a way of looking at price that treats every 30-minute slice of the trading session as evidence of what traders agreed was fair — and draws a statistical distribution from that evidence.
- Credit the origin in one factual sentence: developed by J. Peter Steidlmayer at the Chicago Board of Trade in the mid-1980s.
- State the payoff in one sentence: MP answers a question most chart tools do not — "where did the market find value today, and where did it reject price?"
- Do not open with the keyword. Do not write "Welcome to…".

Length: 3 short paragraphs, ~140 words total.

---

## Auction Market Theory: Why Markets Move (H2)

Target keyword: `auction market theory`

Key points:
- AMT is the philosophy underneath Market Profile. MP is the tool; AMT is the reason MP looks the way it looks.
- The core claim: markets are a two-way auction. Price moves not because there are "more buyers than sellers" (that is impossible — every trade has both sides) but because one side is more aggressive about paying the spread.
- Three components: **Price** (advertises opportunity), **Time** (regulates how long an opportunity lasts), **Volume** (measures whether the market accepted or rejected that price).
- Two states the market is always in: **balance** (price is accepted — rotating inside a value range) or **imbalance** (price is being rejected — drifting toward a new value area).
- End with a one-sentence bridge: "The Market Profile chart is how Steidlmayer made these concepts visible."

Callout: **Note** — "Auction Market Theory and Market Profile are often discussed as if they are the same thing. They are not. AMT is the theory. Market Profile is one visualisation of that theory — Volume Profile is another."

Length: ~400 words.

---

## Time Price Opportunity: How a Market Profile Chart Is Built (H2)

Target keyword: `tpo chart` / `time price opportunity`

Key points:
- A Market Profile chart is built from Time Price Opportunities (TPOs). Each TPO is one letter representing one time bracket (typically 30 minutes) during which the market traded at a given price.
- Explain the letter convention in one short block: "A" is the first 30 minutes, "B" is the second, and so on. The letter prints next to every price level touched during that bracket.
- After one session, stacked letters form a horizontal histogram — widest where the market spent most time, narrow at the extremes.
- The resulting shape is (roughly) a bell curve — but the shape itself, not the fact of being a bell, is the information.
- Reader takeaway: TPOs measure **time at price**, not volume. This is the defining difference between Market Profile and Volume Profile.

Table: "What a TPO tells you"
| Element | What it represents |
|---------|--------------------|
| One letter | 30 minutes of trading at a specific price |
| Stacked letters (long row) | Prices the market visited repeatedly — acceptance |
| Single letter (tail) | Price touched once — rejection |
| Full profile | Statistical distribution of time spent across prices |

Callout: **Tip** — "If you cannot yet read a standard candlestick chart confidently, finish lessons 2.1 (Charts and Timeframes) and 2.2 (Price Action Basics) first. Market Profile overlays on top of that foundation, not under it."

Length: ~450 words.

---

## Value Area, Point of Control, and Initial Balance (H2)

Target keywords: `value area trading`, `point of control trading`

Key points:
- These are the three reference points most traders actually use. Everything else (single prints, excess, tails) is decoration on top of these.

### Point of Control (POC) (H3)

- The price with the most TPOs in the session. In plain language: the price the market spent the most time at — the session's centre of gravity.
- Fair value in a single number.
- What it signals: if price revisits the POC, it is usually a place where the market pauses — either to reject (in a trend) or to rotate (in balance).

### Value Area (VAH and VAL) (H3)

- The band containing roughly **70%** of the session's TPOs — by convention, one standard deviation either side of the POC.
- Value Area High (VAH) = upper boundary; Value Area Low (VAL) = lower boundary.
- What it signals: **inside** the Value Area the market is in agreement — price is accepted. **Outside** the Value Area the market is testing — price is either discovering a new level or getting rejected back in.

### Initial Balance (IB) (H3)

- The range of the **first hour** of the session (first two 30-minute brackets — "A" and "B"). In US equity index futures, roughly 09:30–10:30 NY.
- The IB is a structural predictor, not a trade signal. A wide IB tends to produce a range-bound day. A narrow IB often precedes a trend day that breaks out of it.
- **Keep in Mind:** the "first hour" framing depends on a clear session. In 24-hour FX, traders typically substitute the first hour after the London or NY open.

Callout: **Important** — "POC, Value Area, and Initial Balance are the three reference points you should be able to mark on any profile without thinking. If you never use anything else from Market Profile, these three still add information your price chart does not."

Length: ~600 words.

---

## Profile Shapes: Reading What the Session Is Doing (H2)

Target keyword: `market profile shapes`

Key points:
- The shape of the profile tells you the character of the day. There are four shapes worth recognising — plus one mid-session regime change.
- Visual recognition matters more than precise rules. Traders learn these by seeing hundreds of examples, not by memorising definitions.

Table: "The five profile shapes at a glance"
| Shape | What it looks like | What it means |
|-------|--------------------|---------------|
| **D-shape (normal)** | Bell curve, POC in the middle, symmetrical Value Area | Balanced session. Market accepted a range. Rotation inside Value Area is the default. |
| **P-shape** | Narrow tail at the bottom, wide belly at the top | Session opened low, aggressive buying pushed price up, then accepted the higher range. Often follows a short squeeze or a strong open. |
| **b-shape** | Wide belly at the top, narrow tail at the bottom | Mirror of the P. Session opened high, heavy selling drove price down, then accepted the lower range. |
| **Trend day** | Long, thin profile — almost no bell, TPOs stretched vertically | Imbalance persisted all session. Almost no time spent in value. One-directional day. |
| **Double distribution** | Two separate bells with a thin neck between them | Regime change mid-session. Market built value at one price, accepted a new level, built value again. |

Callout: **Keep in Mind** — "Profile shapes are a human-pattern-matching tool. The same shape can appear for different reasons — a narrow IB followed by a trend day looks almost identical to a failed breakout until the session closes. Do not treat shape recognition as a signal. Treat it as context."

Length: ~500 words.

---

## How to Use Market Profile in Practice (H2)

Key points:
- MP is a context tool. It tells you what kind of day you are in. It does not tell you where to click buy.
- Three practical applications most traders get value from:
  1. **Marking POC, VAH, and VAL on the next session's chart** — they act as supply/demand reference points.
  2. **Checking value migration across sessions** — is today's Value Area above, below, or overlapping yesterday's? Overlapping = continuation of balance; gap = imbalance, expect follow-through.
  3. **Reading the open's relationship to prior Value Area** — open inside prior VA tends toward rotation; open outside tends toward either acceptance (continuation) or rejection (return to value).
- One FTMO-framed note: for traders running 24-hour FX strategies, pick a session window (typically London or NY) and be consistent. An MP across the entire 24-hour day smooths out the signal MP is designed to show.

Callout: **Tip** — "Use Market Profile as a second screen, not your primary chart. Decide your entry on whatever setup your strategy uses. Check the profile for context — is this entry against accepted value or toward it?"

Length: ~400 words.

---

## Market Profile vs Volume Profile: A Quick Clarifier (H2)

Target keyword: `market profile vs volume profile`

Key points:
- One common point of confusion: Market Profile measures **time at price**. Volume Profile measures **volume at price**. Both produce a similar-looking horizontal histogram, but they answer different questions.
- Short comparison table (below).
- When to use which: MP is stronger in session-based markets with clear rotation (index futures, some commodity futures). VP is stronger when liquidity — not time — is the signal (FX, crypto, equities with heavy institutional participation).
- Do not try to learn both at once. Pick the one that fits your instrument and session style. The next lesson (2.7.2.) covers Volume Profile in depth.

Table: "Market Profile vs Volume Profile"
| | Market Profile | Volume Profile |
|---|----------------|----------------|
| Unit | Time (TPO letters) | Volume (contracts / shares) |
| Answers | "Where did the market spend time?" | "Where did the market trade size?" |
| Strongest in | Session-based futures | Any liquid market |
| Same terms | POC, Value Area | POC, Value Area (but measured on volume) |

Internal link: forward to **2.7.2. Volume Profile, Order Flow**.

Length: ~250 words.

---

## Limitations to Keep in Mind (H2)

Key points (this is Academy differentiation — written candidly, not buried):
- **MP assumes the session produces a roughly normal distribution.** In markets that trend strongly from the open, the profile is one long thin shape and POC loses information.
- **Single-day reliability is low.** One session's profile is a snapshot. The signal strengthens when multiple sessions overlap — that is where composite profiles (lesson 2.7.4.) come in.
- **Time is not the same as volume.** A 30-minute bracket at 03:00 UTC in FX contains far less volume than a 30-minute bracket at 14:30 NY. MP weighs them equally. This is the trade-off MP makes for simplicity.
- **MP was designed for floor-era markets.** The structure of daily sessions has changed since 1985 — continuous electronic trading, overnight sessions, globex. Most of MP's logic survives. Some of it (LDB data, floor-close formulas) is historical trivia.

Callout: **Keep in Mind** — "Market Profile is one way of looking at the market. Many profitable traders never use it. Many profitable traders swear by it. Neither group is wrong. The honest framing: if you already have a tested strategy, MP can sharpen your context. It cannot replace the strategy."

Length: ~350 words.

---

## What to Cover Next (H2)

Key points:
- 2.7.2. Volume Profile, Order Flow — the volume-based counterpart to MP; the more common tool in 24-hour markets.
- 2.7.3. Identifying zones of high and low volume — how traders use HVN / LVN as decision points.
- 2.7.4. Introduction to Market Profiling — composite profiles across multiple sessions.

Short closing paragraph (2–3 sentences). No summary of the current lesson — the reader has just read it.

Length: ~120 words.

---

## Internal Links Plan

Minimum 3–5 internal links required. This outline plans 5.

| # | Link Text | Target Lesson (slug placeholder) | Placement |
|---|-----------|----------------------------------|-----------|
| 1 | "Charts and Timeframes" (prerequisite) | 2.1. /lesson/charts-and-timeframes/ | First Tip callout under "Time Price Opportunity" H2 |
| 2 | "Price Action Basics" (related) | 2.2. /lesson/price-action-basics/ | Same Tip callout as #1 |
| 3 | "Volume Profile, Order Flow" (forward) | 2.7.2. /lesson/volume-profile-and-order-flow/ | End of "Market Profile vs Volume Profile" H2 + in "What to Cover Next" |
| 4 | "Identifying High/Low Volume Zones" (forward) | 2.7.3. /lesson/high-low-volume-zones/ | "What to Cover Next" H2 |
| 5 | "Introduction to Market Profiling" (forward) | 2.7.4. /lesson/introduction-to-market-profiling/ | "What to Cover Next" H2 + referenced inline in "Limitations" (composite profiles note) |

---

## Content Validation

Reviewed as a trading educator + technical analysis practitioner:

- **Logical flow:** AMT (why) → TPO (how the chart is built) → three reference points (what to read) → shapes (what the session is doing) → practical use → comparison with VP → limitations → next steps. Each section builds on the previous. A reader who stops at any H2 leaves with a complete micro-understanding of that block.
- **All key concepts present for ADVANCED classification:** AMT, TPO, POC, VAH/VAL, Initial Balance, D/P/b/trend/double-distribution shapes, value migration, MP vs VP, limitations. Nothing essential to a standalone chapter is missing.
- **Didactic order:** POC → Value Area → Initial Balance is the natural order (single point → band around the point → time-based subset). Shapes come after because shape recognition requires the reader to already have the vocabulary for POC and Value Area.
- **Scope discipline:** Volume Profile, Order Flow, HVN/LVN, footprint charts, DOM, full composite workflow, and MP-vs-VP-vs-OF comparison are all forwarded to sibling chapters. The MP-vs-VP section is deliberately a clarifier, not a deep dive.
- **Honest framing:** Limitations section is explicit. Shape recognition has a "not a signal" callout. Practical-use section has "context not signal" framing. No cheerleading, no guru tone.
- **Potential risk — outline is at the upper end of the word range.** Eight H2s is the ceiling of the Structure Guide's recommended 3–7 range. If the draft runs long in Step 3, candidates to compress: "How to Use Market Profile in Practice" can fold into "Limitations" as a single practical-use-and-caveats section. Keep the option open, do not compress preemptively.

**Validation: PASS**
