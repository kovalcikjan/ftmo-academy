# FTMO Academy - Project CLAUDE.md

## PROJECT: FTMO Academy Content

### TWO WORKFLOWS

#### Větev A — Edit existing lesson (`/academy`)

Use when a lesson already exists on the live site.

```
/academy https://academy.ftmo.com/lesson/[slug]/
Keywords: data/output/keywords/[slug]_keywords.xlsx
```

5-step workflow: Keywords → ToV → Structure → HTML → QA
Defined in: `data/output/guides/ftmo_academy_workflow_EN.md`

#### Větev B — New lesson from scratch (`/academy-write`)

Use when no lesson exists yet (status TODO in inventory).

```
/academy-write [topic/slug]
```

7-step workflow: INIT → Competitor Research + Keywords → Brief & Outline → Draft → ToV Check → Structure → HTML → QA
Defined in: `data/output/guides/ftmo_academy_write_workflow_EN.md`

---

### RULES — BOTH WORKFLOWS

**NEVER edit content manually** without running through the appropriate skill.

**STEP CONFIRMATION — REQUIRED:**
After each step, STOP and wait for user confirmation before proceeding.
Automatic step transitions are FORBIDDEN.

**PARAGRAPH AUDIT — MANDATORY FIRST ACTION IN STRUCTURE STEP:**
Before adding any callouts, tables, or H3s — audit every paragraph for length.
Split any paragraph over 100 words. This is the most commonly missed check.

---

### REFERENCE DOCUMENTS

| Document | Purpose | Used in |
|----------|---------|---------|
| `data/output/guides/ftmo_academy_workflow_EN.md` | Edit workflow (5 steps) | /academy |
| `data/output/guides/ftmo_academy_write_workflow_EN.md` | Write workflow (7 steps) | /academy-write |
| `data/output/guides/ftmo_academy_tov_guide_EN.md` | Tone of Voice guide | Both |
| `data/output/guides/ftmo_academy_structure_guide_EN.md` | Structure & E-E-A-T guide | Both |
| `data/output/guides/ftmo_academy_content_inventory.md` | Content inventory (50 lessons) | Both |
| `data/output/guides/ftmo_academy_product_context.md` | FTMO products, rules, terminology | Both |

---

### LOG FORMAT — VERBATIM ONLY

> **THIS IS THE MOST CRITICAL RULE IN THE ENTIRE WORKFLOW.**
>
> The "Original" column in every log MUST be copied **character-by-character from the article file**.
> NEVER reconstruct from memory. NEVER paraphrase. NEVER approximate.
>
> **Correct process:**
> 1. Locate the sentence in the current file (use Read tool if needed)
> 2. Copy it exactly — punctuation, capitalization, formatting included
> 3. Apply the change
> 4. Log: [verbatim from file] → [exact new version] + reason
>
> **Wrong:** writing what you think the original said
> **Right:** reading the file, copying the exact text, then logging it

```markdown
| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|---------------------|--------|
| 1 | "Watching the market fluctuations and volatility in real-time is an essential skill to acquire." | "Reading price data effectively starts with choosing the right chart type." | ToV: throat-clearing → principle-first opening |
```

---

### NAMING CONVENTION

```
data/output/lessons/[slug]/lesson_[slug]_EN_outline.docx  # Step 2: Brief + Outline (expert edits this)
data/output/lessons/[slug]/lesson_[slug]_EN.md            # Final markdown (first version)
data/output/lessons/[slug]/lesson_[slug]_EN_log.md        # Write/edit log (first version)
data/output/lessons/[slug]/lesson_[slug]_EN.html          # Final HTML (first version)
data/output/lessons/[slug]/lesson_[slug]_EN_log.html      # Log HTML (first version)
data/output/lessons/[slug]/lesson_[slug]_EN_v2.md         # Second version
data/output/lessons/[slug]/lesson_[slug]_EN_v2_log.md
data/output/lessons/[slug]/lesson_[slug]_EN_v2.html
data/output/lessons/[slug]/lesson_[slug]_EN_v2_log.html
data/output/keywords/[slug]_keywords.xlsx                 # Keywords file (edit workflow)
```

Slugs use hyphens (matching URL slugs): `types-of-trading-charts`, not `types_of_trading_charts`.

### VERSIONING RULE

When rewriting a lesson (`/academy-write [slug]`):
- INIT detects existing files in the slug folder
- Determines next version number (v2, v3, ...) automatically
- Uses that suffix for ALL 4 output files of the new run
- **Never overwrites or renames existing files**
- Old versions stay in the folder as-is

---

### MODELS

Configuration in `src/config.py`. Default model for testing: `gpt-4o-mini`.
Production: `gpt-4o` or `claude-sonnet-4-20250514`.
