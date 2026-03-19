# FTMO Academy: Content Structure & E-E-A-T Guide

**Version:** 1.0 DRAFT
**Created:** 2026-02-26
**Purpose:** Structural standards for all FTMO Academy content to maximize E-E-A-T signals, readability, and search performance

---

## 1. Executive Summary

### What This Document Is

A comprehensive guide for **structuring** FTMO Academy content - format, hierarchy, lesson templates, and technical requirements.

> **Scope:** Structure, formatting, templates, E-E-A-T signals, technical SEO.
> **For voice and tone, see:** [Tone of Voice Guide](ftmo_academy_tov_guide_EN.md)

### Relationship to ToV Guide

| Document | Focus | Key Question |
|----------|-------|--------------|
| ToV Guide | Voice, language, emotional calibration | "How should we sound?" |
| Structure Guide | Format, hierarchy, templates, technical requirements | "How should content be organized?" |

Both documents work together. ToV defines the *words*, Structure Guide defines the *container*.

### Why Structure Matters

1. **E-E-A-T signals** - Google evaluates expertise through structural elements
2. **User experience** - 79% of users scan rather than read
3. **Accessibility** - Proper structure enables screen readers and assistive technology
4. **Conversion** - Clear structure reduces cognitive load, increases completion rates

---

## 2. E-E-A-T Framework

### Overview

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is Google's quality evaluation framework. For FTMO Academy (YMYL financial content), E-E-A-T signals are critical.

### Experience

**Definition:** First-hand, practical knowledge demonstrated in content.

| Structural Element | Implementation |
|-------------------|----------------|
| **Real examples with specifics** | "When trading a $100,000 FTMO account with 2% risk..." |
| **Process documentation** | Step-by-step workflows with actual numbers |
| **Common mistakes sections** | Demonstrate knowledge of real trader struggles |
| **Scenario-based learning** | "If price breaks above resistance at 1.0850..." |
| **FTMO-specific context** | Connect lessons to Challenge/Verification rules |

**Example block:**

```markdown
> **From FTMO Experience:** In our analysis of over 50,000 Challenge
> attempts, traders who maintained consistent 1-2% risk per trade had
> a 3x higher pass rate than those using variable position sizing.
```

### Expertise

**Definition:** Deep knowledge and competence in the subject matter.

| Structural Element | Implementation |
|-------------------|----------------|
| **Author credentials** | Trading experience, certifications, FTMO tenure |
| **Citation of sources** | Link to authoritative research, data |
| **Technical depth** | Formulas, calculations, methodology explanations |
| **Prerequisite clarity** | Show understanding of learning progression |
| **Expert vocabulary** | Use correct terminology (defined for beginners) |

**Author attribution format:**

```markdown
---
**Author:** [Name]
**Role:** FTMO Academy Content Lead
**Trading Experience:** [X] years
**Specialization:** [Area]
**Last Updated:** [Date]
---
```

### Authoritativeness

**Definition:** Recognition as a leading source on the topic.

| Structural Element | Implementation |
|-------------------|----------------|
| **Institutional backing** | "FTMO Academy" branding, consistent styling |
| **Data from scale** | "Based on analysis of [X] traders..." |
| **External references** | Link to reputable sources (academic, institutional) |
| **Version control** | Document history, update dates |
| **Peer review signals** | "Reviewed by [Role]" |

**Authority statement example:**

```markdown
> FTMO has funded over [X] traders across [Y] countries. This lesson
> draws from analysis of successful funded traders' common practices.
```

### Trustworthiness

**Definition:** Accuracy, transparency, and user safety.

| Structural Element | Implementation |
|-------------------|----------------|
| **Risk disclaimers** | Prominent, specific, not buried |
| **Source transparency** | Where claims come from |
| **Update dates** | When content was last verified |
| **Balanced perspective** | Acknowledge limitations, risks |
| **Contact/support access** | How to get help |

---

## 3. YMYL Requirements

### What Makes Trading Content YMYL

YMYL (Your Money or Your Life) content can impact financial well-being. All FTMO Academy content falls into this category.

### Risk Disclaimers

**Placement requirements:**

| Location | Type | Visibility |
|----------|------|------------|
| **Within strategy content** | Specific risk context | Inline callout box |
| **Before actionable advice** | Decision point warning | Warning callout |
| **Lesson footer** | General trading risk + legal disclaimer | Standard placement (bottom) |

