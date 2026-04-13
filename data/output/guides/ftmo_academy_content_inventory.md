# FTMO Academy: Content Inventory

**Version:** 2.0
**Created:** 2026-02-26
**Updated:** 2026-04-10
**Source:** [Google Sheet "nová struktura"](https://docs.google.com/spreadsheets/d/11iNdOL7YH8Dn5FwVXlz_RC9olhC2kFiNsOffbZMZPHs/edit?gid=1420632502)

---

## Content Hierarchy

The Academy uses a 3-level hierarchy:

| Level | Sheet column | Article? | Description |
|-------|-------------|----------|-------------|
| **Lekce** (Lesson) | B | Yes (summary article composed of chapters) | Top-level section, e.g. "2.1. Graf a timeframe" |
| **Kapitola** (Chapter) | C | Yes (standalone article on a specific topic) | Sub-section, e.g. "2.1.1. Typy grafů" |
| **Podtéma** (Subtopic) | D | No (content within a chapter) | Detail inside a chapter, e.g. "Types of trading charts" |

**Rules:**
- Articles are created for Lekce (B) and Kapitola (C) only.
- Podtéma (D) is content within a chapter, not a separate article.
- Exception: a subtopic with high search volume may get a standalone article **outside** the Academy course structure.

---

## Content Structure Overview

```
PART 1: BASICS (13 lessons)
├── Gateway to Trading (3)
├── Financial Markets (4)
└── Forex (6)

PART 2: TRADING ANALYSIS (10 lekci, ~40 kapitol)
├── 2.1. Graf a timeframe (4 kapitoly)
├── 2.2. Základní price action (5 kapitol)
├── 2.3. Svíčkové formace (1 kapitola + glossary entries)
├── 2.4. Patterny na grafu (3 kapitoly + glossary entries)
├── 2.5. Indikátory a oscilátory (5 kapitol)
├── 2.6. Fibonacci a Elliottovy vlny (2 kapitoly)
├── 2.7. Market profile a objemová analýza (5 kapitol)
├── 2.8. Divergence (3 kapitoly) — NEW
├── 2.9. Confluence a obchodní strategie (2 kapitoly) — NEW
└── 2.10. Backtesting a validace (2 kapitoly) — NEW

PART 3: ADVANCED (10 lessons)
├── Trading Platforms (3)
└── Putting it All Together (7)

PART 4: FTMO EVALUATION (4 lessons)
└── Evaluation Process (4)
```

---

## Detailed Content Inventory

### Part 1: Basics

#### Gateway to Trading (3 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 1.1.1. | Introduction to Trading | /lesson/introduction-to-trading/ | TODO | None | |
| 2 | 1.1.2. | Trader's Dictionary | /lesson/traders-dictionary/ | TODO | Lesson 1 | |
| 3 | 1.1.3. | First Trade Execution | /lesson/first-trade-execution/ | TODO | Lessons 1-2 | |

#### Financial Markets (4 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 1.2.1. | Introduction to Financial Markets | /lesson/introduction-to-financial-markets/ | TODO | Gateway | |
| 2 | 1.2.2. | Instruments Traded in Financial Markets | /lesson/instruments-traded-in-the-financial-markets/ | TODO | Lesson 1 | |
| 3 | 1.2.3. | Trading Terminology | /lesson/trading-terminology/ | TODO | Lesson 1 | |
| 4 | 1.2.4. | CFD - Contracts For Difference | /lesson/cfd/ | TODO | Lessons 1-3 | |

#### Forex (6 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 1.3.1. | What is Forex | /lesson/what-is-forex-and-how-it-differs-from-other-markets/ | TODO | Financial Markets | |
| 2 | 1.3.2. | Forex Market Structure | /lesson/forex-market-structure-and-participants/ | TODO | Lesson 1 | |
| 3 | 1.3.3. | Currencies and Correlations | /lesson/what-is-traded-in-forex-currencies-and-correlations/ | TODO | Lessons 1-2 | Market Correlations |
| 4 | 2.1.2.4. | Trading Hours and Sessions | /lesson/forex-trading-hours-and-sessions/ | UPDATED | Lesson 1 | Economic Calendar, Fundamental Indicators, CFD |
| 5 | 1.3.5. | Types of Analysis | /lesson/technical-fundamental-sentiment-and-statistical-analysis-which-one-is-best/ | TODO | Lessons 1-4 | Part 2 modules |
| 6 | 1.3.6. | Margin Trading | /lesson/margin-trading-explained/ | TODO | Lessons 1-3 | Risk Management |

---

### Part 2: Trading Analysis

> **Hierarchy:** Lekce (B) = summary article from chapters | Kapitola (C) = standalone article | Podtéma (D) = content within chapter, not a separate article.
> **Type column:** L = Lekce, K = Kapitola, P = Podtéma, G = Glossary entry.
> **Source:** [Google Sheet "nová struktura"](https://docs.google.com/spreadsheets/d/11iNdOL7YH8Dn5FwVXlz_RC9olhC2kFiNsOffbZMZPHs/edit?gid=1420632502)

#### 2.1. Graf a timeframe (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.1. | L | Graf a timeframe | Charts and Timeframes | 4,450 | Brief ke zpracování |
| 2.1.1. | K | Typy grafů: čárový, sloupcový, svíčkový | Chart Types: Line, Bar, Candlestick | 500 | Vygenerovaný text k jazykové korektuře |
| 2.1.1.1. | P | Types of trading charts | Types of Trading Charts | — | existující článek |
| — | P | Anatomie svíčky (OHLC) | Candlestick Anatomy (OHLC) | 42,100 | případný backlog |
| 2.1.2. | K | Volba časových rámců pro různé styly | Choosing Timeframes by Trading Style | 1,740 | Brief k revizi eVisions |
| 2.1.2.1. | P | Hierarchie timeframů | Timeframe Hierarchy | 120 | Brief k revizi eVisions |
| 2.1.2.2. | P | Výběr timeframu podle stylu | Choosing Timeframe by Style | 730 | Brief k revizi eVisions |
| 2.1.3. | K | Multiple time frame analýza | Multiple Timeframe Analysis | 1,360 | Brief ke kontrole FTMO |
| 2.1.4. | K | Forex trading hours and sessions | Forex Trading Hours and Sessions | 25,700 | Vygenerovaný text k jazykové korektuře |

#### 2.2. Základní price action (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.2. | L | Základní price action | Price Action Basics | 7,430 | Brief ke zpracování |
| 2.2.1. | K | Support a resistance | Support and Resistance | 9,730 | Vygenerovaný text k revizi FTMO |
| — | P | Flip zóny (resistance → support) | Flip Zones | 30 | — |
| — | P | Dynamic S/R (MA jako podpora/odpor) | Dynamic S/R | 60 | — |
| — | P | Round numbers jako S/R | Round Numbers as S/R | 400 | — |
| — | P | Horizontální úrovně (price levels) | Horizontal Levels | 40 | — |
| 2.2.4. | K | Supply & Demand zóny | Supply and Demand Trading | 3,680 | Vygenerovaný text k jazykové korektuře |
| 2.2.2. | K | Trendové linie a definice trendu | Trend Lines and Trend Definition | 9,890 | Brief ke kontrole FTMO |
| — | P | Trendové linie | Trend Lines | 270 | — |
| — | K | Gap (cenová mezera) | Gap Trading | 3,550 | případný backlog |
| 2.2.3. | K | Market environment: ranges and trends | Market Environment: Ranges vs Trends | 1,780 | Vygenerovaný text k revizi FTMO |
| 2.2.5. | K | Aktivita na levelech | Activity at Levels | 4,220 | Brief ke zpracování |
| — | P | Pullback | Pullback | — | — |
| — | P | Breakout | Breakout | — | — |
| — | P | False breakout (fakeout) | False Breakout (Fakeout) | — | — |

#### 2.3. Svíčkové formace (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.3. | L | Svíčkové formace | Candlestick Formations | — | Brief ke zpracování |
| 2.3.1. | K | Candlestick patterns/formations | Candlestick Patterns | 49,000 | — |
| 2.3.1.1. | P | Marubozu | Marubozu | 2,330 | G |
| 2.3.1.2. | P | Doji (Dragonfly, Gravestone) | Doji | 17,900 | Brief ke zpracování |
| 2.3.1.3. | P | Hammer | Hammer | 17,700 | — |
| 2.3.1.4. | P | Engulfing | Engulfing | 16,100 | — |
| — | P | Shooting Star | Shooting Star | 7,200 | — |
| 2.3.1.5. | P | Inside Bar | Inside Bar | 1,990 | G |
| 2.3.1.6. | P | Three White Soldiers | Three White Soldiers | 2,150 | G |
| 2.3.1.7. | P | Morning Star | Morning Star | 4,990 | G |
| 2.3.1.8. | P | Evening Star | Evening Star | 6,140 | — |
| 2.3.1.9. | P | Interpretace svíček v kontextu trendu | Reading Candlesticks in Context | 2,770 | G |
| — | P | Hanging Man | Hanging Man | 5,740 | G |
| — | P | Harami (bullish/bearish) | Harami | 3,520 | G |
| — | P | Tweezer Top/Bottom | Tweezer Top/Bottom | 2,900 | G |
| — | P | Spinning Top | Spinning Top | 2,260 | G |

#### 2.4. Patterny na grafu (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.4. | L | Patterny na grafu | Chart Patterns | — | — |
| 2.4.1. | K | Cenové formace | Price Formations | 26,200 | — |
| 2.4.1.1. | P | Chart patterns/formations | Chart Patterns Overview | — | — |
| 2.4.1.2. | P | Double top a double bottom | Double Top and Bottom | 16,000 | — |
| 2.4.1.3. | P | Head and shoulders | Head and Shoulders | 25,350 | — |
| 2.4.1.4. | P | Triangles, wedges and flags | Triangles, Wedges and Flags | 46,450 | — |
| 2.4.1.5. | P | Cup and handle | Cup and Handle | 29,800 | — |
| 2.4.2. | K | Pivot points | Pivot Points | 2,520 | — |
| 2.4.3. | K | Harmonic patterns | Harmonic Patterns | 1,310 | — |
| — | P | ABCD pattern | ABCD Pattern | 1,510 | G |
| — | P | Gartley | Gartley Pattern | 990 | G |
| — | P | Bat | Bat Pattern | 680 | G |
| — | P | Butterfly (+ další) | Butterfly Pattern | 550 | G |
| 2.4.5. | K | Wyckoff metodologie | Wyckoff Method | 13,580 | — |
| — | P | Accumulation → Uptrend | Accumulation | 2,120 | G |
| — | P | Distribution → Downtrend | Distribution | 5,510 | G |
| — | P | Schematika fází | Phase Schematics | — | G |

#### 2.5. Indikátory a oscilátory (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.5. | L | Indikátory a oscilátory | Indicators and Oscillators | — | — |
| 2.5.1. | K | Základní pojmy: Perioda, Source, typy výpočtů | Indicator Basics: Period, Source, Calculation Types | 2,120 | — |
| 2.5.2. | K | Klíčové indikátory | Key Indicators | — | — |
| 2.5.2.1. | P | Moving Averages (SMA, EMA, WMA) | Moving Averages | 55,950 | — |
| 2.5.2.2. | P | ATR (Average True Range) | ATR | 11,300 | — |
| 2.5.2.3. | P | Bollinger Bands | Bollinger Bands | 15,530 | — |
| — | P | Ichimoku Kinko Hyo | Ichimoku Cloud | 4,650 | — |
| — | P | ADX (Average Directional Index) | ADX | 3,530 | — |
| — | P | Parabolic SAR | Parabolic SAR | 1,230 | G |
| 2.5.3. | K | Oscilátory (RSI, Stochastics, MACD) | Oscillators | — | — |
| 2.5.3.1. | P | RSI (Relative Strength Index) | RSI | 73,750 | — |
| 2.5.3.2. | P | MACD | MACD | 22,050 | — |
| 2.5.3.3. | P | CCI (Commodity Channel Index) | CCI | 1,830 | — |
| 2.5.3.4. | P | Keltner Channels | Keltner Channels | 1,490 | — |
| 2.5.3.5. | P | VWAP | VWAP | 22,700 | — |
| — | P | Stochastic Oscillator | Stochastic Oscillator | 4,940 | — |
| 2.5.4. | K | Správné použití indikátorů | Proper Use of Indicators | 3,370 | — |
| 2.5.5. | K | Rizika indikátorů | Risks of Indicators | 0 | — |

#### 2.6. Fibonacci a Elliottovy vlny (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.6. | L | Fibonacci a Elliottovy vlny | Fibonacci and Elliott Waves | — | — |
| 2.6.1. | K | Fibonacci trading | Fibonacci Trading | 7,640 | — |
| 2.6.1.1. | P | Fibonacci retracement a extension | Fibonacci Retracement and Extension | — | — |
| 2.6.2. | K | Základní teorie Elliottových vln | Elliott Wave Theory Basics | 7,300 | — |

#### 2.7. Market profile a objemová analýza (Lekce)

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.7. | L | Market profile a objemová analýza | Market Profile and Volume Analysis | — | — |
| 2.7.1. | K | Market profile | Market Profile | 180 | — |
| 2.7.2. | K | Volume Profile, Order Flow | Volume Profile and Order Flow | 2,550 | — |
| 2.7.3. | K | Identifikace zón s vysokým/nízkým objemem | High/Low Volume Zones | 220 | — |
| 2.7.4. | K | Úvod do profilace trhu | Introduction to Market Profiling | — | — |
| 2.7.7. | K | Shrnutí a porovnání přístupů | Summary and Comparison of Approaches | — | — |

#### 2.8. Divergence (Lekce) — NEW

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.8. | L | Divergence | Divergence | — | — |
| 2.8.1. | K | Klasická divergence (bullish a bearish) | Classical Divergence | 7,880 | — |
| 2.8.2. | K | Hidden divergence | Hidden Divergence | 1,970 | — |
| 2.8.3. | K | Divergence v praxi | Divergence in Practice | 1,250 | — |

#### 2.9. Confluence a obchodní strategie (Lekce) — NEW

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.9. | L | Confluence a obchodní strategie | Confluence and Trading Strategy | — | — |
| 2.9.1. | K | Co je confluence | What is Confluence | 1,770 | — |
| 2.9.2. | K | Sestavení obchodního plánu z TA | Building a Trading Plan from TA | 2,370 | — |

#### 2.10. Backtesting a validace (Lekce) — NEW

| Lokace | Type | Name (CZ) | Name (EN) | SV | Status |
|--------|------|-----------|-----------|-----|--------|
| 2.10. | L | Backtesting a validace | Backtesting and Validation | — | — |
| 2.10.1. | K | Manuální backtesting | Manual Backtesting | 6,070 | — |
| 2.10.2. | K | Vyhodnocení výsledků | Evaluating Results | 1,730 | — |

---

### Part 3: Advanced

#### Trading Platforms (3 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 3.1.1. | MetaTrader 4 Guide | /lesson/metatrader-4-guide/ | TODO | Part 1 | |
| 2 | 3.1.2. | MetaTrader 5 Guide | /lesson/metatrader-5-guide/ | TODO | Part 1 | |
| 3 | 3.1.3. | cTrader Guide | /lesson/ctrader-guide/ | TODO | Part 1 | |

#### Putting it All Together (7 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 3.2.1. | Build Robust Trading Strategy | /lesson/building-a-robust-trading-system/ | TODO | Parts 1-2 | Trading Plan |
| 2 | 3.2.2. | Risk Management | /lesson/risk-and-money-management/ | TODO | Part 1 | Max Daily Loss, Max Loss |
| 3 | 3.2.3. | Developing Trading Plan | /lesson/developing-a-trading-plan-comprehensive-guide/ | TODO | Lessons 1-2 | |
| 4 | 3.2.4. | How to Create Trading Idea | /lesson/how-to-create-a-trading-idea/ | TODO | Parts 1-2 | |
| 5 | 3.2.5. | How to Backtest Strategies | /lesson/how-to-backtest-trading-strategies/ | TODO | Backtesting Strategy | Forward Testing |
| 6 | 3.2.6. | Forward Testing | /lesson/forward-testing-of-trading-strategies/ | TODO | Lesson 5 | |
| 7 | 3.2.7. | Overtrading | /lesson/overtrading/ | TODO | Trading Plan | |

---

### Part 4: FTMO Evaluation Process

#### Evaluation Process (4 lessons)

| # | Lokace | Lesson | URL | Status | Prerequisites | Links To |
|---|--------|--------|-----|--------|---------------|----------|
| 1 | 4.1.1. | Minimum Trading Days | /lesson/minimum-trading-days/ | TODO | Risk Management | |
| 2 | 4.1.2. | Maximum Daily Loss | /lesson/maximum-daily-loss/ | TODO | Risk Management | |
| 3 | 4.1.3. | Maximum Loss | /lesson/maximum-loss/ | TODO | Risk Management | |
| 4 | 4.1.4. | Profit Target | /lesson/profit-target/ | TODO | Risk Management | |

---

## Content Analysis Summary

### Part 2 Statistics (new structure)

| Module | Lekce (L) | Kapitoly (K) | Podtémata (P) | Glossary (G) | Total SV |
|--------|-----------|-------------|---------------|--------------|----------|
| 2.1. Graf a timeframe | 1 | 4 | 3 | 0 | 33,870 |
| 2.2. Price action | 1 | 5 | 7 | 0 | 35,780 |
| 2.3. Svíčkové formace | 1 | 1 | 14 | 9 | 161,680 |
| 2.4. Patterny na grafu | 1 | 3 | 10 | 7 | 172,370 |
| 2.5. Indikátory | 1 | 5 | 10 | 1 | 228,850 |
| 2.6. Fibonacci + Elliott | 1 | 2 | 1 | 0 | 14,940 |
| 2.7. Market/Volume profile | 1 | 5 | 0 | 0 | 2,950 |
| 2.8. Divergence | 1 | 3 | 0 | 0 | 11,100 |
| 2.9. Confluence | 1 | 2 | 0 | 0 | 4,140 |
| 2.10. Backtesting | 1 | 2 | 0 | 0 | 7,800 |
| **TOTAL Part 2** | **10** | **32** | **45** | **17** | **673,480** |

---

## Audit Status Legend

| Status | Meaning |
|--------|---------|
| Brief ke zpracování | Brief not yet created |
| Brief k revizi eVisions | Brief ready, awaiting eVisions review |
| Brief ke kontrole FTMO | Brief ready, awaiting FTMO review |
| Vygenerovaný text k jazykové korektuře | AI text generated, awaiting proofreading |
| Vygenerovaný text k revizi FTMO | AI text generated, awaiting FTMO review |
| případný backlog | Nice-to-have, low priority |
| TODO | Not yet analyzed |
| ANALYZED | Content reviewed, issues identified |
| UPDATED | Edits applied |
| APPROVED | Final review complete |

---

## Next Steps

1. **Phase 1:** Audit all 50 lessons for structure/ToV compliance
2. **Phase 2:** Map internal linking opportunities
3. **Phase 3:** Create missing content (gaps)
4. **Phase 4:** Implement E-E-A-T elements across all lessons

---

*Last updated: 2026-03-08 (types-of-trading-charts → DRAFT v7)*
