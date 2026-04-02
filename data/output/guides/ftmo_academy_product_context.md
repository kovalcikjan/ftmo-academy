# FTMO Academy: Product Context Guide

**Version:** 1.0
**Created:** 2026-03-27
**Purpose:** Factual reference for editors and AI — what FTMO is, what it offers, and how its products work

---

## 1. What Is FTMO

FTMO is a proprietary trading firm founded in 2015 in Prague, Czech Republic. It provides simulated trading capital to traders who demonstrate consistent, disciplined performance through a structured evaluation process.

**Business model:** Traders pay a one-time fee to enter an evaluation (the FTMO Challenge). Those who pass receive access to a demo account with simulated capital. Traders earn performance-based rewards — up to 90% of simulated profits.

**Key numbers:**
- 3.5M+ customers served
- $500M+ in rewards distributed
- 140+ countries
- Account sizes from $10,000 to $200,000

**Important distinction:** All FTMO accounts are demo accounts with fictitious funds. Traders receive performance-based rewards, not direct trading profits. This distinction matters for compliance language in Academy content.

---

## 2. Products

### 2.1 FTMO Challenge: 2-Step

The original and most established product. Two evaluation phases, each with specific trading objectives.

| Parameter | Phase 1 (Challenge) | Phase 2 (Verification) |
|-----------|---------------------|------------------------|
| **Profit Target** | 10% | 5% |
| **Max Daily Loss** | 5% | 5% |
| **Max Overall Loss** | 10% | 10% |
| **Min Trading Days** | 4 | 4 |
| **Time Limit** | Unlimited | Unlimited |

**After passing both phases:** Trader receives an FTMO Account with up to 90% profit split.

### 2.2 FTMO Challenge: 1-Step

A newer, single-phase evaluation with tighter risk rules and no verification phase.

| Parameter | Value |
|-----------|-------|
| **Profit Target** | 10% |
| **Max Daily Loss** | 3% (recalculates daily based on balance) |
| **Max Overall Loss** | 10% |
| **Best Day Rule** | Best trading day must not exceed 50% of total profitable days' profit |
| **Min Trading Days** | 4 |
| **Time Limit** | Unlimited |

**After passing:** Trader receives an FTMO Account with 90% profit split.

**Key differences from 2-Step:**
- Single phase (no verification)
- Stricter daily loss limit (3% vs 5%)
- Best Day Rule (prevents passing on a single lucky trade)
- Fixed 90% profit split (2-Step is "up to 90%")

### 2.3 Product Comparison

| Feature | 2-Step | 1-Step |
|---------|--------|--------|
| Evaluation phases | 2 | 1 |
| Total profit target | 15% (10% + 5%) | 10% |
| Max daily loss | 5% | 3% |
| Max overall loss | 10% | 10% |
| Best Day Rule | No | Yes |
| Profit split | Up to 90% | 90% |
| Best for | Traders who prefer relaxed daily limits | Traders who want faster path to funded account |

### 2.4 Account Sizes

Available for both 1-Step and 2-Step:

| Account Size | Example Max Daily Loss (2-Step) | Example Max Daily Loss (1-Step) |
|-------------|-------------------------------|-------------------------------|
| $10,000 | $500 | $300 |
| $25,000 | $1,250 | $750 |
| $50,000 | $2,500 | $1,500 |
| $100,000 | $5,000 | $3,000 |
| $200,000 | $10,000 | $6,000 |

---

## 3. FTMO Account (Post-Evaluation)

After passing the Challenge (and Verification for 2-Step), the trader receives an FTMO Account.

### Account Types

| Type | Key Rule |
|------|----------|
| **Standard** | No holding positions over weekends or overnight (positions must be closed by end of trading day) |
| **Swing** | Positions can be held overnight and over weekends |

### Profit Split and Rewards

- **Base profit split:** 80% to trader
- **Scaled profit split:** Up to 90% after meeting Scaling Plan criteria
- **1-Step accounts:** Start at 90%
- **Payout frequency:** On-demand (bi-weekly processing, ~8h average completion)
- **Fee refund:** Initial Challenge fee is refunded with first reward withdrawal

### Rules That Carry Over

The FTMO Account maintains the same risk parameters as the evaluation:
- Max Daily Loss limit remains active
- Max Overall Loss limit remains active
- Best Day Rule remains active (1-Step accounts only)

---

## 4. Scaling Plan

Traders can grow their account balance beyond the initial size.

### Eligibility

- Minimum 4-month trading cycle on FTMO Account
- At least 10% total net simulated profit over the 4-month period
- Minimum 2 rewards processed
- Positive account balance at scale-up time