**Standard risk disclaimer block:**

```markdown
> **Risk Warning:** Trading involves significant risk of loss.
> Past performance is not indicative of future results. Only
> trade with capital you can afford to lose.
```

**Strategy-specific disclaimer:**

```markdown
> **Important:** This strategy, like all trading approaches, can
> result in losses. Backtest thoroughly and trade with proper
> risk management. The examples shown are for educational purposes
> and do not guarantee similar results.
```

**Cognitive bias disclaimer (for Technical Analysis content):**

```markdown
> **Keep in Mind:** Some of our human tendencies can be dangerous
> for investors.
>
> - See patterns where there aren't any
> - Believe "market lore," technical and fundamental, without evidence
> - Look backwards rather than forward
> - Stick with original price targets of patterns after conditions have changed
```

This type of disclaimer is particularly valuable for Technical Analysis lessons as it:
- Acknowledges limitations of pattern-based analysis
- Demonstrates intellectual honesty (E-E-A-T: Trustworthiness)
- Prevents overconfidence in chart patterns
- Aligns with "realistic educator" positioning from ToV Guide

### "Not Financial Advice" Requirements

**When required:**
- Any lesson discussing specific strategies
- Content mentioning specific instruments, pairs, or setups
- Guidance that could be interpreted as recommendations

**Format:**

```markdown
> **Educational Content Notice:** This material is for educational
> purposes only and does not constitute financial advice. Trading
> decisions should be based on your own analysis and risk tolerance.
```

### Regulatory Compliance

| Requirement | Implementation |
|-------------|----------------|
| **No profit guarantees** | Never state or imply guaranteed returns |
| **No unrealistic claims** | Avoid "easy", "quick profits", "guaranteed" |
| **Geographic awareness** | Note jurisdiction-specific rules where relevant |
| **Clear FTMO relationship** | Distinguish education from product marketing |

### Factual Accuracy Standards

- **All statistics** must include source and date
- **Trading examples** must be realistic and achievable
- **Rules and requirements** must reflect current FTMO terms
- **Market data** must specify timeframe and context
- **Numerical claims** require supporting evidence or source

---

## 4. Content Structure Elements

### Heading Hierarchy

**Rules:**

| Level | Usage | Example |
|-------|-------|---------|
| **H1** | Lesson title only (1 per page) | "Risk Management Fundamentals" |
| **H2** | Major sections | "Why Risk Management Matters" |
| **H3** | Subsections within H2 | "Calculating Position Size" |
| **H4** | Minor divisions (use sparingly) | "Using the Formula" |

**Hierarchy principles:**
- Never skip levels (H2 to H4 directly)
- H2s should create scannable outline
- 3-7 H2 sections per lesson (optimal)
- H3s provide detail, H2s provide overview

**Example structure:**

```markdown
# Position Sizing Mastery (H1)

## Why Position Sizing Matters (H2)
### The Impact on Account Survival (H3)
### Connection to Risk Management (H3)

## The Position Sizing Formula (H2)
### Understanding Each Variable (H3)
### Step-by-Step Calculation (H3)

## Practical Application (H2)
### Example: EUR/USD Trade (H3)
### Example: Gold Trade (H3)

## Common Mistakes (H2)

## Key Takeaways (H2)
```

### Paragraph Rules

| Guideline | Specification |
|-----------|---------------|
| **Length** | 2-4 sentences (40-100 words) |
| **One idea per paragraph** | Single concept focus |
| **First sentence** | Contains main point (inverted pyramid) |
| **Transitions** | Connect to previous/next thought |

**Maximum consecutive paragraphs without visual break:** 3

### Sentence Rules

| Guideline | Specification |
|-----------|---------------|
| **Average length** | 15-20 words |
| **Maximum length** | 30 words |
| **Variety** | Mix short (impact) and medium (explanation) |
| **Active voice** | Default (passive OK for processes) |

### Lists: Bullet vs. Numbered

**Use BULLET lists for:**
- Unordered items (no sequence matters)
- Features, characteristics, examples
- Takeaways and summaries
- Options or alternatives

**Use NUMBERED lists for:**
1. Sequential steps (must follow order)
2. Prioritized items (ranked importance)
3. Processes with clear phases
4. Instructions requiring specific order

