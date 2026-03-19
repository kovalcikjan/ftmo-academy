# Types of Trading Charts — Edit Log

**Article:** `lesson_types-of-trading-charts_EN.md`
**Source:** https://academy.ftmo.com/lesson/types-of-trading-charts/
**Date:** 2026-03-05

---

## Step 1 Log: Keywords

**Keywords file:** `types-of-trading-charts_keywords.xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | `## Types of trading charts – candlestick chart, Renko, Heikin Ashi` | H2 removed in Post-QA — keywords integrated into H1: `Types of Trading Charts: Candlestick Charts, Renko Charts, and Heikin Ashi` | candlestick charts / renko charts | 1000 / 400 | H1 | DONE |
| 2 | `### Renko` | `### Renko Charts` | renko charts | 400 | H3 | DONE |
| 3 | `### Heikin Ashi` | `### Heikin Ashi Candles` | heikin ashi candles | 1400 | H3 | DONE |
| 4 | `Heikin Ashi is another chart representation that comes from Japan.` | `Heikin Ashi candles are another chart representation that comes from Japan.` | heikin ashi candles | 1400 | H3 body | DONE |
| 5 | `here we can have a look at how the Heikin Ashi candle is calculated` | `here we can have a look at how the Heikin Ashi candle formula works` | heikin ashi candle formula | 150 | body | DONE |
| 6 | `Although most traders are using candlestick charts` | unchanged — keyword already present | candlestick charts | 1000 | body | DONE |
| 7 | `Renko is similar to the range and tick charts.` | `Renko charts are similar to range and tick charts.` | renko charts | 400 | H3 body | DONE |
| 8 | `In the tick chart, one tick represents one transaction.` | `In a tick chart, one tick represents one transaction.` | tick chart | 700 | body | DONE |
| 9 | `Our traders can use tick and range charts` | `Our traders can use tick charts and range charts` | tick charts / range charts | 100 | body | DONE |
| 10 | `Bar charts, often called OHLC charts` | unchanged — keyword already present | ohlc charts | 40 | body | DONE |
| 11 | `We have covered Japanese candlesticks in the previous lesson` | unchanged — keyword already present | japanese candlesticks | 200 | body | DONE |
| 12 | `Heikin Ashi filters out the movements and makes a much easier approach to trend following.` | Added after: `Many traders incorporate it into their Heikin Ashi strategy specifically for trend-following entries.` | heikin ashi strategy | 250 | body | DONE |
| 13 | footprint chart, market profile, order flow chart, point and figure chart, kagi chart | — | various | — | — | SKIP — not covered in article |

---

## Step 2 Log: ToV Rewrite

**Guide:** `ftmo_academy_tov_guide_EN.md`
**Topic classification:** BEGINNER — Part 2, Technical Analysis, Lesson 2. Introductory charting concepts.

