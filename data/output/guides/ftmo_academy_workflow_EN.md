# FTMO Academy: Content Workflow

**Version:** 2.3
**Created:** 2026-03-04
**Purpose:** Defines the step-by-step process for creating and editing FTMO Academy content

---

## 1. Workflow Overview

```
INPUT                    PROCESS                              OUTPUT
─────                    ───────                              ──────
Original Article    →    Step 1: Keywords                →    _keywords.md
+ Keywords File     →    Step 2: ToV Rewrite             →    _tov.md
                    →    Step 3: Structure & Formatting  →    _final.md
                    →    Step 4: HTML Conversion         →    .html
                    →    Step 5: QA & Review             →    FINAL
```

### CORE PRINCIPLE: Preserve Content, Enhance Presentation

> **CRITICAL:** The original article content (facts, information, meaning) must NEVER change.
> The workflow only ENHANCES the article through:
> - Step 1: Adding keywords naturally (no new information)
> - Step 2: Improving word choice (same meaning, better words)
> - Step 3: Adding formatting elements (tables, callouts, lists)
> - Step 4: Converting to HTML + placing original images EXACTLY where they were

**What changes:** Keywords, word choice, formatting, presentation
**What NEVER changes:** Facts, information, meaning, content order

---

## 2. Reference Documents

| Document | Handles | Used In Step |
|----------|---------|--------------|
| `[lesson]_keywords.xlsx` | Target keywords for SEO | Step 1 |
| `ftmo_academy_tov_guide_EN.md` | Voice, tone, language, word choice | Step 2 |
| `ftmo_academy_structure_guide_EN.md` | Headings, sections, E-E-A-T, formatting | Step 3 |
| `ftmo_academy_content_inventory.md` | Internal links, prerequisites, content map | Step 3, 5 |

---

## 3. Input Format

### Standard Input (Varianta A)

```
Článek: https://academy.ftmo.com/lesson/[lesson-slug]/
Keywords: /path/to/[lesson-slug]_keywords.xlsx
```

### What Gets Extracted from URL

| Element | How | Used In |
|---------|-----|---------|
| **Article text** | WebFetch → markdown | All steps |
| **Image URLs** | Extract from HTML source | Initialization, Step 3, Step 4 |
| **Image positions** | Note after which paragraph/H2/H3 | Initialization, Step 3, Step 4 |
| **Image alt text** | Extract from `alt` attributes | Step 4 |
| **Video embed** | Extract YouTube URL | Step 4 |

### Image Extraction — MANDATORY at Initialization

During Initialization, create an **Image Map** before any editing begins:

```
## Image Map

| # | Original position (after which heading/paragraph) | Image URL | Alt text | Topic/context |
|---|---------------------------------------------------|-----------|----------|---------------|
| 1 | After H2 "Candlestick Charts", paragraph 2 | https://...candlestick.png | Candlestick chart | Candlestick explanation |
| 2 | After H2 "Bar Charts", paragraph 1 | https://...bar-chart.png | Bar chart OHLC | Bar chart structure |
| ... | ... | ... | ... | ... |
```

**Rules:**
- Extract ALL images from the original article (WebFetch HTML source)
- Record exact position: after which heading + which paragraph number
- Record topic context (what the image illustrates)
- This map carries through all steps — images stay with their topic, not with a fixed paragraph number
- If content is restructured in Step 3, images move with their topic

### What Gets Extracted from Keywords File

| Column | Expected Content | Required |
|--------|------------------|----------|
| **Keyword** | Target keyword phrase | YES |
| **Volume (US)** | Search volume → determines priority | YES |
| **KD** | Keyword difficulty | NO (reference) |
| **Notes** | Manual guidance for specific keywords | NO |

### Volume-Based Priority (Relative)

Volume determines **relative priority within the file**, not absolute thresholds:

| Priority | How to Identify | Placement |
|----------|-----------------|-----------|
| **Top keywords** | Highest volume in file (top 3-5) | Headings (H1, H2, H3) if possible |
| **Secondary** | Mid-range volume | Intro, conclusion, body text |
| **Supporting** | Lower volume | Body text where relevant |

> **Rule:** Sort keywords by volume descending. Top keywords go to headings first.
> All placements depend on **relevance to the specific article**.
> Keywords can repeat naturally if it makes sense in context.

**Important:** Volume thresholds vary by topic. A niche topic may have top keyword at 200 volume, while a popular topic may have 5000+. Always use relative ranking within the file.

### Example Input

```
Článek: https://academy.ftmo.com/lesson/types-of-trading-charts/
Keywords: data/output/keywords/types-of-trading-charts_keywords.xlsx
```

### Invocation

```
/academy https://academy.ftmo.com/lesson/[slug]/
Keywords: /path/to/keywords.xlsx
```

Or step-by-step:
```
/academy step 1 [URL] [keywords.xlsx]
/academy step 2 [markdown file from step 1]
/academy step 3 [markdown file from step 2]
/academy step 4 [markdown file from step 3]
```

---

## LOGGING REQUIREMENTS

Every change must be logged with a reason. The log enables:
- Review of changes after each step
- Error identification during testing
- Precise audit trail of what changed and why

### LOG INTEGRITY — THE MOST CRITICAL RULE

> **The "Original" column MUST always be copied verbatim from the article file at the time of the change.**
> NEVER reconstruct from memory. NEVER paraphrase. NEVER write what you think was there.
>
> **Mandatory process for every logged change:**
> 1. Read the current article file (use Read tool)
> 2. Find the exact sentence(s) to change
> 3. Copy them verbatim into the "Original" column
> 4. Apply the change
> 5. Write the exact new version into the "New" column
>
> **This applies to all steps:**
> - Step 1: "Original" = verbatim from source article (fetched from URL)
> - Step 2: "Original" = verbatim from post-Step-1 article file
> - Step 3: "Original" = verbatim from post-Step-2 article file (where applicable)
>
> A log with approximate originals destroys the audit trail and is worse than no log.

