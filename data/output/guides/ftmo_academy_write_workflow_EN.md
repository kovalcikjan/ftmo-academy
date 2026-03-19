# FTMO Academy: New Lesson Writing Workflow

**Version:** 2.0
**Created:** 2026-03-05
**Updated:** 2026-03-06
**Purpose:** Step-by-step process for writing FTMO Academy lessons from scratch

---

## 1. Workflow Overview

```
INPUT                        PROCESS                                    OUTPUT
─────                        ───────                                    ──────
Topic / Slug           →     INIT: Load refs, create log file      →   Init Summary + log file
                       →     Step 1: Competitor Research            →   URL list (max 10) + keyword set
                       →     Step 2: Brief & Outline                →   Approved Outline
                       →     Step 3: Draft Writing                  →   Full Draft + source citation log
                       →     Step 4: ToV Check                      →   Corrected Draft
                       →     Step 5: Structure & Formatting         →   Formatted Markdown
                       →     Step 6: HTML Conversion                →   lesson_[slug]_EN.html + log.html
                       →     Step 7: QA + Inventory Update          →   FINAL FILES
```

### Core Principle: Create, Don't Compile

> **CRITICAL:** Every FTMO Academy lesson must be original, opinionated, and written in Academy Tone of Voice from the first sentence.
>
> This workflow is NOT:
> - A summarization of competitor content
> - A SEO content brief filled with keywords
> - A neutral draft to be fixed later
>
> This workflow IS:
> - Research-informed original writing
> - Academy ToV applied from Step 3 onward
> - A structured process with one human-approval gate per step

**What the competitor research informs:** Topic scope, structure patterns, content gaps, keyword set
**What it does NOT do:** Provide the source text — that would be plagiarism

---

## 2. Relationship to Edit Workflow

| | Edit Workflow (`/academy`) | Write Workflow (`/academy-write`) |
|--|---------------------------|----------------------------------|
| **Input** | Existing FTMO lesson | No lesson exists yet |
| **Core principle** | Preserve content, enhance presentation | Create original content in Academy ToV |
| **Step 1** | Keywords (integrate into existing text) | Competitor research + keyword discovery |
| **Step 2** | ToV rewrite (same words, better voice) | Brief & Outline (architecture) |
| **Step 3** | Structure & Formatting | Draft Writing (original prose) |
| **Step 4** | HTML | ToV Check (verify, not rewrite) |
| **Step 5** | QA | Structure & Formatting |
| **Step 6** | — | HTML |
| **Step 7** | — | QA + Inventory |

---

## 3. Reference Documents

| Document | Used In |
|----------|---------|
| `ftmo_academy_tov_guide_EN.md` | Init, Step 3, Step 4 |
| `ftmo_academy_structure_guide_EN.md` | Init, Step 2, Step 5 |
| `ftmo_academy_content_inventory.md` | Init, Step 2 |
| `prompts/write_step1_research.md` | Step 1 |
| `prompts/write_step2_brief.md` | Step 2 |
| `prompts/write_step3_draft.md` | Step 3 |
| `prompts/write_step4_tov_check.md` | Step 4 |
| `prompts/step3_structure.md` | Step 5 |
| `prompts/step4_html.md` | Step 6 |

---

## 4. Usage Modes

### Full workflow (default)

```
/academy-write [topic/slug]
```

Runs Init + Steps 1–7. Stops for user confirmation after each step.

### Brief only

```
/academy-write brief [topic/slug]
```

Runs Init + Steps 1–2. Output: approved outline only. Use when you need a content plan without writing.

### Draft from existing brief

```
/academy-write draft [topic/slug]
```

Starts from Step 3. Assumes approved outline exists in conversation context or pasted by user.

### Show TODO inventory

```
/academy-write inventory
```

Reads Content Inventory and lists all TODO lessons grouped by Part/Module.

---

## 5. Initialization

Runs automatically. No user confirmation needed.

### Actions

1. Read all three reference documents (ToV Guide, Structure Guide, Content Inventory)
2. Locate the topic in the inventory — extract: Part, Module, lesson number, lessons it links to
3. Check for existing versions: if files exist in `data/output/lessons/[slug]/`, determine the next version number (v2, v3, etc.) and use it as suffix for ALL output files of this run. Previous files are never renamed or deleted.
   > "Existing version found: lesson_[slug]_EN.md. Output files for this run will use suffix _v[N]."
