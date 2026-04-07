# Edit Log: Types of Trading Charts (v10)

**Slug:** types-of-trading-charts
**Date:** 2026-04-01
**Base version:** v8_final
**Workflow:** /academy (5-step edit)

---

## Step 1 Log: Keywords

**Keywords file:** `data/output/keywords/types-of-trading-charts_keywords.xlsx`

### Changes Applied

| # | Original sentence (full) | New sentence (full) | Keyword | Volume | Position | Status |
|---|--------------------------|---------------------|---------|--------|----------|--------|
| 1 | "There are several ways to display data on a chart, from a standard candlestick chart to Renko or Heikin Ashi." | "There are several types of trading charts, from a standard candlestick chart to Renko charts or Heikin Ashi candles." | trading charts, renko charts, heikin ashi candles | 2,600 / 400 / 1,400 | Intro | DONE |
| 2 | "The most practical approach is to experiment with different charts and settings to find what works for your trading style." | "The most practical approach is to experiment with different types of trading charts and settings to find what works for your trading style." | trading charts | 2,600 | Conclusion | DONE |
| 3 | "**Heikin Ashi candles** are another chart representation that originates from Japan." | "**What is Heikin Ashi?** Heikin Ashi candles are a chart representation that originates from Japan." | what is heikin ashi | 150 | H2 body (opening) | DONE |
| 4 | "However, Heikin Ashi candles are an effective tool for both entries and trade management." | "However, Heikin Ashi candles are an effective tool for entries and trade management, making them a core component of any Heikin Ashi strategy focused on riding trends." | heikin ashi strategy | 250 | Body | DONE |

### New Content Added

| # | Change | Keywords Integrated | Combined Volume | Status |
|---|--------|---------------------|-----------------|--------|
| 5 | New H2 section "Other Chart Types" added before Conclusion | point and figure chart (400), kagi chart (90), line break chart (40), footprint chart (700), market profile (500) | 1,730 | DONE |

### Already Present (no changes needed)

| Keyword | Volume | Location |
|---------|--------|----------|
| heikin ashi | 2,000 | H2 heading, body, conclusion |
| heikin ashi candles | 1,400 | H2 heading, body, key takeaways |
| candlestick charts | 1,000 | H2 heading, body, intro, conclusion |
| tick chart / tick charts | 700/100 | Body, conclusion |
| renko charts / renko chart | 400/200 | H2 heading, body, conclusion |
| japanese candlesticks | 200 | Links, body |
| heikin ashi candle formula | 150 | Body (bold) |
| range charts | 100 | Body, conclusion |
| ohlc charts | 40 | Body (bold) |
| reading candlestick charts | 50 | Bar Charts section |

### Skipped

| Keyword | Volume | Reason |
|---------|--------|--------|
| order flow chart | 250 | Advanced concept, out of scope |
| renko chart patterns / pdf | 200/50 | Patterns covered in separate lesson |
| renko chart strategy / trading strategy | 150/50 | Strategy not in scope |
| heikin ashi candle patterns | 150 | Patterns covered in separate lesson |
| renko chart free | 90 | Commercial keyword |
| best renko chart settings | 40 | Settings detail beyond scope |
| renko chart formula | 30 | Formula detail beyond scope |
| how renko chart works | 20 | Already explained implicitly |

---

## Step 2 Log: ToV Rewrite

**Topic classification:** BEGINNER

### Sentence Changes

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "Watching market fluctuations and volatility in real-time is an essential skill to develop." | "Reading price data in real time starts with choosing the right chart type." | ToV: throat-clearing opener replaced with principle-first opening that leads directly to the lesson topic |
| 2 | "**Candlestick charts** are the most popular method of charting and applying technical analysis." | "**Candlestick charts** are the most popular format for technical analysis." | ToV: tighter phrasing, "method of charting and applying" is wordy |
| 3 | "**Time-based periodicity** is the most popular and common among traders." | "**Time-based periodicity** is the most common setting among traders." | ToV: "popular and common" is redundant; added "setting" for clarity |
| 4 | "If you use something like a 40-minute or 3-hour chart, the candlestick patterns on your chart may carry less relevance since fewer traders observe them." | "If you use a 40-minute or 3-hour chart, the candlestick patterns on your chart may carry less relevance since fewer traders observe them." | ToV: "something like" is casual filler, removed |
| 5 | "Non-time-based charts are less common, but they still provide traders with valuable information." | "Non-time-based charts are less common, but they provide traders with valuable information." | ToV: "still" is filler, removed |
| 6 | "Traders can use **tick charts** and **range charts** in the FTMO cTrader platform — these two are the most popular non-time-based formats." | "Traders can use **tick charts** and **range charts** in the FTMO cTrader platform. These are the most popular non-time-based formats." | Banned punctuation: em dash replaced with full stop; "two" removed (redundant) |
| 7 | "Consider EURUSD, which is quoted in five decimal places — one tick would equal 0.00001 or 1 pipette." | "Consider EURUSD, which is quoted in five decimal places: one tick would equal 0.00001 or 1 pipette." | Banned punctuation: em dash replaced with colon |
| 8 | "Compared to [Japanese candlesticks](/lesson/japanese-candlesticks/), bar charts are less intuitive for new traders when it comes to reading candlestick charts." | "Compared to [Japanese candlesticks](/lesson/japanese-candlesticks/), bar charts are less intuitive for new traders reading candlestick charts." | ToV: "when it comes to" is wordy, removed |
| 9 | "However, they may present a cleaner picture when it comes to marking out [support and resistance](/lesson/support-and-resistance/)." | "However, they may present a cleaner picture for marking out [support and resistance](/lesson/support-and-resistance/)." | ToV: "when it comes to" is wordy, replaced with "for" |
| 10 | "Here is how the **Heikin Ashi candle formula** works: Heikin Ashi candles are constructed the same way as the candlestick chart but use a different calculation method." | "The **Heikin Ashi candle formula** constructs candles the same way as a standard candlestick chart but applies a different calculation method." | ToV: "Here is how...works:" is throat-clearing; restructured to lead with the subject directly |
| 11 | "Chart type is a reading tool — the edge comes from your analysis of what the chart shows, not from the format itself." | "Chart type is a reading tool. The edge comes from your analysis of what the chart shows, not from the format itself." | Banned punctuation: em dash replaced with full stop |
| 12 | "The most practical approach is to experiment with different types of trading charts and settings to find what works for your trading style. Regular time-based candlestick charts remain the most popular format, used by traders worldwide. Tick charts, range charts, Renko charts, and Heikin Ashi candles can also add value to your strategy when applied to the right context." | "Start with candlestick charts. They are the industry standard for a reason. Once you are comfortable reading price action, experiment with different types of trading charts and settings to find what works for your trading style. Tick charts, range charts, Renko charts, and Heikin Ashi candles can add value to your strategy when applied to the right context." | ToV: conclusion rewritten to be action-oriented per guide; "also" filler removed; same facts preserved (candlestick = most popular, other types add value) |

