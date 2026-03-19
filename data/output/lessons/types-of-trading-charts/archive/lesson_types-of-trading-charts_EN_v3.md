# Types of Trading Charts: Candlestick, Renko & Heikin Ashi

---
**Prerequisites:** [Japanese Candlesticks](/lesson/japanese-candlesticks/)
**Last Updated:** 2026-03-05
---

Monitoring real-time market movements is an essential trading skill. There are several ways to display price data on a chart — from standard **candlestick charts** to more specialized formats like **Renko** or **Heikin Ashi**. This lesson covers the specifics of each chart type and how they differ.

The ways of displaying data on a price chart are nearly endless. No two traders analyse charts in exactly the same way. Although most traders use candlestick charts, which we covered in the [Japanese Candlesticks](/lesson/japanese-candlesticks/) lesson, there is more depth to explore. This lesson also covers bar charts, Renko, and Heikin Ashi charts.

![Types of trading charts overview](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

---

## Candlestick Charts

Japanese candlesticks are covered in the previous lesson. Here is a quick recap. They are the most popular charting method for technical analysis. The anatomy of a candlestick consists of the **body** and the **wick**. If the candle closes above the open, we have a bullish candlestick. If the candle closes below the open, we have a bearish candlestick. Wicks represent the highest and lowest points where the market traded.

### Time-Based Charts

The image below shows two candlestick charts displayed side by side in the FTMO cTrader platform.

Although they look the same, there is one significant difference between them. The chart on the left is based on time and the chart on the right is not. **Chart periodicity** is the main function we control when setting up a candlestick chart. Time-based periodicity is the most widely used option among traders. Most trading platforms allow traders to set up charts based on minutes, hours, days, weeks, and seconds.

The most popular timeframes used by traders are:

- 1-minute, 5-minute, 15M, 30M, 60M
- 4-hour, daily, weekly, monthly

> **Tip:** Using standard timeframes is effective because many traders are also watching them. If we use a non-standard chart like a 40-minute or 3-hour setting, candlestick patterns carry less weight because other traders are not watching those levels.

### Non-Time-Based Charts

Non-time-based charts are less common, but they can still provide valuable information. Traders can use **tick and range charts** in the FTMO cTrader platform — these are the most popular non-time-based chart types.

- **Tick chart:** One tick represents one transaction. A tick forms each time the market moves by the minimum price increment. For EURUSD, quoted in five decimal places, one tick equals 0.00001, or 1 pipette.
- **Range chart:** Each bar closes when the distance between its high and low reaches the chosen range value. Every range bar has an identical high-to-low range and closes at either the high or low.

Using tick and range charts eliminates noise and displays trends more clearly by removing time periods when markets are inactive. This becomes clear when comparing a DAX four-hour chart with the 100-range chart in cTrader. Both the uptrend and downtrend appeared cleaner on the range chart once we removed the time factor and focused on price rotations.

![Time-based vs range chart comparison](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

---

## Bar Charts

The only difference between a candlestick and a bar chart is the visual representation. **Bar charts**, often called **OHLC charts**, display as vertical bars with two notches indicating the open and close. In practice, candlestick patterns are harder to read on bar charts, making them less intuitive for traders learning to identify formations. On the other hand, bar charts can present a cleaner picture when marking out [support and resistance](/lesson/support-and-resistance/) levels.

![Bar chart (OHLC) example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

---

## Renko Charts

**Renko charts** are similar to range and tick charts. They eliminate the time factor from trading and change the chart's visual presentation entirely. Instead of candlesticks, the chart displays **bricks**. The name Renko came from the Japanese renga, which stands for brick. The Renko chart prints a new brick when the market moves more than the **brick size** away from the previous brick.

For example, if one brick represents a 5-pip movement, until the market moves those 5 pips in one direction from the last brick's close, no new bricks appear. Renko charts are effective not only for filtering out noise but also for identifying [support and resistance](/lesson/support-and-resistance/) areas.

![Renko chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

---

## Heikin Ashi

**Heikin Ashi candles** are another chart representation that comes from Japan. It means "average bar." While the formula itself is not strictly necessary to know, here is the Heikin Ashi candle formula for reference. Heikin Ashi candles follow the same structure as standard candlesticks but use a different calculation method. A Heikin Ashi chart can be configured for time-based, range, or tick settings.

Heikin Ashi filters out minor price movements and supports a more straightforward approach to trend following. The trade-off is that the smoothing effect can obscure important price information.

> **Note:** Because Heikin Ashi uses averaged data, it is an effective tool for both entries and trade management — but consider using it alongside regular candlestick charts for precise entry and exit levels.

![Heikin Ashi chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

---

> **Keep in Mind:** When using any chart type for technical analysis, be aware of these common tendencies:
>
> - Seeing patterns where there are none
> - Assuming past chart patterns predict future price movements
> - Favouring a chart type because it confirms an existing bias

---

## Conclusion

The best approach is to experiment with different chart types and settings to find what fits your trading style. Regular time-based candlestick charts will always be the most popular, as they are used by traders worldwide. However, tick charts, range charts, Renko, and Heikin Ashi can all be incorporated into a trading strategy and add significant value.

| Chart Type | Time-Based | Best For | Trade-off |
|------------|------------|----------|-----------|
| Candlestick | Yes | Pattern recognition, general analysis | None — the standard |
| Bar (OHLC) | Yes | Support and resistance levels | Less intuitive for pattern reading |
| Renko | No | Noise reduction, trend clarity | No time or volume information |
| Heikin Ashi | Optional | Trend following | Lagging; obscures exact prices |

---

## Key Takeaways

- **Candlestick charts** remain the most popular method — versatile and suitable for all analysis types
- **Bar charts** convey identical information to candlesticks but offer a cleaner view of [support and resistance](/lesson/support-and-resistance/) levels
- **Renko charts** remove time entirely and display only significant price moves as bricks — effective for noise reduction
- **Heikin Ashi** smooths price action for trend following, but lags behind actual price data
- **Tick and range charts** eliminate low-activity time periods, revealing cleaner trends
- Experiment with different chart types to identify what best fits your trading approach

---

## Next Steps

- [Technical Indicators](/lesson/technical-indicators/) — combine chart types with indicator analysis
- [Chart Patterns Trading](/lesson/chart-patterns-trading/) — recognise patterns across different chart types
- [Market Environment: Range vs. Trend](/lesson/market-environment-range-vs-trend/) — apply chart reading to identify current market conditions

---

**Author:** FTMO Academy Content Team
**Last Updated:** 2026-03-05

---

> **Educational Content Notice:** This material is for educational purposes only and does not constitute financial advice. Trading decisions should be based on your own analysis and risk tolerance.

> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose.