4. Create the log file immediately: `data/output/lessons/[slug]/lesson_[slug]_EN_v[N]_log.md` (or without suffix if first version)
5. Output Init Summary

### Log File — Initialize at INIT

Create `data/output/lessons/[slug]/lesson_[slug]_EN_log.md` with:

```markdown
# Write Log: [Lesson Title]

**Slug:** [slug]
**Date:** [today]
**Workflow version:** 2.0

---

## INIT

| Item | Value |
|------|-------|
| Inventory position | Part N: [Name] > [Module], Lesson N of M |
| Status in inventory | TODO / UPDATED / etc. |
| Links to | [lessons] |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions found | None / v3 at [path] — ignored per user instruction |
```

### Init Summary Format

```
Topic:         [Lesson name]
Slug:          [lesson-slug]
Part:          [Part N — Name]
Module:        [Module name]
Position:      Lesson N of M in module
Links to:      [lesson titles]
Status in inv: TODO | ANALYZED | UPDATED | APPROVED
Existing ver.: None | [filename] — will create vN+1

Keywords: loaded in Step 1 (Ahrefs MCP)

Confirm to start Step 1 (Competitor Research + Keyword Discovery).
```

If slug is not in the inventory, flag it and ask for confirmation before proceeding.

---

## 6. Step 1 — Competitor Research + Keyword Discovery

**Prompt:** `prompts/write_step1_research.md`

### Purpose

Understand the competitive landscape before writing. Scope the topic. Build the keyword set. Output: URL list + keywords — both used in Step 2.

### Phase A — URL Discovery & Fetch

**Discovery — use EXA MCP (primary tool):**

1. Run 3–4 EXA semantic searches for the topic with varied query formulations:
   - `"[topic] explained trading"` — broad
   - `"[topic] guide for traders"` — educational angle
   - `"how to use [topic] trading"` — practical angle
   - `"[topic] candlestick bar line chart"` — specific angle if relevant
2. Collect all returned URLs — target 15–20 candidates
3. Cross-reference with Ahrefs MCP `serp-overview` for the top 2–3 keywords to add SERP-ranked pages
4. Deduplicate, exclude: forums (Reddit, Quora), paywalled content, non-EN pages, PDF files
5. Select top 8–10 most relevant URLs for fetching

**Fetch — extract content:**

6. WebFetch each selected URL — extract: H1, H2/H3 structure, topics covered, depth, unique angles, gaps
7. If WebFetch fails (timeout / blocked): note in log as "fetch failed, skipped" — proceed with remaining pages
8. Minimum 3 successfully fetched pages to continue

**Why EXA over manual domain guessing:**
EXA returns semantically relevant pages for the exact topic — not just known domains. A lesser-known broker academy with excellent coverage will surface; a well-known domain with irrelevant content will not.

**Append to log file after each fetch:**

| URL | Source | DR | SERP pos. | Fetch status |
|-----|--------|----|-----------|-------------|
| https://... | EXA | 81 | 9 | fetched |
| https://... | Ahrefs SERP | 77 | 8 | fetched |
| https://... | EXA | — | — | failed — timeout |

### Phase B — Keyword Discovery

1. Call Ahrefs MCP `keywords-explorer-matching-terms` with seed = topic name in EN
2. Call Ahrefs MCP `keywords-explorer-related-terms` with same seed
3. Merge results from Phase A (topics found in competitor pages) + Ahrefs MCP output
4. Deduplicate, sort by volume descending
5. Filter: remove branded terms, volume < 10, clearly out-of-scope terms
6. Output: top 20 keywords

### Output

**URL List (max 10 — selected from fetched pages):**

| # | URL | DR | SERP pos. | Key Topics | Notable Gap |
|---|-----|----|-----------|------------|-------------|

**Keyword Set (top 20):**

| # | Keyword | Volume | KD |
|---|---------|--------|----|

**Content Gap Summary:** 3–5 bullets on what Academy can do better

### Stop Condition

> **Step 1 complete.** Fetched [N] pages ([N] successful). Keyword set: [N] terms. Key gap: [sentence].
> Add or remove URLs and keywords if needed → confirm to proceed to Step 2.

