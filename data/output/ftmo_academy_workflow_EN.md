# FTMO Academy: Content Workflow

**Version:** 1.1
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

---

## 2. Reference Documents

| Document | Handles | Used In Step |
|----------|---------|--------------|
| `[lesson]_keywords.xlsx` | Target keywords for SEO | Step 1 |
| `ftmo_academy_tov_guide_EN.md` | Voice, tone, language, word choice | Step 2 |
| `ftmo_academy_structure_guide_EN.md` | Headings, sections, E-E-A-T, formatting | Step 3 |
| `ftmo_academy_content_inventory.md` | Internal links, prerequisites, content map | Step 3, 5 |

---

## LOGGING REQUIREMENTS

Každá úprava musí být zalogována s odůvodněním. Log umožňuje:
- Zpětnou kontrolu změn
- Identifikaci chyb při testování
- Učení se z rozhodnutí

### Log Format

```
## Step [X] Log: [Step Name]

| # | Original | Changed To | Reason |
|---|----------|------------|--------|
| 1 | "text before" | "text after" | [důvod dle guide] |
| 2 | ... | ... | ... |
```

### Příklad Step 1 (Keywords):

```
## Step 1 Log: Keywords

| # | Original | Changed To | Keyword | Priority | Position |
|---|----------|------------|---------|----------|----------|
| 1 | "Renko is similar to" | "Renko charts are similar to" | renko charts | HIGH | Intro |
| 2 | "Heikin Ashi is another" | "Heikin Ashi candles are another" | heikin ashi candles | HIGH | H2 section |
```

### Příklad Step 2 (ToV Rewrite):

```
## Step 2 Log: ToV Rewrite

| # | Original | Changed To | Reason |
|---|----------|------------|--------|
| 1 | "it is a great tool" | "it is an effective tool" | ToV: avoid casual language ("great") |
| 2 | "might be a little less clean" | "may be less clear" | ToV: precise language, avoid "a little" |
| 3 | "we will do just a quick recap" | "here is a quick recap" | ToV: direct statement, less casual |
```

### Příklad Step 3 (Structure & Formatting):

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

## 3. Step 1: Keywords

### Purpose
Integrate target keywords naturally into the original content.

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

### Keyword Frequency

| Priority | Min | Max | Notes |
|----------|-----|-----|-------|
| HIGH | 2x | 4x | Main keyword, must appear |
| MEDIUM | 1x | 2x | Secondary keywords |
| LOW | 0x | 1x | Only if fits naturally |

### Keyword Placement Positions

| Position | Priority | Example |
|----------|----------|---------|
| **H1 title** | HIGH only | "Types of Trading Charts" |
| **Intro paragraph** | HIGH | First mention of topic |
| **H2 headings** | HIGH/MEDIUM | Section titles |
| **First sentence after H2** | HIGH | Opening statement |
| **Conclusion** | HIGH | Summary/wrap-up |
| **Body text** | All | Where it fits naturally |

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

### Decision Tree

```
For each HIGH/MEDIUM keyword:

1. Is there a natural place in the text?
   → NO: Skip this keyword
   → YES: Continue

2. Would it change the sentence meaning?
   → YES: Skip this instance
   → NO: Continue

3. Is keyword already at max frequency?
   → YES: Skip
   → NO: Add keyword + log the change
```

### Log Format (Step 1)

```
## Step 1 Log: Keywords

| # | Original | Changed To | Keyword | Priority | Position |
|---|----------|------------|---------|----------|----------|
| 1 | "Renko is similar to" | "Renko charts are similar to" | renko charts | HIGH | Intro |
| 2 | "understanding Heikin Ashi" | "understanding Heikin Ashi candles" | heikin ashi candles | HIGH | H2 section |
```

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

- [ ] Keywords file reviewed (HIGH/MEDIUM/LOW identified)
- [ ] HIGH keywords: 2-4x occurrences
- [ ] MEDIUM keywords: 1-2x occurrences
- [ ] LOW keywords: 0-1x (only if natural)
- [ ] Keywords in H1/H2 where appropriate
- [ ] Keywords in intro and conclusion
- [ ] First mention uses full keyword form
- [ ] No meaning changes (decision tree applied)
- [ ] No keyword stuffing
- [ ] Text reads naturally
- [ ] All changes logged with position

---

## 4. Step 2: ToV Rewrite

### Purpose
Adjust language and tone according to ToV Guide. NO structural changes.

### Input
- Content with keywords from Step 1
- ToV Guide (`ftmo_academy_tov_guide_EN.md`)

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

### Example Transformations

**Casual → Professional:**
> "But it is a great tool for both entries and trade management."
> → "It is an effective tool for both entries and trade management."

**Vague → Specific:**
> "They might present a little cleaner picture"
> → "They may present a cleaner picture"

**Passive → Active:**
> "Bar charts are represented as vertical bars"
> → "Bar charts display as vertical bars"

**Hype → Factual:**
> "This amazing technique will transform your trading!"
> → "This technique provides a structured approach to analysis."

### ToV Rewrite Checklist

