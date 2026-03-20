# FTMO Academy Content Editor

Today is {{ date }}. Arguments: $ARGUMENTS

## Reference Documents

**Tone of Voice Guide:** \`data/output/guides/ftmo_academy_tov_guide_EN.md\`
**Structure Guide:** \`data/output/guides/ftmo_academy_structure_guide_EN.md\`
**Content Inventory:** \`data/output/guides/ftmo_academy_content_inventory.md\`
**Workflow:** \`data/output/guides/ftmo_academy_workflow_EN.md\`

## Workflow

> **CRITICAL: After each step, STOP and wait for user confirmation ("ok", "continue", "approved" etc.) before starting the next step. NEVER transition automatically.**

**Initialization (no confirmation needed):**
1. Read all reference documents (ToV Guide + Structure Guide + Content Inventory)
2. Identify the article in the inventory (Part, Module, position)
3. Fetch and display the original article

**Step 1 → STOP**
- Run keyword integration per \`prompts/step1_keywords.md\`
- Output: edited article + Step 1 log (full original sentence → full new sentence)
- Wait for confirmation: "Step 1 complete. Proceed to Step 2 (ToV rewrite)?"

**Step 2 → STOP**
- Run ToV rewrite per \`prompts/step2_tov.md\`
- Output: edited article + Step 2 log (full original sentence → full new sentence)
- Wait for confirmation: "Step 2 complete. Proceed to Step 3 (Structure)?"

**Step 3 → STOP**
- Run structure & formatting per \`prompts/step3_structure.md\`
- Output: final article
- Wait for confirmation: "Step 3 complete. Save files and proceed to Step 4 (HTML)?"

**Step 4 → STOP**
- Run HTML conversion
- Wait for confirmation before saving

**Step 5:**
- QA review
- Update inventory status

## Audit Checklist

### E-E-A-T & YMYL
- [ ] Risk disclaimer present and visible
- [ ] Author attribution
- [ ] Sources cited for statistics
- [ ] No profit guarantees

### Structure
- [ ] Single H1 (lesson title)
- [ ] Logical H2-H3-H4 hierarchy
- [ ] ToC (if >1500 words)
- [ ] Prerequisites stated
- [ ] Internal links (3-5 minimum)

### Tone of Voice
- [ ] Professional guide, not textbook or friend
- [ ] Confident and direct, not warm/emotional
- [ ] No hype, no false promises
- [ ] Facts about risks included

### Readability
- [ ] Average sentence length 15-20 words
- [ ] Paragraphs 40-100 words
- [ ] Max 3 paragraphs without visual break
- [ ] Bold for scanning anchors
- [ ] Active voice

### Callouts & Formatting
- [ ] Correct callout types (Warning, Tip, Note, Important, Example)
- [ ] Not too many callouts (1-2 per H2 section)
- [ ] Tables for comparisons
- [ ] Correct list types (bullet vs numbered)

## Output Format

\`\`\`markdown
# Content Audit: [Article Title]

## Summary
- Overall score: [X/10]
- Main issues: [list]
- Strengths: [list]

## E-E-A-T Issues
| Issue | Location | Recommendation |
|-------|----------|----------------|

## Structure Issues
| Issue | Location | Recommendation |
|-------|----------|----------------|

## ToV Issues
| Issue | Original text | Suggested rewrite |
|-------|--------------|-------------------|

## Readability Issues
| Issue | Location | Recommendation |
|-------|----------|----------------|

## Priority Actions
1. [Most important change]
2. [Second most important]
3. [Third most important]

## Suggested Rewrites
### [Section 1]
**Original:**
> ...

**Rewrite:**
> ...

**Why:** [Reason per guide]
\`\`\`

## Usage Modes

**Analyze only (default):**
\`/academy [URL or path]\`
- Audit and recommendations only
- Does not create edited file

**Rewrite mode:**
\`/academy rewrite [URL or path]\`
- Runs full audit
- Creates new file: \`lesson_[slug]_EN.md\`

**Quick check:**
\`/academy quick [URL or path]\`
- Top 5 issues only
- Brief output

**Section focus:**
\`/academy tov [URL or path]\` — ToV issues only
\`/academy structure [URL or path]\` — structure issues only
\`/academy eeat [URL or path]\` — E-E-A-T issues only

**Translation check:**
\`/academy check\` — translate sentence change log from English to Czech
- Input format (one or more entries):
  \`\`\`
  #: [number]
    Original sentence (full): "..."
    New sentence (full): "..."
    Reason: ...
  \`\`\`
- For each entry, output both English and Czech versions:
  \`\`\`
  **#: [number]**

  **Original sentence (full):**
  "[EN original]"
  *"[CZ original]"*

  **New sentence (full):**
  "[EN new]"
  *"[CZ new]"*

  **Reason:**
  [EN reason]
  *[CZ reason]*
  \`\`\`
- Translate naturally, not word-for-word. Keep Czech fluent.
- Preserve formatting (quotes, dashes, punctuation style).

**Content inventory operations:**
\`/academy inventory\` — show Content Inventory summary
\`/academy links [lesson-url]\` — suggest internal links for a lesson
\`/academy gaps\` — show content gaps and suggestions
\`/academy prereqs [lesson-url]\` — verify/suggest prerequisites

## Important Rules

- Always read all reference documents before analyzing (ToV, Structure, Inventory)
- Suggest SPECIFIC changes, not general advice
- On rewrite, preserve original structure where it works
- Use examples from guides to illustrate changes
- All output in English
- Log format: full original sentence vs full new sentence — never excerpts

## Content Inventory Workflow

When analyzing an article:
1. Read Content Inventory for context
2. Identify where the article sits (Part/Module/Lesson #)
3. Suggest internal links to related lessons from inventory
4. Verify prerequisites per inventory
5. After analysis, update Status in inventory (TODO → ANALYZED)