**List formatting rules:**
- 3-7 items optimal
- Parallel grammatical structure
- No periods for single phrases, periods for full sentences
- Nested lists: maximum 2 levels deep

### Tables

**When to use tables:**
- Comparing 2+ items across multiple attributes
- Reference data (formulas, rules, specifications)
- Before/after comparisons
- Specification lists

**Table formatting:**

| Requirement | Specification |
|-------------|---------------|
| Header row | Always required, bold |
| Alignment | Left for text, right for numbers |
| Maximum columns | 5 (wider tables break mobile) |
| Cell content | Concise (1-3 words optimal) |

**Example - Comparison table:**

| Account Size | 1% Risk | 2% Risk | 3% Risk |
|-------------|---------|---------|---------|
| $25,000 | $250 | $500 | $750 |
| $50,000 | $500 | $1,000 | $1,500 |
| $100,000 | $1,000 | $2,000 | $3,000 |

### Callout Boxes

**Types and usage:**

| Type | Icon/Color | Usage |
|------|------------|-------|
| **Warning** | Yellow/Orange | Risk alerts, common mistakes, danger zones |
| **Tip** | Green/Blue | Efficiency advice, pro techniques |
| **Note** | Blue/Gray | Additional context, clarifications |
| **Important** | Red/Bold | Critical information, must-know |
| **Example** | Gray/Neutral | Practical illustrations |
| **Keep in Mind** | Green/Olive | Cognitive biases, limitations, honest caveats |

**Markdown format:**

```markdown
> **Warning:** [Critical risk or mistake to avoid]

> **Tip:** [Practical advice for better results]

> **Note:** [Additional context or clarification]

> **Important:** [Critical information that must not be missed]

> **Example:** [Practical illustration of concept]

> **Keep in Mind:** [Cognitive bias, limitation, or honest caveat about the topic]
```

**Frequency guideline:** 1-2 callouts per major section (H2), avoid back-to-back callouts.

### Quotes & Citations

**Use quotes for:**
- Expert/authority statements
- Key principles worth memorizing
- Research findings
- FTMO official positions

**Citation format:**

```markdown
> "Risk management is the foundation of professional trading."
> *- FTMO Trading Guidelines*

According to research by [Source], traders who maintain consistent
risk parameters show [X]% higher long-term profitability.
```

**External source requirements:**
- Link to original where possible
- Include author/organization
- Include publication date for time-sensitive data

### Code/Formula Blocks

**Use for:**
- Mathematical formulas
- Calculations with variables
- Specific parameter values
- Technical indicators settings

**Format:**

```markdown
Position Size = (Account Balance x Risk %) / (Entry - Stop Loss)
```

**Example with values:**

```markdown
Position Size = ($50,000 x 0.02) / (1.0850 - 1.0800)
Position Size = $1,000 / 0.0050
Position Size = 200,000 units (2 standard lots)
```

### Visual Breaks & Spacing

**Horizontal rules (---):**
- Between major thematic shifts
- Before/after important standalone sections
- Maximum 3 per lesson

**Whitespace requirements:**
- Double line break before H2
- Single line break before H3
- Blank line between paragraphs
- Blank line before/after lists, tables, callouts

---

## 5. Lesson Template & Patterns

### Lesson Structure Template

Every FTMO Academy lesson should follow this structure:

1. **HOOK** (1-2 sentences)
   - Why this matters
   - What you'll learn

2. **CORE CONCEPT** (main content)
   - Definition/explanation
   - Visual/example
   - Key principles

3. **PRACTICAL APPLICATION**
   - How to use this
   - Real examples with numbers
   - Connection to FTMO where relevant

4. **COMMON MISTAKES**
   - What to avoid
   - Why traders fail here

5. **KEY TAKEAWAYS**
   - 3-5 bullet points
   - Actionable summary

6. **NEXT STEPS**
   - What to learn next
   - How this connects to other lessons

---

### Opening Patterns

**For Beginners:**
> "[Concept] is fundamental to trading. This lesson covers:
> - What it is
> - Why it matters
> - How to apply it
>
> Prerequisites: [list or "none"]"

**For Intermediate:**
> "[Concept] directly impacts your trading results.
> Get this right: [benefit]. Get it wrong: [consequence].
> Here's the framework."

**For Advanced:**
> "This lesson addresses the nuances of [concept] that affect Challenge performance. Assumed knowledge: [list]. Key focus: [specific advanced aspect]."

