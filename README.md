# 🚀 MentalkB Docassemble PoC
> **Proof-of-concept:** migrating MentalkB wizard flows from Catalyst into [docassemble](https://docassemble.org/).

<<<<<<< HEAD
_For the detailed walkthrough with screenshots, see [docs/setup-guide.md](docs/setup-guide.md)._ 


# ⚡ **Quick Start**

1. Copy `.env.example` to `.env` and change secrets if needed.

2. Place sanitized MentalkB dump at `db-init/001_mentalkb.sql`.

3. Start the entire stack with `docker compose up -d` (or `make up`).
4. Wait for the containers to report healthy, then open <http://localhost:8080>.
5. Log in with the credentials from `.env`, install the `docassemble-mentalkb` package from this repo, and browse to `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.

## Project Layout 

- `docker-compose.yml` – docassemble + Postgres + pgAdmin stack
- `db-init/` – seed SQL executed the first time Postgres starts
- `packages/docassemble-mentalkb/`
  - `docassemble/mentalkb/`
    - `loader.py` – SQLAlchemy loader pulling pages/questions/options
    - `util.py` – DB write hook (persists to `intake_sessions`)
    - `data/questions/interview.yml` – docassemble interview 'driver'(essentially the .yml file is an orchestrator of elements, a UX engine per say)
    - `templates/summary.md` – export template (will swap for DOCX)
  - `setup.py`, `MANIFEST.in` – Python packaging metadata(package and dependency configuration essentially)
- `docs/` – setup guide and architecture notes

## ✨ Highlights ✨

- Dynamic interview: pages, questions, and options load live from Postgres.
- One-command bootstrap: `docker compose up -d` brings the full stack online.
- Responses persist to `intake_sessions` and generate a downloadable summary.


## Next Steps 

- Extend rules mapping for complex branching or page logic.
- Replace the Markdown summary with branded DOCX/PDF output.
- Harden credentials and add CI checks when moving beyond the PoC.

---

Built for the MentalkB migration feasibility study. Work in progress.

=======
**Proof-of-concept:** migrating MentalkB wizard flows from Catalyst into [docassemble](https://docassemble.org/).

_For the detailed walkthrough with screenshots, see [docs/setup-guide.md](docs/setup-guide.md)._ 

## Quick Start

1. Copy `.env.example` to `.env` and customize secrets if needed.
2. Place the sanitized MentalkB dump at `db-init/001_mentalkb.sql`.
3. Start the stack with `docker compose up -d` (or `make up`).
4. Wait for the containers to report healthy, then open <http://localhost:8080>.
5. Log in with the credentials from `.env`, install the `docassemble-mentalkb` package from this repo, and browse to `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.

## Project Layout (modular map)

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

## Module Responsibilities

- **Runtime stack (`docker-compose.yml`)** – brings up Postgres (seeded via `db-init`), pgAdmin, and Docassemble with `MENTALKB_DB_URL` injected.
- **DB → UI mapping (`loader.py`)** – resolves pages from `pages`, joins layout via `pages_layout`, fetches questions/options, normalizes datatypes/required flags for docassemble widgets.
- **Persistence (`util.py`)** – ensures `public.intake_sessions` exists and inserts a JSON snapshot on interview completion.
- **Interview flow (`data/questions/interview.yml`)** – iterates the KB-provided pages/questions, saves answers, and emits an attachment.
- **Export (`templates/summary.md`)** – minimal Markdown summary (swap for a branded DOCX later without touching the flow).
- **Docs (`docs/`)** – reviewer-friendly setup guide and architecture mapping.

## Contracts & Boundaries

- **Input:** Postgres DB with `pages`, `pages_layout`, `questions`, and `questions_options` tables.
- **Config:** `MENTALKB_DB_URL` (wired through `.env` → docker compose).
- **Outputs:** one row per interview saved to `public.intake_sessions` and a downloadable summary attachment.

## Highlights

- Dynamic interview: pages, questions, and options load live from Postgres.
- One-command bootstrap: `docker compose up -d` brings the full stack online.
- Responses persist to `intake_sessions` and generate a downloadable summary.

## Next Steps

- Extend rules mapping for complex branching or page logic.
- Replace the Markdown summary with branded DOCX/PDF output.
- Harden credentials and add CI checks when moving beyond the PoC.

---

Built for the MentalkB migration feasibility study.
>>>>>>> eec956d (0Dv1.00)