### Word / Phrase Changes

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | `"What are the specifics of these charts and how do they differ? You will find out in this lesson."` | `"This lesson covers the main types of trading charts, what makes each one different, and how to choose the right display for your analysis."` | ToV BEGINNER: "This lesson covers..." opener; original was a vague rhetorical question |
| 2 | `"The ways of displaying data on our price chart are pretty much endless."` | `"Price charts can be displayed in nearly unlimited ways."` | ToV: casual "pretty much" → "nearly"; inverted pyramid — direct statement first |
| 3 | `"This is why we will never find two traders that do and watch exactly the same things in their trading."` | `"This is why no two traders watch exactly the same things."` | ToV: redundant "do and"; shorter, more direct |
| 4 | `"Although most traders are using candlestick charts which we covered in the previous video, there is more depth in those as well."` | `"Although most traders use candlestick charts — covered in the previous lesson — there is more depth to explore."` | ToV: "previous video" → "previous lesson"; "are using" → "use"; "in those as well" → clearer |
| 5 | `"Besides candlestick charts, we will also have a look at different graphical representations of price charts such as bar charts, Renko or Heikin Ashi charts."` | `"This lesson also covers bar charts, Renko charts, and Heikin Ashi candles."` | ToV: "we will have a look at" → direct statement; shorter |
| 6 | `"We have covered Japanese candlesticks in the previous lesson, so we will do just a quick recap now."` | `"Japanese candlesticks are covered in the previous lesson. Here is a quick recap."` | ToV: "just" filler removed; split into two shorter sentences |
| 7 | `"They are the most popular methods of charting and viewing technical analysis."` | `"They are the most widely used chart type in technical analysis."` | ToV: "most popular methods of charting and viewing" → cleaner, more precise |
| 8 | `"If the candle closes below the open, we look at a bearish candlestick."` | `"If the candle closes below the open, it is a bearish candlestick."` | ToV: "we look at" → "it is" (factual, direct) |
| 9 | `"As we can see in the image below, we have two candlestick charts next to each other in our FTMO cTrader platform."` | `"The image below shows two candlestick charts side by side in the FTMO cTrader platform."` | ToV: "As we can see" filler removed; active sentence |
| 10 | `"Although they look the same, there is one significant difference between them."` | `"Although they look the same, there is one significant difference."` | ToV: "between them" redundant (implied) |
| 11 | `"The time periodicity is the most popular and common amongst traders."` | `"Time periodicity is the most common choice among traders."` | ToV: "most popular and common" redundant → "most common"; "amongst" → "among" |
| 12 | `"Although we can set up our chart with any setting we want, using those popular timeframes works simply because many traders are also watching them."` | `"You can set up a chart with any periodicity, but standard timeframes work because many traders monitor them."` | ToV: "simply" filler removed; "watching" → "monitor"; "any setting we want" → "any periodicity" |
| 13 | `"If we use something like a 40-minute or 3-hour chart, the candlestick patterns on our chart might have a lower weight as no other traders see them."` | `"A 40-minute or 3-hour chart carries less weight — fewer traders monitor those intervals, so candlestick patterns formed on them have reduced significance."` | ToV: "might have a lower weight" → "carries less weight"; "as no other traders see them" → specific and direct |
| 14 | `"The non-time-based charts are less common, but they still can give traders valuable information."` | `"Non-time-based charts are less common, but they can still provide valuable information."` | ToV: "still can give" → "can still provide"; removed unnecessary "The" |
| 15 | `"Our traders can use tick charts and range charts in our FTMO cTrader platform, these two are also the most popular non-time-based charts."` | `"In the FTMO cTrader platform, traders can access tick charts and range charts — the two most popular non-time-based options."` | ToV: comma splice fixed; "Our traders" → "traders"; cleaner structure |
| 16 | `"In other words, one tick is made when the market fluctuates by the minimal price increment."` | `"One tick occurs when the market moves by the minimum price increment."` | ToV: "is made" passive → "occurs"; "In other words" filler removed; "minimal" → "minimum" |
| 17 | `"If we take a look at EURUSD, which is quoted in five decimal places."` | `"Take EURUSD as an example — it is quoted in five decimal places."` | ToV + Grammar: sentence fragment fixed; direct framing |
| 18 | `"One tick would equal 0.00001 or 1 pipette."` | `"One tick equals 0.00001, or 1 pipette."` | ToV: "would equal" → "equals" (factual, present tense) |
| 19 | `"Using a range of tick charts can eliminate noise and display trends in a much clearer picture as we will get rid of time periods when markets are not moving and staying range-bound."` | `"Range and tick charts eliminate noise and display trends more clearly by removing periods when price is not moving."` | ToV: long sentence → shorter; "in a much clearer picture" → "more clearly"; "we will get rid of" → "removing" |
| 20 | `"This can be clearly seen when we compare this DAX four-hour chart with the 100 range chart in cTrader."` | `"The effect is visible when comparing a DAX four-hour chart with a 100-range chart in cTrader."` | ToV: "This can be clearly seen" passive → active; vague "this" removed |
| 21 | `"We can notice that both uptrend and downtrend were much cleaner on the range chart once we eliminated the time factor and put our focus on price rotations."` | `"Both the uptrend and downtrend appear cleaner on the range chart once the time factor is removed and focus shifts to price rotations."` | ToV: "We can notice" filler removed; "put our focus on" → "focus shifts to" |
| 22 | `"Bar charts, often called OHLC charts, are represented as vertical bars with two notches that represent the open and close of the bar."` | `"Bar charts, often called OHLC charts, display as vertical bars with two notches indicating the open and close of each bar."` | ToV: "are represented as" passive → "display as" active |
| 23 | `"Compared to Japanese candlesticks, bar charts might be a little less clean for new traders when it comes to candlestick patterns."` | `"Compared to Japanese candlesticks, bar charts are less intuitive for new traders when reading candlestick patterns."` | ToV: "might be a little less clean" → "are less intuitive"; "when it comes to" filler removed |
| 24 | `"On the other hand, they might present a little cleaner picture when it comes to marking out support and resistance."` | `"On the other hand, they may provide a clearer view for marking support and resistance levels."` | ToV: "might present a little cleaner picture" → "may provide a clearer view"; "when it comes to" removed |
| 25 | `"It eliminates the time factor from trading and changes the visuals of our chart completely."` | `"Renko eliminates the time factor from trading and changes the chart's visual representation entirely."` | ToV + Grammar: "It" ambiguous pronoun → "Renko"; "visuals of our chart" → "chart's visual representation" |
| 26 | `"We won't see candlesticks anymore, but we will be looking at bricks instead."` | `"Instead of candlesticks, the chart displays bricks."` | ToV: more direct; contraction removed; unnecessary "anymore" removed |
| 27 | `"The name Renko came from the Japanese renga, which stands for brick."` | `"The name comes from the Japanese word renga, meaning brick."` | ToV: tighter; italics added for foreign word |
| 28 | `"Let's say we define that one brick signifies a movement of 5 pips."` | `"For example, if one brick represents 5 pips..."` | ToV: "Let's say" casual → "For example, if"; "signifies a movement of" → "represents" |
| 29 | `"Renko charts are not only great for filtering out noise but also for marking out support and resistance areas."` | `"Renko charts are effective for filtering out noise and marking support and resistance areas."` | ToV: "great" hype word → "effective"; "not only... but also" → simpler |
| 30 | `"It means 'average bar' and although this is not something we need to know, here we can have a look at how the Heikin Ashi candle formula works."` | `"The name translates to 'average bar.' Here is how the Heikin Ashi candle formula works:"` | ToV: "this is not something we need to know" dismissive → removed; "here we can have a look" → "Here is how" |
| 31 | `"We can set up a Heikin Ashi chart as we want, on the specified time, range or tick."` | `"A Heikin Ashi chart can be set up on any preferred timeframe — time-based, range, or tick."` | ToV: "as we want" casual → "on any preferred timeframe"; clearer enumeration |
| 32 | `"Heikin Ashi filters out the movements and makes a much easier approach to trend following."` | `"Heikin Ashi smooths price movements and simplifies trend following."` | ToV: "filters out the movements" → "smooths price movements"; "makes a much easier approach" → "simplifies" |
| 33 | `"The downside of it is that we might miss some valuable information as it might smooth out the chart a little too much."` | `"The trade-off is that some price detail is lost — the smoothing can obscure short-term signals."` | ToV: "The downside of it is that" → "The trade-off is that"; "a little too much" casual removed; more specific |
| 34 | `"But it is a great tool for both entries and trade management."` | `"However, it remains an effective tool for both entries and trade management."` | ToV: "But" sentence start → "However,"; "great" → "effective" |
| 35 | `"To conclude this chapter, the best thing we can do is to play with different charts and settings and find what suits us the best, that is always the smartest approach."` | `"Experimenting with different charts and settings is the most effective way to find what works for your trading style."` | ToV: "To conclude this chapter" filler removed; "play with" → "experimenting with"; "us" → "your" (consistent reader address) |
| 36 | `"But tick charts, range charts, Renko or Heikin Ashi, can be utilized in our strategy and bring a lot of use to our personal trading."` | `"However, tick charts, range charts, Renko charts, or Heikin Ashi candles can all be incorporated into your strategy and add value to your trading."` | ToV: "But" → "However,"; "bring a lot of use" vague → "add value"; "our personal trading" → "your trading" |

