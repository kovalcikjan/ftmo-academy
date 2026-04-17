# Types of Trading Charts

> **Prerequisites:** Before starting this lesson, complete [Japanese Candlesticks](/lesson/japanese-candlesticks/).

A trading chart type determines how price data is displayed visually. Reading price data in real time starts with choosing the right format. There are several types of trading charts, from a standard candlestick chart to Renko charts or Heikin Ashi candles. This lesson covers the specifics of these chart types and how they differ.

---

## Candlestick Charts

The previous lesson covers [Japanese Candlesticks](/lesson/japanese-candlesticks/). Here is a quick recap. **Candlestick charts are the most popular format for technical analysis.** The anatomy of a candlestick consists of the *body* and the *wick*. If the candle closes above the open, it forms a *bullish candlestick*. If the candle closes below the open, it forms a *bearish candlestick*. Wicks represent the highest and lowest prices reached during the period.

*Candlestick anatomy: body, wick, bullish vs bearish candle*

![](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

The image below shows two candlestick charts next to each other in the cTrader platform. The chart on the left uses a time-based periodicity, the chart on the right does not.

*Two candlestick charts: time-based (left) vs non-time-based (right)*

![](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

**Chart periodicity is the main function you can control when setting up a candlestick chart.**

### Time-Based Charts

**Time-based periodicity** is the most common setting among traders. Most trading platforms allow you to set up charts based on seconds, minutes, hours, days, and weeks. The most popular timeframes are:

- 1-minute, 5-minute, 15M, 30M, 60M
- 4-hour, daily, weekly, monthly

Although you can set up a chart with any setting, using popular timeframes is practical because many traders monitor them simultaneously. If you use a 40-minute or 3-hour chart, the [candlestick patterns](/lesson/chart-patterns-trading/) on your chart may carry less weight since fewer traders observe them.

> **Note:** For a deeper look at how different timeframes work together, see [Multiple Timeframe Analysis](/lesson/multiple-timeframe-analysis/).

### Non-Time-Based Charts

Non-time-based charts are less common, but they provide traders with valuable information. Traders can use *tick charts* and *range charts* in the cTrader platform. **These are the two most popular non-time-based formats.**

In a *tick chart*, one tick represents one transaction. One tick is recorded when the market fluctuates by the minimum price increment. Consider EURUSD, which is quoted in five decimal places: one tick would equal 0.00001 or 1 pipette.

In a *range bar*, every bar closes once the distance between its high and low equals the chosen range. This means every bar covers the same price range and closes at either its high or its low.

Using range charts or tick charts can eliminate noise and display trends more clearly by filtering out time periods when markets are not moving and remain range-bound. This effect is visible when comparing a DAX four-hour chart with a 100 range chart in cTrader. Both the uptrend and the downtrend appear cleaner on the range chart once you remove the time factor and focus on price rotations.

> **Tip:** If your candlestick charts feel visually noisy, try a higher timeframe first before switching to a non-time-based format. A daily chart often filters the same noise that range or tick charts do, with less complexity.

## Bar Charts

The only difference between the candlestick and the bar chart is the visual representation.

*Bar chart (OHLC): vertical bars with open and close notches*

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

*Bar charts*, often called *Open, High, Low, Close (OHLC) charts*, use vertical bars with two notches to mark the open and close of each bar. Compared to [Japanese candlesticks](/lesson/japanese-candlesticks/), bar charts are less intuitive for traders accustomed to reading candlestick charts. However, they may present a cleaner picture when identifying [support and resistance](/lesson/support-and-resistance/).

## Renko Charts

**Renko charts eliminate the time factor from trading entirely.** They are similar to range and tick charts, but change the visuals of the chart completely. Instead of candlesticks, the chart displays bricks. The name Renko comes from the Japanese word *renga*, which means brick.

*Renko chart: price bricks without a time axis*

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

A Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. For example, if one brick represents a movement of 5 pips, no new bricks appear until the market moves those 5 pips in one direction from the close of the last brick. Renko charts are effective for filtering out noise and for marking out [support and resistance](/lesson/support-and-resistance/) areas.

## Heikin Ashi Candles

**What is Heikin Ashi?** Heikin Ashi candles are a charting method that originates from Japan. Heikin Ashi translates to "average bar." The *Heikin Ashi candle formula* uses the same visual structure as a standard candlestick chart but applies a different calculation method. You can set up a Heikin Ashi chart on any specified time, range, or tick setting.

*Heikin Ashi chart: smoothed candles for trend following*

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

Heikin Ashi candles smooth out price movements and provide a clearer approach to trend following. The trade-off is that some valuable information may be lost, as the smoothing can become excessive. However, Heikin Ashi candles are an effective tool for entries and trade management, making them a core component of any Heikin Ashi strategy focused on riding trends.

> **Keep in Mind:** Switching chart formats does not create an edge. Every chart type displays the same underlying price data. The edge comes from your analysis of what the chart shows, not from the format itself.

## Other Chart Types

Beyond the chart types covered in this lesson, traders may encounter additional formats. A **point and figure chart** strips away time entirely and plots only significant price moves, making it one of the oldest charting methods. **Kagi charts** and **line break charts** follow a similar philosophy, focusing on price direction rather than time intervals.

More advanced formats such as a **footprint chart**, **order flow chart**, or **market profile** display volume at each price level, giving traders insight into where the most activity occurs. These specialised chart types are less common among retail traders but can complement candlestick or Renko analysis in specific contexts.

## Conclusion

Start with candlestick charts. They are the industry standard for a reason. Once you are comfortable reading price action, experiment with different types of trading charts and settings to find what works for your trading style. Tick charts, range charts, Renko charts, and Heikin Ashi candles can add value to your strategy when applied to the right context.

| Chart Type | Shows | Time Factor | Best For |
|------------|-------|-------------|----------|
| Candlestick | OHLC (body + wicks) | Yes | Pattern recognition, most analysis |
| Bar (OHLC) | OHLC (vertical bar + ticks) | Yes | Volatility context, support/resistance |
| Renko | Price bricks | No | Trend direction, noise filtering |
| Heikin Ashi | Averaged OHLC | Yes | Trend following, smoother view |
| Tick | Per-transaction bars | No | Intraday activity, volume context |
| Range | Fixed-range bars | No | Trend clarity, filtering chop |

## Key Takeaways

- **Candlestick charts** are the most widely used format. Start here as your default.
- **Bar charts (OHLC)** show the same data in a different visual form, useful for [support and resistance](/lesson/support-and-resistance/) analysis.
- **Non-time-based charts** (tick, range) filter out periods of low activity and display trends more clearly.
- **Renko charts** eliminate time entirely and focus on price movement through bricks.
- **Heikin Ashi candles** smooth price data for easier trend following, at the cost of precise price information.
- The right chart depends on your trading style, timeframe, and what you need to see.

## Next Steps

Build on this foundation with these related lessons:

- [Market Environment: Range vs. Trend](/lesson/market-environment-range-vs-trend/): how to identify what the chart is showing you
- [Support and Resistance](/lesson/support-and-resistance/): key price levels visible across all chart types
- [Chart Patterns](/lesson/chart-patterns-trading/): recognisable formations on candlestick charts
- [Multiple Timeframe Analysis](/lesson/multiple-timeframe-analysis/): combining different timeframes for stronger analysis

---

**About the Author**
**FTMO Academy Content Team**
*Last Updated: 2026-04-10*

---

> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose.

> **Educational Content Notice:** This material is for educational purposes only and does not constitute financial advice. Trading decisions should be based on your own analysis and risk tolerance.