---

### Closing Patterns

**Summary + Action:**
> "Key takeaways:
> - [Point 1]
> - [Point 2]
> - [Point 3]
>
> Now it's time to practice. [Specific action step]."

**Connection to FTMO:**
> "Understanding [concept] is essential for your FTMO Challenge. In the next lesson, we'll build on this foundation with [next topic]."

---

### Text Formatting

| Element | Usage |
|---------|-------|
| **Bold** | Key terms, important points |
| *Italic* | Emphasis, introducing new terms |
| `Code` | Calculations, specific values |
| > Blockquote | Key principles, memorable phrases |
| Bullet points | Lists, takeaways |
| Numbered lists | Sequential steps |

### Numbers & Data

- Use specific numbers: "2% risk per trade" not "small risk"
- Include context: "$500 on a $25,000 account (2%)"
- Round appropriately: "approximately 60%" not "59.7%"
- Currency: USD as default, specify when different

---

## 6. Readability & UX

### Scanability

**F-Pattern Optimization:**
- Front-load important content in paragraphs
- Place key terms at start of bullet points
- Use bold for scanning anchors
- Left-align all text

**Inverted Pyramid:**
- Lead with conclusion/main point
- Follow with supporting details
- End with background/context

**Example:**

```markdown
**GOOD (Inverted Pyramid):**
Position sizing determines how many lots you trade. Calculate it
using your account balance, risk percentage, and stop loss distance.
This prevents emotional decisions and protects your capital.

**BAD (Buried Lead):**
When you're looking at a trade setup and trying to figure out the
right amount to risk, there are several factors to consider including
your account balance, your risk tolerance, and the specific setup
characteristics, which together help you determine your position size.
```

### Typography

**Font Family:** Poppins (Google Fonts)

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| **H1** | 2.25rem (36px) | 700 | 1.2 |
| **H2** | 1.5rem (24px) | 600 | 1.3 |
| **H3** | 1.25rem (20px) | 600 | 1.4 |
| **Body** | 1rem (16px) | 400 | 1.7 |
| **Small/Caption** | 0.875rem (14px) | 400 | 1.5 |

| Element | Specification |
|---------|---------------|
| **Line length** | 65-75 characters (optimal reading) |
| **Max content width** | 1160px |
| **Sentence length** | 15-20 words average |
| **Paragraph length** | 40-100 words |
| **Bold usage** | Key terms, important points (not full sentences) |
| **Italic usage** | First use of new terms, emphasis |
| **ALL CAPS** | Avoid (except acronyms: FTMO, USD, EUR) |

### Cognitive Load Management

**Chunking:**
- Break complex topics into 3-5 digestible pieces
- One concept per section
- Clear transitions between chunks

**Progressive Disclosure:**
- Start simple, add complexity
- Beginner content before advanced
- "Learn more" links for deep dives

**Complexity Reduction:**
- Reduce unnecessary options
- Default recommendations
- Clear "if this, then that" guidance

### Navigation Elements

**Table of Contents:**
- Required for lessons >1,500 words
- Link to H2 sections
- Place after introduction, before content

**Format:**

```markdown
## In This Lesson
- [Why Risk Management Matters](#why-risk-management-matters)
- [Calculating Position Size](#calculating-position-size)
- [Practical Examples](#practical-examples)
- [Common Mistakes](#common-mistakes)
- [Key Takeaways](#key-takeaways)
```

**Prerequisites Block:**

```markdown
> **Prerequisites:** Before starting this lesson, complete:
> - [Introduction to Forex](link)
> - [Understanding Pips and Lots](link)
```

**Breadcrumbs:**
- Show learning path position
- Format: Module > Section > Lesson

### Visual Hierarchy

**Priority levels (most to least prominent):**
1. H1 - Lesson title
2. H2 - Section headers
3. Callout boxes (Warning, Important)
4. Bold text within paragraphs
5. H3 - Subsection headers
6. Regular text
7. Supplementary content (captions, footnotes)

---

## 7. Crawlability & Technical SEO

### Semantic HTML Requirements

| Element | HTML Tag | Usage |
|---------|----------|-------|
| Lesson title | `<h1>` | One per page |
| Sections | `<h2>`, `<h3>`, `<h4>` | Proper hierarchy |
| Paragraphs | `<p>` | All body text |
| Lists | `<ul>`, `<ol>`, `<li>` | Proper nesting |
| Tables | `<table>`, `<thead>`, `<tbody>` | Include headers |
| Quotes | `<blockquote>` | With citations |
| Emphasis | `<strong>`, `<em>` | Semantic use |