---

## Step 3 Log: Structure & Formatting

**Guide:** `ftmo_academy_structure_guide_EN.md`
**Article length:** ~600 words → Short (<1000 words) → limits: 1–2 callouts, 1 table, 1–2 lists

### Phase 0: Paragraph Audit

All 14 paragraphs checked. No paragraph exceeds 100 words. No splits required.

### Structural Changes

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Prerequisites added | `> **Prerequisites:** [Japanese Candlesticks](/lesson/japanese-candlesticks/)` at top | E-E-A-T: learning path; lesson explicitly references prior lesson |
| 2 | Bold — key terms | **candlestick charts**, **bar charts**, **Renko charts**, **Heikin Ashi candles** in H2 intro | Structure: key terms bolded on first use for scanning |
| 3 | Internal link | "Japanese Candlesticks" → `/lesson/japanese-candlesticks/` in H3 opener | Structure: prerequisite linked inline |
| 4 | Bold — anatomy terms | **body**, **wick** in candlestick anatomy paragraph | Structure: first-use term highlighting |
| 5 | H4 added | `#### Time-Based Charts` before periodicity content | Structure: Candlestick Charts section splits into two distinct topics; H4 adds scannability without skipping levels |
| 6 | Bold — term | **Chart periodicity** on first use | Structure: key concept highlighted |
| 7 | Callout Tip added | After standard timeframes paragraph — "Standard timeframes (1H, 4H, Daily) are monitored by a large number of traders simultaneously..." | Structure: actionable insight; 1 callout for this H3 section |
| 8 | H4 added | `#### Tick and Range Charts` before non-time-based content | Structure: logical split of time-based vs non-time-based; parallel H4 structure |
| 9 | Bold — terms | **tick charts**, **range charts** on first use | Structure: key terms highlighted |
| 10 | Bold — term | **bar chart** on first use in H3 Bar Charts | Structure: first-use term highlighting |
| 11 | Internal link | "support and resistance" → `/lesson/support-and-resistance/` in Bar Charts section | Structure: inline link to related concept mentioned in text |
| 12 | Internal link | "support and resistance" → `/lesson/support-and-resistance/` in Renko Charts section | Structure: second mention also linked (different H3 section) |
| 13 | Callout Keep in Mind added | After Heikin Ashi effect paragraph — cognitive bias warning for TA lessons | Structure: standard Keep in Mind for all TA lessons per Structure Guide |
| 14 | Comparison table added | Conclusion — 4 chart types × Time-Based / Best For | Structure: comparison data from existing content; aids decision-making |
| 15 | Key Takeaways section added | 6 bullet points — one per chart type/concept | Structure: scannable recap; E-E-A-T helpfulness signal |
| 16 | Next Steps section added | 3 internal links: Market Environment, Support & Resistance, Technical Indicators | Structure: 3–5 internal links requirement met (5 total including inline) |
| 17 | Author box added | "FTMO Academy Content Team / Last Updated: March 5, 2026" | E-E-A-T: authorship and freshness signals |
| 18 | Educational Content Notice added | Standard disclaimer callout at article end | YMYL: required for all lessons |
| 19 | Risk Warning added | Standard risk disclaimer at article end | YMYL: required for all lessons |

