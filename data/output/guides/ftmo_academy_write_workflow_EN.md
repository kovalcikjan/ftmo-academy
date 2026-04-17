# FTMO Academy: New Lesson Writing Workflow

**Version:** 3.4
**Created:** 2026-03-05
**Updated:** 2026-04-17
**Purpose:** Step-by-step process for writing FTMO Academy lessons from scratch

---

## 1. Workflow Overview

```
INPUT                        PROCESS                                    OUTPUT
─────                        ───────                                    ──────
Topic / Slug           →     INIT: Load refs, create log file      →   Init Summary + log file
                       →     Step 1: Competitor Research            →   [slug]_step1.xlsx (URLs + Keywords)
                       →     Step 2: Brief & Outline                →   [slug]_EN_outline.docx
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

### New article (default)

```
/academy-write [topic/slug]
```

Runs Init + Steps 1–7. Stops for user confirmation after each step.

### Continue existing article

```
/academy-write continue [slug]
/academy-write continue [folder-path]
```

Runs Init with auto-detection of last completed step → resumes from the next incomplete step. See Section 5 for detection logic.

### Brief only

```
/academy-write brief [topic/slug]
```

Runs Init + Steps 1–2. Output: approved outline only. Use when you need a content plan without writing.

### No arguments — interactive menu

```
/academy-write
```

Shows a menu with two options:
1. **New article** — user provides topic or slug
2. **Continue article** — user provides slug, folder path, or topic

Waits for user input. Does NOT display inventory or TODO list.

---

## 5. Initialization

Runs automatically. No user confirmation needed.

### Input Identification — Lokace

Every lesson has a unique **Lokace** identifier (e.g., `2.1.1.1.`) from the Content Inventory. This prevents confusion between similarly named lessons.

**Accepted input formats:**
- Lokace only: `/academy-write 2.1.1.1.` — resolves to lesson via inventory lookup
- Topic + Lokace: `/academy-write types-of-trading-charts 2.1.1.1.` — explicit match
- Topic only: `/academy-write types-of-trading-charts` — inventory lookup by name (warn if ambiguous)

**Resolution logic:**
1. If Lokace is provided → look up in Content Inventory, use as primary identifier
2. If only topic/slug → search inventory by name, check for ambiguity (multiple matches = ask user for Lokace)
3. If lesson not found in inventory → proceed anyway (new lesson), but ask user to assign a Lokace number

### Actions

1. Read reference documents: ToV Guide, Structure Guide, Workflow
2. Read Content Inventory — extract Lokace, internal linking targets (Part, Module, related lessons). NOT for task management or TODO tracking
3. **Resolve lesson identity** via Lokace (see above). If ambiguous, stop and ask for Lokace number
4. Determine mode:
   - **NEW mode:** Check for existing files in `data/output/lessons/[slug]/`. If found, determine next version number (v2, v3...) and use as suffix for ALL output files. Never overwrite. Create log file. Proceed to Step 1.
   - **CONTINUE mode:** Auto-detect last completed step (see detection logic below). Report status. Proceed from next step.
5. Output Init Summary (including Lokace)

### CONTINUE — Auto-detection Logic

Scan `data/output/lessons/[slug]/` for files and determine last completed step:

| Files found | Last completed step | Resume from |
|-------------|-------------------|-------------|
| Only `_log.md` | INIT | Step 1 |
| `_step1.xlsx` | Step 1 | Step 2 |
| `_outline.docx` | Step 2 | Step 3 |
| `_EN.md` (draft, no HTML) | Step 3-5 (read log to determine) | Next incomplete step |
| `_EN.html` + `_log.html` | Step 6 | Step 7 |
| All 4 final files + QA in log | Step 7 | Done — ask if user wants a new version |

For Steps 3-5 ambiguity: read the log file and check which step sections exist (`## Step 3`, `## Step 4`, `## Step 5`).

When resuming, read all existing output files (xlsx, outline, draft) to restore context before proceeding.

### Log File — Initialize at INIT (NEW mode only)

Create `data/output/lessons/[slug]/lesson_[slug]_EN_log.md` with:

```markdown
# Write Log: [Lesson Title]

**Slug:** [slug]
**Lokace:** [X.Y.Z.N.]
**Date:** [today]
**Workflow version:** 3.3

---

## INIT

| Item | Value |
|------|-------|
| Lokace | [X.Y.Z.N.] |
| Inventory position | Part N: [Name] > [Module], Lesson N of M |
| Internal linking targets | [related lessons from inventory] |
| Keywords source | Ahrefs MCP (Step 1) |
| Existing versions found | None / v3 at [path] — ignored per user instruction |
```

### Init Summary — NEW mode

```
Topic:         [Lesson name]
Lokace:        [X.Y.Z.N.]
Slug:          [lesson-slug]
Part:          [Part N — Name]
Module:        [Module name]
Position:      Lesson N of M in module
Links to:      [lesson titles from inventory]
Existing ver.: None | [filename] — will create vN+1

Keywords: loaded in Step 1 (Ahrefs MCP)

Confirm to start Step 1 (Competitor Research + Keyword Discovery).
```

### Init Summary — CONTINUE mode

```
Continuing:    [Lesson name]
Lokace:        [X.Y.Z.N.]
Slug:          [lesson-slug]
Folder:        [full absolute path]
Files found:   [list of existing files]
Last step:     Step [N] — [name]
Resume from:   Step [N+1] — [name]

Confirm to start Step [N+1].
```

If slug is not in the inventory, proceed anyway — inventory is for linking context only, not a prerequisite.

---

## 6. Step 1 — Competitor Research + Keyword Discovery

**Prompt:** `prompts/write_step1_research.md`

### Purpose

Understand the competitive landscape before writing. Scope the topic. Build the keyword set. Output: URL list + keywords — both used in Step 2.

### Krok 0: Provider Selection (Ahrefs primary, DataForSEO fallback)

Before running Krok 3 and Krok 5, decide which MCP provider to use for metrics and keyword discovery:

1. **Primary — Ahrefs MCP.** Probe availability by calling `site-explorer-domain-rating` on one test seed domain (e.g. the domain of the first candidate URL collected in Krok 2). If the call returns a valid response with data → proceed with the Ahrefs branch (Krok 3A, Krok 5A, Krok 7A).
2. **Fallback — DataForSEO MCP (`dfs-mcp`).** If the Ahrefs probe fails (timeout, auth error, "tool not available", empty/error result) → switch automatically to the DFS branch (Krok 3B, Krok 5B, Krok 7B) and append the following line to `lesson_[slug]_EN_log.md`:

   > Ahrefs MCP unavailable — fell back to DataForSEO MCP. DR score replaced by qualitative ETV-based proxy; organic traffic is domain-level only.

3. Kroky 1, 2, 4, 6 are identical for both branches. Only Kroky 3, 5 and the xlsx headers in Krok 7 change.

### Krok 1: Seed Keyword Validation

1. **Translate** the user's topic (often in Czech) to English
2. **Verify** the seed is correct for trading education context:
   - Run 1 quick WebSearch: `"[translated topic] trading education"`
   - Check how trading academies (Babypips, Investopedia, broker education) name this topic
   - Confirm or adjust the seed based on actual usage
3. **Output:** 1 confirmed main seed keyword (e.g. `trading timeframes`)

### Krok 2: WebSearch — 4 queries, 6 URLs each

1. Run exactly **4 WebSearch queries** with varied formulations of the confirmed seed:
   - `"[seed] explained trading"` — broad
   - `"[seed] guide for traders"` — educational angle
   - `"how to choose [seed]"` — practical angle
   - topic-specific angle query (adapt to subject)
2. From each query, select **top 6 URLs**
3. **Deduplicate + filter:** exclude forums (Reddit, Quora), paywalled content, non-EN pages, PDF files
4. Result: **up to 24 URLs** in the candidate table (duplicates across queries marked in Source column)

### Krok 3: Enrich every URL with metrics

Run either Krok 3A (Ahrefs — primary) or Krok 3B (DFS — fallback) depending on provider selection from Krok 0.

#### Krok 3A — Ahrefs branch (primary)

5. For all URLs in the table, call Ahrefs MCP:
   - `site-explorer-metrics` (mode=exact) → **Organic traffic** + org_keywords for the specific URL
   - `site-explorer-domain-rating` → **Domain Rating (DR)** for the domain