### Log Format

```
## Step [X] Log: [Step Name]

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "text before" | "text after" | [reason per guide] |
| 2 | ... | ... | ... |
```

### Step 1 Example (Keywords):

```
## Step 1 Log: Keywords

| # | Original sentence (full) | New sentence (full) | Keyword | Volume | Position | Status |
|---|--------------------------|---------------------|---------|--------|----------|--------|
| 1 | "Renko is similar to the range and tick charts." | "Renko charts are similar to range and tick charts." | renko charts | 400 | Intro | DONE |
| 2 | "Heikin Ashi is another chart representation that comes from Japan." | "Heikin Ashi candles are another chart representation that comes from Japan." | heikin ashi candles | 1400 | H3 body | DONE |
| 3 | "Bar charts, often called OHLC charts, are represented as vertical bars..." | unchanged — keyword already present | ohlc charts | 40 | Body | DONE |
```

### Step 2 Example (ToV Rewrite):

Log must contain **full sentences** — never excerpts. Always the complete original sentence vs the complete new sentence.

```
## Step 2 Log: ToV Rewrite

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "But it is a great tool for both entries and trade management." | "Heikin Ashi candles are effective for trend-following entries and trade management — less so for precise timing." | ToV: "But" sentence opener; "great" hype word; trade-off made explicit |
| 2 | "Compared to Japanese candlesticks, bar charts might be a little less clean for new traders when it comes to candlestick patterns." | "In practice, candlestick patterns are harder to read on bar charts, making them less intuitive for traders still learning to identify formations." | ToV: "a little less clean" hedging → direct; "might" removed |
| 3 | "We have covered Japanese candlesticks in the previous lesson, so we will do just a quick recap now." | "Japanese candlesticks are covered in the previous lesson. Here is a quick recap:" | ToV: "just" filler removed; two shorter direct sentences |
```

### Step 3 Example (Structure & Formatting):

```
## Step 3 Log: Structure & Formatting

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H3 added | "Time-Based Charts" under Candlestick Charts | Structure: logical subsection |
| 2 | Table added | Trading Style / Timeframes | Formatting: comparison data |
| 3 | Callout added | Tip about popular timeframes | Formatting: highlight actionable info |
| 4 | Meta added | Prerequisites: Japanese Candlesticks | E-E-A-T: learning path |
```

---

## 4. Step 1: Keywords

### Purpose
Integrate target keywords naturally into the original content.

> **RULE:** Only ADD keywords to existing text. NEVER change the meaning or information.
> Keywords enrich the text, they don't replace content.

### Input
- Original article
- Keywords file (`[lesson]_keywords.xlsx`)

### What CHANGES

| Area | Example |
|------|---------|
| **Keyword variants** | "Heikin Ashi" → "Heikin Ashi candles" |
| **Natural synonyms** | "chart" → "trading chart" (if keyword) |
| **Phrases** | Add keyword where it fits naturally |

### What STAYS THE SAME

| Area | Rule |
|------|------|
| **Meaning** | Sentence meaning unchanged |
| **Facts** | No new information added |
| **Readability** | Text must flow naturally |
| **Keyword stuffing** | NEVER force keywords unnaturally |

### Keyword Frequency (Relative)

| Priority | How to Identify | Target | Focus |
|----------|-----------------|--------|-------|
| **Top keywords** | Highest volume in file | 2-3x | Headings + intro + conclusion |
| **Secondary** | Mid-range volume | 1-2x | H3 + intro/conclusion |
| **Supporting** | Lower volume | 0-1x | Body text where relevant |

> **Rule:** Quality over quantity. 1-2 well-placed changes beat 5 forced ones.
> **Notes column:** If keyword has specific instructions in Notes, follow those instead.
> **Repetition:** Keywords can appear multiple times if natural and relevant.

### Keyword Placement Positions

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

### Keyword Integration Rules

1. **First mention = full form**
   - "Renko" → "Renko charts" (first time)
   - Later mentions can use shorter form

2. **Never change meaning**
   - "a range of tick charts" ≠ "range charts"
   - If substitution changes meaning → SKIP

3. **Natural flow required**
   - Sentence must read naturally after change
   - If awkward → SKIP

4. **Use keyword variants**
   - "renko" → "renko charts" / "renko chart"
   - Match singular/plural to context

5. **Significant changes require confirmation**
   - If keyword requires more than minor text adjustment
   - PROPOSE the change, do NOT apply automatically
   - Mark as "PENDING" in log
   - Examples:
     - Synonym: xlsx "OHLC charts", text "bar charts" → PENDING
     - Restructure: xlsx "heikin ashi strategy", text "approach to trend following" → PENDING
     - New content needed: xlsx "tick chart settings" but no related text → SKIP or propose NEW

### Decision Tree

```
Process keywords sorted by Volume (descending):

1. Determine relative priority:
   → Top 3-5 by volume: prioritize for headings
   → Rest: body text based on relevance

2. Check Notes column:
   → Has specific instructions? Follow those.
   → Empty? Continue with standard rules.

3. Is there relevant text in article?
   → NO: Log as SKIP (or propose NEW for top keywords)
   → YES: Continue

4. Can keyword fit in a heading? (for top keywords)
   → YES + natural: Add to H2/H3
   → NO: Place in body text instead

5. How much change is needed?
   → MINOR (variant, singular/plural): Apply + log as DONE
   → SIGNIFICANT (synonym, restructure): Log as PENDING

6. Does it fit naturally?
   → YES: Add keyword
   → NO: Skip this instance
```

### Log Format (Step 1)

