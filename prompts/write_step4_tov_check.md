# Step 4: Tone of Voice Check (Light Pass)

You are reviewing a draft that was already written in Academy Tone of Voice. This is a verification step, not a full rewrite.

## CORE PRINCIPLE

> **VERIFY AND FIX — DO NOT REWRITE.**
> The draft from Step 3 is already in Academy ToV. Your job is to catch slippage — sentences that missed the mark — and fix only those.
> Untouched sentences are correct as written. Do not improve what isn't broken.

---

## What This Step Is NOT

- NOT a full ToV rewrite (that would be Step 2 in the `/academy` edit workflow)
- NOT a content review (substance was handled in Steps 1-3)
- NOT a structural pass (that comes in Step 5)

If the draft is well-written, this step may produce 0-5 flagged items. That is a success, not a sign of insufficient review.

---

## Review Checklist

Work through the draft section by section. For each paragraph, ask:

### Tone Markers

| Check | Pass condition |
|-------|----------------|
| Section openings lead with value | No "In this section we will..." openers |
| Principle → mechanics → application pattern | Concept explanations follow this flow |
| Short-long-short sentence rhythm | No 3+ consecutive long sentences |
| Casual markers absent | No "pretty much", "kind of", "a bit", "just", "basically" |
| Consistent reader addressing | "you/your" dominant; no mid-paragraph switch to "one" or "the trader" |
| No hype language | No "amazing", "great", "life-changing", "guaranteed" |
| No condescension | No "It's simple", "Obviously", "Even beginners can" |
| No vague advice | "Manage your risk" only with specifics attached |
| Emotional calibration correct | No cheerleading, no empathy phrases, no fear-mongering |
| Closings are action-oriented | No generic summaries |

### Vocabulary Spot Check

Scan for prohibited patterns:

| Pattern | Fix |
|---------|-----|
| "But" at sentence start | → "However," or restructure |
| "pretty much / kind of / sort of" | → Remove or replace with precise language |
| "a little / a bit" | → Remove (hedging weakens authority) |
| "just" as filler | → Remove entirely |
| "great / amazing / awesome" | → "effective / useful / reliable" |
| "Basically, ..." | → Remove — get to the point |
| "So, ..." as opener | → Direct statement |
| Exclamation marks | → Remove. Confidence doesn't shout. |

---

## Output Format

### Issues Found

For each issue, provide the full original sentence and the corrected version:

```
## Step 4 Log: ToV Check

**Sentences reviewed:** [N]
**Issues found:** [N]

| # | Location | Issue Type | Original sentence (full) | Corrected sentence (full) |
|---|----------|------------|--------------------------|---------------------------|
| 1 | Intro, para 2 | Casual marker ("just") | "You just need to..." | "Apply the following..." |
| 2 | H2 "Risk", para 1 | Vague advice | "Make sure to manage your risk carefully." | "Cap your risk per trade at 1 to 2% of account equity. Define it before entering, not after." |
```

**Issue Types:** Casual marker / Hype language / Vague advice / Condescension / Wrong opener / Cheerleading / Rhythm (3+ long sentences) / Prohibited phrase

### Article (corrected)

Output the full article with only the flagged sentences replaced. All other text is unchanged.

> **CRITICAL:** Output as plain markdown. Do NOT wrap in a code fence. Start directly with the `#` heading.

---

## If No Issues Found

```
## Step 4 Log: ToV Check

**Sentences reviewed:** [N]
**Issues found:** 0

Draft passes ToV verification. No corrections applied.
```

Then output the article unchanged.

---

## Stop Condition

After the log and corrected article:

> **Step 4 complete.**
>
> ToV check: [N] issues found and corrected.
>
> Review the corrections above. You can:
> - Approve and proceed to Step 5 (Structure & Formatting)
> - Request additional changes before proceeding

**Wait for user confirmation before proceeding to Step 5.**

---

## Input

Review the draft from Step 3 (with any user edits applied). Apply only targeted corrections.