- [ ] No factual information added
- [ ] No factual information removed
- [ ] Order of information preserved
- [ ] Keywords from Step 1 preserved
- [ ] Word choice matches ToV Guide vocabulary
- [ ] Active voice used where appropriate
- [ ] No prohibited phrases (hype, vague, condescending)
- [ ] Reader addressing is consistent
- [ ] Tone matches ToV spectrum (semi-formal, confident, low emotion)

---

## 5. Step 3: Structure & Formatting

### Purpose
Apply heading hierarchy, meta elements, E-E-A-T compliance, and visual formatting.

### Input
- ToV-adjusted content from Step 2
- Structure Guide (`ftmo_academy_structure_guide_EN.md`)
- Content Inventory (`ftmo_academy_content_inventory.md`)

### What CHANGES

**Structure:**

| Area | Action |
|------|--------|
| **Headings** | Apply H1 → H2 → H3 → H4 hierarchy |
| **Sections** | Add/reorganize logical sections |
| **Meta elements** | Add Prerequisites, ToC, Disclaimers |
| **Internal links** | Add links to related lessons |
| **E-E-A-T** | Add author attribution, sources, dates |

**Formatting:**

| Area | Action |
|------|--------|
| **Lists** | Convert appropriate content to bullet/numbered lists |
| **Tables** | Create comparison tables where useful |
| **Callouts** | Add Tip, Note, Warning, Example boxes |
| **Bold text** | Highlight key terms for scanning |
| **Paragraphs** | Break long paragraphs (max 100 words) |

### What STAYS THE SAME

| Area | Rule |
|------|------|
| **Facts** | All content preserved |
| **Tone** | ToV adjustments from Step 2 preserved |
| **Keywords** | Keywords from Step 1 preserved |

### Formatting Rules

| Element | Rule |
|---------|------|
| **Callouts** | Max 1-2 per H2 section |
| **Tables** | Use for comparisons, lists of 3+ items with multiple attributes |
| **Bullet lists** | Use for features, characteristics, non-sequential items |
| **Numbered lists** | Use for steps, sequences, rankings |
| **Bold** | Key terms, important phrases (not entire sentences) |
| **Paragraphs** | 40-100 words, max 3 without visual break |

### Structure & Formatting Checklist

**Structure:**
- [ ] Single H1 (lesson title)
- [ ] Logical H2-H3-H4 hierarchy
- [ ] ToC present (if >1500 words)
- [ ] Prerequisites stated
- [ ] Risk disclaimer present
- [ ] Educational notice present
- [ ] Author attribution present
- [ ] Published/Updated dates present
- [ ] 3-5 internal links to related lessons

**Formatting:**
- [ ] Not too many callouts (balanced)
- [ ] Tables used appropriately
- [ ] Lists improve readability (not forced)
- [ ] Bold highlights scanning anchors
- [ ] Paragraphs are digestible
- [ ] Visual breaks every 2-3 paragraphs

---

## 6. Step 4: HTML Conversion

### Purpose
Convert markdown to styled HTML with FTMO branding.

### Elements

| Element | Specification |
|---------|---------------|
| **Font** | Poppins (Google Fonts) |
| **Colors** | #0781fe (blue), #123a83 (dark), #000000 (header/footer) |
| **Max width** | 1160px |
| **Header** | Black background, FTMO logo, navigation |
| **Footer** | Black background, FTMO logo, links |
| **Images** | From original article, with captions |
| **Video** | YouTube embed if available |

### HTML Checklist

- [ ] FTMO branding applied
- [ ] Responsive design
- [ ] Images included with alt text
- [ ] Video embedded (if applicable)
- [ ] Header/footer present
- [ ] Meta tags (title, description, keywords)

---

## 7. Step 5: QA & Review

### Purpose
Final quality check before publishing.

### QA Checklist

**Content Accuracy:**
- [ ] All facts match original source
- [ ] No information added or removed
- [ ] Links work correctly

**ToV Compliance:**
- [ ] Tone matches ToV Guide
- [ ] No prohibited phrases
- [ ] Appropriate for target persona

**Structure Compliance:**
- [ ] E-E-A-T elements present
- [ ] Heading hierarchy correct
- [ ] Internal links present

**Formatting:**
- [ ] Balanced use of visual elements
- [ ] Readable and scannable
- [ ] Mobile-friendly

**Technical:**
- [ ] HTML renders correctly
- [ ] Images load
- [ ] No broken links

---

## 8. File Naming Convention

```
lesson_[slug]_EN.md           # Final markdown
lesson_[slug]_EN.html         # Final HTML
lesson_[slug]_EN_keywords.md  # After Step 1 (optional)
lesson_[slug]_EN_tov.md       # After Step 2 (optional)
lesson_[slug]_EN_v2.html      # Alternative version
```

---

## 9. Quick Reference

### When editing existing content:

1. **Apply Keywords** - integrate SEO keywords naturally (Step 1)
2. **Apply ToV** - adjust language only (Step 2)
3. **Apply Structure & Formatting** - headings, meta elements, visual elements (Step 3)
4. **Convert to HTML** - if needed (Step 4)
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

---

*This workflow should be followed for all FTMO Academy content creation and editing.*