**Avoid:**
- `<div>` for structural elements
- `<br>` for spacing (use CSS)
- Multiple `<h1>` tags
- Skipped heading levels

### Structured Data (Schema.org)

**Required schemas for Academy content:**

**Article/Course schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Risk Management Fundamentals",
  "description": "Learn essential risk management principles for trading",
  "provider": {
    "@type": "Organization",
    "name": "FTMO Academy"
  },
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online"
  }
}
```

**FAQPage schema (for FAQ sections):**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the maximum daily loss limit?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The maximum daily loss limit is 5% of initial account balance."
    }
  }]
}
```

**HowTo schema (for step-by-step content):**
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Calculate Position Size",
  "step": [{
    "@type": "HowToStep",
    "text": "Determine your account balance"
  }]
}
```

### Internal Linking Rules

| Guideline | Specification |
|-----------|---------------|
| **Minimum links per lesson** | 3-5 internal links |
| **Link placement** | Within content flow (not just end) |
| **Anchor text** | Descriptive (not "click here") |
| **Link to prerequisites** | Always include |
| **Link to next lesson** | Always include at end |
| **Link to related content** | 2-3 per lesson |

**Anchor text examples:**

```markdown
GOOD: Learn more about [calculating position size](/lessons/position-sizing)
BAD: Click [here](/lessons/position-sizing) to learn more
```

**Internal linking structure:**
- Prerequisites: Link at top
- Related concepts: Link inline when mentioned
- Advanced topics: Link for "learn more"
- Next steps: Link at conclusion

### Meta Requirements

**Title tag:**
- Format: `[Lesson Title] | FTMO Academy`
- Length: 50-60 characters
- Include primary keyword

**Meta description:**
- Length: 150-160 characters
- Include primary keyword
- Clear value proposition
- Action-oriented when appropriate

**Example:**

```html
<title>Position Sizing: How to Calculate Lot Size | FTMO Academy</title>
<meta name="description" content="Learn the exact formula to calculate
position size for any trade. Step-by-step guide with examples for
FTMO Challenge accounts.">
```

**Open Graph / Social:**
- og:title
- og:description
- og:image (featured image)
- og:type: article

---

## 8. Additional Google Signals

### Helpful Content System

**Alignment requirements:**

| Signal | Implementation |
|--------|----------------|
| **People-first content** | Write for traders, not algorithms |
| **Demonstrated expertise** | Show experience, not just compile information |
| **Primary purpose** | Educate, not just attract traffic |
| **Satisfying experience** | Reader should feel informed after reading |
| **Clear audience focus** | Content appropriate for stated skill level |

**Content must answer:**
- Does this help a real trader?
- Would an expert create this content?
- Does this add value beyond existing content?
- Is this better than what's currently ranking?

### AI Content Policies

**Transparency requirements:**
- Disclose AI assistance where relevant
- Human review mandatory for all content
- Expert verification for technical accuracy
- Original analysis, not rehashed information

**Quality standards:**
- Factually accurate
- Free of AI artifacts ("As an AI...", "I don't have personal experience...")
- Natural language patterns
- Specific, practical examples (not generic)

### Author Transparency

**Required elements:**

```markdown
---
**About the Author**

**[Name]** is a [Role] at FTMO Academy with [X] years of trading
experience. Specializing in [area], they have helped [achievement
or credential]. Connect on [platform].

*This content was reviewed by [Reviewer Name], [Reviewer Role].*