```
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

### Example Transformations

**Original:**
> "Renko is similar to the range and tick charts."

**With keyword "Renko charts":**
> "Renko charts are similar to range and tick charts."

**Original:**
> "Heikin Ashi is another chart representation from Japan."

**With keyword "Heikin Ashi candles":**
> "Heikin Ashi candles are another chart representation from Japan."

### Keywords Checklist

**Relative priority:**
- [ ] Keywords sorted by Volume (descending)
- [ ] Top keywords (by volume): placed in headings where possible
- [ ] Secondary keywords: in intro, conclusion, body
- [ ] Supporting keywords: body text where relevant

**Notes column:**
- [ ] Keywords with Notes: followed specific instructions

**Integration:**
- [ ] First mention uses full keyword form
- [ ] Minor changes applied directly (DONE)
- [ ] Significant changes proposed (PENDING)
- [ ] All PENDING confirmed or REJECTED
- [ ] Missing keywords marked SKIP or NEW

**Quality:**
- [ ] Placements are relevant to article content
- [ ] No keyword stuffing
- [ ] Text reads naturally
- [ ] Repetition is natural (not forced)
- [ ] All changes logged with Volume + Status

---

## 5. Step 2: ToV Rewrite

### Purpose
Adjust language and tone according to ToV Guide. NO structural changes.

> **RULE:** Change WORDS, not INFORMATION.
> - "great" → "effective" (same meaning, better word)
> - "a little less clean" → "less clear" (same meaning, tighter)
> The facts and information MUST remain identical.

### Input
- Content with keywords from Step 1
- ToV Guide (`ftmo_academy_tov_guide_EN.md`)
- Content Inventory (`ftmo_academy_content_inventory.md`) - for topic classification

---

### Phase 0: Topic Classification

Before rewriting, classify the article topic difficulty:

| Topic Type | Persona | Content Inventory Location |
|------------|---------|---------------------------|
| **Basic concepts** | BEGINNER | Part 1, intro lessons |
| **Intermediate/Advanced** | ADVANCED | Part 2-5, specialized lessons |

**Classification examples:**

| Article | Classification | Why |
|---------|---------------|-----|
| What is Forex Trading | BEGINNER | Foundational concept |
| Japanese Candlesticks | BEGINNER | Basic charting |
| Types of Trading Charts | BEGINNER | Basic charting |
| Risk Management | ADVANCED | Requires trading basics |
| Scaling Strategies | ADVANCED | Requires position management knowledge |
| Trading Psychology | ADVANCED | Requires trading experience context |

**Tone differences by classification:**

| Aspect | BEGINNER Topic | ADVANCED Topic |
|--------|----------------|----------------|
| **Opening style** | "This lesson covers..." | "Here's the framework..." |
| **Terms** | Define ALL terms on first use | Define only NEW terms |
| **Explanation depth** | Why + How + Example | How + Example (skip obvious "why") |
| **Pacing** | Step by step, slower | Faster, scannable |
| **Assumed knowledge** | None | Basic terminology OK |
| **Tone markers** | Structured instructor | Professional guide |

> **Log requirement:** Record classification in Step 2 log header:
> `**Topic classification:** BEGINNER` or `**Topic classification:** ADVANCED`

---

### Reference: ToV Guide Elements

#### Tonal Spectrum (ToV Guide Section 3)

| Dimension | Position | Scale 1-5 |
|-----------|----------|-----------|
| **Formality** | Semi-formal (professional but accessible) | 3.5 |
| **Confidence** | High (expert position) | 4 |
| **Emotion** | Low (facts > feelings) | 2 |
| **Technicality** | Medium (explain, then use) | 3 |
| **Directness** | High (clear instructions, no fluff) | 4 |
| **Warmth** | Low to medium (respect, not friendship) | 2.5 |

#### Vocabulary: Use vs Avoid (ToV Guide Section 5)

| USE | AVOID | Why |
|-----|-------|-----|
| Consistent | Lucky | Emphasis on skill, not chance |
| Process | Secret | No guru messaging |
| Develop | Natural talent | Skills can be learned |
| Challenging | Easy | Realistic expectations |
| Professional | Amateur | Aspirational identity |
| Framework | Hack | Structure, not shortcuts |
| Risk management | Gambling | Professional approach |
| Skill | Gift | Learnable, not innate |
| Strategy | System | Flexibility |
| Discipline | Willpower | Process, not willpower |

#### Casual Language Markers (ToV Guide Section 5)

| Pattern | Problem | Fix |
|---------|---------|-----|
| "pretty much" | Too casual | "nearly", "almost" |
| "a little" | Hedging | Remove or use "somewhat" |
| "just" (as filler) | Unnecessary | Remove entirely |
| "great", "amazing" | Hype words | "effective", "useful" |
| "play with" | Too informal | "experiment with" |
| "a lot of" | Vague | "significant", specific number |
| "But" at sentence start | Casual transition | "However," |
| "gonna", "wanna" | Too casual | "going to", "want to" |

#### Prohibited Phrases (ToV Guide Section 5)

**Hype & Promises:**
- "Get rich", "Easy money", "Guaranteed profits"
- "Life-changing income", "Financial freedom in X months"
- "Secret strategy", "What they don't want you to know"

**Condescending:**
- "It's simple, just...", "Obviously..."
- "Even beginners can understand...", "As everyone knows..."
- "You should already know..."

**Vague:**
- "Trade smarter", "Be disciplined" (without specifics)
- "Manage your risk" (without specifics)
- "Follow your plan" (without explaining how)

#### Power Phrases to Use (ToV Guide Section 5)

**Educational:**
- "Here's how this works in practice..."
- "The key principle is..."
- "A common mistake to avoid..."
- "Let's break this down..."
- "To apply this..."

**Factual Context:**
- "This typically takes 3-6 months of consistent practice..."
- "Statistically, most traders need multiple attempts..."
- "The goal is consistency, measured by [specific metrics]..."

**FTMO-Specific:**
- "To prepare for your Challenge..."
- "This directly applies to FTMO's rules..."
- "When trading a funded account..."
- "Professional traders approach this by..."

#### Emotional Calibration (ToV Guide Section 6)

**Core Principle:** Support = Competence, NOT Empathy

| Express | Don't Express |
|---------|---------------|
| Matter-of-fact acknowledgement | Emotional empathy ("we understand how hard...") |
| Confidence in frameworks | Cheerleading ("You can do it!") |
| Caution about risks | Excitement/Hype |
| Respect for reader | Excessive warmth |

**Example:**
- WRONG: "We know how frustrating this must be for you."
- RIGHT: "Here's the framework to solve this problem."

#### Sentence Structure (ToV Guide Section 5)

| Guideline | Specification |
|-----------|---------------|
| Average length | 15-20 words |
| Voice | Active preferred |
| Mix | Short (definitions) + medium (explanations) |

### What CHANGES

| Area | Example |
|------|---------|
| **Word choice** | "great" → "effective", "a little" → "may" |
| **Sentence structure** | Shorter sentences, active voice |
| **Reader addressing** | Consistent we/you/traders |
| **Tone** | Casual → professional, emotional → factual |
| **Prohibited phrases** | Remove hype, vague advice, condescending language |

### What STAYS THE SAME

| Area | Rule |
|------|------|
| **Facts** | All numbers, definitions, examples preserved exactly |
| **Order** | Information sequence unchanged |
| **Formatting** | Keep original structure (handled in Step 3) |
| **Headings** | Keep original hierarchy (handled in Step 3) |
| **Length** | Similar word count (no adding/removing content) |
| **Keywords** | Keywords from Step 1 preserved |

### Decision Tree

```
For each sentence/phrase:

1. Contains casual language marker?
   → YES: Fix per table above
   → NO: Continue

2. Contains prohibited phrase?
   → YES: Rewrite or remove
   → NO: Continue

3. Contains hype word (great, amazing, easy)?
   → YES: Replace with factual alternative
   → NO: Continue

4. Is sentence too long (>25 words)?
   → YES: Split into 2 sentences
   → NO: Continue

5. Uses passive voice unnecessarily?
   → YES: Convert to active
   → NO: Keep

6. Reader addressing consistent?
   → Check: "you/your" OR "we" OR "traders"
   → Mix OK, but be consistent within paragraph
```

### Example Transformations

**Casual → Professional:**
> "But it is a great tool for both entries and trade management."
> → "However, it is an effective tool for both entries and trade management."

**Vague → Specific:**
> "They might present a little cleaner picture"
> → "They may present a cleaner picture"

**Passive → Active:**
> "Bar charts are represented as vertical bars"
> → "Bar charts display as vertical bars"

**Hype → Factual:**
> "This amazing technique will transform your trading!"
> → "This technique provides a structured approach to analysis."

**Filler removal:**
> "We will do just a quick recap now"
> → "Here is a quick recap"

**Emotional → Factual:**
> "Don't worry, losses are rare if you follow our method!"
> → "Losses are inevitable in trading. The goal is to manage them effectively."

### Log Format (Step 2)

```
## Step 2 Log: ToV Rewrite

**Guide:** `ftmo_academy_tov_guide_EN.md`
**Topic classification:** BEGINNER | ADVANCED

### Word/Phrase Changes

| # | Original | Changed To | Reason |
|---|----------|------------|--------|
| 1 | "pretty much endless" | "nearly endless" | ToV: casual marker "pretty much" |
| 2 | "a little less clean" | "less clear" | ToV: remove hedging "a little" |
| 3 | "great tool" | "effective tool" | ToV: hype word "great" |
| 4 | "But it is" | "However, it is" | ToV: casual "But" at start |

### Paragraph Rewrites (if any)