### Growth Progression (from $200,000 base)

| Timeline | Balance | Max Daily Loss | Max Overall Loss |
|----------|---------|----------------|------------------|
| Start | $200,000 | $10,000 | $20,000 |
| +4 months | $250,000 | $12,500 | $25,000 |
| +8 months | $300,000 | $15,000 | $30,000 |
| +12 months | $350,000 | $17,500 | $35,000 |

- Each scale-up: 25% balance increase
- Maximum allocation: $2,000,000
- Profit split increases to 90% after first scale-up

---

## 5. Other Products

### Free Trial

- Free demo evaluation with simplified rules
- No fee, unlimited attempts
- Purpose: let traders test the evaluation format before committing
- Does NOT lead to an FTMO Account

### Premium Programme

- Exclusive tier for top-performing funded traders
- Enhanced benefits and conditions
- Invitation-based

---

## 6. Evaluation Process Flow

```
ENTRY POINT
    │
    ├── Free Trial (optional) ──→ Practice only
    │
    ├── 2-Step Challenge
    │   ├── Phase 1: Challenge (10% target, 5% daily loss, 10% max loss)
    │   │   ├── PASS ──→ Phase 2
    │   │   └── FAIL ──→ Retry (new fee)
    │   │
    │   └── Phase 2: Verification (5% target, same loss limits)
    │       ├── PASS ──→ FTMO Account
    │       └── FAIL ──→ Retry (new fee)
    │
    └── 1-Step Challenge
        ├── Single phase (10% target, 3% daily loss, 10% max loss + Best Day Rule)
        │   ├── PASS ──→ FTMO Account
        │   └── FAIL ──→ Retry (new fee)
        │
        └── FTMO Account
            ├── Trade with simulated capital
            ├── Earn up to 90% of simulated profits
            └── Scaling Plan ──→ Up to $2,000,000
```

---

## 7. Trading Platforms

| Platform | Availability |
|----------|-------------|
| MetaTrader 4 | All products |
| MetaTrader 5 | All products |
| cTrader | All products |

---

## 8. Terminology for Academy Content

When writing Academy content, use these terms consistently:

| Term | Definition | Notes |
|------|-----------|-------|
| **FTMO Challenge** | The evaluation process (1-Step or 2-Step) | Not "test" or "exam" |
| **Verification** | Phase 2 of the 2-Step Challenge | Only in 2-Step context |
| **FTMO Account** | Post-evaluation trading account | Not "funded account" (compliance) |
| **Simulated capital** | The fictitious funds in the account | Not "real money" or "capital" |
| **Performance-based rewards** | Trader's share of simulated profits | Not "salary" or "earnings" |
| **Profit split** | Percentage of simulated profit paid as reward | Standard: 80%, Scaled: up to 90% |
| **Max Daily Loss** | Maximum permitted loss in a single day | Resets daily |
| **Max Overall Loss** | Maximum permitted loss from initial balance | Absolute limit |
| **Best Day Rule** | 1-Step only: best day capped at 50% of all profitable days | Prevents single-trade passes |
| **Scaling Plan** | Account growth program for consistent traders | After 4 months, 10% profit |
| **Free Trial** | Free practice evaluation | No path to FTMO Account |

### Compliance-Sensitive Language

| Avoid | Use Instead | Why |
|-------|------------|-----|
| "Funded account" | "FTMO Account" | All accounts are demo accounts |
| "Trading with real money" | "Trading with simulated capital" | Legal accuracy |
| "Profit" (standalone) | "Simulated profit" or "performance-based rewards" | Regulatory compliance |
| "You will earn" | "You may receive rewards" | No guarantees |
| "Investment" | "Fee" or "evaluation fee" | Challenge fee is not an investment |

---

## 9. How to Use This Document

This document is a **factual reference**, not a writing guide. Use it alongside:

| Document | Purpose |
|----------|---------|
| [ToV Guide](ftmo_academy_tov_guide_EN.md) | How to write (voice, tone, language) |
| [Structure Guide](ftmo_academy_structure_guide_EN.md) | How to format (headings, E-E-A-T, templates) |
| [Content Inventory](ftmo_academy_content_inventory.md) | What content exists and its status |
| **This document** | What FTMO is and how its products work |

When writing or editing Academy content:
1. Check **this document** for product facts and correct terminology
2. Check **ToV Guide** for how to phrase it
3. Check **Structure Guide** for how to format it

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-27 | Initial creation |

---

*This document should be updated whenever FTMO changes its products, rules, or terminology. Source of truth: ftmo.com*
