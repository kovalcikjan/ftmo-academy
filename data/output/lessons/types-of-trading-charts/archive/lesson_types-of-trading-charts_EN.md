# Types of Trading Charts: Candlestick, Renko & Heikin Ashi

> **Prerequisites:** Before starting this lesson, complete:
> - [Japanese Candlesticks](/lesson/japanese-candlesticks/)

**Last Updated:** 2026-03-05

---

Price data can be displayed on a chart in multiple ways — from standard **candlestick charts** to specialized formats like **Renko** or **Heikin Ashi candles**. Each type filters and presents price information differently. This lesson covers the specifics of each chart type and what distinguishes them.

Most traders use candlestick charts, covered in the [Japanese Candlesticks](/lesson/japanese-candlesticks/) lesson. There are alternatives worth understanding: bar charts, Renko, and Heikin Ashi candles. No two traders analyse charts in exactly the same way.

## Candlestick Charts

Japanese candlesticks are covered in the previous lesson — this is a quick recap. They are the most popular charting method for technical analysis. The anatomy consists of the **body** and the **wick**. A candle closing above its open is bullish; closing below is bearish. Wicks mark the highest and lowest points of the trading range.

![Candlestick anatomy showing body and wick structure](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

### Time-Based Charts

![Time-based vs range chart comparison in FTMO cTrader](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

The chart on the left is time-based; the chart on the right is not. **Chart periodicity** is the primary setting when configuring a candlestick chart. Time-based periodicity is the most widely used option — most platforms support minutes, hours, days, weeks, and seconds.

The most popular timeframes are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly, and monthly.

> **Tip:** Using standard timeframes is effective because many traders watch the same levels. A non-standard chart — such as 40-minute or 3-hour — produces candlestick patterns that fewer traders observe, which reduces their significance.

### Non-Time-Based Charts

Time is not the only way to structure a chart. **Tick and range charts** are the most popular non-time-based alternatives available in the FTMO cTrader platform. In a tick chart, one tick represents one transaction — it forms each time the market moves by the minimum price increment.

For EURUSD, quoted in five decimal places, one tick equals 0.00001 — or 1 pipette. In a range bar, each bar closes when the distance between its high and low reaches the chosen range value. Every range bar has an identical high-to-low range and closes at either its high or low.

Tick and range charts eliminate noise and display trends more clearly by removing time periods when markets are inactive. The difference is visible when comparing a DAX four-hour chart with the 100-range chart in cTrader — both the uptrend and downtrend appeared cleaner on the range chart once the time factor was removed and the focus shifted to price rotations.

## Bar Charts

The only difference between a candlestick and a bar chart is the visual representation.

![Bar chart (OHLC) example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

**Bar charts**, often called **OHLC charts**, display as vertical bars with two notches indicating the open and close. Candlestick patterns are harder to read on bar charts, making them less intuitive for traders still learning to identify formations. However, bar charts can present a cleaner picture when marking out [support and resistance](/lesson/support-and-resistance/) levels.

## Renko Charts

**Renko charts** eliminate the time factor entirely and display only significant price movements. Instead of candlesticks, the chart uses **bricks** — each representing a fixed price increment. The name comes from the Japanese renga, meaning brick.

![Renko chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

A new brick appears when the market moves more than the **brick size** away from the previous brick. If one brick represents a 5-pip movement, no new brick forms until price travels those 5 pips from the last brick's close. This makes Renko charts effective for filtering out noise and identifying [support and resistance](/lesson/support-and-resistance/) areas.

## Heikin Ashi Candles

**Heikin Ashi candles** are a Japanese chart type built on a different calculation method than standard candlesticks. The name translates as "average bar." The formula itself is not required knowledge — but for reference, here is the Heikin Ashi candle formula. Structurally, Heikin Ashi candles follow the same format as standard candlesticks. A Heikin Ashi chart can be configured for time-based, range, or tick settings.

![Heikin Ashi chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

Heikin Ashi filters out minor price movements and produces a more straightforward view for trend following. The trade-off: the smoothing effect can obscure important price information.

> **Note:** Because Heikin Ashi uses averaged data, it is an effective tool for both entries and trade management — but consider using it alongside regular candlestick charts for precise entry and exit levels.

## Conclusion

Start with candlestick charts — they are the industry standard, used by traders worldwide. Once comfortable reading price action, experiment with Heikin Ashi candles or Renko charts to see whether noise reduction improves your decision-making. Tick charts and range charts serve the same purpose, removing inactive time periods to reveal cleaner trends.

| Chart Type | Time-Based | Best For | Trade-off |
|------------|------------|----------|-----------|
| Candlestick | Yes | Pattern recognition, general analysis | None — the standard |
| Bar (OHLC) | Yes | Support and resistance levels | Less intuitive for pattern reading |
| Renko | No | Noise reduction, trend clarity | No time or volume information |
| Heikin Ashi | Optional | Trend following | Lagging; obscures exact prices |
| Tick / Range | No | Noise reduction, inactive period removal | Requires platform support |

> **Keep in Mind:** When using any chart type for technical analysis, be aware of these common tendencies:
>
> - Seeing patterns where there are none
> - Assuming past chart patterns predict future price movements
> - Favouring a chart type because it confirms an existing bias

---

### Key Takeaways

- **Candlestick charts** remain the most popular method — versatile and suitable for all analysis types
- **Bar charts** convey identical information to candlesticks but offer a cleaner view of [support and resistance](/lesson/support-and-resistance/) levels
- **Renko charts** remove time entirely and display only significant price moves as bricks — effective for noise reduction
- **Heikin Ashi candles** smooth price action for trend following, but lag behind actual price data
- **Tick and range charts** eliminate low-activity time periods, revealing cleaner trends
- Experiment with different chart types to find what fits your trading approach

### Next Steps

- [Technical Indicators](/lesson/technical-indicators/) — combine chart types with indicator analysis
- [Chart Patterns Trading](/lesson/chart-patterns-trading/) — recognise patterns across different chart types
- [Market Environment: Range vs. Trend](/lesson/market-environment-range-vs-trend/) — apply chart reading to identify current market conditions

---

**Author:** FTMO Academy Content Team
**Role:** FTMO Academy
**Last Updated:** 2026-03-05

> **Educational Content Notice:** This material is for educational purposes only and does not constitute financial advice. Trading decisions should be based on your own analysis and risk tolerance.

> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose.