**Wait for user confirmation.**

---

## 7. Step 2 — Brief & Outline

**Prompt:** `prompts/write_step2_brief.md`

### Purpose

Define the architecture of the lesson before any prose is written. The approved outline is the contract for Step 3.

### Actions (in order)

1. Classify lesson: BEGINNER or ADVANCED
2. Set word count target
3. State differentiation from competitors
4. Map top 3–5 keywords to H1/H2 headings
5. Write full heading skeleton with key points per section
6. Plan internal links (3–5 minimum)

### BEGINNER vs. ADVANCED Classification

| Signal | BEGINNER | ADVANCED |
|--------|----------|----------|
| Entry level | No prior TA knowledge | Requires indicator / strategy knowledge |
| Topic type | What is X / How does X work | When to use X / Edge cases / Optimization |
| Assumed knowledge | None | Part 1 + prior Technical Analysis |
| Depth | Why + How + Example | How + Example (skip the obvious "why") |

### Keyword Placement in Step 2 — Headings Only

Use the keyword set from Step 1. Step 2 assigns keywords to headings only.

- Top 3–5 keywords by volume → assign to H1 or H2 where topic naturally fits
- Never force a keyword into a heading if it breaks natural language
- Remaining keywords → body text in Step 3 (no pre-assignment needed here)

| # | Keyword | Volume | Heading assignment |
|---|---------|---------|--------------------|
| 1 | [kw] | [vol] | H1 |
| 2 | [kw] | [vol] | H2 |
| — | remaining [N] kw | — | Step 3 (body) |

### Output Format

```
## Lesson Brief: [Title]

Topic:          [Name]
Slug:           [slug]
Part:           [Part N — Name]
Module:         [Module Name]
Position:       Lesson N of M
Classification: BEGINNER | ADVANCED — [one-sentence reason]
Word Count:     [N–N words] — [basis: competitor avg / complexity]

Differentiation:
- [What this lesson does that competitors don't]
- [FTMO-specific context to include]
- [Topics deliberately excluded]

Keywords — headings:
| # | Keyword | Volume | Heading |
|---|---------|--------|---------|

Outline:
# [H1 — Lesson Title] ← contains primary keyword
  Key point: [what the reader learns overall]

## [H2 — Section]
  Target keyword: [keyword]
  Key points:
  - [Specific fact or principle to cover]
  - [...]
  Callout: [Type — description]
  Table: [What to compare]

  ### [H3 — Subsection]
    Key points:
    - [...]

Internal Links:
1. [Link text] → [Lesson] — [slug] — [placement]
```

### Content Validation: Outline Review

Before presenting the outline for approval, review it as a trading expert and educator:

- Does the structure logically follow the topic?
- Are all key concepts present for the given classification (BEGINNER/ADVANCED)?
- Is the order of sections didactically correct — does each section build on the previous?
- Are there gaps — concepts a trader would expect to find but are missing?
- Are there sections that don't belong or are out of scope?

Output: validation note (pass / flagged issues) appended below the outline.

### Stop Condition

> **Step 2 complete.** Outline for "[Title]" — [BEGINNER/ADVANCED], ~[N] words.
> [N] H2s, [N] H3s, [N] keywords mapped to headings. Content validation: [pass / issues].
> Approve or edit outline → proceed to Step 3.

**Wait for user approval. Do not begin writing until the outline is approved.**

---

## 8. Step 3 — Draft Writing

**Prompt:** `prompts/write_step3_draft.md`

### Purpose

Write the full lesson in Academy Tone of Voice, following the approved outline exactly.

### Core Constraints

1. **Follow the approved outline.** Every H2 and H3 must appear. Deviations require flagging.
2. **Academy ToV from sentence one.** No neutral draft. No "fix tone later."
3. **Integrate keywords naturally** — see rules below.
4. **Respect classification.** BEGINNER = define everything. ADVANCED = assume foundations, skip obvious "why."
5. **Stay within word count target.** Flag if significantly over or under before finishing.

### Keyword Integration — Core Principle

> The primary goal is a well-written, readable lesson in Academy ToV.
> Keywords are a secondary consideration — not a checklist.

