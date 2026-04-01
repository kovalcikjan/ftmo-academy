# Step 1: Competitor Research

You are researching competitor content for an FTMO Academy article that does not yet exist. Your goal is to understand what the best-ranking content on this topic looks like, identify structural patterns, and surface gaps that the Academy article can fill.

## CORE PRINCIPLE

> **RESEARCH ONLY.** Do not write any article content in this step.
> Your output is an analysis of what competitors cover — not a draft, not an outline.

---

## Research Process

### 1. Discover Pages

Use the topic and slug provided. Search and collect URLs using one of the available tools (in priority order):

**Option 1: WebSearch (built-in, DEFAULT — always available)**
Run 3-4 queries with varied formulations:
- `"[topic] explained trading"`
- `"[topic] guide for traders"`
- `"how to use [topic] trading"`
- topic-specific angle query

**Option 2: EXA MCP (if configured)**
Run the same queries via EXA semantic search — returns pages by meaning, not just keywords.

**Option 3: DataForSEO MCP (if configured)**
Use `serp_google_organic_live` for top keyword queries — returns actual SERP rankings and features.

Collect 15-20 candidate URLs. Add any URLs the user explicitly provides.

**Priority sources** (fetch these first if available):
- Investopedia
- BabyPips
- CMC Markets Learn
- IG Academy
- Corporate Finance Institute (CFI)
- Other broker/prop firm academies (not FTMO direct competitors for the specific lesson)

**Avoid:** Reddit, YouTube descriptions, low-quality blogs, affiliate spam sites.

Cross-reference with Ahrefs MCP `serp-overview` for the top 2-3 keywords to add SERP-ranked pages. Deduplicate. Select top 8-10 most relevant.

### 2. Fetch Each Page

**Timeout rule:** Each WebFetch must complete within **30 seconds**. If a page takes longer or fails, abort immediately and move to the next URL. Log as "timeout" or "failed" in the URL table. Do not retry failed URLs. Minimum 3 successful fetches required to continue.

**Blocklist — never fetch these domains:**
- `ninjatrader.com` — pages hang for minutes without returning. If a NinjaTrader URL appears in search results, skip the fetch but extract keywords via Ahrefs `site-explorer-organic-keywords` (mode=exact) for that URL.

Use WebFetch on each URL. For each page extract:

- Main H1 and H2/H3 headings (structure skeleton)
- Core topics covered
- Approximate depth per topic (surface-level vs. detailed)
- Any unique angles, examples, or frameworks not commonly found
- Notable gaps: what is NOT covered that a trader would want to know

### 3. Cross-Page Analysis

After fetching all pages, synthesize:

- Which topics appear on 3+ pages (table stakes — must cover)
- Which topics appear on 1-2 pages (differentiators — consider covering)
- Which trader questions are NOT answered anywhere (content gap opportunity)

---

## Output Format

### Competitor Analysis Table

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
