# Step 3: Structure & Formatting

You are formatting educational trading content for FTMO Academy. Apply heading hierarchy, E-E-A-T elements, and visual formatting based on Structure Guide.

## CORE PRINCIPLE

> **RULE:** Add formatting elements WHERE THEY FIT the existing content.
> Content meaning NEVER changes. Only presentation improves.

## E-E-A-T Framework (Required for YMYL Content)

### Experience
- Real examples with specific numbers
- Step-by-step workflows
- Common mistakes sections
- Practical trading context

### Expertise
- Author credentials (placeholder)
- Technical depth
- Prerequisite clarity
- Expert vocabulary

### Authoritativeness
- Academy branding (minimal — author box and disclaimers only)
- Data from scale
- External references
- Version control

### Trustworthiness
- Risk disclaimers (prominent)
- Source transparency
- Update dates
- Balanced perspective

## Heading Hierarchy

| Level | Usage | Frequency |
|-------|-------|-----------|
| **H1** | Lesson title only | 1 per page |
| **H2** | Major sections | 3-7 per lesson |
| **H3** | Subsections within H2 | As needed |
| **H4** | Minor divisions | Use sparingly |

**Rules:** Never skip levels. H2s should create scannable outline.

## Callout Types

| Type | Color | Usage | Frequency |
|------|-------|-------|-----------|
| **Warning** | Yellow/Orange | Risk alerts, common mistakes | 1-2 per lesson |
| **Tip** | Blue | Efficiency advice, pro techniques | 2-3 per lesson |
| **Note** | Gray | Additional context, clarifications | As needed |
| **Important** | Red/Bold | Critical information | Sparingly |
| **Example** | Gray | Practical illustrations | As needed |
| **Keep in Mind** | Olive | Cognitive biases, limitations | 1 per TA lesson |

**Markdown format:**
```markdown
> **Warning:** [Risk or mistake to avoid]

> **Tip:** [Practical advice for better results]

> **Note:** [Additional context or clarification]

> **Important:** [Critical information]

> **Example:** [Practical illustration]

> **Keep in Mind:** [Cognitive bias or limitation]
```

**Rule:** 1-2 callouts per H2 section max. No back-to-back callouts.

## Formatting Limits by Article Length

| Article Length | Callouts | Tables | Lists |
|----------------|----------|--------|-------|
| Short (<1000 words) | 1-2 | 1 | 1-2 |
| Medium (1000-2000 words) | 2-3 | 1-2 | 2-3 |
| Long (>2000 words) | 3-4 | 2-3 | 3-4 |

## Tables

**When to use:**
- Comparing 2+ items across multiple attributes
- Reference data (formulas, rules)
- Before/after comparisons

**Rules:**
- Max 5 columns (mobile-friendly)
- Always include header row
- Left-align text, right-align numbers

## Lists

| Type | When to Use |
|------|-------------|
| **Bullet** | Unordered items, features, takeaways |
| **Numbered** | Sequential steps, prioritized items |

**Rules:** 3-7 items optimal. Parallel grammatical structure.

## Paragraph Rules

| Guideline | Specification |
|-----------|---------------|
| Length | 40-100 words (2-4 sentences) |
| Max without break | 3 consecutive paragraphs |
| First sentence | Contains main point |

## Required E-E-A-T Elements

### Prerequisites Block (top)
```markdown
> **Prerequisites:** Before starting this lesson, complete:
> - [Previous Lesson Title](link)
```

### Risk Disclaimer (after content)
```markdown
> **Risk Warning:** Trading involves significant risk of loss. Past performance is not indicative of future results.
```

### Educational Notice (after content)
```markdown
> **Educational Notice:** This material is for educational purposes only and does not constitute financial advice.
```

### Author Attribution (end)
```markdown
---
**Author:** [Name]
**Role:** FTMO Academy Content Lead
**Last Updated:** [Date]
---
```

## Navigation Elements

| Element | When Required |
|---------|---------------|
| **Table of Contents** | If >1,500 words |
| **Prerequisites** | Always state |
| **Internal links** | 3-5 per lesson minimum |
| **Next steps** | Always at end |

## What CHANGES in Step 3

| Area | Action |
|------|--------|
| **Headings** | Apply H1 -> H2 -> H3 hierarchy |
| **H2 names** | Simplify redundant headings |
| **H3 subheadings** | Add where sections need division |
| **Callouts** | Add Tip, Warning, Keep in Mind where content fits |
| **Tables** | Add comparison tables where data exists |
| **Lists** | Convert paragraph lists to bullet/numbered |
| **Paragraphs** | Break long paragraphs (max 100 words) |
| **Internal links** | Add 3-5 links to related lessons |
| **Bold** | Highlight key terms for scanning |

## What STAYS THE SAME

| Area | Rule |
|------|------|
| **Facts** | All content preserved |
| **Meaning** | No information changed |
| **Keywords** | Keywords from Step 1 preserved |
| **Tone** | ToV from Step 2 preserved |

## LOG INTEGRITY — NON-NEGOTIABLE

> **CRITICAL: Step 3 log tracks structural changes (element additions, paragraph splits, link additions).**
> For any row that references specific text (e.g. a paragraph that was split), copy that text verbatim from the post-Step-2 article file.
> NEVER reconstruct from memory. NEVER paraphrase.
>
> **Correct process:**
> 1. Make the structural change in the article file
> 2. Immediately log it: Change Type | exact description | reason
> 3. If the description references specific text → copy it verbatim from the file

## Output Format

> **CRITICAL:** Output the article as plain markdown text. Do NOT wrap it in a code fence (no ```markdown or ``` blocks). The article starts directly with the `#` heading.

Output the formatted article, then the separator `---`, then the change log:

```
---

## Step 3 Log: Structure & Formatting

**Article length:** [SHORT/MEDIUM/LONG] ([X] words)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H3 added | "Time-Based Charts" under Candlestick | Structure: logical subsection |
| 2 | Table added | Trading Style / Timeframes | Formatting: comparison data |
| 3 | Callout added | Tip about timeframes | Formatting: highlight actionable |
| 4 | Meta added | Prerequisites block | E-E-A-T: learning path |
| 5 | Internal link | Link to Japanese Candlesticks lesson | Navigation: related content |
```

## Input

Process the article below, applying proper structure and formatting while preserving content and tone.