| # | Section | Change Type | Reason |
|---|---------|-------------|--------|
| 1 | Intro | Added definition | BEGINNER: define all terms |
| 2 | Risk section | Reframed emotional → factual | ToV: emotional calibration |
```

### ToV Rewrite Checklist

**Phase 0: Classification:**
- [ ] Topic classified (BEGINNER or ADVANCED)
- [ ] Classification logged in header

**Tone by Classification:**
- [ ] BEGINNER: All terms defined on first use
- [ ] BEGINNER: "This lesson covers..." style openings
- [ ] BEGINNER: Why + How + Example depth
- [ ] ADVANCED: Only new terms defined
- [ ] ADVANCED: "Here's the framework..." style openings
- [ ] ADVANCED: How + Example depth (skip obvious "why")

**Vocabulary (ToV Guide Section 5):**
- [ ] No casual markers ("pretty much", "a little", "just")
- [ ] No hype words ("great", "amazing", "easy")
- [ ] USE vocabulary preferred over AVOID vocabulary
- [ ] Power phrases used where appropriate

**Prohibited Phrases (ToV Guide Section 5):**
- [ ] No hype/promises
- [ ] No condescending language
- [ ] No vague advice (specifics provided)

**Emotional Calibration (ToV Guide Section 6):**
- [ ] No emotional empathy phrases
- [ ] No cheerleading
- [ ] Factual tone throughout
- [ ] Competence-based support

**Sentence Structure (ToV Guide Section 5):**
- [ ] Average 15-20 words per sentence
- [ ] Active voice preferred
- [ ] Long sentences split

**Preservation:**
- [ ] No factual information added
- [ ] No factual information removed
- [ ] Order of information preserved
- [ ] Keywords from Step 1 preserved

**Consistency:**
- [ ] Reader addressing consistent (you/we/traders)
- [ ] Tone matches spectrum (semi-formal, confident, low emotion)
- [ ] Tone matches classification (BEGINNER/ADVANCED)

---

## 6. Step 3: Structure & Formatting

### Purpose
Apply heading hierarchy, E-E-A-T elements, and visual formatting based on Structure Guide.

> **RULE:** Add formatting elements WHERE THEY FIT the existing content.
> Content meaning NEVER changes. Only presentation improves.

### Input
- ToV-adjusted content from Step 2
- Structure Guide (`ftmo_academy_structure_guide_EN.md`)
- Content Inventory (`ftmo_academy_content_inventory.md`)

---

### Phase 0: Paragraph Audit — MANDATORY FIRST ACTION

> **CRITICAL:** Before adding any formatting elements, audit every paragraph for length.
> Long paragraphs carry over from Step 2 unchanged and MUST be fixed here.

**Process:**
1. Go through every paragraph in the article
2. Count words (estimate is fine — flag anything that looks over 80 words)
3. Split any paragraph exceeding 100 words into 2–3 shorter paragraphs
4. Each split paragraph must start with a clear topic sentence

**Rules:**
- Split at a natural logical break (topic shift, new example, new aspect)
- Do NOT add new content when splitting — only insert a paragraph break
- Do NOT split if it creates a paragraph under 20 words
- Log every split in the Step 3 log

**Example — paragraph too long (130 words):**
> "The Asian session has the lowest volume... accounting for 20% of all transactions. During the Asian session, approximately 20% of daily forex volume is traded. Other participating economies include Singapore, New Zealand, and Australia..."

**Split into two paragraphs:**
> P1: "The Asian session has the lowest volume... accounting for 20% of all transactions." (~75 words)
> P2: "During the Asian session, approximately 20%... should monitor closely." (~55 words)

> **Only after paragraph audit is complete, proceed to heading structure, callouts, and other formatting.**

---

### Reference: Structure Guide Elements

#### Heading Hierarchy (Structure Guide Section 4)

| Level | Usage | Frequency |
|-------|-------|-----------|
| **H1** | Lesson title only | 1 per page |
| **H2** | Major sections | 3-7 per lesson |
| **H3** | Subsections within H2 | As needed |
| **H4** | Minor divisions | Use sparingly |

**Rules:** Never skip levels. H2s should create scannable outline.

#### Callout Types (Structure Guide Section 4)

| Type | Color | Usage | Frequency |
|------|-------|-------|-----------|
| **Warning** | Yellow/Orange | Risk alerts, common mistakes | 1-2 per lesson |
| **Tip** | Blue | Efficiency advice, pro techniques | 2-3 per lesson |
| **Note** | Gray | Additional context, clarifications | As needed |
| **Important** | Red/Bold | Critical information | Sparingly |
| **Example** | Gray | Practical illustrations | As needed |
| **Keep in Mind** | Olive | Cognitive biases, limitations | 1 per TA lesson |

**Rule:** 1-2 callouts per H2 section max. No back-to-back callouts.

#### Tables (Structure Guide Section 4)

**When to use:**
- Comparing 2+ items across multiple attributes
- Reference data (formulas, rules)
- Before/after comparisons

**Rules:**
- Max 5 columns (mobile-friendly)
- Always include header row
- Left-align text, right-align numbers

#### Lists (Structure Guide Section 4)

| Type | When to Use |
|------|-------------|
| **Bullet** | Unordered items, features, takeaways |
| **Numbered** | Sequential steps, prioritized items |

**Rules:** 3-7 items optimal. Parallel grammatical structure.

#### Paragraph Rules (Structure Guide Section 4)

| Guideline | Specification |
|-----------|---------------|
| Length | 40-100 words (2-4 sentences) |
| Max without break | 3 consecutive paragraphs |
| First sentence | Contains main point |

#### E-E-A-T Elements (Structure Guide Section 2-3)

**Required in every article:**

| Element | Location |
|---------|----------|
| **Author attribution** | Author box at end |
| **Published date** | Author box |
| **Updated date** | Author box |
| **Risk Warning** | After content |
| **Educational Notice** | After content |

#### Navigation (Structure Guide Section 6)

| Element | When Required |
|---------|---------------|
| **Table of Contents** | If >1,500 words |
| **Prerequisites** | Always state (markdown only — not in HTML) |
| **Internal links** | 3-5 per lesson minimum |
| **Next steps** | Always at end |

#### Internal Link Anchor Text Rule

> **NEVER use generic anchor text.** Always use the keyword or lesson title as the link text.

| WRONG | RIGHT |
|-------|-------|
| `[previous lesson](/lesson/japanese-candlesticks/)` | `[Japanese Candlesticks](/lesson/japanese-candlesticks/)` |
| `[here](/lesson/support-and-resistance/)` | `[support and resistance](/lesson/support-and-resistance/)` |
| `[click here](/lesson/technical-indicators/)` | `[technical indicators](/lesson/technical-indicators/)` |
| `[this article](/lesson/chart-patterns/)` | `[chart patterns](/lesson/chart-patterns/)` |

**Rule:** Anchor text = lesson title or primary keyword of the target page. This applies to all internal links in both markdown and HTML output.

### Formatting Limits by Article Length

| Article Length | Callouts | Tables | Lists |
|----------------|----------|--------|-------|
| Short (<1000 words) | 1-2 | 1 | 1-2 |
| Medium (1000-2000 words) | 2-3 | 1-2 | 2-3 |
| Long (>2000 words) | 3-4 | 2-3 | 3-4 |

### What CHANGES in Step 3

| Area | Action |
|------|--------|
| **Headings** | Apply H1 → H2 → H3 hierarchy |
| **H2 names** | Simplify redundant headings |
| **H3 subheadings** | Add where sections need division |
| **Callouts** | Add Tip, Warning, Keep in Mind where content fits |
| **Tables** | Add comparison tables where data exists |
| **Lists** | Convert paragraph lists to bullet/numbered |
| **Paragraphs** | Break long paragraphs (max 100 words) |
| **Internal links** | Add 3-5 links to related lessons |
| **Bold** | Highlight key terms for scanning |
| **Image notes** | Update Image Map positions if sections were restructured |
| **Placeholders** | Mark H2 sections with visual topics but no image as `[IMAGE NEEDED]` |

### What STAYS THE SAME

| Area | Rule |
|------|------|
| **Facts** | All content preserved |
| **Meaning** | No information changed |
| **Keywords** | Keywords from Step 1 preserved |
| **Tone** | ToV from Step 2 preserved |

### Structure & Formatting Checklist

**Phase 0: Paragraph Audit (FIRST — before anything else):**
- [ ] Every paragraph counted and checked for length
- [ ] No paragraph exceeds 100 words
- [ ] No paragraph is under 20 words (unless intentional short impact sentence)
- [ ] Max 3 consecutive paragraphs without a visual break (heading, callout, list, table)
- [ ] All splits logged in Step 3 log

**Heading Structure:**
- [ ] Single H1 (lesson title)
- [ ] 3-7 H2 major sections
- [ ] H3 subsections where needed
- [ ] No skipped levels

**E-E-A-T Elements:**
- [ ] Author attribution with credentials
- [ ] Published/Updated dates
- [ ] Risk Warning callout
- [ ] Educational Content Notice

**Navigation:**
- [ ] ToC present (if >1500 words)
- [ ] Prerequisites stated
- [ ] 3-5 internal links
- [ ] Next steps/related lessons

**Callouts (per Structure Guide):**
- [ ] Tip callouts for actionable advice
- [ ] Warning callouts for risks/mistakes
- [ ] Keep in Mind for cognitive biases (TA lessons)
- [ ] Max 1-2 per H2 section

**Tables:**
- [ ] Comparison tables where data exists
- [ ] Max 5 columns
- [ ] Header row present

**Lists:**
- [ ] Bullet lists for features/characteristics
- [ ] Numbered lists for sequential steps
- [ ] 3-7 items per list

**Readability:**
- [ ] Paragraphs 40-100 words
- [ ] Max 3 paragraphs without visual break
- [ ] Bold for key terms (not full sentences)

---

## 7. Step 4: HTML Conversion

### Purpose
Convert markdown to styled HTML with FTMO branding.

> **RULE:** Images follow their TOPIC, not a fixed paragraph number.
> Use the Image Map from Initialization to place each image next to the content it illustrates.

### Image Placement Rules

1. **Original images:** Place each image from the Image Map next to its topic (same H2/H3 section)
2. **Sizing:** All images use `max-width: 500px` and `width: 100%` — smaller by default, readable without dominating layout
3. **Alt text:** Descriptive, keyword-rich where natural (from Image Map)
4. **Captions:** Add `<figcaption>` with brief description
5. **Missing images:** If an H2 section has NO image and the topic would benefit from one, add a placeholder

### Image HTML Format

```html
<figure class="lesson-figure">
    <img src="[URL]" alt="[descriptive alt text]" style="max-width:500px;width:100%;" loading="lazy">
    <figcaption>[Brief caption describing what the image shows]</figcaption>
