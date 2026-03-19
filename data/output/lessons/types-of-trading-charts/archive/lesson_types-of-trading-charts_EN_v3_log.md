# Types of Trading Charts: Candlestick, Renko & Heikin Ashi - Edit Log v3

**Article:** `lesson_types-of-trading-charts_EN_v3.md`
**Source:** https://academy.ftmo.com/lesson/types-of-trading-charts/
**Date:** 2026-03-05

---

## Step 1 Log: Keywords

**Keywords file:** `types_of_trading_charts_keywords.xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | H1: "Types of Trading Charts" | H1: "Types of Trading Charts: Candlestick, Renko & Heikin Ashi" | heikin ashi + candlestick charts | 2000+1000 | H1 | DONE |
| 2 | H3: "Renko" | H3: "Renko Charts" | renko charts | 400 | H3 heading | DONE |
| 3 | "Heikin Ashi is another chart representation" | "Heikin Ashi candles are another chart representation" | heikin ashi candles | 1400 | H3 body | DONE |
| 4 | "Renko is similar to the range and tick charts." | "Renko charts are similar to the range and tick charts." | renko charts | 400 | H3 body | DONE |
| 5 | "here we can have a look at how the Heikin Ashi candle is calculated" | "here we can have a look at the Heikin Ashi candle formula" | heikin ashi candle formula | 150 | H3 body | DONE |
| 6 | H3: "Heikin Ashi" → "Heikin Ashi Candles Explained" | unchanged | heikin ashi candles explained | 250 | H3 heading | REJECTED |
| - | heikin ashi (2000) | already present in H3 heading | heikin ashi | 2000 | H3 | DONE |
| - | candlestick charts (1000) | already present in H3 + body | candlestick charts | 1000 | H3/body | DONE |
| - | tick chart / tick charts (700/100) | already present in body | tick chart / tick charts | 700/100 | body | DONE |
| - | japanese candlesticks (200) | already present in body | japanese candlesticks | 200 | body | DONE |
| - | renko chart (200) | already present in body | renko chart | 200 | body | DONE |
| - | range charts (100) | already present in body | range charts | 100 | body | DONE |
| - | ohlc charts (40) | already present in body | ohlc charts | 40 | body | DONE |
| - | footprint chart (700) | not in article | footprint chart | 700 | - | SKIP |
| - | market profile (500) | not in article | market profile | 500 | - | SKIP |
| - | point and figure chart (400) | not in article | point and figure chart | 400 | - | SKIP |
| - | order flow chart (250) | not in article | order flow chart | 250 | - | SKIP |
| - | heikin ashi strategy (250) | not in article | heikin ashi strategy | 250 | - | SKIP |
| - | renko chart patterns (200) | not in article | renko chart patterns | 200 | - | SKIP |
| - | kagi chart (90) | not in article | kagi chart | 90 | - | SKIP |
| - | hollow candlestick (50) | not in article | hollow candlestick | 50 | - | SKIP |
| - | line break chart (40) | not in article | line break chart | 40 | - | SKIP |

---

## Step 2 Log: ToV Rewrite

**Guide:** `ftmo_academy_tov_guide_EN.md`
**Topic classification:** BEGINNER

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "Watching the market fluctuations and volatility in real-time is an essential skill to acquire." | "Monitoring real-time market movements is an essential trading skill." | ToV: vague opener tightened; "Watching" -> "Monitoring"; redundant "fluctuations and volatility" simplified |
| 2 | "What are the specifics of these charts and how do they differ? You will find out in this lesson." | "This lesson covers the specifics of each chart type and how they differ." | ToV: BEGINNER style direct statement replaces rhetorical question + filler "You will find out" |
| 3 | "The ways of displaying data on our price chart are pretty much endless." | "The ways of displaying data on a price chart are nearly endless." | ToV: casual marker "pretty much" -> "nearly" |
| 4 | "This is why we will never find two traders that do and watch exactly the same things in their trading." | "No two traders analyse charts in exactly the same way." | ToV: "This is why we will never find" -> direct statement; awkward "do and watch" -> "analyse"; tightened |
| 5 | "Although most traders are using candlestick charts which we covered in the previous video, there is more depth in those as well." | "Although most traders use candlestick charts, which we covered in the previous lesson, there is more depth to explore." | ToV: "are using" -> "use"; "previous video" -> "previous lesson"; "more depth in those as well" -> "more depth to explore" |
| 6 | "Besides candlestick charts, we will also have a look at different graphical representations of price charts such as bar charts, Renko or Heikin Ashi charts." | "This lesson also covers bar charts, Renko, and Heikin Ashi charts." | ToV: "have a look at" -> casual -> "covers"; redundant "graphical representations of price charts" removed |
| 7 | "We have covered Japanese candlesticks in the previous lesson, so we will do just a quick recap now." | "Japanese candlesticks are covered in the previous lesson. Here is a quick recap." | ToV: "just" filler removed; split into two direct sentences; BEGINNER pacing |
| 8 | "They are the most popular methods of charting and viewing technical analysis." | "They are the most popular charting method for technical analysis." | ToV: "methods of charting and viewing technical analysis" -> awkward -> tightened |
| 9 | "If the candle closes below the open, we look at a bearish candlestick." | "If the candle closes below the open, we have a bearish candlestick." | ToV: "we look at" -> inconsistent with parallel "we have" in preceding sentence; parallel structure applied |
| 10 | "As we can see in the image below, we have two candlestick charts next to each other in our FTMO cTrader platform." | "The image below shows two candlestick charts displayed side by side in the FTMO cTrader platform." | ToV: "As we can see" -> filler removed; active structure; "next to each other" -> "side by side" |
| 11 | "The time periodicity is the most popular and common amongst traders." | "Time-based periodicity is the most widely used option among traders." | ToV: "popular and common" -> redundant -> "most widely used"; "amongst" -> "among" |
| 12 | "Most trading platforms will allow us to set up charts based on minutes, hours, days, weeks, and seconds." | "Most trading platforms allow traders to set up charts based on minutes, hours, days, weeks, and seconds." | ToV: "will allow us" -> "allow traders" (professional, present tense) |
| 13 | "Although we can set up our chart with any setting we want, using those popular timeframes works simply because many traders are also watching them." | "Using those standard timeframes is effective because many traders are also watching them." | ToV: "Although we can set up our chart with any setting we want" -> filler removed; "works simply" -> "is effective"; "popular" -> "standard" |
| 14 | "If we use something like a 40-minute or 3-hour chart, the candlestick patterns on our chart might have a lower weight as no other traders see them." | "If we use a non-standard chart like a 40-minute or 3-hour setting, candlestick patterns carry less weight because other traders are not watching those levels." | ToV: "something like" -> "a non-standard chart like"; "might have a lower weight" -> "carry less weight"; "as" -> "because" |
| 15 | "The non-time-based charts are less common, but they still can give traders valuable information." | "Non-time-based charts are less common, but they can still provide valuable information." | ToV: word order "still can" -> "can still"; "give" -> "provide" |
| 16 | "Our traders can use tick and range charts in our FTMO cTrader platform, these two are also the most popular non-time-based charts." | "Traders can use tick and range charts in the FTMO cTrader platform — these are the most popular non-time-based chart types." | ToV: "Our traders" -> "Traders"; comma splice fixed with em dash |
| 17 | "In other words, one tick is made when the market fluctuates by the minimal price increment." | "A tick forms each time the market moves by the minimum price increment." | ToV: "is made when" -> passive -> "forms"; "fluctuates" -> "moves"; "minimal" -> "minimum" |
| 18 | "If we take a look at EURUSD, which is quoted in five decimal places. One tick would equal 0.00001 or 1 pipette." | "For EURUSD, quoted in five decimal places, one tick equals 0.00001, or 1 pipette." | ToV: sentence fragment fixed; "take a look at" -> removed; "would equal" -> "equals"; two sentences merged |
| 19 | "In the range bar, every bar will end once the range between its high and low equals the chosen range." | "In a range bar, each bar closes when the distance between its high and low reaches the chosen range value." | ToV: "will end once" -> "closes when" (active, present tense) |
| 20 | "This means that every bar will have the same bar range and close either at high or low." | "Every range bar has an identical high-to-low range and closes at either the high or low." | ToV: "This means that" -> filler removed; "will have" -> "has" (present tense) |
| 21 | "Using a range of tick charts can eliminate noise and display trends in a much clearer picture as we will get rid of time periods when markets are not moving and staying range-bound." | "Using tick and range charts eliminates noise and displays trends more clearly by removing time periods when markets are inactive." | ToV: "a range of tick charts" -> "tick and range charts"; "in a much clearer picture" -> "more clearly"; "get rid of" -> "removing" |
| 22 | "This can be clearly seen when we compare this DAX four-hour chart with the 100 range chart in cTrader." | "This becomes clear when comparing a DAX four-hour chart with the 100-range chart in cTrader." | ToV: "This can be clearly seen when we compare" -> "This becomes clear when comparing" (active, direct) |
| 23 | "We can notice that both uptrend and downtrend were much cleaner on the range chart once we eliminated the time factor and put our focus on price rotations." | "Both the uptrend and downtrend appeared cleaner on the range chart once we removed the time factor and focused on price rotations." | ToV: "We can notice that" -> filler removed; "put our focus on" -> "focused on" |
| 24 | "Bar charts, often called OHLC charts, are represented as vertical bars with two notches that represent the open and close of the bar." | "Bar charts, often called OHLC charts, display as vertical bars with two notches indicating the open and close." | ToV: "are represented as" -> passive -> "display as"; "that represent" -> "indicating" |
| 25 | "Compared to Japanese candlesticks, bar charts might be a little less clean for new traders when it comes to candlestick patterns." | "In practice, candlestick patterns are harder to read on bar charts, making them less intuitive for traders learning to identify formations." | ToV: "a little less clean" -> hedging -> "harder to read"; "might be" removed |
| 26 | "On the other hand, they might present a little cleaner picture when it comes to marking out support and resistance." | "On the other hand, bar charts can present a cleaner picture when marking out support and resistance levels." | ToV: "they might" -> "bar charts can" (confident, direct); "a little cleaner" -> "a cleaner" |
| 27 | "It eliminates the time factor from trading and changes the visuals of our chart completely." | "They eliminate the time factor from trading and change the chart's visual presentation entirely." | ToV: pronoun "It" -> "They" (agrees with plural "Renko charts"); "visuals of our chart" -> "chart's visual presentation" |
| 28 | "We won't see candlesticks anymore, but we will be looking at bricks instead." | "Instead of candlesticks, the chart displays bricks." | ToV: future tense -> present; direct statement |
| 29 | "Let's say we define that one brick signifies a movement of 5 pips." | "For example, if one brick represents a 5-pip movement," | ToV: "Let's say" -> casual -> "For example"; tightened into conditional clause |
| 30 | "So, until the market moves these 5 pips in one direction (from the close of the last brick), no more bricks will be drawn." | "Until the market moves those 5 pips in one direction from the last brick's close, no new bricks appear." | ToV: "So," -> filler removed; "will be drawn" -> passive -> "appear" |
| 31 | "Renko charts are not only great for filtering out noise but also for marking out support and resistance areas." | "Renko charts are effective not only for filtering out noise but also for identifying support and resistance areas." | ToV: "great" -> hype word -> "effective"; "marking out" -> "identifying" |
| 32 | "It means 'average bar' and although this is not something we need to know, here we can have a look at the Heikin Ashi candle formula." | "It means 'average bar.' While the formula itself is not strictly necessary to know, here is the Heikin Ashi candle formula for reference." | ToV: "here we can have a look at" -> casual -> "here is"; split into two sentences |
| 33 | "The Heikin Ashi is constructed the same way as the candlestick chart but has a different calculation method." | "Heikin Ashi candles follow the same structure as standard candlesticks but use a different calculation method." | ToV: "is constructed" -> passive -> "follow"; keyword "Heikin Ashi candles" preserved |
| 34 | "We can set up a Heikin Ashi chart as we want, on the specified time, range or tick." | "A Heikin Ashi chart can be configured for time-based, range, or tick settings." | ToV: "as we want" -> casual -> removed; "specified time" -> "time-based" |
| 35 | "Heikin Ashi filters out the movements and makes a much easier approach to trend following." | "Heikin Ashi filters out minor price movements and supports a more straightforward approach to trend following." | ToV: "the movements" -> "minor price movements"; "much easier" -> "more straightforward" (avoids prohibited "easy") |
| 36 | "The downside of it is that we might miss some valuable information as it might smooth out the chart a little too much." | "The trade-off is that the smoothing effect can obscure important price information." | ToV: "The downside of it is" -> "The trade-off is"; tightened; "a little too much" hedging removed |
| 37 | "But it is a great tool for both entries and trade management." | "However, it is an effective tool for both entries and trade management." | ToV: "But" at sentence start -> "However,"; "great" -> "effective" |
| 38 | "To conclude this chapter, the best thing we can do is to play with different charts and settings and find what suits us the best, that is always the smartest approach." | "The best approach is to experiment with different chart types and settings to find what fits your trading style." | ToV: "To conclude this chapter" -> filler removed; "play with" -> "experiment with"; BEGINNER direct address |
| 39 | "But tick charts, range charts, Renko or Heikin Ashi, can be utilized in our strategy and bring a lot of use to our personal trading." | "However, tick charts, range charts, Renko, and Heikin Ashi can all be incorporated into a trading strategy and add significant value." | ToV: "But" -> "However,"; "bring a lot of use" -> vague -> "add significant value" |

---

## Step 3 Log: Structure & Formatting

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H2 removed | H2 "Types of trading charts – candlestick chart, Renko, Heikin Ashi" removed | Structure: redundant with H1; intro text kept as body paragraph |
| 2 | H3 -> H2 | "Candlestick charts" promoted from H3 to H2 | Structure: major independent section deserves H2 weight |
| 3 | H3 -> H2 | "Bar charts" promoted from H3 to H2 | Structure: major independent section deserves H2 weight |
| 4 | H3 -> H2 | "Renko Charts" promoted from H3 to H2 | Structure: major independent section deserves H2 weight |
| 5 | H3 -> H2 | "Heikin Ashi" promoted from H3 to H2 | Structure: major independent section deserves H2 weight |
| 6 | H3 added | "Time-Based Charts" under H2 Candlestick Charts | Structure: long section split into two logical subsections |
| 7 | H3 added | "Non-Time-Based Charts" under H2 Candlestick Charts | Structure: tick/range charts logically separate from time-based |
| 8 | List added | Popular timeframes (1M, 5M, 15M...) converted to bullet list | Formatting: prose enumeration -> scannable list |
| 9 | List added | Tick chart / Range chart converted to bullet list with bold labels | Formatting: two-item comparison -> parallel bullet structure |
| 10 | Callout added | Tip in Time-Based Charts: standard timeframes + non-standard warning | Structure Guide: actionable advice -> Tip callout |
| 11 | Callout added | Note in Heikin Ashi: averaged data + use alongside candlesticks | Structure Guide: important limitation -> Note callout |
| 12 | Callout added | Keep in Mind before Conclusion: cognitive biases in chart analysis | Structure Guide: 1 Keep in Mind per TA lesson |
| 13 | Table added | Chart type comparison (Candlestick / Bar / Renko / Heikin Ashi) in Conclusion | Formatting: 4 items compared across multiple attributes -> table |
| 14 | Section added | Key Takeaways (6-item bullet list) | Structure Guide: lesson template requires Key Takeaways |
| 15 | Section added | Next Steps with 3 internal links | Structure Guide: lesson template requires Next Steps |
| 16 | Internal link | [Japanese Candlesticks](/lesson/japanese-candlesticks/) in intro paragraph | Structure Guide: prerequisite linked inline; anchor text = lesson title |
| 17 | Internal link | [support and resistance](/lesson/support-and-resistance/) in Bar Charts body | Structure Guide: related concept linked inline |
| 18 | Internal link | [support and resistance](/lesson/support-and-resistance/) in Renko Charts body | Structure Guide: related concept linked inline |
| 19 | Internal link | [Technical Indicators](/lesson/technical-indicators/) in Next Steps | Content Inventory: Links To — Technical Indicators |
| 20 | Internal link | [Chart Patterns Trading](/lesson/chart-patterns-trading/) in Next Steps | Content Inventory: Links To — Chart Patterns |
| 21 | Internal link | [Market Environment: Range vs. Trend](/lesson/market-environment-range-vs-trend/) in Next Steps | Related: trend/range context relevant to chart type selection |
| 22 | Bold added | body, wick, Chart periodicity, tick and range charts, Bar charts, OHLC charts, Renko charts, bricks, brick size, Heikin Ashi candles | Structure Guide: bold for key terms on first use |
| 23 | Prerequisites added | [Japanese Candlesticks] at top (markdown only) | Structure Guide: always state prerequisites; not in HTML |
| 24 | E-E-A-T added | Author box + Last Updated date | Structure Guide: required in every article |
| 25 | E-E-A-T added | Educational Content Notice + Risk Warning at end | Structure Guide: required for all YMYL content |
| 26 | HR separators | --- between H2 sections | Structure Guide: visual breaks between major thematic shifts |

---

## Summary

| Step | Status | Changes |
|------|--------|---------|
| Step 1: Keywords | DONE | 5 changes (4 DONE + P1 approved + P2 rejected) |
| Step 2: ToV Rewrite | DONE | 39 sentence-level changes |
| Step 3: Structure | DONE | 26 structural changes (6 internal links, 3 callouts, 1 table, 2 lists) |
| Step 4: HTML | DONE | v3 HTML generated |