- Top keywords are already placed in headings (Step 2) — do not repeat them artificially in body text
- Secondary keywords: weave in where they fit the sentence naturally
- Declension and word-order variations are acceptable — keywords do not need to appear verbatim
- If a keyword cannot be placed without forcing it — leave it out
- Never place the same keyword twice in the same H2 section
- Never open the article with a keyword in the first sentence

Priority order:
1. Reader understands the topic clearly
2. Article reads naturally in Academy ToV
3. Keywords present where they fit

### Writing Rhythm

**Pattern:** Short statement → Medium explanation with specifics → Short conclusion or transition.

```
Example:
"Risk management protects your capital. Without a defined risk per trade —
typically 0.5% to 2% of your account — even profitable strategies eventually
fail. Define your risk before you enter the trade."
```

**Section openings:** Lead with the principle, not a preamble.

```
WRONG: "In this section, we're going to look at how candlestick charts work."
RIGHT: "Candlestick charts display four data points per period: open, high, low, and close."
```

**Transitions:** Forward-moving, never summarizing.

```
WRONG: "Now that we've covered candlestick charts, let's look at bar charts."
RIGHT: "Bar charts display the same four data points. The difference is visual."
```

### Output Format

Output as plain markdown. Start directly with `#`.

### Step 3 Log — Append to Log File

After the draft, append to `lesson_[slug]_EN_log.md`:

```markdown
## Step 3 — Draft

**Classification:** BEGINNER | ADVANCED
**Word count:** [N] words (target: [N–N])

### Keyword Integration

| # | Keyword | Volume | Placement | Context sentence |
|---|---------|--------|-----------|-----------------|

### Outline Deviations

| # | Type | Description | Reason |
|---|------|-------------|--------|

If none: "None — outline followed exactly."

### Full Article with Source Citations

Complete article text with each factual claim followed by its source in brackets.

> "Candlestick charts are the most widely used chart type in retail and institutional trading."
> [https://zerodha.com/varsity/chapter/chart-types/]
>
> "In cTrader, tick and range charts are available natively."
> [FTMO platform knowledge — no external source]

Rules:
- Every factual sentence needs a source URL from Step 1 research
- Interpretations, ToV phrasing, and general knowledge do not need a source
- FTMO-specific or platform knowledge: mark as [FTMO platform knowledge]
- If no source found: flag as [SOURCE NEEDED]
```

### Stop Condition

> **Step 3 complete.** Draft: "[Title]" — [BEGINNER/ADVANCED] — [N] words.
> Keywords integrated: [N]. Deviations: [N]. Source citations: [N] (flagged: [N]).
> Review draft → approve or request edits → proceed to Step 4.

**Wait for user confirmation.**

---

## 9. Step 4 — ToV Check

**Prompt:** `prompts/write_step4_tov_check.md`

### Purpose

Light verification pass. The draft is already in Academy ToV. This step catches slippage — it is NOT a rewrite.

### What to Check

| Check | Pass condition |
|-------|----------------|
| Section openings | Lead with value — no "In this section we will..." |
| Sentence rhythm | No 3+ consecutive long sentences |
| Casual markers | No "pretty much", "kind of", "a bit", "just" (filler), "basically" |
| Hype language | No "amazing", "great", "life-changing", "guaranteed" |
| Condescension | No "It's simple", "Obviously", "Even beginners can" |
| Vague advice | "Manage your risk" only with specifics attached |
| Emotional calibration | No cheerleading, no empathy phrases |
| Closings | Action-oriented — no generic summaries |

### Scope Guideline

If the draft is well-written: 0–5 flagged items is a success. Do not rewrite what isn't broken.
If more than 10 items need fixing: consider returning to Step 3 rather than patching sentence by sentence.

### Step 4 Log — Append to Log File

```markdown
## Step 4 — ToV Check

**Sentences reviewed:** [N]
**Issues found:** [N]

| # | Location | Issue Type | Original (full sentence) | Corrected (full sentence) |
|---|----------|------------|--------------------------|---------------------------|

If 0 issues: "ToV check clean — no corrections needed."
```

Then: full article with only corrected sentences replaced.

### Stop Condition

> **Step 4 complete.** [N] issues found and corrected.
> Review corrections → approve → proceed to Step 5.

**Wait for user confirmation.**

---

## 10. Step 5 — Structure & Formatting

**Prompt:** `prompts/step3_structure.md`

### Purpose

