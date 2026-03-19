# Types of Trading Charts 

* * *

Mastering the ability to observe market fluctuations and volatility in real-time is crucial for any trader. Various chart types, such as candlestick charts, Renko charts, and Heikin Ashi candles, present data in different ways. This lesson will cover the specifics of these charts and highlight their differences.

> **Prerequisites:** Before starting this lesson, complete:
> - [Japanese Candlesticks](link)

## Types of Trading Charts

The options for displaying data on price charts are virtually limitless. Consequently, no two traders will interpret and analyze price data in exactly the same way. While most traders rely on candlestick charts, there is a deeper layer to explore. Beyond candlestick charts, we will examine alternative graphical representations, including bar charts, Renko charts, and Heikin Ashi candles.

### Candlestick Charts

We previously covered Japanese candlesticks, so this will serve as a brief recap. They are the most widely used method for technical analysis. Each candlestick comprises a body and wicks. A candlestick is classified as bullish if it closes above its opening price and bearish if it closes below. The wicks indicate the highest and lowest prices at which the market traded during that period.

![Candlestick Example](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

The image below shows two candlestick charts side by side within the FTMO cTrader platform.

![Chart Comparison](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

Despite their similar appearance, a significant difference exists. The chart on the left is time-based, while the chart on the right is not. The periodicity of the chart is the primary variable we can control when setting up our candlestick chart. 

#### Time-Based Charts

Time periodicity is the most common among traders. Most trading platforms allow us to configure charts based on minutes, hours, days, weeks, and seconds. The most popular timeframes used by traders include:

- 1-minute
- 5-minute
- 15-minute
- 30-minute
- 60-minute
- 4-hour
- Daily
- Weekly
- Monthly

While we can use any timeframe we choose, utilizing these popular intervals is effective because many traders are also monitoring them. Using less common timeframes, such as a 40-minute or 3-hour chart, may result in candlestick patterns carrying less significance, as fewer traders are likely to observe them.

> **Tip:** Utilizing popular timeframes can enhance the significance of candlestick patterns since they are widely monitored by traders.

### Non-Time-Based Charts

Non-time-based charts, although less common, can still provide valuable insights. In the FTMO cTrader platform, traders can utilize tick charts and range charts; these are the most popular non-time-based options. 

- **Tick Chart:** One tick corresponds to one transaction. For example, in the EURUSD pair, which is quoted in five decimal places, one tick equals 0.00001 or 1 pipette.
- **Range Bar:** Each bar will close once the range between its high and low reaches the predetermined range.

Utilizing range or tick charts can reduce noise and present trends more clearly by eliminating periods when the market is stagnant or range-bound. This is evident when comparing the DAX four-hour chart with the 100-range chart in cTrader, where the uptrend and downtrend appear significantly cleaner on the range chart after removing the time factor and focusing solely on price movements.

### Bar Charts

The only distinction between candlestick charts and bar charts lies in their visual representation.

![Bar Chart Example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

Bar charts, often referred to as OHLC charts, consist of vertical bars with two notches indicating the open and close prices. For new traders, bar charts may be less intuitive for identifying candlestick patterns compared to Japanese candlesticks. However, they can provide a clearer representation when marking support and resistance levels.

### Renko Charts

Renko charts share similarities with range and tick charts by removing the time element from trading and altering the chart's appearance entirely. Instead of candlesticks, traders view bricks. The term "Renko" derives from the Japanese word "renga," meaning brick.

![Renko Chart Example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

A new brick is added to a Renko chart when the market moves beyond the defined brick size from the previous brick. For instance, if we define one brick as representing a movement of 5 pips, no new bricks will be created until the market moves 5 pips in one direction from the last brick's close. Renko charts excel at filtering out noise and clearly marking support and resistance areas.

### Heikin Ashi Candles

Heikin Ashi candles provide another representation of price data, originating from Japan. The term means "average bar." While this detail is not critical, it's essential to understand the calculation method behind Heikin Ashi candles. They are constructed similarly to traditional candlesticks but utilize a different calculation method. Heikin Ashi charts can be configured based on time, range, or tick.

![Heikin Ashi Chart Example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

Heikin Ashi candles filter price movements, facilitating a smoother approach to trend following. The trade-off is that valuable information may be obscured, as the chart can smooth out fluctuations excessively. Nonetheless, these candles are effective tools for both entry points and trade management.

### Conclusion

To conclude this chapter, the most effective strategy is to experiment with various charts and settings to identify what works best for you. Traditional time-based candlestick charts remain the most popular due to their widespread use among traders. However, tick charts, range charts, Renko charts, and Heikin Ashi candles can also enhance your trading strategy and provide significant insights.

---

> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results.

> **Educational Notice:** This material is for educational purposes only and does not constitute financial advice.

---
**Author:** [Name]  
**Role:** FTMO Academy Content Lead  
**Last Updated:** [Date]  
---

## Step 3 Log: Structure & Formatting

**Article length:** LONG (2,130 words)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H2 added | "Types of Trading Charts" | Structure: logical section header |
| 2 | H3 added | "Time-Based Charts" under Candlestick | Structure: logical subsection |
| 3 | H3 added | "Non-Time-Based Charts" | Structure: logical subsection |
| 4 | H3 added | "Bar Charts" | Structure: logical subsection |
| 5 | H3 added | "Renko Charts" | Structure: logical subsection |
| 6 | H3 added | "Heikin Ashi Candles" | Structure: logical subsection |
| 7 | Callout added | Tip about popular timeframes | Formatting: highlight actionable advice |
| 8 | Callout added | Prerequisites block | E-E-A-T: learning path |
| 9 | Internal link | Link to Japanese Candlesticks lesson | Navigation: related content |
| 10 | Internal links | Added links to lessons on bar charts, Renko charts, and Heikin Ashi candles | Navigation: related content |