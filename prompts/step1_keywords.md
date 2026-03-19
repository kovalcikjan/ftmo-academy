# Step 1: Keyword Integration

You are optimizing educational content for SEO. Your task is to naturally integrate target keywords into the provided article.

## CORE PRINCIPLE

> **CRITICAL:** Only ADD keywords to existing text. NEVER change the meaning or information.
> Keywords enrich the text, they don't replace content.

## Rules

### What CHANGES

| Area | Example |
|------|---------|
| **Keyword variants** | "Heikin Ashi" -> "Heikin Ashi candles" |
| **Natural synonyms** | "chart" -> "trading chart" (if keyword) |
| **Phrases** | Add keyword where it fits naturally |

### What STAYS THE SAME

| Area | Rule |
|------|------|
| **Meaning** | Sentence meaning unchanged |
| **Facts** | No new information added |
| **Readability** | Text must flow naturally |
| **Keyword stuffing** | NEVER force keywords unnaturally |

## Volume-Based Priority (Relative)

Volume determines **relative priority within the file**, not absolute thresholds:

| Priority | How to Identify | Target | Focus |
|----------|-----------------|--------|-------|
| **Top keywords** | Highest volume in file (top 3-5) | 2-3x | Headings + intro + conclusion |
| **Secondary** | Mid-range volume | 1-2x | H3 + intro/conclusion |
| **Supporting** | Lower volume | 0-1x | Body text where relevant |

> **Rule:** Sort keywords by Volume descending. Top keywords go to headings first.
> All placements depend on **relevance to the specific article**.
> Keywords can repeat naturally if it makes sense in context.

## Keyword Placement Positions

| Position | Which Keywords | Example |
|----------|----------------|---------|
| **H1 title** | #1 keyword (if fits) | "Types of Trading Charts" |
| **H2 headings** | Top 3-5 keywords | "## Renko Charts" |
| **H3 headings** | Top + secondary | "### Heikin Ashi Strategy" |
| **Intro paragraph** | Top keywords | First mention of topic |
| **Conclusion** | Top keywords | Summary/wrap-up |
| **Body text** | All keywords | Where relevant and natural |

> **Rule:** Top keywords should appear in headings first, then body text. Headings have more SEO weight.
> **Flexibility:** If a top keyword doesn't fit naturally in a heading, place it in body text instead.

## Keyword Integration Rules

1. **First mention = full form**
   - "Renko" -> "Renko charts" (first time)
   - Later mentions can use shorter form

2. **Never change meaning**
   - "a range of tick charts" != "range charts"
   - If substitution changes meaning -> SKIP

3. **Natural flow required**
   - Sentence must read naturally after change
   - If awkward -> SKIP

4. **Use keyword variants**
   - "renko" -> "renko charts" / "renko chart"
   - Match singular/plural to context

5. **Significant changes require confirmation**
   - If keyword requires more than minor text adjustment
   - PROPOSE the change, do NOT apply automatically
   - Mark as "PENDING" in log
   - Examples:
     - Synonym: xlsx "OHLC charts", text "bar charts" -> PENDING
     - Restructure: xlsx "heikin ashi strategy", text "approach to trend following" -> PENDING
     - New content needed: xlsx "tick chart settings" but no related text -> SKIP or propose NEW

## Decision Tree

```
Process keywords sorted by Volume (descending):

1. Determine relative priority:
   -> Top 3-5 by volume: prioritize for headings
   -> Rest: body text based on relevance

2. Check Notes column:
   -> Has specific instructions? Follow those.
   -> Empty? Continue with standard rules.

3. Is there relevant text in article?
   -> NO: Log as SKIP (or propose NEW for top keywords)
   -> YES: Continue

4. Can keyword fit in a heading? (for top keywords)
   -> YES + natural: Add to H2/H3
   -> NO: Place in body text instead

5. How much change is needed?
   -> MINOR (variant, singular/plural): Apply + log as DONE
   -> SIGNIFICANT (synonym, restructure): Log as PENDING

6. Does it fit naturally?
   -> YES: Add keyword
   -> NO: Skip this instance
```

## LOG INTEGRITY — NON-NEGOTIABLE

> **CRITICAL: The "Original" column MUST be copied verbatim from the article file — character by character.**
> NEVER reconstruct from memory. NEVER paraphrase. NEVER approximate.
>
> **Correct process for each change:**
> 1. Locate the exact sentence in the source article file
> 2. Copy it exactly as it appears — including punctuation, capitalization, formatting
> 3. Apply the keyword change
> 4. Log: [verbatim original] → [exact changed version]
>
> **If you are unsure of the exact wording — re-read the file before logging.**
> A log with approximate originals is worse than no log.

## Output Format

Output the modified article with keywords integrated. After the article, include a change log:

```
---

## Step 1 Log: Keywords

**Keywords file:** `[filename].xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | "Renko is similar to" | "Renko charts are similar to" | renko charts | 400 | H3 | DONE |
| 2 | "understanding Heikin Ashi" | "understanding Heikin Ashi candles" | heikin ashi candles | 1400 | H2 | DONE |
| 3 | "bar charts are vertical" | "OHLC charts are vertical" | ohlc charts | 40 | Body | PENDING |
```

**Status values:**
- `DONE` - Change applied (minor change or approved)
- `PENDING` - Significant change, awaiting confirmation
- `SKIP` - No similar text exists, cannot integrate
- `NEW` - Requires new content (H3 section, new paragraph)
- `REJECTED` - Proposed change rejected by user

## Input

The article text and keywords list follow below. Process the article and integrate keywords naturally.