Apply heading hierarchy, callouts, tables, lists, E-E-A-T elements, and navigation blocks.

### MANDATORY FIRST ACTION: Paragraph Audit

Before adding any callouts, tables, or H3s — check every paragraph for length.
Split any paragraph over 100 words. Paragraphs from Step 3 do not automatically comply.

### What Changes

| Element | Action |
|---------|--------|
| Heading hierarchy | Apply H1 → H2 → H3 (never skip levels) |
| Paragraphs | Split any over 100 words |
| Callouts | Add Warning, Tip, Note, Keep in Mind where content fits |
| Tables | Add comparison tables where data exists |
| Lists | Convert embedded paragraph lists to bullet/numbered |
| Bold | Highlight key terms for scanning |
| ToC | Add if >1,500 words |
| Image placeholders | Add after each H2 section and where visual explanation would help — format: `[IMAGE: description of what the image should show]` |
| CTA placeholders | Add where relevant — format: `[CTA: description, e.g. "Start FTMO Challenge" button]` |
| Internal links | Ensure 3–5 minimum |
| Author block | Add at end |
| Risk disclaimer | Add at end |
| Educational notice | Add at end |

### What Does NOT Change

Content, facts, meaning, keywords, tone — all preserved exactly.

### Callout Type Decision Rules

| Type | Use when |
|------|----------|
| Warning | Live trading risk — wrong action = real monetary loss |
| Tip | Practical shortcut or platform-specific note |
| Note | Clarification that prevents misunderstanding |
| Important | Concept critical to understanding the lesson |
| Keep in Mind | Required for TA lessons — addresses bias or common mistake |

### When NOT to Add a Callout

- Section already has 2 callouts → skip
- Content is informational only, no action or risk → no callout needed
- Callout would repeat what the paragraph already says clearly

### Callout Limits by Article Length

| Length | Callouts | Tables | Lists |
|--------|----------|--------|-------|
| Short (<1,000 words) | 1–2 | 1 | 1–2 |
| Medium (1,000–2,000 words) | 2–3 | 1–2 | 2–3 |
| Long (>2,000 words) | 3–4 | 2–3 | 3–4 |

Max 1–2 callouts per H2. No back-to-back callouts.

### Required E-E-A-T Elements

```markdown
> **Risk Warning:** Trading involves significant risk of loss.
> Past performance is not indicative of future results. Only trade with capital you can afford to lose.

> **Educational Content Notice:** This material is for educational purposes only
> and does not constitute financial advice.

---
**Author:** FTMO Academy Content Team
**Last Updated:** [Date]
---
```

### Stop Condition

> **Step 5 complete.** Formatted article ready.
> Review formatting → approve → proceed to Step 6 (HTML).

**Wait for user confirmation.**

---

## 11. Step 6 — HTML Conversion

**Prompt:** `prompts/step4_html.md`

### Purpose

Convert the final markdown to clean, semantic HTML following FTMO Academy conventions. Generate both output HTML files simultaneously.

### Output Files — Generated Simultaneously

Both files are created in this step. Do not finish Step 6 without both files saved.

1. `lesson_[slug]_EN.html` — final lesson HTML
2. `lesson_[slug]_EN_log.html` — styled HTML version of the log file (sidebar nav, outline block with H1/H2/H3 tags, competitor URLs as clickable links)

### Meta Data Rules

- Meta title: 50–60 characters (primary keyword near front)
- Meta description: 150–160 characters (topic + benefit, no clickbait)
- Canonical URL: `/lesson/[slug]/`

### Template Reference

- Template: FTMO Academy v2_balanced
- Defined in: `prompts/step4_html.md`
- Brand colors: H1 `#2d2d2d` | H2/H3 `#123a83` | Links `#0781fe` | Table headers `#123a83`
- Font: Poppins (Google Fonts)

### Conversion Rules

| Markdown | HTML |
|----------|------|
| `# H1` | `<h1>` |
| `## H2` | `<h2>` |
| `### H3` | `<h3>` |
| `**bold**` | `<strong>` |
| `*italic*` | `<em>` |
| `> **Warning:** ...` | `<div class="callout callout-warning">` |
| `> **Tip:** ...` | `<div class="callout callout-tip">` |
| `> **Note:** ...` | `<div class="callout callout-note">` |
| `> **Important:** ...` | `<div class="callout callout-important">` |
| `> **Keep in Mind:** ...` | `<div class="callout callout-keep-in-mind">` |
| Bullet list | `<ul><li>` |
| Numbered list | `<ol><li>` |
| Table | `<table><thead><tbody>` |
| `---` (HR) | `<hr>` |
| Inline code | `<code>` |
| Code block | `<pre><code>` |