### Tone Markers Applied
- [x] Section openings lead with value
- [x] Short-long-short sentence rhythm
- [x] Casual markers eliminated ("something like", "still")
- [x] Consistent reader addressing (you/your)
- [x] No hype, no empathy, no cheerleading
- [x] Confident but not aggressive
- [x] All facts and keywords preserved
- [x] Em dashes removed (3 instances)
- [x] No contractions in body text

---

## Step 3 Log: Structure & Formatting

**Article length:** MEDIUM (~1,150 words)

### Paragraph Audit

| Section | Words | Action |
|---------|-------|--------|
| Other Chart Types (single paragraph) | ~100 | Split into 2 paragraphs |
| All other paragraphs | <70 | No action needed |

### Changes Applied

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Paragraph split | Other Chart Types: split after "...rather than time intervals." into two paragraphs (price-only formats vs. volume-based formats) | Structure: paragraph at 100-word limit, natural thematic break between price-only and volume-based chart types |
| 2 | Callout added | Note after Time-Based Charts: "For a deeper look at how different timeframes work together, see Multiple Timeframe Analysis." | Navigation: relevant internal link, connects timeframe discussion to advanced lesson |
| 3 | Internal link added | Multiple Timeframe Analysis (/lesson/multiple-timeframe-analysis/) added in Note callout (change #2) and in Next Steps section | Navigation: 5th unique internal link (was 4, now 5); directly relevant to timeframe discussion |
| 4 | Em dashes removed | Key Takeaways: 3 em dashes replaced with periods or commas (e.g. "— start here" to ". Start here"; "— useful for" to ", useful for"; "— at the cost" to ", at the cost") | Banned punctuation: em dashes not allowed in article text |
| 5 | Em dashes removed | Next Steps: 3 em dashes replaced with colons (e.g. "— how to identify" to ": how to identify") | Banned punctuation: em dashes not allowed; colons suit the label-description pattern |
| 6 | Spelling | "recognizable" changed to "recognisable" in Next Steps | Language: British English required |

### Structure Checklist
- [x] Single H1 (lesson title)
- [x] Logical H2-H3 hierarchy (no skipped levels)
- [x] Prerequisites stated
- [x] Internal links: 5 unique lessons (Japanese Candlesticks, Chart Patterns, Support/Resistance, Market Environment, Multiple Timeframe Analysis)
- [x] Callouts: 3 total (1 Note, 1 Tip, 1 Warning) within medium-article limits (2-3)
- [x] No back-to-back callouts
- [x] Comparison table present (6 chart types)
- [x] Key Takeaways present
- [x] Next Steps present
- [x] Author attribution present
- [x] Risk Warning present
- [x] Educational Notice present
- [x] No paragraphs over 100 words
- [x] No em dashes in article text
- [x] British English throughout

---

## Step 4 Log: HTML Conversion + DOCX

### Files Generated

| File | Path |
|------|------|
| HTML | `data/output/lessons/types-of-trading-charts/lesson_types-of-trading-charts_EN_v10.html` |
| DOCX | `data/output/lessons/types-of-trading-charts/lesson_types-of-trading-charts_EN_v10.docx` |

### HTML Template: v2_balanced

| Element | Status |
|---------|--------|
| Meta title | "Types of Trading Charts \| FTMO Academy" (41 chars) |
| Meta description | 155 chars |
| Canonical URL | https://academy.ftmo.com/lesson/types-of-trading-charts/ |
| Poppins font loaded | Yes |
| H1 color #2d2d2d | Yes |
| H2/H3 color #123a83 | Yes |
| Links color #0781fe | Yes |
| Table headers #123a83 | Yes |
| ToC nested (H2 + H3) | Yes |
| No Prerequisites inline block | Correct (handled by CMS sidebar) |
| Images at original positions | Yes (4 images) |
| Alt text on all images | Yes |
| Callouts styled (Note, Tip, Warning) | Yes |
| Key Takeaways section | Yes (styled background) |
| Comparison table | Yes (6 chart types, 4 columns) |
| Author box | Yes |
| Educational Notice | Yes |
| Risk Warning | Yes |
| Black header + footer | Yes |
| Responsive (max-width 1160px) | Yes |
| No max-width on paragraphs/lists | Correct |

### DOCX
- Generated via python-docx
- Headings, bold, tables, lists preserved
- Image placeholders marked as [Image: description]