6. Add DR + Organic Traffic (URL-level) columns to the URL table

> **Note:** DR is a domain-level metric (one call per unique domain, not per URL).
> Organic traffic is URL-level (one call per URL via `site-explorer-metrics` with `mode=exact`).

#### Krok 3B — DataForSEO branch (fallback)

5. For every **unique domain** in the candidate table, call:
   - `mcp__dfs-mcp__dataforseo_labs_google_domain_rank_overview` with `target=<domain>`
   - Extract `items[0].metrics.organic.etv` → estimated monthly organic traffic (proxy for Ahrefs traffic)
   - Extract `items[0].metrics.organic.count` → number of ranking keywords (proxy for domain authority signal)
6. Build a **DR proxy** (qualitative scale, since DFS has no direct DR score):

   | ETV (monthly organic) | DR proxy label |
   |-----------------------|----------------|
   | > 1,000,000 | very high |
   | > 100,000 | high |
   | > 10,000 | medium |
   | > 1,000 | low |
   | ≤ 1,000 | very low |

7. Parallelize domain calls for efficiency (15+ unique domains → run concurrently).
8. **Per-domain metric, not per-URL:** URLs sharing the same domain share the same ETV/count values — populate both URL rows with the same domain-level figure.
9. **Empty results:** some domains return `items: []`. Log them as `no DFS data` in the Fetch Status column but keep the URL row.
10. Add **DR proxy** + **Organic Traffic (domain/mo)** columns to the URL table.

### Krok 4: Select top 10 for fetching + extract content

7. From the enriched URLs, select **top 10** by: relevance > DR > organic traffic
8. WebFetch each selected URL — extract:

   | Extract | Purpose |
   |---------|---------|
   | **H1** | How competitor framed the title |
   | **H2/H3 structure** | Section coverage — basis for our outline |
   | **Topics covered** | What is standard in SERP — must cover |
   | **Topics missing** | Content gaps — our differentiation |
   | **Depth** | Surface overview vs. detailed guide |
   | **Tables/comparisons** | What formats competitors use |
   | **Unique angle** | What makes each one different |
   | **Word count estimate** | Benchmark for our target |

9. **Timeout:** Each WebFetch must complete within **30 seconds**. If a page takes longer, abort immediately — log as "timeout, skipped" and move to the next URL. Do not retry.
10. **Blocklist:** Skip `ninjatrader.com` entirely — never fetch (pages hang for minutes without blocking). Instead, extract keywords only via Ahrefs `site-explorer-organic-keywords` if a NinjaTrader URL ranked in search results.
11. If WebFetch fails (timeout / blocked / error): note in log — proceed with remaining pages
12. Minimum 3 successfully fetched pages to continue

### Krok 5: Keyword Discovery

Run either Krok 5A (Ahrefs — primary) or Krok 5B (DFS — fallback) depending on provider selection from Krok 0.

**Seed selection (both branches):**
- Main seed from Krok 1 (e.g. `trading timeframes`)
- 2–3 additional seeds derived from H2 headings of fetched competitor pages (e.g. `best timeframe for swing trading`)

#### Krok 5A — Ahrefs branch (primary)

Combine all seeds comma-separated into a single string.

**Ahrefs queries — exactly 2 calls:**
1. `keywords-explorer-matching-terms` — all seeds in one call
2. `keywords-explorer-related-terms` — all seeds in one call

#### Krok 5B — DataForSEO branch (fallback)

**DFS queries — exactly 2 calls (one seed per call, not combined):**

1. **Call 1:** `mcp__dfs-mcp__dataforseo_labs_google_keyword_suggestions`
   - `keyword` = main seed (from Krok 1)
   - `limit` = **50** (do **not** use 100 — at 100 the response exceeds the token limit and is auto-saved to a file, forcing Python parsing)
   - `filters` = `[["keyword_info.search_volume", ">=", 50]]`
   - `order_by` = `["keyword_info.search_volume,desc"]`
   - Field paths in result: `keyword`, `keyword_info.search_volume`, `keyword_properties.keyword_difficulty`, `keyword_properties.detected_language`