### HTML Skeleton

```html
<article class="academy-lesson">

  <!-- lesson content -->

  <!-- Image placeholder format: -->
  <!-- <div class="image-placeholder">[IMAGE: description of what the image should show]</div> -->

  <!-- CTA placeholder format: -->
  <!-- <div class="cta-placeholder">[CTA: description, e.g. "Start FTMO Challenge" button]</div> -->

  <div class="lesson-disclaimers">
    <!-- risk warning + educational notice -->
  </div>

  <div class="lesson-author">
    <!-- author block -->
  </div>

</article>
```

### Step 6 Log — Append to Log File

```markdown
## Step 6 — HTML

**Elements converted:** [N] headings, [N] callouts, [N] tables, [N] lists
**Meta title:** "[title]" ([N] chars)
**Meta description:** "[desc]" ([N] chars)
**Manual fixes applied:** [list any non-standard elements, or "none"]
```

### Stop Condition

> **Step 6 complete.** HTML ready for review. Both files saved:
> - lesson_[slug]_EN.html
> - lesson_[slug]_EN_log.html
>
> Approve HTML → proceed to Step 7 (QA + Inventory).

**Wait for user confirmation.**

---

## 12. Step 7 — QA + Inventory Update

### Purpose

Final quality gate before publishing. Validate content as a trading expert. Run full checklist. Save all output files. Update the Content Inventory.

### Content Validation — Trading Expert Review

This is the first and most important QA check. Review independently of ToV and formatting.

#### 1. Brief & Outline Re-check
- Does the outline still make sense after seeing the full article?
- Are all planned sections present and in correct order?

#### 2. Full Article Review (as experienced trader + trading educator)

- [ ] All facts are technically accurate
- [ ] No oversimplifications that would mislead a beginner
- [ ] No advanced assumptions in a BEGINNER lesson
- [ ] Concepts explained in correct sequence — no forward references without context
- [ ] Examples are realistic and relevant to trading practice
- [ ] Nothing missing that a trader would expect in this topic
- [ ] Nothing included that is out of scope or distracting

### Source Citation Audit

- [ ] All factual claims have source citations in log
- [ ] No [SOURCE NEEDED] flags remaining (or flagged for human review)
- [ ] FTMO-specific claims marked as [FTMO platform knowledge]

### QA Checklist

#### E-E-A-T & YMYL
- [ ] Risk disclaimer present and visible
- [ ] Educational notice included
- [ ] Author attribution block present
- [ ] No profit guarantees or hype language
- [ ] All statistics have sources

#### Structure
- [ ] Single H1 (lesson title)
- [ ] Logical H2-H3 hierarchy (no skipped levels)
- [ ] 3–7 H2 sections
- [ ] ToC present (if >1,500 words)
- [ ] Next steps / internal links at end (3–5 minimum)

#### Tone of Voice
- [ ] Professional guide — not textbook, not friend
- [ ] Confident and direct
- [ ] No hype, no false promises
- [ ] Risk acknowledged factually

#### Readability
- [ ] Average sentence length 15–20 words
- [ ] Paragraphs 40–100 words
- [ ] Max 3 consecutive paragraphs without visual break
- [ ] Bold used for scanning anchors
- [ ] Active voice dominant

#### Keywords
- [ ] Primary keyword in H1 or first H2
- [ ] Top keywords present in body
- [ ] No keyword stuffing

#### Callouts & Formatting
- [ ] Correct callout types used
- [ ] 1–2 callouts per H2 section max
- [ ] Tables used for comparisons
- [ ] Correct list types (bullet vs. numbered)

### Files to Save — All Four Required

Version suffix `_vN` applied if previous version exists (determined at INIT). Never overwrite existing files.

