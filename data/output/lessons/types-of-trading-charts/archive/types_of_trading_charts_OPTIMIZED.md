# Types of Trading Charts: Candlestick, Renko & Heikin Ashi Explained

---
**Prerequisites:** [Japanese Candlesticks](/lesson/japanese-candlesticks/) | [Introduction to Technical Analysis](/lesson/technical-fundamental-sentiment-and-statistical-analysis-which-one-is-best/)
**Last Updated:** 2026-02-27
---

## In This Lesson

- [Why Chart Type Selection Matters](#why-chart-type-selection-matters)
- [Time-Based vs Price-Based Charts](#time-based-vs-price-based-charts)
- [Candlestick Charts](#candlestick-charts)
- [Bar Charts (OHLC)](#bar-charts-ohlc)
- [Heikin Ashi Charts](#heikin-ashi-charts)
- [Renko Charts](#renko-charts)
- [Tick and Range Charts](#tick-and-range-charts)
- [Point and Figure Charts](#point-and-figure-charts)
- [Choosing the Right Chart Type](#choosing-the-right-chart-type)
- [Key Takeaways](#key-takeaways)

---

## Why Chart Type Selection Matters

The method you use to display price data on your charts directly affects how you interpret market movements. While **candlestick charts** remain the most widely used tool among traders globally, alternatives such as **Renko**, **Heikin Ashi**, and **Point and Figure charts** offer distinct advantages for specific trading approaches.

This lesson covers the most common chart types, explains when to use each one, and helps you determine which visualization best fits your trading style.

---

## Time-Based vs Price-Based Charts

Before examining individual chart types, understanding this fundamental distinction will help you choose the right tool:

| Category | How It Works | Best For |
|----------|--------------|----------|
| **Time-Based** | New bar forms after fixed time interval (1M, 5M, 1H, Daily) | General analysis, pattern recognition |
| **Price-Based** | New bar forms after price moves specific amount | Trend following, noise reduction |

**Time-based charts** (candlestick, bar, line) create new bars at regular intervals regardless of price movement. **Price-based charts** (Renko, Point & Figure, tick, range) ignore time entirely—new elements appear only when price moves a specified amount.

> **Tip:** Many traders use both approaches: time-based charts for overall market context, price-based charts for cleaner trend identification.

---

## Candlestick Charts

Japanese candlesticks represent the most popular method of charting and viewing technical analysis. Each candlestick displays four data points: open, close, high, and low prices.

### How Candlesticks Work

- **Bullish candlestick:** Close price is higher than open price
- **Bearish candlestick:** Close price is lower than open price
- **Body:** The filled area between open and close
- **Wicks (shadows):** Lines extending above and below the body, showing the high and low

### Candlestick Timeframes

Candlestick charts operate on two primary bases:

**Time-based options:**
- Minutes: 1M, 5M, 15M, 30M
- Hours: 1H, 4H
- Days, weeks, months

Many traders prefer these standard timeframes because their widespread adoption creates meaningful, recognizable patterns.

**Non-time-based options:**
- **Tick charts:** One tick represents one transaction (the minimum price increment). For EURUSD quoted in five decimal places, one tick equals 0.00001 or 1 pipette.
- **Range charts:** Each bar completes once the high-low range reaches a specified value, ensuring consistent bar ranges.

Both non-time-based approaches eliminate noise from sideways markets, revealing cleaner trends.

> **Note:** Regular time-based candlestick charts remain the most popular choice globally because of their versatility and widespread adoption.

---

## Bar Charts (OHLC)

Bar charts, also called **OHLC charts** (Open-High-Low-Close), use vertical lines with small notches indicating the open and close prices.

### Structure

- Vertical line spans from high to low
- Left notch marks the open price
- Right notch marks the close price

### When to Use Bar Charts

Bar charts provide the same information as candlesticks but with a different visual presentation. Some traders find they present a cleaner picture when marking out **support and resistance** levels, particularly on higher timeframes where candlestick patterns become less relevant.

The choice between bar charts and candlesticks often comes down to personal preference—both convey identical price information.

---

## Heikin Ashi Charts

**Heikin Ashi**—Japanese for "average bar"—is a candlestick modification that smooths price data to clarify trend direction.

### Heikin Ashi Candle Formula

Unlike regular candlesticks that use actual OHLC prices, Heikin Ashi candles use averaged values:

```
Open  = (Previous HA Open + Previous HA Close) / 2
Close = (Current Open + High + Low + Close) / 4
High  = Maximum of (Current High, HA Open, HA Close)
Low   = Minimum of (Current Low, HA Open, HA Close)
```

### How to Read Heikin Ashi Candles

| Candle Appearance | What It Indicates |
|-------------------|-------------------|
| Green candles with no lower wick | Strong uptrend |
| Red candles with no upper wick | Strong downtrend |
| Small body with long wicks | Potential reversal or consolidation |

### Heikin Ashi vs Regular Candlesticks

| Aspect | Regular Candlesticks | Heikin Ashi |
|--------|---------------------|-------------|
| Price accuracy | Exact OHLC | Averaged values |
| Trend clarity | Can be noisy | Smoother, cleaner |
| Entry/exit precision | High | Lower (lagging) |
| Best for | Pattern recognition | Trend following |

### Basic Heikin Ashi Strategy

Heikin Ashi filters out minor price movements and makes trend-following approaches more straightforward. A simple application:

1. Enter when candles change from red to green (potential uptrend)
2. Hold while green candles continue
3. Exit when candles change back to red

> **Important:** Because Heikin Ashi uses averaged data, it can obscure important price information. Consider using it alongside regular candlestick charts for entry and exit precision.

---

## Renko Charts

**Renko**—from the Japanese word "renga" meaning brick—eliminates time from the equation entirely. These charts consist of bricks that only form when price moves a specified amount.

### How Renko Charts Work

The Renko chart prints a new brick when the market moves more than the brick size away from the previous brick. For example, if one brick signifies a movement of 5 pips, no more bricks will be drawn until the market moves those 5 pips in one direction from the previous brick's closing value.

### Brick Size Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **Fixed** | Set specific pip/point value | Consistent visual, predictable |
| **ATR-based** | Uses Average True Range indicator | Adapts to volatility changes |

### Advantages and Limitations

**Advantages:**
- Excellent noise reduction
- Clear support and resistance identification
- Clean trend visualization

**Limitations:**
- Unpredictable timing of new bricks
- No volume or time information
- Can miss entries due to delayed signals

> **Tip:** Renko charts work best when combined with other analysis methods rather than used in isolation.

---

## Tick and Range Charts

### Tick Charts

A **tick chart** creates a new bar after a specified number of transactions, regardless of time or price movement.

- Each tick represents one transaction (one minimal price increment)
- For EURUSD quoted to five decimal places: 1 tick = 0.00001 (1 pipette)
- Useful for analyzing market activity intensity

### Range Charts

A **range chart** creates a new bar when price moves a specified distance (the "range").

- Every bar has exactly the same high-low range
- Eliminates time-based noise during low-activity periods
- Popular for intraday trading

**Practical comparison:** When comparing a DAX four-hour chart with a 100-range chart, both uptrend and downtrend appear much cleaner on the range chart due to noise elimination.

---

## Point and Figure Charts

**Point and Figure (P&F) charts** are among the oldest charting methods, using X's and O's instead of bars or candles.

### How P&F Charts Work

- **X columns:** Rising prices
- **O columns:** Falling prices
- New column forms only when price reverses by a specified amount

### Key Characteristics

- Completely ignores time
- Focuses purely on significant price movements
- Excellent for identifying support, resistance, and breakout levels
- Popular for long-term analysis

> **Note:** Point and Figure charts have a steeper learning curve but offer valuable perspective for traders focused on major price levels.

---

## Choosing the Right Chart Type

| Your Trading Goal | Recommended Chart | Why |
|-------------------|-------------------|-----|
| **General analysis** | Candlestick | Versatile, pattern-rich |
| **Trend following** | Heikin Ashi, Renko | Noise reduction |
| **Precise entries/exits** | Candlestick | Exact price data |
| **Support/resistance focus** | Renko, P&F, Bar | Cleaner levels |
| **Scalping/active trading** | Tick, Range | Time-independent |
| **Long-term positioning** | Candlestick, P&F | Broader perspective |

> **Keep in Mind:** Some of our human tendencies can be dangerous for investors.
>
> - See patterns where there aren't any
> - Believe "market lore," technical and fundamental, without evidence
> - Look backwards rather than forward
> - Stick with original price targets of patterns after conditions have changed

The most effective approach is to experiment with different charts and settings to discover what suits your trading style. While regular time-based candlestick charts will always be the most popular choice, tick charts, range charts, Renko, and Heikin Ashi offer valuable alternatives for specific situations.

---

> **Risk Warning:** Trading involves significant risk of loss. The chart types discussed in this lesson are analytical tools—they do not guarantee profitable trades. Always apply proper risk management.

---

## Key Takeaways

- **Candlestick charts** remain the most widely used due to their versatility and pattern recognition capability
- **Heikin Ashi** smooths price action using averaged calculations—ideal for trend following, but lacks precision for exact entries
- **Renko charts** ignore time and only print new bricks when price moves significantly—excellent for noise reduction
- **Tick and Range charts** create bars based on activity or price movement, not time—useful for eliminating sideways noise
- **Point and Figure charts** use X's and O's to track significant price movements—valuable for support/resistance analysis
- The best chart type depends on your trading style and specific goals—experimentation is key

---

## Next Steps

Continue your technical analysis education:
- [Support and Resistance](/lesson/support-and-resistance/) - Apply chart reading to identify key levels
- [Technical Indicators](/lesson/technical-indicators/) - Combine chart types with indicator analysis
- [Chart Patterns Trading](/lesson/chart-patterns-trading/) - Recognize patterns across chart types

---

*This lesson is part of FTMO Academy's Technical Analysis module.*