2. **Call 2:** `mcp__dfs-mcp__dataforseo_labs_google_related_keywords`
   - `keyword` = secondary seed (strongest H2-derived seed)
   - `depth` = 2
   - `limit` = 100
   - `filters` = `[["keyword_data.keyword_info.search_volume", ">=", 30]]`
   - `order_by` = `["keyword_data.keyword_info.search_volume,desc"]`
   - Field paths in result: `keyword_data.keyword`, `keyword_data.keyword_info.search_volume`, `keyword_data.keyword_properties.keyword_difficulty` (note: `keyword_data.*` wrapping, different from `keyword_suggestions`)

**Large-response fallback:** if DFS returns `Error: result exceeds maximum allowed tokens` and auto-saves data to `/Users/admin/.claude/projects/-Users-admin/<session>/tool-results/*.txt`, parse the file with `.venv/bin/python` using `json.load()` to extract the items.

### Krok 6: Merge + Deduplicate + Filter + Cluster

1. **Merge** all keywords from Ahrefs (matching + related) + topics from competitor H2/H3 headings
2. **Exact dedup** — remove identical phrases
3. **Filter:**
   - Remove branded terms (specific broker/platform names)
   - Remove non-EN keywords
   - Remove clearly out-of-scope keywords
   - Volume threshold (dynamic, based on main keyword volume):
     - Main KW > 500 vol → cutoff 20
     - Main KW 100–500 vol → cutoff 10
     - Main KW < 100 vol → cutoff 0 (keep all)
4. **Intent clustering** — keywords with the same search intent get the same cluster number
5. Sort by volume descending

Output: **up to 30 keywords** (exact count depends on topic — niche topics may yield 5–10, broad topics up to 30)

> **Keyword count is topic-dependent.** Do not force a fixed number. Include all relevant keywords up to 30 maximum. The user reviews and adjusts the final set before Step 2.

### Krok 7: Generate xlsx

Save as `data/output/lessons/[slug]/[slug]_step1.xlsx` with two sheets. Column headers depend on which provider branch ran in Kroky 3 and 5.

#### Krok 7A — Ahrefs branch headers

**Sheet "URLs" (up to 24 rows):**

| # | URL | Source | Query # | DR | Organic Traffic | Fetch Status | H1 | Key Topics | Notable Gap | Word Count |
|---|-----|--------|---------|----|-----------------|--------------|-----|------------|-------------|------------|

**Sheet "Keywords" (up to 30 rows):**

| # | Keyword | Volume | KD | Cluster | Status | Notes |
|---|---------|--------|----|---------|--------|-------|

#### Krok 7B — DFS branch headers

**Sheet "URLs" (up to 24 rows):**

| # | URL | Source | Query # | DR proxy | Organic Traffic (domain/mo) | Fetch Status | H1 | Key Topics | Notable Gap | Word Count |
|---|-----|--------|---------|----------|-----------------------------|--------------|-----|------------|-------------|------------|

- **DR proxy** — qualitative label based on domain ETV (very high / high / medium / low / very low). Cell note or header subtitle: `qualitative — based on domain ETV`.
- **Organic Traffic (domain/mo)** — domain-level ETV from `domain_rank_overview`. URL-level traffic is not available in the DFS fallback.

**Sheet "Keywords" (up to 30 rows):**

| # | Keyword | Volume | KD | Cluster | Status | Notes |
|---|---------|--------|----|---------|--------|-------|

(Keywords headers are identical in both branches.)

#### Common rules (both branches)

- Status and Notes columns are **empty** — user fills these during review
- Content Gap Summary (3–5 bullets) appended to the log file, not the xlsx

### Stop Condition

> **Step 1 complete.** [N] URLs collected, [N] fetched successfully. [N] keywords proposed ([N] clusters).
> Key gap: [sentence].
> **xlsx saved at:** `[full absolute path]`
> Review URLs + keywords in the xlsx → add, remove, or annotate → confirm to proceed to Step 2.

**IMPORTANT:** Always output the FULL ABSOLUTE path (e.g. `/Users/admin/Projects/ftmo-academy/data/output/lessons/[slug]/[filename]`), not a relative path.

**Wait for user confirmation.**

---

## 7. Step 2 — Brief & Outline

**Prompt:** `prompts/write_step2_brief.md`

### Purpose

Define the architecture of the lesson before any prose is written. The approved outline is the contract for Step 3.

