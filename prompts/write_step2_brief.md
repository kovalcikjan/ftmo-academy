# Step 2: Brief & Outline

You are creating the editorial brief and content outline for a new FTMO Academy lesson. This outline is the blueprint for the draft — it must be approved by the user before any writing begins.

## CORE PRINCIPLE

> **PLAN, DON'T WRITE.** This step produces a structured outline with key points per section.
> No prose, no full sentences in the article body. Only the architecture.

---

## Inputs Available at This Step

- Competitor analysis from Step 1 (topics, structure patterns, gaps)
- Keywords xlsx parsed in initialization (keyword, volume, notes)
- Content Inventory context (Part, Module, lesson position, prerequisites, related lessons)
- ToV Guide classification rules (BEGINNER vs. ADVANCED)

---

## Brief Structure

### 1. Lesson Metadata

```
Topic:          [Topic name]
Slug:           [lesson-slug]
Part:           [Part X — Name]
Module:         [Module Y — Name]
Position:       Lesson [N] of [total in module]

Classification: BEGINNER | ADVANCED
  Reason: [one sentence justification]

Word Count Target: [range, e.g. 1,200–1,600 words]
  Basis: [competitor average / topic complexity / inventory pattern]
```

**Classification rules (from ToV Guide):**
- BEGINNER: foundational concepts (what is X, how does X work), intro/overview lessons
- ADVANCED: requires prior trading knowledge, indicator/strategy/risk/psychology lessons

### 2. Prerequisites Block

```
Prerequisites:
- [Lesson title] — [URL or slug] — [Why required]
- [Lesson title] — [URL or slug] — [Why required]
```

Source from Content Inventory. If no direct prerequisite exists, state "None — entry-level lesson."

### 3. Target Keywords (Top 10 by Volume)

List the top 10 keywords from the xlsx, sorted by volume:

| # | Keyword | Volume | Planned Placement |
|---|---------|--------|-------------------|
| 1 | ... | ... | H1 / H2 / Intro |
| 2 | ... | ... | H2 / Body |

**Placement options:** H1, H2, H3, Intro, Body, Conclusion

### 4. Content Outline

This is the core deliverable. For each section:

```
# [H1 — Lesson Title]
  Target keyword: [keyword]
  Key point: [What the reader learns from this section]

## [H2 — Section Name]
  Target keyword: [keyword, if applicable]
  Key points:
  - [Point 1: specific fact, concept, or principle to cover]
  - [Point 2]
  - [Point 3]
  Callout: [Type — brief description, if applicable]
  Table: [What to compare, if applicable]

  ### [H3 — Subsection Name]
    Key points:
    - [Point 1]
    - [Point 2]
```

**Rules for the outline:**
- H1 must contain or closely reflect the top keyword
- H2s should create a scannable, logical learning progression
- Key points are bullets of WHAT to say — not HOW to say it (that comes in Step 3)
- Each H2 section should have 2-5 key points
- Mark where callouts and tables will appear (type only, not content)
- Mark where internal links will go (use inventory for related lessons)

### 5. Internal Links Plan

```
Planned internal links (3-5 minimum):
1. [Linked text] → [Lesson title] — [slug/URL] — [placement: intro / body / end]
2. ...
```

Source from Content Inventory. Prefer lessons in same Module, then same Part.

### 6. Competitor Differentiation

```
What this article does better/differently than competitors:
- [Specific angle or depth decision, grounded in Step 1 gap analysis]
- [FTMO-specific context to include]
- [Topics deliberately excluded and why]
```

---

## Output Checklist

Before presenting the brief, verify:

- [ ] Classification stated with justification
- [ ] Word count target with basis
- [ ] Prerequisites sourced from inventory
- [ ] Top 10 keywords with planned placement
- [ ] H1 contains primary keyword
- [ ] H2s form logical learning path
- [ ] Every H2 has 2-5 key points
- [ ] Callout and table placements marked
- [ ] 3-5 internal links planned
- [ ] Differentiation from competitors stated

---

## Output Format

Generate the outline content as markdown, save as temporary `.md`, then convert to `.docx`:

```bash
.venv/bin/python src/export_outline_docx.py data/output/lessons/[slug]/lesson_[slug]_EN_outline.md
```

Delete the intermediate `.md` after successful conversion. The `.docx` is the single deliverable — trading expert edits it directly. Step 3 reads from the (potentially edited) `.docx`.

---

## Stop Condition

After outputting the brief:

> **Step 2 complete.**
>
> Outline for "[Lesson Title]" — [BEGINNER/ADVANCED], ~[N] words.
> [N] H2 sections, [N] H3 subsections, [N] keywords mapped.
>
> **Outline saved at:** `[full absolute path to .docx]`
>
> Send .docx to trading expert for review. You can:
> - Approve as-is and proceed to Step 3 (Draft Writing)
> - Have the expert edit headings, scope, or depth in the .docx
> - Return the edited .docx → Step 3 reads from it

**Wait for user approval before writing any article content.**

---

## Input

Process based on the competitor analysis from Step 1, the parsed keywords, and the Content Inventory context established during initialization.
