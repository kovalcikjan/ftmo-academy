# Step 1: Competitor Research

You are researching competitor content for an FTMO Academy article that does not yet exist. Your goal is to understand what the best-ranking content on this topic looks like, identify structural patterns, and surface gaps that the Academy article can fill.

## CORE PRINCIPLE

> **RESEARCH ONLY.** Do not write any article content in this step.
> Your output is an analysis of what competitors cover — not a draft, not an outline.

---

## 0. Provider Selection (before Krok 3)

Decide which MCP provider will supply URL metrics and keyword discovery:

1. **Primary — Ahrefs MCP.** Probe by calling `site-explorer-domain-rating` on one test domain (e.g. the domain of the first candidate URL). If the call returns valid data → proceed with the Ahrefs branch (Krok 3A, Krok 5A, Krok 7A).
2. **Fallback — DataForSEO MCP (`dfs-mcp`).** If the Ahrefs probe fails (timeout, auth error, "tool not available", empty or error result) → switch automatically to the DFS branch (Krok 3B, Krok 5B, Krok 7B) and append the following line to the lesson log file:

   > Ahrefs MCP unavailable — fell back to DataForSEO MCP. DR score replaced by qualitative ETV-based proxy; organic traffic is domain-level only.

Kroky 1, 2, 4, 6 are identical for both branches.

---

## Research Process

### 1. Discover Pages

Use the topic and slug provided. Run WebSearch (built-in, always available):

- `"[topic] explained trading"` — broad
- `"[topic] guide for traders"` — educational angle
- `"how to choose [topic]"` — practical angle
- topic-specific angle query

4 queries × 6 URLs each → up to 24 candidate URLs. Add any URLs the user explicitly provides. Deduplicate + filter (exclude forums, paywall, non-EN, PDF).

**Priority sources** (fetch these first if available):
- Investopedia
- BabyPips
- CMC Markets Learn
- IG Academy
- Corporate Finance Institute (CFI)
- Other broker/prop firm academies (not FTMO direct competitors for the specific lesson)

**Avoid:** Reddit, YouTube descriptions, low-quality blogs, affiliate spam sites.

### 2. Enrich URLs with Metrics (branch on provider)

Run either 2A (Ahrefs — primary) or 2B (DFS — fallback) depending on the probe from Section 0.

#### 2A — Ahrefs branch (primary)

For all URLs in the candidate table:
- `site-explorer-metrics` (mode=exact) → **Organic Traffic** + org_keywords for the specific URL
- `site-explorer-domain-rating` → **Domain Rating (DR)** for the domain (one call per unique domain, not per URL)

Columns added to URL table: `DR`, `Organic Traffic` (URL-level).

#### 2B — DataForSEO branch (fallback)

For every **unique domain** in the candidate table (URLs of the same domain share the same metrics — do not call per URL):

- `mcp__dfs-mcp__dataforseo_labs_google_domain_rank_overview` with `target=<domain>`
- Extract `items[0].metrics.organic.etv` → estimated monthly organic traffic (proxy for Ahrefs traffic)
- Extract `items[0].metrics.organic.count` → ranking keyword count (proxy authority signal)

Build a **DR proxy** (qualitative scale, since DFS has no direct DR score):

| ETV (monthly organic) | DR proxy label |
|-----------------------|----------------|
| > 1,000,000 | very high |
| > 100,000 | high |
| > 10,000 | medium |
| > 1,000 | low |
| ≤ 1,000 | very low |

- Parallelize calls for 15+ unique domains.
- Empty results (`items: []`) → log as `no DFS data` in Fetch Status, keep the URL row.
- Columns added to URL table: `DR proxy` (qualitative — based on domain ETV), `Organic Traffic (domain/mo)` (domain-level ETV, URL-level not available).

### 3. Fetch Each Page

**Timeout rule:** Each WebFetch must complete within **30 seconds**. If a page takes longer or fails, abort immediately and move to the next URL. Log as "timeout" or "failed" in the URL table. Do not retry failed URLs. Minimum 3 successful fetches required to continue.

**Blocklist — never fetch these domains:**
- `ninjatrader.com` — pages hang for minutes without returning. If a NinjaTrader URL appears in search results, skip the fetch but (Ahrefs branch only) extract keywords via `site-explorer-organic-keywords` (mode=exact) for that URL. On the DFS branch simply skip the URL.

Select top 10 by: relevance > DR (or DR proxy) > traffic. Then WebFetch each URL. For each page extract:

- Main H1 and H2/H3 headings (structure skeleton)
- Core topics covered
- Approximate depth per topic (surface-level vs. detailed)
- Any unique angles, examples, or frameworks not commonly found
- Notable gaps: what is NOT covered that a trader would want to know
- Word count estimate

### 4. Keyword Discovery (branch on provider)

Seed selection (both branches):
- Main seed = confirmed seed from Krok 1
- 2–3 secondary seeds derived from H2 headings of fetched competitor pages

#### 4A — Ahrefs branch (primary)

Combine all seeds comma-separated into a single string. Exactly 2 calls:

1. `keywords-explorer-matching-terms` — all seeds in one call
2. `keywords-explorer-related-terms` — all seeds in one call

#### 4B — DataForSEO branch (fallback)

Exactly 2 calls (one seed per call, not combined):

1. **`mcp__dfs-mcp__dataforseo_labs_google_keyword_suggestions`**
   - `keyword` = main seed
   - `limit` = **50** (do not use 100 — at 100 the response exceeds the token limit and is auto-saved to a file, forcing Python parsing)
   - `filters` = `[["keyword_info.search_volume", ">=", 50]]`
   - `order_by` = `["keyword_info.search_volume,desc"]`
   - Field paths: `keyword`, `keyword_info.search_volume`, `keyword_properties.keyword_difficulty`, `keyword_properties.detected_language`

2. **`mcp__dfs-mcp__dataforseo_labs_google_related_keywords`**
   - `keyword` = secondary seed (strongest H2-derived seed)
   - `depth` = 2
   - `limit` = 100
   - `filters` = `[["keyword_data.keyword_info.search_volume", ">=", 30]]`
   - `order_by` = `["keyword_data.keyword_info.search_volume,desc"]`
   - Field paths: `keyword_data.keyword`, `keyword_data.keyword_info.search_volume`, `keyword_data.keyword_properties.keyword_difficulty` (note `keyword_data.*` wrapping — different from `keyword_suggestions`)

**Large-response fallback:** if DFS returns `Error: result exceeds maximum allowed tokens` and auto-saves data to `/Users/admin/.claude/projects/-Users-admin/<session>/tool-results/*.txt`, parse with `.venv/bin/python` using `json.load()`.

### 5. Cross-Page Analysis

After fetching all pages, synthesize:

- Which topics appear on 3+ pages (table stakes — must cover)
- Which topics appear on 1-2 pages (differentiators — consider covering)
- Which trader questions are NOT answered anywhere (content gap opportunity)

---

## Output Format

### xlsx file (branch on provider)

Save as `data/output/lessons/[slug]/[slug]_step1.xlsx`. Column headers differ per provider branch.

**Sheet "URLs" — Ahrefs branch (up to 24 rows):**

| # | URL | Source | Query # | DR | Organic Traffic | Fetch Status | H1 | Key Topics | Notable Gap | Word Count |
|---|-----|--------|---------|----|-----------------|--------------|-----|------------|-------------|------------|

**Sheet "URLs" — DFS branch (up to 24 rows):**

| # | URL | Source | Query # | DR proxy | Organic Traffic (domain/mo) | Fetch Status | H1 | Key Topics | Notable Gap | Word Count |
|---|-----|--------|---------|----------|-----------------------------|--------------|-----|------------|-------------|------------|

**Sheet "Keywords" (identical in both branches, up to 30 rows):**

| # | Keyword | Volume | KD | Cluster | Status | Notes |
|---|---------|--------|----|---------|--------|-------|

- Status + Notes columns empty — user fills during review
- Content Gap Summary goes into the log file, not the xlsx

### Competitor Analysis Table (in chat, for quick review)

| # | URL | Key Topics Covered | Structure Pattern | Unique Angle or Example | Notable Gap |
|---|-----|--------------------|-------------------|------------------------|-------------|
| 1 | ... | ... | ... | ... | ... |

**Structure Pattern examples:** "Definition → Types → Examples → Pros/Cons", "How it works → When to use → Common mistakes"

### Topic Coverage Matrix

List all topics found across pages. Mark coverage:

| Topic | Sources (count) | Depth | Include? |
|-------|-----------------|-------|----------|
| What is [X] | 8/9 | Surface | Yes — required |
| [X] vs [Y] | 5/9 | Medium | Yes |
| [X] calculation formula | 2/9 | Deep | Yes — differentiator |
| [X] in crypto | 1/9 | Surface | No — out of scope |

**Include? options:** Yes — required / Yes — differentiator / Maybe / No — out of scope

### Content Gap Summary

3-5 bullet points identifying what the Academy article can do better or differently:

- Example: "No competitor explains the practical application step-by-step — all stop at theory"
- Example: "No competitor covers practical application with real position-sizing examples"
- Example: "Risk management integration missing — most treat it as pure theory"

### Recommended Competitor URLs (for user review)

List the 5-7 most useful pages found, with one-line summary of why each is valuable:

```
1. [URL] — Best structural reference, covers X in depth
2. [URL] — Unique angle on Y
3. [URL] — Most comprehensive on Z
```

---

## Stop Condition

After outputting the analysis:

> **Step 1 complete.**
>
> Fetched [N] competitor pages. Key findings:
> - Table stakes topics: [list top 3-5]
> - Differentiator opportunities: [list 1-3]
> - Main gap: [one sentence]
>
> Review the competitor analysis above. You can:
> - Confirm and proceed to Step 2 (Brief & Outline)
> - Add specific URLs to fetch before proceeding
> - Flag any topics to exclude from scope

**Wait for user response before proceeding.**

---

## Input

Topic and slug are provided in the skill invocation arguments. Keywords xlsx has been parsed in initialization.

Begin by fetching competitor pages for the topic.
