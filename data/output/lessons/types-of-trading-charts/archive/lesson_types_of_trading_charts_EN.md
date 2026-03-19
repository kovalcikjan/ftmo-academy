# Types of Trading Charts

Watching the market fluctuations and volatility in real-time is an essential skill to acquire. There are several ways to display data on the chart, from simple candlestick charts to Renko charts or Heikin Ashi candles. What are the specifics of these charts and how do they differ? You will find out in this lesson.

## Overview

The ways of displaying data on a price chart are nearly endless. This is why we will never find two traders that do and watch exactly the same things in their trading. Although most traders are using candlestick charts which we covered in the previous video, there is more depth in those as well. Besides candlestick charts, we will also have a look at different graphical representations of price charts such as bar charts, Renko charts or Heikin Ashi candles.

### Candlestick charts

We have covered [Japanese candlesticks](/lesson/japanese-candlesticks) in the previous lesson, so here is a quick recap. They are the most popular methods of charting and viewing technical analysis.

**Candlestick anatomy:**
- **Body** - distance between open and close
- **Wick** - highest and lowest points where the market traded
- **Bullish candle** - closes above the open
- **Bearish candle** - closes below the open

As we can see in the image below, we have two candlestick charts next to each other in our FTMO cTrader platform.

Although they look the same, there is one significant difference between them. The chart on the left is based on time and the chart on the right is not. The chart periodicity is the main function we can control when setting up our candlestick chart. The time periodicity is the most popular and common amongst traders. Most trading platforms will allow us to set up charts based on minutes, hours, days, weeks, and seconds. The most popular charts used by traders are 1-minute, 5-minute, 15M, 30M, 60M, 4-hour, daily, weekly and monthly charts.

> **Tip:** Stick to popular timeframes (1M, 5M, 15M, 1H, 4H, Daily). These work because many traders watch them - your patterns carry more weight when others see them too.

Although we can set up our chart with any setting we want, using those popular timeframes works simply because many traders are also watching them. If we use something like a 40-minute or 3-hour chart, the candlestick patterns on our chart might have a lower weight as no other traders see them.

The non-time-based charts are less common, but they still can give traders valuable information. Our traders can use tick and range charts in our FTMO cTrader platform, these two are also the most popular non-time-based charts. In the tick chart, one tick represents one transaction. In other words, one tick is made when the market fluctuates by the minimal price increment.

If we take a look at EURUSD, which is quoted in five decimal places. One tick would equal 0.00001 or 1 pipette. In the range bar, every bar will end once the range between its high and low equals the chosen range. This means that every bar will have the same bar range and close either at high or low. Using a range of tick charts can eliminate noise and display trends in a much clearer picture as we will get rid of time periods when markets are not moving and staying range-bound. This can be clearly seen when we compare this DAX four-hour chart with the 100 range chart in cTrader. We can notice that both uptrend and downtrend were much cleaner on the range chart once we eliminated the time factor and put our focus on price rotations.

### Bar charts

The only difference between the candlestick and the bar chart is the visual representation.

Bar charts, often called OHLC charts, are represented as vertical bars with two notches that represent the open and close of the bar. Compared to Japanese candlesticks, bar charts may be less clear for new traders when it comes to candlestick patterns. On the other hand, they may present a cleaner picture when it comes to marking out support and resistance.

### Renko Charts

Renko charts are similar to the range and tick charts. It eliminates the time factor from trading and changes the visuals of our chart completely. We won't see candlesticks anymore, but we will be looking at bricks instead. The name Renko came from the Japanese renga, which stands for brick.

The Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. Let's say we define that one brick signifies a movement of 5 pips. So, until the market moves these 5 pips in one direction (from the close of the last brick), no more bricks will be drawn. Renko charts are effective for filtering out noise and for marking out support and resistance areas.

### Heikin Ashi Candles

Heikin Ashi candles are another chart representation that comes from Japan. It means "average bar" and although this is not something we need to know, here we can have a look at how the Heikin Ashi candle is calculated. The Heikin Ashi is constructed the same way as the candlestick chart but has a different calculation method. We can set up a Heikin Ashi chart as we want, on the specified time, range or tick.

Heikin Ashi filters out the movements and makes trend following much easier, which is why it is often used in Heikin Ashi strategies. The downside is that it may smooth out valuable price information. However, it is an effective tool for both entries and trade management.

## Chart Types Comparison

| Chart Type | Best For | Limitation |
|------------|----------|------------|
| **Candlestick** | Standard analysis, pattern recognition | Can show noise in choppy markets |
| **Bar (OHLC)** | Support/resistance marking | Less visual clarity for patterns |
| **Renko** | Trend clarity, noise filtering | Removes time element |
| **Heikin Ashi** | Trend following, entries/exits | May smooth out key price levels |

## Conclusion

The best approach is to experiment with different chart types and settings to find what suits your trading style. For more on reading price action, see [Support and Resistance](/lesson/support-and-resistance). Regular time-based candlestick charts will always be the most popular as they are used by traders worldwide. But tick charts, range charts, Renko charts or Heikin Ashi candles, can be utilized in your strategy and add value to your trading.