### Actions (in order)

1. Classify lesson: BEGINNER or ADVANCED
2. Set word count target (based on competitor avg + topic complexity)
3. State differentiation from competitors (what Academy does that others don't)
4. Map top 3–5 keywords to H1/H2 headings
5. Write full heading skeleton with key points, callouts, and tables per section
6. Plan internal links (3–5 minimum from Content Inventory)
7. Content validation (trading expert review)

### BEGINNER vs. ADVANCED Classification

| Signal | BEGINNER | ADVANCED |
|--------|----------|----------|
| Entry level | No prior TA knowledge | Requires indicator / strategy knowledge |
| Topic type | What is X / How does X work | When to use X / Edge cases / Optimization |
| Assumed knowledge | None | Part 1 + prior Technical Analysis |
| Depth | Why + How + Example | How + Example (skip the obvious "why") |

### Keyword Placement in Step 2 — Headings Only

Use the keyword set from Step 1 xlsx. Step 2 assigns keywords to headings only.

- Top 3–5 keywords by volume → assign to H1 or H2 where topic naturally fits
- Never force a keyword into a heading if it breaks natural language
- Remaining keywords → body text in Step 3 (no pre-assignment needed here)

| # | Keyword | Volume | Heading assignment |
|---|---------|---------|--------------------|
| 1 | [kw] | [vol] | H1 |
| 2 | [kw] | [vol] | H2 |
| — | remaining [N] kw | — | Step 3 (body) |

### Content Validation: Outline Review

Before presenting the outline for approval, review it as a trading expert and educator:

- Does the structure logically follow the topic?
- Are all key concepts present for the given classification (BEGINNER/ADVANCED)?
- Is the order of sections didactically correct — does each section build on the previous?
- Are there gaps — concepts a trader would expect to find but are missing?
- Are there sections that don't belong or are out of scope?

Output: validation note (pass / flagged issues) appended below the outline.

### Output — Two Artifacts

**1. Outline file (.docx)** — saved immediately, editable by trading expert:

Generate the outline content as markdown internally, then convert to `.docx` using the export script:

```bash
.venv/bin/python src/export_outline_docx.py data/output/lessons/[slug]/lesson_[slug]_EN_outline.md
```

This produces `lesson_[slug]_EN_outline.docx` in the same folder. Delete the intermediate `.md` file after successful conversion — the `.docx` is the single source of truth.

The outline content structure (used internally before conversion):

```markdown
# Lesson Brief & Outline: [Title]

## Brief

| Item | Value |
|------|-------|
| Topic | [Name] |
| Czech Title | [Český název lekce z inventáře] |
| Slug | [slug] |
| Part | [Part N — Name] |
| Module | [Module Name] |
| Position | [Lesson N of M / new] |
| Classification | BEGINNER | ADVANCED — [one-sentence reason] |
| Word Count | [N–N words] — [basis] |

## Differentiation

- [What this lesson does that competitors don't]
- [FTMO-specific context to include]
- [Topics deliberately excluded]

## Keywords — Headings

| # | Keyword | Volume | Heading |
|---|---------|--------|---------|

## Outline

# [H1 — Lesson Title] (H1)

Key point: [what the reader learns overall]

---

## [Section Name] (H2)

Target keyword: [keyword] (if assigned)

Key points:
- [Specific fact or principle to cover]
- [...]

Callout: [Type — description]
Table: [What to compare]

### [Subsection Name] (H3)

- [...]

---

## Internal Links Plan

| # | Link Text | Target Lesson | Slug | Placement |
|---|-----------|---------------|------|-----------|

## Content Validation

- [validation notes]
- **Validation: PASS | ISSUES**
```

**2. Log file** — append Step 2 section to existing `lesson_[slug]_EN_log.md`

### Reading the Outline Back (Step 3 / Continue Mode)

When resuming from an edited `.docx` outline, extract its text content before proceeding:

```bash
.venv/bin/python src/read_outline_docx.py data/output/lessons/[slug]/lesson_[slug]_EN_outline.docx
```

This outputs the `.docx` content as plain text to stdout. Use it to restore outline context for Step 3.

### Stop Condition

> **Step 2 complete.** Outline for "[Title]" — [BEGINNER/ADVANCED], ~[N] words.
> [N] H2s, [N] H3s, [N] keywords mapped to headings. Content validation: [pass / issues].
> **Outline saved at:** `[full absolute path to .docx]`
> Send .docx to trading expert for review → approve (with or without edits) → proceed to Step 3.

**IMPORTANT:** Always output the FULL ABSOLUTE path (e.g. `/Users/admin/Projects/ftmo-academy/data/output/lessons/[slug]/lesson_[slug]_EN_outline.docx`), not a relative path.

**Wait for user approval. Do not begin writing until the outline is approved.**

---

## 8. Step 3 — Draft Writing

**Prompt:** `prompts/write_step3_draft.md`

### Purpose

Write the full lesson in Academy Tone of Voice, following the approved outline exactly.

### Reading the Approved Outline

The approved outline is stored as `.docx`. Before writing, extract its content:

```bash
.venv/bin/python src/read_outline_docx.py data/output/lessons/[slug]/lesson_[slug]_EN_outline.docx
```

If the trading expert edited the `.docx`, those edits are the current source of truth — follow the extracted content, not the original Step 2 output from memory.

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

### Inventory Update (optional — linking context only)

If internal links were used in the lesson, update the "Links To" column in `ftmo_academy_content_inventory.md` for cross-reference. Do NOT update status columns — inventory is not used for task management.

### Stop Condition

> **Step 7 complete.** QA: [PASS / FAIL].
> Content validation: [PASS / issues found].
> Source citations: [N] verified, [N] flagged.
> Files saved: 4/4.
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
[slug]_step1.xlsx                    # Step 1 output: URLs + Keywords (user reviews)
lesson_[slug]_EN_outline.docx        # Step 2 output: Brief + Outline (trading expert reviews/edits)
lesson_[slug]_EN.md                  # Final markdown
lesson_[slug]_EN_log.md              # Write log (all steps)
lesson_[slug]_EN.html                # Final HTML
lesson_[slug]_EN_log.html            # Log HTML
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
| 3.0 | 2026-03-20 | **Step 1 rewrite:** 7-step process (seed validation → 4 WebSearch queries × 6 URLs → Ahrefs DR + organic traffic per URL → top 10 fetch with extraction checklist → keyword discovery 2 Ahrefs calls → merge/dedup/filter/cluster → xlsx output). Removed EXA/DataForSEO options, removed Ahrefs SERP cross-reference. Added: DR via `domain-rating` + traffic via `site-explorer-metrics` (mode=exact). Keywords max 30 with intent clustering. Output = xlsx with 2 sheets. **Step 2 rewrite:** outline saved as separate editable file `lesson_[slug]_EN_outline.md`. Updated naming convention with Step 1 xlsx + Step 2 outline files. |
| 3.1 | 2026-03-23 | **Entry point rewrite:** Removed inventory mode — inventory used only for internal linking context, not task management. Added interactive menu (New / Continue) when no arguments. Added CONTINUE mode with auto-detection of last completed step from existing files. Step 7 inventory update now optional (linking context only). Steps 1-2 stop messages require full absolute file paths. |
| 3.2 | 2026-03-23 | **Step 2 output format:** Changed outline output from `.md` to `.docx` (generated via `src/export_outline_docx.py`). Trading expert edits the `.docx` directly — single source of truth, no duplicate files. Added `src/read_outline_docx.py` for reading edited `.docx` back when resuming from Step 3. Updated naming convention and auto-detection logic. |
| 3.4 | 2026-04-17 | Step 1: Added DataForSEO MCP fallback (`domain_rank_overview` + `keyword_suggestions` + `related_keywords`). Activates automatically when Ahrefs MCP fails. DR score replaced by qualitative ETV proxy; organic traffic becomes domain-level. Provider selection logic added at start of Step 1 (Krok 0). Kroky 3, 5, 7 branch into A (Ahrefs) / B (DFS) variants; Kroky 1, 2, 4, 6 unchanged. |

---

*Companion document: [Edit Workflow](ftmo_academy_workflow_EN.md) — for existing lessons*
*Reference: [ToV Guide](ftmo_academy_tov_guide_EN.md) | [Structure Guide](ftmo_academy_structure_guide_EN.md)*