</figure>
```

### Placeholder for Missing Images

When a section discusses a visual concept (chart type, pattern, indicator) but the original article has no image for it:

```html
<figure class="lesson-figure lesson-figure--placeholder">
    <div class="placeholder-img" style="max-width:500px;width:100%;height:250px;background:var(--light-gray);border:2px dashed var(--silver);display:flex;align-items:center;justify-content:center;border-radius:8px;">
        <span style="color:var(--muted);font-size:14px;">[IMAGE NEEDED: description of what should go here]</span>
    </div>
    <figcaption>[Caption for future image]</figcaption>
</figure>
```

### Image Checklist (Step 4)

- [ ] All images from Image Map placed in correct topic sections
- [ ] All images use `max-width: 500px; width: 100%`
- [ ] All images have descriptive alt text
- [ ] All images have `<figcaption>`
- [ ] All images use `loading="lazy"`
- [ ] Visual H2 sections without images have placeholders
- [ ] Image Map logged in Step 4 log with final positions

### Template: v3_standard

Use the `v3_standard` template as the standard for all articles.
Reference implementation: `lesson_types-of-trading-charts_EN_v3.html`

---

### Page Layout (top to bottom)

Every article must follow this exact element order:

```
<header class="site-header">          ← black bg, FTMO logo, nav, CTA
<nav class="breadcrumbs">             ← Academy › Module › Lesson title
<main class="lesson-wrap">
  <header class="lesson-header">      ← module label + H1 + meta (date + team)
  <p class="lesson-intro">            ← 1 hook sentence (outside article, before ToC)
  <nav class="toc">                   ← Table of Contents
  <article class="lesson-content">
    ... H2 sections ...
    <h2>Conclusion</h2>               ← synthesis text + comparison table (if applicable)
    <section class="key-takeaways">   ← bullet recap (AFTER conclusion)
    <section class="next-steps">      ← 2-3 internal links
  </article>
  <div class="author-box">
  <div class="disclaimer disclaimer--educational">
  <div class="disclaimer disclaimer--risk">
</main>
<footer class="site-footer">
```

> **NO TL;DR or Overview sections.**
> **NO Prerequisites block in HTML** — handled by FTMO Academy CMS (sidebar/metadata).

---

### Lesson Header

Every article starts with a `.lesson-header` block containing three elements:

```html
<header class="lesson-header">
    <span class="lesson-header__module">Technical Analysis &mdash; Lesson 2</span>
    <h1>Types of Trading Charts</h1>
    <div class="lesson-header__meta">Last updated: March 5, 2026 &nbsp;&bull;&nbsp; FTMO Academy Content Team</div>
