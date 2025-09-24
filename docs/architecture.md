# 📋️ Architecture Notes
 
## Project layout (modular map)
```
mentalkb-da-poc/
├─ docker-compose.yml           # Stack: Postgres (+seed), pgAdmin, Docassemble
├─ .env.example                 # Copy to .env; credentials & MENTALKB_DB_URL
├─ db-init/
│  └─ 001_mentalkb.sql          # Seed dump (runs once on first boot)
├─ packages/
│  └─ docassemble-mentalkb/
│     ├─ setup.py               # Python package metadata + deps
│     ├─ MANIFEST.in            # Bundle YAML/templates in the wheel/zip
│     ├─ README.md              # Package-level notes (short)
│     └─ docassemble/
│        └─ mentalkb/
│           ├─ __init__.py
│           ├─ loader.py        # READS from DB (pages/layout/questions/options)
│           ├─ util.py          # WRITES interview snapshot to intake_sessions
│           ├─ data/
│           │  └─ questions/
│           │     └─ interview.yml   # Dynamic interview (page-by-page wizard)
│           └─ templates/
│              └─ summary.md    # Export template (swap for DOCX when ready)
├─ docs/
│  ├─ setup-guide.md            # How to run + screenshots
│  └─ architecture.md           # DB mapping & extension points
├─ Makefile                     # Optional: up/down/logs/psql helpers
└─ README.md                    # One-page overview (this doc)
```
## Module responsibilities (who does what)
**Runtime stack**: docker-compose.yml
*Brings up Postgres (seeded from db-init), pgAdmin, and Docassemble with MENTALKB_DB_URL injected.*

**DB → UI mapping**: loader.py

**Pages** from pages (+ visibility + ordering)

**Page items via pages_layout** → join to questions

**Options** from questions_options (fallbacks allowed if you added them)

## Type/required normalization for Docassemble fields

**Persistence**: util.py
Creates (if missing) and inserts into public.intake_sessions (created_at, user_email, data jsonb) at interview completion.

**Interview flow**: data/questions/interview.yml
Iterates pages/questions from the loader; saves; emits an attachment.

**Export**: templates/summary.md
Minimal summary; replace with a branded summary.docx when you’re ready (no code changes beyond filename).

**Docs**: docs/
Short setup + architecture mapping for reviewers.

## Contracts & boundaries 

**Input**: A Postgres DB that contains pages, pages_layout, questions, and questions_options.

**Config**: MENTALKB_DB_URL (set via .env → compose).

**Output**: A single row per interview saved to public.intake_sessions; one downloadable attachment.

## Data sources
- **pages**: defines section titles and ordering (`id`, `title`, `sort`).
- **questions**: mapped to docassemble fields (`id`, `page_id`, `type`, `question`, `required`, `sort`).
- **options**: response choices for radio/checkbox style controls (`id`, `question_id`, `label`, `value`, `sort`).

*Adjust the SQL in `loader.py` if the actual dump uses different table or column names.*

## Flow
1. `loader.KB` connects via `MENTALKB_DB_URL` and caches page/question/option metadata.
2. The interview YAML iterates through pages in sort order and renders each question with the correct docassemble datatype and options.
3. On completion, `util.save_session_results` persists a JSON snapshot to `intake_sessions` (auto-created when missing).
4. A Markdown attachment (`templates/summary.md`) summarizes answers; swap for DOCX/PDF as needed.

## Extension points
- Implement branching by evaluating stored rule expressions before rendering questions.
- Populate additional exports (DOCX, PDF) using docassemble templates.
- Replace Markdown summary with official document templates.
- Integrate authentication by deriving `user_email` from docassemble user sessions.

## Limitations
- Assumes flat page order; no conditional jumps implemented yet.
- Loader performs read-only queries; ensure DB user has appropriate permissions.
- Seeding relies on docker volume reset; provide migration scripts for production.

## Platform stance
- **Database** owns interview content (pages, questions, options).
- **Docassemble** renders UX and calls lightweight `code:` snippets for rules.
- **Python helpers** (`loader.py`, future `rules.py`) provide reusable predicates so rule logic stays versioned and testable.

This split lets content designers update data without redeploying code while keeping engineering control over critical branching and validation.