*Last updated: [Date]*
---
```

**Author page requirements:**
- Photo
- Bio (2-3 paragraphs)
- Credentials/experience
- Published content list
- Contact method

### Content Freshness

| Content Type | Review Frequency | Update Triggers |
|--------------|------------------|-----------------|
| **Core concepts** | Annually | Fundamental changes only |
| **FTMO rules/requirements** | Quarterly | Any rule changes |
| **Strategy content** | Semi-annually | Market structure changes |
| **Data/statistics** | Quarterly | New data available |
| **Current events references** | As needed | When outdated |

**Freshness signals:**
- "Last updated" date visible
- Changelog for significant updates
- Retired content marked clearly
- Regular review schedule documented

---

## 9. Checklists

### Pre-Publish Checklist

**E-E-A-T & YMYL**
- [ ] Risk disclaimer present and visible at top
- [ ] "Not financial advice" statement included (if applicable)
- [ ] Author attribution present
- [ ] All statistics have sources
- [ ] No profit guarantees or unrealistic claims
- [ ] Last updated date included

**Structure**
- [ ] Single H1 (lesson title)
- [ ] Logical H2-H3-H4 hierarchy (no skipped levels)
- [ ] Table of contents (if >1,500 words)
- [ ] Prerequisites listed
- [ ] Next steps/related content linked

**Readability**
- [ ] Average sentence length 15-20 words
- [ ] Paragraphs 40-100 words
- [ ] No more than 3 consecutive paragraphs without visual break
- [ ] Key terms bolded for scanning
- [ ] Active voice predominant

**Callouts & Formatting**
- [ ] Appropriate callout types used
- [ ] Not too many callouts (1-2 per H2 section)
- [ ] Tables used for comparisons
- [ ] Lists properly formatted (bullet vs. numbered)
- [ ] Code blocks for formulas/calculations

**Technical SEO**
- [ ] Meta title 50-60 characters
- [ ] Meta description 150-160 characters
- [ ] 3-5 internal links minimum
- [ ] Descriptive anchor text (not "click here")
- [ ] Images have alt text

**Quality**
- [ ] Matches ToV Guide principles
- [ ] Appropriate for target persona
- [ ] Practical examples included
- [ ] Common mistakes section (if applicable)
- [ ] Actionable takeaways

---

### Structure Audit Checklist

Use this checklist to audit existing content for structural compliance.

**Heading Structure**
- [ ] One H1 only
- [ ] H2s create scannable outline
- [ ] No skipped levels
- [ ] 3-7 H2 sections

**Content Blocks**
- [ ] Paragraphs appropriately sized
- [ ] Lists used effectively
- [ ] Tables for comparisons
- [ ] Callouts for emphasis

**E-E-A-T Signals**
- [ ] Author visible
- [ ] Experience demonstrated
- [ ] Sources cited
- [ ] Updated date shown

**YMYL Compliance**
- [ ] Risk warnings present
- [ ] Disclaimers accurate
- [ ] No problematic claims
- [ ] Balanced perspective

**Navigation**
- [ ] ToC present (if needed)
- [ ] Prerequisites clear
- [ ] Internal links sufficient
- [ ] Next steps clear

**Readability Score**
- [ ] Flesch Reading Ease: 60+ (target)
- [ ] Average sentence length: <25 words
- [ ] Passive voice: <15%

---

## Appendix: Quick Reference

### Structural Elements Summary

| Element | When to Use | Frequency |
|---------|-------------|-----------|
| H1 | Lesson title | 1 per page |
| H2 | Major sections | 3-7 per lesson |
| H3 | Subsections | As needed |
| Warning callout | Risk/mistakes | 1-2 per lesson |
| Tip callout | Pro advice | 2-3 per lesson |
| Keep in Mind | Cognitive biases, limitations | 1 per TA lesson |
| Table | Comparisons | As needed |
| Bullet list | Unordered items | Frequently |
| Numbered list | Sequential steps | For processes |
| Blockquote | Key principles | 1-2 per lesson |
| Code block | Formulas | For calculations |

### Callout Quick Reference

```markdown
> **Warning:** [Risk or mistake]

> **Tip:** [Practical advice]

> **Note:** [Additional context]

> **Important:** [Must-know information]

> **Example:** [Illustration]

> **Keep in Mind:** [Cognitive bias or limitation]
```

### E-E-A-T Signal Locations

| Signal Type | Location in Content |
|-------------|---------------------|
| Experience | Examples, scenarios, "common mistakes" |
| Expertise | Author bio, technical depth, methodology |
| Authority | FTMO branding, data citations, scale references |
| Trust | Disclaimers, sources, update dates, balanced view |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 DRAFT | 2026-02-26 | Initial creation |

---

## Approval

- [ ] Content Lead
- [ ] SEO Lead
- [ ] Brand Manager
- [ ] Legal/Compliance Review

---

*This document should be reviewed quarterly and updated based on Google algorithm changes, user feedback, and content performance data.*

*Companion document: FTMO Academy Tone of Voice Guide*
