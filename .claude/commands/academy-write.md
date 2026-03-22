# FTMO Academy — Write From Scratch

Today is {{ date }}. Arguments: $ARGUMENTS

## Reference Documents

**Workflow:** \`data/output/guides/ftmo_academy_write_workflow_EN.md\`
**ToV Guide:** \`data/output/guides/ftmo_academy_tov_guide_EN.md\`
**Structure Guide:** \`data/output/guides/ftmo_academy_structure_guide_EN.md\`
**Content Inventory:** \`data/output/guides/ftmo_academy_content_inventory.md\`

## Prompts

| Step | Prompt file |
|------|-------------|
| Step 1 — Competitor Research + Keywords | \`prompts/write_step1_research.md\` |
| Step 2 — Brief & Outline | \`prompts/write_step2_brief.md\` |
| Step 3 — Draft Writing | \`prompts/write_step3_draft.md\` |
| Step 4 — ToV Check | \`prompts/write_step4_tov_check.md\` |
| Step 5 — Structure & Formatting | \`prompts/step3_structure.md\` |
| Step 6 — HTML | \`prompts/step4_html.md\` |

## Workflow

> **CRITICAL: After each step, STOP and wait for user confirmation ("ok", "continue", "approved", etc.) before starting the next step. NEVER transition automatically.**

Full detail for every step is defined in the Workflow document above. This file is a summary reference.

---

**INIT (no confirmation needed):**
1. Read all reference documents (Workflow + ToV Guide + Structure Guide + Content Inventory)
2. Check for existing versions in \`data/output/lessons/[slug]/\` — if found, determine next version number (v2, v3...) and use as suffix for ALL output files this run. Never overwrite or rename existing files.
3. Create log file immediately with correct suffix: \`data/output/lessons/[slug]/lesson_[slug]_EN[_vN]_log.md\`
4. Output Init Summary — no keywords yet (keywords come from Step 1)

---

**Step 1 — Competitor Research + Keyword Discovery → STOP**

Phase A — URL Discovery & Fetch:
- **Search tool (pick one available, in priority order):**
  1. **WebSearch (built-in, DEFAULT)** — always available, no setup needed
  2. **EXA MCP** — semantic search, if configured
  3. **DataForSEO MCP** — SERP data + keyword ideas, if configured
- Run 3-4 searches with varied query formulations:
  - "[topic] explained trading"
  - "[topic] guide for traders"
  - "how to use [topic] trading"
  - topic-specific angle query
- Collect 15-20 candidate URLs
- Cross-reference with Ahrefs MCP \`serp-overview\` (top 2-3 keywords) for SERP-ranked pages
- Deduplicate, exclude forums / paywalled / non-EN / PDFs
- Select top 8-10 most relevant → WebFetch each
- Log each URL: URL | source (WebSearch/EXA/DataForSEO/Ahrefs) | DR | SERP pos. | fetch status
- If fetch fails: note in log, skip — minimum 3 successful fetches to continue

Phase B — Keyword Discovery:
- Ahrefs MCP \`keywords-explorer-matching-terms\` + \`keywords-explorer-related-terms\` for topic seed
- Merge with topics found in Phase A — deduplicate, sort by volume, filter branded/irrelevant
- Output: top 20 keywords

Output: URL list (max 10) + keyword set (top 20) + content gap summary (3-5 bullets)

> "Step 1 complete. [N] pages fetched. [N] keywords. xlsx saved at: [full absolute path]. Add or remove URLs/keywords → confirm to proceed to Step 2."

---

**Step 2 — Brief & Outline → STOP**

- Classification: BEGINNER or ADVANCED
- Word count target
- Differentiation from competitors (before outline)
- Keyword mapping: top 3-5 keywords → H1/H2 headings only (body keywords handled in Step 3)
- Full heading skeleton with key points per section
- Internal links plan (3-5 minimum from inventory)
- Content validation: review outline as trading expert + educator before presenting

> "Step 2 complete. Outline for '[Title]' — [BEGINNER/ADVANCED], ~[N] words. Content validation: [pass/issues]. Outline saved at: [full absolute path]. Approve or edit → proceed to Step 3."

---

**Step 3 — Draft Writing → STOP**

- Write full article in Academy ToV from approved outline
- Keyword integration principle: **reader clarity first, keywords second**
  - Secondary keywords woven naturally into body prose
  - Declension/variations acceptable — verbatim not required
  - If keyword cannot be placed naturally — leave it out
- Append to log:
  - Keyword integration table
  - Outline deviations
  - Full article with inline source citations: each factual claim → source URL from Step 1 research
    (FTMO-specific = mark as [FTMO platform knowledge]; missing source = [SOURCE NEEDED])

> "Step 3 complete. [N] words. Keywords: [N]. Deviations: [N]. Source citations: [N] (flagged: [N]). Review draft → proceed to Step 4."

---

**Step 4 — ToV Check → STOP**

- Light verification pass only — draft is already in Academy ToV
- 0-5 flagged items = success; >10 items = return to Step 3
- Append to log: sentences reviewed, issues found, correction table

> "Step 4 complete. [N] issues found and corrected. Approve → proceed to Step 5."

---

**Step 5 — Structure & Formatting → STOP**

- MANDATORY FIRST ACTION: paragraph audit — split any paragraph over 100 words
- Apply heading hierarchy, callouts, tables, lists, bold
- Callout types: Warning (trading risk) | Tip (practical/platform) | Note (clarification) | Important (critical concept) | Keep in Mind (TA bias — required for TA lessons)
- Do NOT add callout if: section already has 2, content is informational only, callout repeats the paragraph
- Add: ToC (if >1,500 words), image placeholders, CTA placeholders, author block, risk disclaimer, educational notice

> "Step 5 complete. Formatted article ready. Approve → proceed to Step 6."

---

**Step 6 — HTML → STOP**

- Convert markdown to semantic HTML (FTMO Academy v2_balanced template)
- Meta title: 50-60 chars | Meta description: 150-160 chars | Canonical: /lesson/[slug]/
- Generate BOTH files simultaneously:
  - \`lesson_[slug]_EN.html\` — final lesson HTML
  - \`lesson_[slug]_EN_log.html\` — styled HTML version of log (sidebar nav, outline block, clickable URLs)
- Append conversion log to \`lesson_[slug]_EN_log.md\`

> "Step 6 complete. Both HTML files saved. Approve → proceed to Step 7."

---

**Step 7 — QA + Inventory Update**

1. Content validation (trading expert review — FIRST):
   - Brief & outline re-check
   - Full article: facts accurate, correct classification depth, didactic sequence, nothing missing/out of scope

2. Source citation audit:
   - All factual claims have sources in log
   - No [SOURCE NEEDED] flags remaining

3. Full QA checklist: E-E-A-T, structure, ToV, readability, keywords, formatting

4. Save all 4 files:
   - [ ] \`lesson_[slug]_EN.md\`
   - [ ] \`lesson_[slug]_EN_log.md\`
   - [ ] \`lesson_[slug]_EN.html\`
   - [ ] \`lesson_[slug]_EN_log.html\`

---

## Entry — Choose Mode

When `/academy-write` is invoked, ask the user to choose:

\`\`\`
Choose mode:
1. New article — enter topic (e.g. "trading timeframes")
2. Continue — paste full path to approved brief (.md or .docx)
3. Edit workflow — modify skills, scripts, or workflow documents
\`\`\`

### Mode 1: New article
- User provides topic name
- Check \`data/output/lessons/[slug]/\` for existing files:
  - No folder → create folder → INIT → Step 1
  - Folder exists with finished article (.md + .html) → new version (v2, v3...) → INIT → Step 1
- Runs full workflow: INIT → Step 1 → Step 2 → ... → Step 7

### Mode 2: Continue from approved brief
- User provides full absolute path to the approved brief file
  (e.g. \`/Users/joe/Projects/ftmo-academy/data/output/lessons/trading-timeframes/lesson_trading-timeframes_EN_outline.md\`)
- Read the brief file + corresponding xlsx from the same folder
- Skip Step 1 and Step 2 — continue from Step 3
- Version detection: check folder for existing versions → use next suffix

### Mode 3: Edit workflow
- Only mode where editing skills, scripts, prompts, or workflow documents is allowed
- In all other modes, NEVER modify skills, scripts, or workflow files

## Important Rules

- Read all reference documents before starting
- No keywords needed upfront — keywords come from Step 1 (Ahrefs MCP)
- Draft in Academy ToV from sentence one — no neutral draft first
- Outline is a hard stop — do not begin writing without user approval
- Every factual claim in Step 3 must have a source URL from Step 1 research
- Both HTML files generated in Step 6 — never just one
- Log file created at INIT and appended after every step