</header>
```

| Element | Content |
|---------|---------|
| `lesson-header__module` | Module name + lesson number (from Content Inventory) |
| `h1` | Lesson title |
| `lesson-header__meta` | "Last updated: [date] • FTMO Academy Content Team" |

---

### Lesson Intro

One short paragraph placed **between lesson-header and ToC** — outside `<article>`:

```html
<p class="lesson-intro">There are several ways to display price data on a chart — ...</p>
```

- 1–2 sentences max
- States what the lesson covers (the "hook")
- Does NOT repeat the H1

---

### Conclusion + Key Takeaways

Both sections are required. They serve different E-E-A-T purposes and must appear in this order:

| Section | Purpose | E-E-A-T signal | Content |
|---------|---------|----------------|---------|
| **Conclusion** | Synthesis + decision framework | Expertise | Narrative paragraph + comparison table (if applicable) |
| **Key Takeaways** | Scannable recap | Helpfulness | Bullet list (3–6 items) |
| **Next Steps** | Navigation | Trust/UX | 2–3 internal links to related lessons |

> **Conclusion** is an H2 section inside `<article>`. It synthesizes what was covered and, where relevant, includes a comparison table as a reference artifact.
> **Key Takeaways** is a `<section class="key-takeaways">` after Conclusion. It is a bullet recap, not a repeat of the Conclusion text.

---

### CSS Architecture

**MANDATORY: Use `:root` CSS variables. Never hardcode brand colors.**

```css
:root {
    --azure:      #0781fe;   /* primary accent: links, buttons, CTA */
    --torea-bay:  #123a83;   /* headings, ToC, table headers */
    --silver:     #c6c6c6;   /* borders, secondary backgrounds */
    --black:      #000000;   /* header/footer background */
    --white:      #ffffff;   /* content background */
    --light-gray: #f5f5f7;   /* ToC bg, callout bg, key-takeaways bg */
    --body-text:  #1a1a2e;   /* body text */
    --muted:      #555;      /* secondary text, figcaptions */
}
```

All CSS rules must reference these variables, not hex values directly.

---

### Callout System (BEM naming)

**MANDATORY: Use BEM class naming for all callouts.**

```html
<div class="callout callout--tip">
    <span class="callout__label">Tip</span>
    <p>...</p>
</div>
```

| Modifier class | Color | Usage |
|----------------|-------|-------|
| `callout--tip` | Blue (`--azure`) | Actionable advice, pro techniques |
| `callout--warning` | Yellow/orange | Risk alerts, common mistakes |
| `callout--note` | Gray (`--light-gray`) | Additional context, clarifications |
| `callout--important` | Red/bold | Critical must-know information |
| `callout--keep-in-mind` | Olive/green | Cognitive biases, limitations (TA lessons) |

**Rules:**
- Label class is always `callout__label` (never `callout-title`, `callout-label`, or similar)
- Modifier class uses double-dash BEM: `callout--tip` (never `callout-tip`)
- Max 1–2 callouts per H2 section

---

### Table of Contents Styling

```
Background:  var(--light-gray) / #f5f5f7
Text color:  var(--torea-bay) / #123a83
Border-left: 4px solid var(--torea-bay)
Font:        Poppins, 14px
Structure:   Nested (H2 = 1., H3 = 1.1., 1.2., etc.)
```

---

### FTMO Brand Colors (Official)

| CSS Variable | Hex | Usage |
|--------------|-----|-------|
| `--azure` | `#0781fe` | Links, buttons, CTA, callout--tip accent |
| `--torea-bay` | `#123a83` | H1–H3, ToC text, table headers |
| `--silver` | `#c6c6c6` | Borders, secondary backgrounds |
| `--black` | `#000000` | Header/footer background |
| `--white` | `#ffffff` | Content background |
| `--light-gray` | `#f5f5f7` | ToC bg, callout bg, key-takeaways bg |
| `--body-text` | `#1a1a2e` | Body text |
| `--muted` | `#555` | Secondary text, figcaptions |

---

### HTML Checklist

**Page structure (top to bottom):**
- [ ] `site-header` (black, logo, nav, CTA)
- [ ] `breadcrumbs` (Academy › Module › Lesson)
- [ ] `lesson-header` (module label + H1 + meta)
- [ ] `lesson-intro` paragraph (before ToC, outside article)
- [ ] `toc` (ToC with nested H2/H3 links)
- [ ] `lesson-content` article (H2 sections)
- [ ] `Conclusion` H2 (synthesis + table if applicable)
- [ ] `key-takeaways` section (bullets, AFTER conclusion)
- [ ] `next-steps` section (2–3 internal links)
- [ ] `author-box` (name + dates)
- [ ] `disclaimer--educational`
- [ ] `disclaimer--risk`
- [ ] `site-footer`
- [ ] NO Prerequisites inline block
- [ ] NO TL;DR / Overview section

**CSS:**
- [ ] `:root` variables defined (all 8 variables present)
- [ ] No hardcoded hex colors in CSS rules
- [ ] Poppins font loaded via Google Fonts

**Callouts:**
- [ ] BEM naming: `callout--tip`, `callout--warning`, etc.
- [ ] Label class: `callout__label` (never `callout-title` or `callout-label`)
- [ ] Max 1–2 per H2 section

**Images:**
- [ ] All images from Image Map placed in correct topic sections
- [ ] All images: `max-width: 500px; width: 100%`
- [ ] All images have descriptive `alt` text
- [ ] All images wrapped in `<figure class="lesson-figure">` with `<figcaption>`
- [ ] All images use `loading="lazy"`
- [ ] Visual H2 sections without images have `lesson-figure--placeholder`
- [ ] Image Map positions logged in Step 4 log

**Content:**
- [ ] Video embedded if applicable (after lesson-header, before ToC)
- [ ] Tables styled (dark blue header via `--torea-bay`)
- [ ] Internal links: 3–5 minimum, descriptive anchor text

**Meta:**
- [ ] `<title>` 50–60 chars, includes primary keyword
- [ ] `<meta name="description">` 150–160 chars
- [ ] `<link rel="canonical">` present
- [ ] `lang="en"` on `<html>`
- [ ] Responsive (`max-width: 1160px`, mobile breakpoint at 768px)

---

## 8. Step 5: QA & Review

### Purpose
Final quality check before publishing.

### QA Checklist

**Content Accuracy:**
- [ ] All facts match original source
- [ ] No information added or removed
- [ ] Meaning unchanged throughout
- [ ] Links work correctly
- [ ] Images placed in correct positions (matching original)

