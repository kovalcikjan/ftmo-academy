# Types of Trading Charts

---

Watching market fluctuations and volatility in real-time is an essential skill to develop. There are several ways to display data on a chart, from a standard candlestick chart to Renko or Heikin Ashi. This lesson covers the specifics of these chart types and how they differ.

## Types of trading charts – candlestick charts, Renko charts, and Heikin Ashi candles

The ways of displaying data on a price chart are nearly endless. No two traders watch and interpret the exact same things in their trading. Although most traders use candlestick charts, which we covered in the previous lesson, there is more depth to explore. Besides candlestick charts, this lesson also examines different graphical representations such as bar charts, Renko charts, and Heikin Ashi candles.

### Candlestick charts

Japanese candlesticks are covered in the previous lesson. Here is a quick recap. Candlestick charts are the most popular method of charting and applying technical analysis. The anatomy of a candlestick consists of the body and the wick. If the candle closes above the open, it forms a bullish candlestick. If the candle closes below the open, it forms a bearish candlestick. Wicks represent the highest and lowest points where the market traded.

![](https://academy.ftmo.com/wp-content/uploads/2023/03/c-25.jpg)

The image below shows two candlestick charts next to each other in the FTMO cTrader platform.

![](https://academy.ftmo.com/wp-content/uploads/2021/03/timeframevsrange.png)

Although they look the same, there is one significant difference between them. The chart on the left is based on time and the chart on the right is not. Chart periodicity is the main function you can control when setting up a candlestick chart. Time-based periodicity is the most popular and common among traders. Most trading platforms allow you to set up charts based on minutes, hours, days, weeks, and seconds. The most popular timeframes are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly, and monthly charts. Although you can set up a chart with any setting, using popular timeframes is practical because many traders monitor them simultaneously. If you use something like a 40-minute or 3-hour chart, the candlestick patterns on your chart may carry less relevance since fewer traders observe them. Non-time-based charts are less common, but they still provide traders with valuable information. Traders can use tick charts and range charts in the FTMO cTrader platform — these two are also the most popular non-time-based charts. In a tick chart, one tick represents one transaction. In other words, one tick is recorded when the market fluctuates by the minimal price increment.

Consider EURUSD, which is quoted in five decimal places. One tick would equal 0.00001 or 1 pipette. In the range bar, every bar ends once the range between its high and low equals the chosen range. This means that every bar has the same bar range and closes either at high or low. Using range charts or tick charts can eliminate noise and display trends more clearly by filtering out time periods when markets are not moving and remain range-bound. This effect is visible when comparing a DAX four-hour chart with a 100 range chart in cTrader. Both the uptrend and downtrend appear cleaner on the range chart once the time factor is eliminated and the focus shifts to price rotations.

### Bar charts

The only difference between the candlestick and the bar chart is the visual representation.

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115043.png)

Bar charts, often called OHLC charts, are represented as vertical bars with two notches that mark the open and close of the bar. Compared to Japanese candlesticks, bar charts are less intuitive for new traders when it comes to reading candlestick charts. However, they may present a cleaner picture when it comes to marking out support and resistance.

### Renko Charts

Renko charts are similar to range and tick charts. They eliminate the time factor from trading and change the visuals of the chart entirely. Instead of candlesticks, the chart displays bricks. The name Renko comes from the Japanese word renga, which means brick.

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115503.png)

A Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. For example, if one brick represents a movement of 5 pips, no new bricks appear until the market moves those 5 pips in one direction from the close of the last brick. Renko charts are effective for filtering out noise and for marking out support and resistance areas.

### Heikin Ashi Candles

Heikin Ashi candles are another chart representation that originates from Japan. Heikin Ashi translates to "average bar." Here is how the Heikin Ashi candle formula works: Heikin Ashi candles are constructed the same way as the candlestick chart but use a different calculation method. You can set up a Heikin Ashi chart on any specified time, range, or tick setting.

![](https://academy.ftmo.com/wp-content/uploads/2023/03/Snimek-obrazovky-2023-07-18-115656.png)

Heikin Ashi candles filter out price movements and provide a smoother approach to trend following. The trade-off is that some valuable information may be lost, as the smoothing can become excessive. However, Heikin Ashi candles are an effective tool for both entries and trade management.

### Conclusion

The most practical approach is to experiment with different charts and settings to find what works for your trading style. Regular time-based candlestick charts remain the most popular format, used by traders worldwide. Tick charts, range charts, Renko charts, and Heikin Ashi candles can also add value to your strategy when applied to the right context.
