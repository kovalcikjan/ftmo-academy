# Types of Trading Charts: Candlestick Charts, Renko Charts, and Heikin Ashi

> **Prerequisites:** Before starting this lesson, complete [Japanese Candlesticks](/lesson/japanese-candlesticks/).

This lesson covers the main types of trading charts, what makes each one different, and how to choose the right display for your analysis.

## In This Lesson
- [Candlestick Charts](#candlestick-charts)
- [Bar Charts](#bar-charts)
- [Renko Charts](#renko-charts)
- [Heikin Ashi Candles](#heikin-ashi-candles)
- [Conclusion](#conclusion)

Price charts can be displayed in nearly unlimited ways. This is why no two traders watch exactly the same things. Although most traders use **candlestick charts** — covered in the previous lesson — there is more depth to explore. This lesson also covers **bar charts**, **Renko charts**, and **Heikin Ashi candles**.

## Candlestick Charts

[Japanese Candlesticks](/lesson/japanese-candlesticks/) are covered in the previous lesson. Here is a quick recap. They are the most widely used chart type in technical analysis. The anatomy of a candlestick consists of the **body** and the **wick**. If the candle closes above the open, it is a bullish candlestick. If the candle closes below the open, it is a bearish candlestick. Wicks represent the highest and lowest points where the market traded.

![Candlestick chart anatomy](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

The image below shows two candlestick charts side by side in the FTMO cTrader platform.

![Time-based vs range-based candlestick charts](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

### Time-Based Charts

Although they look the same, there is one significant difference. The chart on the left is time-based; the chart on the right is not. **Chart periodicity** is the main variable to control when setting up a candlestick chart. Time periodicity is the most common choice among traders. Most trading platforms support charts based on minutes, hours, days, weeks, and seconds. The most popular timeframes are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly, and monthly.

You can set up a chart with any periodicity, but standard timeframes work because many traders monitor them. A 40-minute or 3-hour chart carries less weight — fewer traders monitor those intervals, so candlestick patterns formed on them have reduced significance.

> **Tip:** Standard timeframes (1H, 4H, Daily) are monitored by a large number of traders simultaneously. Candlestick patterns on these timeframes carry more market weight because more participants react to them at the same time.

### Tick and Range Charts

Non-time-based charts are less common, but they can still provide valuable information. In the FTMO cTrader platform, traders can access **tick charts** and **range charts** — the two most popular non-time-based options. In a tick chart, one tick represents one transaction. One tick occurs when the market moves by the minimum price increment.

Take EURUSD as an example — it is quoted in five decimal places. One tick equals 0.00001, or 1 pipette. In a range bar, every bar closes once the range between its high and low equals the chosen range value. This means every bar has the same range and closes either at its high or low. Range and tick charts eliminate noise and display trends more clearly by removing periods when price is not moving.

The effect is visible when comparing a DAX four-hour chart with a 100-range chart in cTrader. Both the uptrend and downtrend appear cleaner on the range chart once the time factor is removed and focus shifts to price rotations.

## Bar Charts

The only difference between a candlestick and a **bar chart** is the visual representation.

![OHLC bar chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

Bar charts, often called OHLC charts, display as vertical bars with two notches indicating the open and close of each bar. Compared to Japanese candlesticks, bar charts are less intuitive for new traders when reading candlestick patterns. On the other hand, they may provide a clearer view for marking [support and resistance](/lesson/support-and-resistance/) levels.

## Renko Charts

Renko charts are similar to range and tick charts. Renko eliminates the time factor from trading and changes the chart's visual representation entirely. Instead of candlesticks, the chart displays bricks. The name comes from the Japanese word *renga*, meaning brick.

![Renko brick chart example](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

A Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. For example, if one brick represents 5 pips, no new brick is drawn until the market moves those 5 pips in one direction from the close of the last brick. Renko charts are effective for filtering out noise and marking [support and resistance](/lesson/support-and-resistance/) areas.

## Heikin Ashi Candles

Heikin Ashi candles are another chart representation that comes from Japan. The name translates to "average bar." Here is how the Heikin Ashi candle formula works: the chart is constructed the same way as a candlestick chart but uses a different calculation method. A Heikin Ashi chart can be set up on any preferred timeframe — time-based, range, or tick.

![Heikin Ashi smoothed candlestick chart](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

Heikin Ashi smooths price movements and simplifies trend following. Many traders incorporate it into their Heikin Ashi strategy specifically for trend-following entries. The trade-off is that some price detail is lost — the smoothing can obscure short-term signals. However, it remains an effective tool for both entries and trade management.

> **Keep in Mind:** Some human tendencies can work against you when reading charts:
> - Seeing patterns where there are none
> - Favouring a chart type based on habit rather than evidence
> - Sticking with a chart setup after market conditions have changed

## Conclusion

Experimenting with different charts and settings is the most effective way to find what works for your trading style. Regular time-based candlestick charts remain the most popular, used by traders worldwide. However, tick charts, range charts, Renko charts, or Heikin Ashi candles can all be incorporated into your strategy and add value to your trading.

| Chart Type | Time-Based | Best For |
|------------|------------|----------|
| **Candlestick** | Yes (also Range / Tick) | General analysis, pattern recognition |
| **Bar (OHLC)** | Yes | Support and resistance marking |
| **Renko** | No (price-based) | Noise filtering, trend clarity |
| **Heikin Ashi** | Yes (also Range / Tick) | Trend following, entries |

---

## Key Takeaways

- **Candlestick charts** are the most widely used chart type; time periodicity determines how each candle forms.
- **Standard timeframes** (1H, 4H, Daily) carry more market weight because more traders monitor them simultaneously.
- **Tick and range charts** remove the time factor and can display trends more clearly by eliminating low-activity periods.
- **Bar charts** use a different visual format — useful for traders who prefer a cleaner view when marking support and resistance.
- **Renko charts** filter noise by only drawing a new brick when price moves a defined distance.
- **Heikin Ashi candles** smooth price data to simplify trend following — at the cost of some short-term detail.

## Next Steps

- [Market Environment: Range vs. Trend](/lesson/market-environment-range-vs-trend/) — understand the conditions each chart type is designed to display
- [Support and Resistance](/lesson/support-and-resistance/) — apply the chart reading skills from this lesson
- [Technical Indicators](/lesson/technical-indicators/) — combine chart types with indicators for a complete analysis framework

---

**Author:** FTMO Academy Content Team
**Last Updated:** March 5, 2026

---

> **Educational Content Notice:** This material is for educational purposes only and does not constitute financial advice. Trading decisions should be based on your own analysis and risk tolerance.

> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose.