**ToV Compliance:**
- [ ] Tone matches ToV Guide
- [ ] No prohibited phrases
- [ ] Appropriate for target persona

**Structure Compliance:**
- [ ] E-E-A-T elements present
- [ ] Heading hierarchy correct
- [ ] Internal links present

**Formatting:**
- [ ] Formatting elements used (tables, callouts, lists) per article length limit
- [ ] Tables present where comparisons exist
- [ ] Callouts present where tips/warnings fit
- [ ] Balanced use of visual elements
- [ ] Readable and scannable
- [ ] Mobile-friendly

**Technical:**
- [ ] HTML renders correctly
- [ ] Images load
- [ ] No broken links

---

## 9. File Naming Convention

```
lesson_[slug]_EN.md           # Final markdown
lesson_[slug]_EN_log.md       # Edit log (all steps) — source for HTML/PDF
lesson_[slug]_EN_log.html     # Log rendered with diff colors (red/green)
lesson_[slug]_EN_log.pdf      # Log exported to PDF via Chrome headless
lesson_[slug]_EN.html         # Final HTML article
[slug]_keywords.xlsx          # Keywords file
```

### Log File Structure

Every article gets a `_log.md` file tracking all changes:

```markdown
# [Article Title] - Edit Log

**Article:** `lesson_[slug]_EN.md`
**Source:** [original URL]
**Date:** YYYY-MM-DD

---

## Step 1 Log: Keywords
| # | Original | Changed To | Keyword | Position | Status |

## Step 2 Log: ToV Rewrite
| # | Original | Changed To | Reason |

## Step 3 Log: Structure & Formatting
| # | Change Type | Description | Reason |

## Summary
| Step | Status | Changes |
```

### Log HTML & PDF Export

After all steps are complete, generate the visual diff log automatically:

```bash
python src/generate_log.py data/output/lesson_[slug]_EN_log.md
```

This single command:
1. Parses `_log.md` (header metadata, all Step sections, Summary)
2. Generates `lesson_[slug]_EN_log.html` with diff-style formatting:
   - **Red background + `-` prefix** = original sentence (removed/changed)
   - **Green background + `+` prefix** = new sentence (replacement)
   - **Gray background + italic** = merged or skipped entries
   - DONE/SKIP/PENDING badges per keyword row
   - Step sections clearly separated with headers
3. Exports `lesson_[slug]_EN_log.pdf` via Chrome headless

Both output files are saved in the same directory as the input `_log.md`.

> **Note:** Chrome headless preserves all CSS colors and styling in the PDF output. No additional tools required on macOS. Chrome must be installed at `/Applications/Google Chrome.app/`.

---

## 10. Quick Reference

### When editing existing content:

1. **Apply Keywords** - integrate SEO keywords naturally (Step 1)
2. **Apply ToV** - adjust language only (Step 2)
3. **Apply Structure & Formatting** - headings, meta elements, visual elements (Step 3)
4. **Convert to HTML** - if needed (Step 4)
4.5. **Export log to HTML + PDF** - `python src/generate_log.py data/output/lesson_[slug]_EN_log.md`
5. **QA Review** - final check (Step 5)

### Key principle:

> **Preserve facts, transform presentation.**

The content meaning never changes. Only how it's expressed and formatted.

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-04 | Initial creation |
| 1.1 | 2026-03-04 | Added keyword integration logic (frequency, positions, decision tree) |
| 1.2 | 2026-03-04 | Added synonym confirmation rule, status tracking, H1/H2/H3 priority |
| 1.3 | 2026-03-04 | Refined PENDING logic: minor=auto, significant=confirm, added SKIP/NEW/REJECTED |
| 1.4 | 2026-03-04 | Added _log.md file requirement for each article |
| 1.5 | 2026-03-04 | Added Step 3 proportional limits based on article length |
| 1.6 | 2026-03-04 | Added CORE PRINCIPLE (preserve content), image placement rules, use FULL allowance rule |
| 1.7 | 2026-03-05 | Expanded Step 2 with ToV Guide references (vocabulary, emotional calibration, decision tree) |
| 1.8 | 2026-03-05 | Added Phase 0: Topic Classification (BEGINNER vs ADVANCED) to Step 2 |
| 1.9 | 2026-03-05 | Added Section 3: Input Format (URL + Keywords xlsx) |
| 2.0 | 2026-03-05 | Step 4: Official FTMO colors, ToC styling, NO TL;DR rule, Key Takeaways |
| 2.1 | 2026-03-05 | Step 1: Volume-based priority (replaces manual HIGH/MEDIUM/LOW), simplified xlsx structure |
| 2.2 | 2026-03-05 | Step 1: Relative volume priority (no absolute thresholds), relevance-based placement |
| 2.3 | 2026-03-05 | Step 2 log: full sentences required (původní věta celá vs nová věta celá) |
| 2.4 | 2026-03-05 | Section 9: log HTML/PDF export — diff colors (red/green), Chrome headless command |
| 2.5 | 2026-03-05 | Step 4: Prerequisites NOT in HTML (CMS handles it); ToC required in HTML |
| 2.6 | 2026-03-05 | Step 3: internal link anchor text rule — keyword/title only, never "previous lesson", "here", "click here" |
| 2.7 | 2026-03-05 | Step 3: Phase 0 Paragraph Audit added as mandatory first action — split all paragraphs >100 words before any other formatting |
| 2.7 | 2026-03-05 | Section 9: replaced manual log export with `python src/generate_log.py`; added Step 4.5 to Quick Reference |
| 2.8 | 2026-03-05 | Step 4: Full rewrite — template v3_standard, Page Layout order, lesson-header spec, lesson-intro rule, Conclusion+Key Takeaways E-E-A-T rationale, :root CSS variables (mandatory), BEM callout naming (mandatory), updated HTML checklist |

---

*This workflow should be followed for all FTMO Academy content creation and editing.*
