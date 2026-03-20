# FTMO Academy Content System

AI-assisted content creation and editing system for FTMO Academy trading education lessons.

## Quick Start

### 1. Clone & Setup

```bash
git clone git@github.com:kovalcikjan/ftmo-academy.git
cd ftmo-academy
cp .env.example .env
# Fill in your API keys in .env
```

### 2. Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -e .
```

### 3. Configure Claude Code

This project includes two slash commands as project-level Claude Code skills in `.claude/commands/`. They are automatically available when you open Claude Code inside this repo directory.

**Required MCP server:**
- **Ahrefs** — keyword research, SERP analysis, backlinks

**Optional MCP servers (enhance Step 1 research):**
- **EXA** — semantic web search (better relevance than keyword search)
- **DataForSEO** — real-time SERP data, keyword ideas, on-page analysis

Without any optional MCP, Step 1 uses built-in `WebSearch` + `WebFetch` (always works).

#### MCP Setup

```bash
# Ahrefs (required) — configured via Claude.ai account or .mcp.json
# See: https://docs.anthropic.com/en/docs/claude-code/mcp

# EXA (optional)
claude mcp add --transport http exa "https://mcp.exa.ai/mcp?exaApiKey=YOUR_EXA_KEY"

# DataForSEO (optional) — base64 encode "login:password"
claude mcp add --header "Authorization: Basic BASE64_LOGIN_PASSWORD" --transport http dfs-mcp https://mcp.dataforseo.com/http
```

## Workflows

### `/academy-write [slug]` — Write New Lesson

7-step workflow for creating lessons from scratch:

| Step | Action | Output |
|------|--------|--------|
| INIT | Load references, create log | Init summary |
| 1 | Competitor research + keywords (WebSearch + Ahrefs MCP) | URL list + keyword set |
| 2 | Brief & outline | Approved outline |
| 3 | Draft writing (Academy ToV) | Full article + source citations |
| 4 | ToV verification pass | Correction log |
| 5 | Structure & formatting | Formatted markdown |
| 6 | HTML conversion | lesson.html + log.html |
| 7 | QA + inventory update | 4 final files |

**Usage modes:**
- `academy-write [slug]` — full workflow
- `academy-write brief [slug]` — outline only (Steps 1-2)
- `academy-write draft [slug]` — from existing outline (Steps 3-7)
- `academy-write inventory` — list TODO lessons

### `/academy [URL or path]` — Edit Existing Lesson

5-step workflow for editing lessons already on the live site:

| Step | Action |
|------|--------|
| 1 | Keyword integration |
| 2 | ToV rewrite |
| 3 | Structure & formatting |
| 4 | HTML conversion |
| 5 | QA review |

## Project Structure

```
ftmo-academy/
├── .claude/commands/          # Claude Code slash commands (portable)
│   ├── academy-write.md       # /academy-write skill
│   └── academy.md             # /academy skill
├── CLAUDE.md                  # Project instructions for Claude
├── data/
│   ├── raw/lessons/           # Source articles (READ-ONLY)
│   ├── output/
│   │   ├── guides/            # ToV guide, structure guide, workflow, inventory
│   │   ├── keywords/          # Keyword research XLSX files
│   │   └── lessons/[slug]/    # Output: .md, _log.md, .html, _log.html
├── prompts/                   # Step-specific prompt templates
│   ├── write_step1_research.md
│   ├── write_step2_brief.md
│   ├── write_step3_draft.md
│   ├── write_step4_tov_check.md
│   ├── step1_keywords.md
│   ├── step2_tov.md
│   ├── step3_structure.md
│   └── step4_html.md
├── src/                       # Python utilities
│   ├── config.py              # API keys, model config
│   ├── generate_log.py        # Log MD → HTML/PDF converter
│   ├── create_keyword_xlsx.py # Keyword XLSX generator
│   ├── model_tester.py        # Multi-model content tester
│   └── step4_html.py          # HTML conversion helper
├── .env.example               # API key template
└── pyproject.toml             # Project dependencies
```

## Reference Documents

| Document | Purpose |
|----------|---------|
| `data/output/guides/ftmo_academy_tov_guide_EN.md` | Tone of Voice — how Academy content should sound |
| `data/output/guides/ftmo_academy_structure_guide_EN.md` | Structure & E-E-A-T — formatting, headings, callouts |
| `data/output/guides/ftmo_academy_write_workflow_EN.md` | Write workflow — detailed step-by-step for new lessons |
| `data/output/guides/ftmo_academy_workflow_EN.md` | Edit workflow — step-by-step for existing lessons |
| `data/output/guides/ftmo_academy_content_inventory.md` | Content inventory — 50 lessons, status, prerequisites |

## Output Files

Each lesson produces 4 files in `data/output/lessons/[slug]/`:

```
lesson_[slug]_EN.md          # Final markdown
lesson_[slug]_EN_log.md      # Audit/change log
lesson_[slug]_EN.html        # Final HTML (FTMO Academy template)
lesson_[slug]_EN_log.html    # Styled HTML log
```

Versioning: `_v2`, `_v3` suffixes for subsequent rewrites. Previous versions are never overwritten.

## Key Rules

- **Step confirmation required** — each step stops for user approval before proceeding
- **Academy Tone of Voice** — professional guide, not textbook or friend. No hype, no emotional validation.
- **Paragraph audit** — mandatory first action in Structure step: split any paragraph >100 words
- **Source citations** — every factual claim needs a source URL in the log
- **Log verbatim** — original sentences copied character-by-character, never from memory
