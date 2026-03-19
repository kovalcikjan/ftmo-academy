# Edit Log — Types of Trading Charts

**Article:** types-of-trading-charts
**Source:** https://academy.ftmo.com/lesson/types-of-trading-charts/
**Date:** 2026-03-05

---

## Step 1 Log: Keywords

**Keywords file:** `types-of-trading-charts_keywords.xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | "### Heikin Ashi" | "### Heikin Ashi Candles" | heikin ashi candles | 1400 | H3 | DONE |
| 2 | "Heikin Ashi is another chart representation that comes from Japan." | "Heikin Ashi candles are another chart representation that comes from Japan." | heikin ashi candles | 1400 | H3 body | DONE |
| 3 | "It means "average bar" and although this is not something we need to know, here we can have a look at how the Heikin Ashi candle is calculated." | "It means "average bar" and although this is not something we need to know, here is the Heikin Ashi candle formula for reference." | heikin ashi candle formula | 150 | H3 body | DONE |
| 4 | "### Renko" | "### Renko Charts" | renko charts | 400 | H3 | DONE |
| 5 | "Renko is similar to the range and tick charts. It eliminates the time factor from trading and changes the visuals of our chart completely." | "Renko charts are similar to the range and tick charts. They eliminate the time factor from trading and change the visuals of our chart completely." | renko charts | 400 | H3 body | DONE |
| 6 | "But tick charts, range charts, Renko or Heikin Ashi, can be utilized in our strategy and bring a lot of use to our personal trading." | "But tick charts, range charts, Renko charts or Heikin Ashi candles, can be utilized in our strategy and bring a lot of use to our personal trading." | renko charts + heikin ashi candles | 400 / 1400 | Conclusion | DONE |
| 7 | — | — | heikin ashi strategy | 250 | HA body | SKIP (PENDING — requires new content) |
| 8 | — | — | heikin ashi vs candles | 200 | HA section | SKIP (PENDING — requires new callout/section) |
| 9 | — | — | footprint chart, market profile, point and figure chart, order flow chart, kagi chart, line break chart, renko chart patterns, hollow candlestick, renko chart free | — | — | SKIP (out of article scope) |

**Naturally present — no change needed:**

- heikin ashi (2000): present throughout as "Heikin Ashi"
- candlestick charts (1000): present throughout
- tick chart / tick charts (700/100): present in body
- japanese candlesticks (200): present in Candlestick charts section
- range charts (100): present in body and conclusion
- ohlc charts (40): present in Bar charts section

---

## Step 2 Log: ToV Rewrite

**Topic classification:** BEGINNER

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "Watching the market fluctuations and volatility in real-time is an essential skill to acquire. There are several ways to display data on the chart, from a simple candlestick chart to Renko or Heikin Ashi. What are the specifics of these charts and how do they differ? You will find out in this lesson." | "Price data can be displayed on a chart in multiple ways — from standard **candlestick charts** to specialized formats like **Renko** or **Heikin Ashi candles**. Each type filters and presents price information differently. This lesson covers the specifics of each chart type and what distinguishes them." | ToV: throat-clearing opener + question format → principle-first; merged intro into single direct statement |
| 2 | "The ways of displaying data on our price chart are pretty much endless. This is why we will never find two traders that do and watch exactly the same things in their trading. Although most traders are using candlestick charts which we covered in the previous video, there is more depth in those as well. Besides candlestick charts, we will also have a look at different graphical representations of price charts such as bar charts, Renko or Heikin Ashi charts." | "Most traders use candlestick charts, covered in the Japanese Candlesticks lesson. There are alternatives worth understanding: bar charts, Renko, and Heikin Ashi candles. No two traders analyse charts in exactly the same way." | ToV: "pretty much endless" vague; "which we covered in the previous video" → lesson reference; "there is more depth in those as well" + "we will also have a look at" throat-clearing → direct enumeration |
| 3 | "We have covered Japanese candlesticks in the previous lesson, so we will do just a quick recap now. They are the most popular methods of charting and viewing technical analysis. The anatomy of a candlestick consists of the body and the wick. If the candle closes above the open, we have a bullish candlestick. If the candle closes below the open, we look at a bearish candlestick. Wicks represent the highest and lowest points where the market traded." | "Japanese candlesticks are covered in the previous lesson — this is a quick recap. They are the most popular charting method for technical analysis. The anatomy consists of the **body** and the **wick**. A candle closing above its open is bullish; closing below is bearish. Wicks mark the highest and lowest points of the trading range." | ToV: "just" filler removed; "we look at a bearish candlestick" informal → direct; "represent" → "mark"; "trading range" tighter than "where the market traded" |
| 4 | "As we can see in the image below, we have two candlestick charts next to each other in our FTMO cTrader platform." | "The two charts below are both candlestick charts displayed in the FTMO cTrader platform — but they are not the same." | ToV: "As we can see" filler → lead with the contrast that follows |
| 5 | "Although they look the same, there is one significant difference between them. The chart on the left is based on time and the chart on the right is not. The chart periodicity is the main function we can control when setting up our candlestick chart. The time periodicity is the most popular and common amongst traders. Most trading platforms will allow us to set up charts based on minutes, hours, days, weeks, and seconds. The most popular charts used by traders are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly and monthly charts. Although we can set up our chart with any setting we want, using those popular timeframes works simply because many traders are also watching them. If we use something like a 40-minute or 3-hour chart, the candlestick patterns on our chart might have a lower weight as no other traders see them. The non-time-based charts are less common, but they still can give traders valuable information. Our traders can use tick and range charts in our FTMO cTrader platform, these two are also the most popular non-time-based charts. In the tick chart, one tick represents one transaction. In other words, one tick is made when the market fluctuates by the minimal price increment." | "The chart on the left is time-based; the chart on the right is not. **Chart periodicity** is the primary setting when configuring a candlestick chart. Time-based periodicity is the most widely used option — most platforms support minutes, hours, days, weeks, and seconds. ¶ The most popular timeframes are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly, and monthly. Using standard timeframes is effective because many traders watch the same levels. A non-standard chart — such as 40-minute or 3-hour — produces candlestick patterns that fewer traders observe, which reduces their significance. ¶ Time is not the only way to structure a chart. **Tick and range charts** are the most popular non-time-based alternatives available in the FTMO cTrader platform. In a tick chart, one tick represents one transaction — it forms each time the market moves by the minimum price increment." | ToV: 160+ word paragraph split into 3; "might have a lower weight" → "reduces their significance"; "Our traders can use" institutional phrasing removed; "In other words" filler removed; "Although they look the same, there is one significant difference" → dropped, contrast moved to row 4 |
| 6 | "If we take a look at EURUSD, which is quoted in five decimal places. One tick would equal 0.00001 or 1 pipette. In the range bar, every bar will end once the range between its high and low equals the chosen range. This means that every bar will have the same bar range and close either at high or low. Using a range of tick charts can eliminate noise and display trends in a much clearer picture as we will get rid of time periods when markets are not moving and staying range-bound. This can be clearly seen when we compare this DAX four-hour chart with the 100 range chart in cTrader. We can notice that both uptrend and downtrend were much cleaner on the range chart once we eliminated the time factor and put our focus on price rotations." | "For EURUSD, quoted in five decimal places, one tick equals 0.00001 — or 1 pipette. In a range bar, each bar closes when the distance between its high and low reaches the chosen range value. Every range bar has an identical high-to-low range and closes at either its high or low. ¶ Tick and range charts eliminate noise and display trends more clearly by removing time periods when markets are inactive. The difference is visible when comparing a DAX four-hour chart with the 100-range chart in cTrader — both the uptrend and downtrend appeared cleaner on the range chart once the time factor was removed and the focus shifted to price rotations." | ToV: "If we take a look at" → direct; fragment sentence merged; "This can be clearly seen when we compare" → "The difference is visible when"; "We can notice that" filler removed; paragraph split into 2 |
| 7 | "The only difference between the candlestick and the bar chart is the visual representation." | "The only difference between a candlestick and a bar chart is the visual representation." | ToV: "the candlestick" → "a candlestick" — removes false definiteness |
| 8 | "Bar charts, often called OHLC charts, are represented as vertical bars with two notches that represent the open and close of the bar. Compared to Japanese candlesticks, bar charts might be a little less clean for new traders when it comes to candlestick patterns. On the other hand, they might present a little cleaner picture when it comes to marking out support and resistance." | "**Bar charts**, often called **OHLC charts**, display as vertical bars with two notches indicating the open and close. Candlestick patterns are harder to read on bar charts, making them less intuitive for traders still learning to identify formations. However, bar charts can present a cleaner picture when marking out support and resistance levels." | ToV: "are represented as...that represent" double → "display as...indicating"; "might be a little less clean" hedging → direct; "when it comes to" (×2) filler removed; "On the other hand" → "However" |
| 9 | "Renko charts are similar to the range and tick charts. They eliminate the time factor from trading and change the visuals of our chart completely. We won't see candlesticks anymore, but we will be looking at bricks instead. The name Renko came from the Japanese renga, which stands for brick." | "**Renko charts** eliminate the time factor entirely and display only significant price movements. Instead of candlesticks, the chart uses **bricks** — each representing a fixed price increment. The name comes from the Japanese renga, meaning brick." | ToV: "are similar to range and tick charts" doesn't lead with value → principle-first; "We won't see candlesticks anymore, but we will be looking at bricks instead" informal → direct; "which stands for brick" → "meaning brick" |
| 10 | "The Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. Let's say we define that one brick signifies a movement of 5 pips. So, until the market moves these 5 pips in one direction (from the close of the last brick), no more bricks will be drawn. Renko charts are not only great for filtering out noise but also for marking out support and resistance areas." | "A new brick appears when the market moves more than the **brick size** away from the previous brick. If one brick represents a 5-pip movement, no new brick forms until price travels those 5 pips from the last brick's close. This makes Renko charts effective for filtering out noise and identifying support and resistance areas." | ToV: "Let's say we define" informal → "If one brick represents"; "no more bricks will be drawn" passive → "no new brick forms"; "are not only great for...but also for marking out" → direct connector; "marking out" → "identifying" |
| 11 | "Heikin Ashi candles are another chart representation that comes from Japan. It means "average bar" and although this is not something we need to know, here is the Heikin Ashi candle formula for reference. The Heikin Ashi is constructed the same way as the candlestick chart but has a different calculation method. We can set up a Heikin Ashi chart as we want, on the specified time, range or tick." | "**Heikin Ashi candles** are a Japanese chart type built on a different calculation method than standard candlesticks. The name translates as "average bar." The formula itself is not required knowledge — but for reference, here is the Heikin Ashi candle formula. Structurally, Heikin Ashi candles follow the same format as standard candlesticks. A Heikin Ashi chart can be configured for time-based, range, or tick settings." | ToV: "are another chart representation" weak opener → principle-first; "It means" dangling → "The name translates as"; "The Heikin Ashi is constructed the same way as" → "Structurally, Heikin Ashi candles follow the same format as"; "We can set up...as we want" informal → direct |
| 12 | "Heikin Ashi filters out the movements and makes a much easier approach to trend following. The downside of it is that we might miss some valuable information as it might smooth out the chart a little too much. But it is a great tool for both entries and trade management." | "Heikin Ashi filters out minor price movements and produces a more straightforward view for trend following. The trade-off: the smoothing effect can obscure important price information. It is an effective tool for both entries and trade management." | ToV: "filters out the movements" vague → "minor price movements"; "makes a much easier approach" → "produces a more straightforward view"; "The downside of it is that we might miss some valuable information as it might smooth out the chart a little too much" wordy → concise; "But" opener + "great" → "effective" |
| 13 | "To conclude this chapter, the best thing we can do is to play with different charts and settings and find what suits us the best, that is always the smartest approach. Regular time-based candlestick charts will always be the most popular as they are used by traders worldwide. But tick charts, range charts, Renko charts or Heikin Ashi candles, can be utilized in our strategy and bring a lot of use to our personal trading." | "Start with candlestick charts — they are the industry standard, used by traders worldwide. Once comfortable reading price action, experiment with Heikin Ashi candles or Renko charts to see whether noise reduction improves your decision-making. Tick charts and range charts serve the same purpose, removing inactive time periods to reveal cleaner trends." | ToV: "To conclude this chapter, the best thing we can do is to play" throat-clearing → action-oriented opener; "that is always the smartest approach" removed; "bring a lot of use to our personal trading" vague → specific benefit; "But" opener removed |

---

## Step 3 Log: Structure & Formatting

**Article length:** SHORT (~650 words)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H1 updated | "Types of Trading Charts" → "Types of Trading Charts: Candlestick, Renko & Heikin Ashi" | SEO: descriptive title with primary keywords in H1 |
| 2 | Meta block added | Prerequisites callout + Last Updated date + `---` separator inserted before body | E-E-A-T: learning path, version control |
| 3 | H2 removed | Redundant section heading "Types of trading charts – candlestick chart, Renko, Heikin Ashi" removed | Structure: duplicate of H1; no informational value |
| 4 | H3 → H2 | "### Candlestick Charts" → "## Candlestick Charts" | Structure: top-level section, not a subsection |
| 5 | H3 → H2 | "### Bar Charts" → "## Bar Charts" | Structure: top-level section, not a subsection |
| 6 | H3 → H2 | "### Renko Charts" → "## Renko Charts" | Structure: top-level section, not a subsection |
| 7 | H3 → H2 | "### Heikin Ashi Candles" → "## Heikin Ashi Candles" | Structure: top-level section, not a subsection |
| 8 | H3 → H2 | "### Conclusion" → "## Conclusion" | Structure: top-level section, not a subsection |
| 9 | H3 added | "### Time-Based Charts" added under ## Candlestick Charts | Structure: logical subsection for time-based periodicity content |
| 10 | H3 added | "### Non-Time-Based Charts" added under ## Candlestick Charts | Structure: logical subsection for tick/range chart content |
| 11 | Sentence removed | "The two charts below are both candlestick charts displayed in the FTMO cTrader platform — but they are not the same." removed | Structure: made redundant by new H3 "Time-Based Charts" which contextualises the image |
| 12 | Alt text added | Image 1: `![Candlestick anatomy showing body and wick structure](...)` | E-E-A-T: accessibility + image SEO |
| 13 | Alt text added | Image 2: `![Time-based vs range chart comparison in FTMO cTrader](...)` | E-E-A-T: accessibility + image SEO |
| 14 | Alt text added | Image 3: `![Bar chart (OHLC) example](...)` | E-E-A-T: accessibility + image SEO |
| 15 | Alt text added | Image 4: `![Renko chart example](...)` | E-E-A-T: accessibility + image SEO |
| 16 | Alt text added | Image 5: `![Heikin Ashi chart example](...)` | E-E-A-T: accessibility + image SEO |
| 17 | Paragraph split | "The most popular timeframes are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly, and monthly. Using standard timeframes is effective because many traders watch the same levels. A non-standard chart — such as 40-minute or 3-hour — produces candlestick patterns that fewer traders observe, which reduces their significance." split: first sentence remains as standalone paragraph; second and third sentences moved into Tip callout | Structure: paragraph audit — single-sentence break improves scan; actionable advice suits Tip format |
| 18 | Callout added | Tip: "Using standard timeframes is effective because many traders watch the same levels. A non-standard chart — such as 40-minute or 3-hour — produces candlestick patterns that fewer traders observe, which reduces their significance." | Formatting: actionable advice → Tip callout per guide |
| 19 | Sentence removed | "It is an effective tool for both entries and trade management." removed from Heikin Ashi body paragraph | Structure: content preserved in Note callout (row 20); avoids duplication |
| 20 | Callout added | Note: "Because Heikin Ashi uses averaged data, it is an effective tool for both entries and trade management — but consider using it alongside regular candlestick charts for precise entry and exit levels." | Formatting: nuanced advice + trade-off context → Note callout |
| 21 | Callout added | Keep in Mind: "When using any chart type for technical analysis, be aware of these common tendencies: Seeing patterns where there are none / Assuming past chart patterns predict future price movements / Favouring a chart type because it confirms an existing bias" | Formatting: cognitive bias warning → Keep in Mind callout per guide (1 per TA lesson) |
| 22 | Table added | Chart type comparison table (5 rows: Candlestick, Bar/OHLC, Renko, Heikin Ashi, Tick/Range) with columns: Chart Type, Time-Based, Best For, Trade-off | Formatting: comparison data → table per guide; improves scannability |
| 23 | Internal link added | "Most traders use candlestick charts, covered in the [Japanese Candlesticks](/lesson/japanese-candlesticks/) lesson." | Navigation: cross-reference to prerequisite lesson |
| 24 | Internal link added | "However, bar charts can present a cleaner picture when marking out [support and resistance](/lesson/support-and-resistance/) levels." | Navigation: related concept link |
| 25 | Internal link added | "This makes Renko charts effective for filtering out noise and identifying [support and resistance](/lesson/support-and-resistance/) areas." | Navigation: related concept link |
| 26 | Internal link added | "**Bar charts** convey identical information to candlesticks but offer a cleaner view of [support and resistance](/lesson/support-and-resistance/) levels" (Key Takeaways) | Navigation: reinforces related concept link in summary |
| 27 | `---` separator added | Horizontal rule added before Key Takeaways section | Structure: visual separation between body and summary elements |
| 28 | H3 + list added | "### Key Takeaways" with 6 bullet points summarising all chart types | E-E-A-T: learning reinforcement; scannable summary per guide |
| 29 | H3 + list added | "### Next Steps" with 3 internal links: Technical Indicators, Chart Patterns Trading, Market Environment | Navigation: always-required end element per guide |
| 30 | `---` + author block added | `---` + Author, Role, Last Updated | E-E-A-T: author attribution per guide |
| 31 | Callout added | Educational Content Notice: "This material is for educational purposes only and does not constitute financial advice. Trading decisions should be based on your own analysis and risk tolerance." | E-E-A-T: YMYL educational notice per guide |
| 32 | Callout added | Risk Warning: "Trading involves significant risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose." | E-E-A-T: YMYL risk disclaimer — mandatory per guide |

---

## Step 4 Log: HTML Conversion

**Output file:** `lesson_types-of-trading-charts_EN.html`

| # | Element | Description |
|---|---------|-------------|
| 1 | `<title>` | "Types of Trading Charts: Candlestick, Renko & Heikin Ashi | FTMO Academy" |
| 2 | `<meta name="description">` | Unique description with primary keywords |
| 3 | `<meta name="keywords">` | candlestick charts, heikin ashi candles, renko charts, heikin ashi candle formula, tick chart, ohlc charts |
| 4 | `<meta property="og:*">` | Open Graph tags for title, description, type |
| 5 | Sticky header | FTMO brand nav with Get Funded CTA |
| 6 | Breadcrumb | Academy > Technical Analysis > Types of Trading Charts |
| 7 | Lesson header | Module label "Technical Analysis — Lesson 2", H1, last updated meta |
| 8 | Prerequisites callout | Blue callout, link to /lesson/japanese-candlesticks/ |
| 9 | H2 sections | Candlestick Charts, Bar Charts, Renko Charts, Heikin Ashi Candles, Conclusion |
| 10 | H3 subsections | Time-Based Charts, Non-Time-Based Charts (under Candlestick Charts) |
| 11 | Images (×5) | All images with alt text, `lesson-img` class |
| 12 | Tip callout | `.callout--tip` — timeframe advice |
| 13 | Note callout | `.callout--note` — Heikin Ashi trade-off |
| 14 | Keep in Mind callout | `.callout--keep-in-mind` — cognitive biases list |
| 15 | Comparison table | `.table-wrap > table` — 5 chart types × 4 columns |
| 16 | Key Takeaways box | `.key-takeaways` — 6 bullet points |
| 17 | Next Steps | 3 internal links (Technical Indicators, Chart Patterns, Market Environment) |
| 18 | Author box | `.author-box` — FTMO Academy Content Team, March 5, 2026 |
| 19 | Educational Notice | `.disclaimer-educational` |
| 20 | Risk Warning | `.disclaimer-risk` |
| 21 | Footer | FTMO brand footer with Learn + FTMO link columns |
| 22 | CSS | Full FTMO brand styles — Azure #0781fe, Torea Bay #123a83, Poppins font, responsive |