### Internal Links Summary (5 total)

| Anchor Text | URL | Position |
|-------------|-----|----------|
| Japanese Candlesticks | /lesson/japanese-candlesticks/ | Prerequisites block |
| Japanese Candlesticks | /lesson/japanese-candlesticks/ | H3 Candlestick Charts opener (inline) |
| support and resistance | /lesson/support-and-resistance/ | Bar Charts (inline) |
| support and resistance | /lesson/support-and-resistance/ | Renko Charts (inline) |
| Market Environment: Range vs. Trend | /lesson/market-environment-range-vs-trend/ | Next Steps |
| Support and Resistance | /lesson/support-and-resistance/ | Next Steps |
| Technical Indicators | /lesson/technical-indicators/ | Next Steps |

---

## Summary

| Step | Status | Changes |
|------|--------|---------|
| Step 1: Keywords | DONE | 12 changes applied, 1 SKIP (off-topic keywords) |
| Step 2: ToV Rewrite | DONE | 36 changes — casual markers, hype words, passive voice, sentence fragments, filler phrases |
| Step 3: Structure | DONE | 19 changes — H4s, callouts, table, Key Takeaways, Next Steps, E-E-A-T elements |
| Step 4: HTML | DONE | v3_standard template; 5 images placed at exact original positions; BEM callouts; :root CSS variables; responsive |
| Step 5: QA | DONE | All checks passed. 2 minor notes (short caption sentence, list-like H2) — both acceptable. Article approved. |
| Post-QA Amendments | DONE | H1 expanded, H2 container removed, headings promoted, ToC added, image resized — see below |

---

## Post-QA Amendments

| # | Change Type | File | Description |
|---|-------------|------|-------------|
| 1 | H1 updated | .md + .html | `Types of Trading Charts` → `Types of Trading Charts: Candlestick Charts, Renko Charts, and Heikin Ashi` |
| 2 | H2 removed | .md + .html | `## Candlestick Charts, Renko Charts, and Heikin Ashi` removed — content moved into H1; intro paragraph kept as standalone |
| 3 | Heading promotion | .md + .html | `### Candlestick Charts` → `## Candlestick Charts` · `### Bar Charts` → `## Bar Charts` · `### Renko Charts` → `## Renko Charts` · `### Heikin Ashi Candles` → `## Heikin Ashi Candles` |
| 4 | Heading promotion | .md + .html | `#### Time-Based Charts` → `### Time-Based Charts` · `#### Tick and Range Charts` → `### Tick and Range Charts` |
| 5 | ToC added | .md + .html | H2-only ToC (`## In This Lesson`) added after intro paragraph; HTML uses `<nav class="toc">` with anchor links |
| 6 | Anchor IDs added | .html | `#candlestick-charts`, `#bar-charts`, `#renko-charts`, `#heikin-ashi-candles`, `#conclusion` |
| 7 | Meta title updated | .html | `Types of Trading Charts: Candlestick, Renko, Heikin Ashi \| FTMO Academy` (55 chars) |
| 8 | Image resized | .html | `c-25.jpg` (candlestick anatomy) set to `width: 30%` via inline style |