- [ ] `data/output/lessons/[slug]/lesson_[slug]_EN[_vN].md`
- [ ] `data/output/lessons/[slug]/lesson_[slug]_EN[_vN]_log.md`
- [ ] `data/output/lessons/[slug]/lesson_[slug]_EN[_vN].html`
- [ ] `data/output/lessons/[slug]/lesson_[slug]_EN[_vN]_log.html`

### Inventory Update

In `ftmo_academy_content_inventory.md`:

- [ ] Status updated: TODO → DRAFT (not yet reviewed by human) or PUBLISHED (approved and live)
- [ ] Links To column updated (all internal links used in lesson)
- [ ] Last updated date updated

```
TODO → DRAFT (if not yet reviewed by a human)
TODO → PUBLISHED (if approved and live)
```

### Stop Condition

> **Step 7 complete.** QA: [PASS / FAIL].
> Content validation: [PASS / issues found].
> Source citations: [N] verified, [N] flagged.
> Files saved: 4/4.
> Inventory updated: [Lesson] → [new status].
>
> [If FAIL]: [N] issues found — list with severity.

---

## 13. Log Integrity — Non-Negotiable

> **CRITICAL: The log is an audit trail. It must be accurate.**
>
> In Steps 3–6, whenever you log an "original" sentence or text block:
> 1. Locate the exact text in the current file using the Read tool
> 2. Copy it character-by-character — punctuation, capitalization included
> 3. NEVER reconstruct from memory
> 4. NEVER paraphrase
>
> **Wrong:** writing what you think the original said
> **Right:** reading the file, copying the exact text, then logging it
>
> Logs with approximate originals destroy the audit trail and are worse than no log.

---

## 14. Naming Convention

```
lesson_[slug]_EN.md           # Final markdown
lesson_[slug]_EN_log.md       # Write log (all steps)
lesson_[slug]_EN.html         # Final HTML
lesson_[slug]_EN_log.html     # Log HTML
```

Slugs use hyphens (matching URL slugs):
- Correct: `types-of-trading-charts`
- Wrong: `types_of_trading_charts`, `TypesOfTradingCharts`

---

## 15. Step Confirmation Rule

> **Every step ends with a STOP.**
> After each step's output, wait for explicit user confirmation ("ok", "continue", "approved", or equivalent) before starting the next step.
> Automatic step transitions are strictly forbidden.

---

## 16. Common Failure Modes

| Failure | Prevention |
|---------|------------|
| Summarizing competitors instead of researching them | Step 1 output = analysis table, NOT article content |
| Starting to write before outline is approved | Hard stop at end of Step 2 — no exceptions |
| Writing neutral draft then applying ToV | Write in Academy ToV from sentence one in Step 3 |
| Forcing keywords into unnatural positions | Reader clarity > keyword placement — always |
| Paragraphs over 100 words surviving to Step 5 | Mandatory paragraph audit is Step 5's FIRST action |
| Log originals reconstructed from memory | Always re-read the file before logging |
| Missing source citations for factual claims | Source citation log is mandatory in Step 3 |
| Generating only lesson HTML, skipping log HTML | Both HTML files generated simultaneously in Step 6 |
| Completing Step 7 without saving all four files | 4-file checklist enforced before marking done |
| Content validation skipped | Trading expert review is Step 7's FIRST action |

---

## 17. Quality Targets

| Metric | Target |
|--------|--------|
| Step 3 → Step 4 ToV issues | < 5 per 1,500 words |
| Step 5 paragraph audit failures | 0 (all split before proceeding) |
| Internal links per lesson | 3–5 minimum |
| QA checklist pass rate | 100% before marking PUBLISHED |
| Word count accuracy | Within ±15% of Step 2 target |
| Source citations flagged [SOURCE NEEDED] | 0 before Step 7 sign-off |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-05 | Initial creation |
| 2.0 | 2026-03-06 | Restructured Step 1 (competitor research + keyword discovery combined); INIT simplified (no keywords); Log file created at INIT; Source citation log added to Step 3; Content validation (trading expert review) added to Step 2 and Step 7; Callout type decision rules added to Step 5; Both HTML files generated in Step 6; 4-file checklist in Step 7; Keyword integration core principle added |

---

*Companion document: [Edit Workflow](ftmo_academy_workflow_EN.md) — for existing lessons*
*Reference: [ToV Guide](ftmo_academy_tov_guide_EN.md) | [Structure Guide](ftmo_academy_structure_guide_EN.md)*
