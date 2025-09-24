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

## Project Layout

```
mentalkb-da-poc/
├── docker-compose.yml            # Stack: Postgres (+seed), pgAdmin, Docassemble
├── .env.example                  # Copy to .env; credentials & MENTALKB_DB_URL
├── db-init/
│   ├── 000_bootstrap_intake_sessions.sql
│   └── 001_mentalkb.sql          # Seed dump (runs once on first boot)
├── packages/
│   └── docassemble-mentalkb/
│       ├── setup.py              # Python package metadata + deps
│       ├── MANIFEST.in           # Bundle YAML/templates in the wheel/zip
│       ├── README.md             # Package-level notes
│       ├── tests/                # Loader smoke tests (pytest)
│       └── docassemble/mentalkb/
│           ├── __init__.py
│           ├── loader.py         # Reads pages/layout/questions/options from DB
│           ├── util.py           # Writes interview snapshot to intake_sessions
│           ├── data/questions/interview.yml
│           └── templates/summary.md
├── docs/
│   ├── setup-guide.md            # How to run + screenshots
│   ├── architecture.md           # DB mapping & extension points
│   ├── migration-strategy.md     # Java → Docassemble playbook
│   ├── rules-catalog.md          # Traceability table of legacy rules
│   ├── limitations.md            # Known gaps and risks
│   └── runbook.md                # Operational steps
├── tools/rule-miner/             # Java rule extraction helpers
├── .github/workflows/smoke.yml   # CI seeding + loader smoke
└── Makefile                      # up/down/logs/psql/smoke helpers
```

## Module Responsibilities

- **Runtime stack (`docker-compose.yml`)** – brings up Postgres (seeded via `db-init`), pgAdmin, and Docassemble with `MENTALKB_DB_URL` injected.
- **DB → UI mapping (`loader.py`)** – resolves pages from `pages`, joins layout via `pages_layout`, fetches questions/options, normalizes datatypes/required flags for Docassemble widgets.
- **Persistence (`util.py`)** – ensures `public.intake_sessions` exists and inserts a JSON snapshot on interview completion.
- **Interview flow (`data/questions/interview.yml`)** – iterates KB-provided pages/questions, saves answers, and emits an attachment.
- **Export (`templates/summary.md`)** – minimal Markdown summary (swap for DOCX later without touching flow).
- **Rule mining (`tools/rule-miner/`)** – inventories legacy Java rule sites so we can map them to YAML patterns.

## Documentation

- Migration strategy: [docs/migration-strategy.md](docs/migration-strategy.md)
- Rules catalog & traceability: [docs/rules-catalog.md](docs/rules-catalog.md)
- Limitations & risks: [docs/limitations.md](docs/limitations.md)
- Operational runbook: [docs/runbook.md](docs/runbook.md)

## Contracts & Boundaries

- **Input:** Postgres DB with `pages`, `pages_layout`, `questions`, and `questions_options` tables.
- **Config:** `MENTALKB_DB_URL` (wired through `.env` → docker compose environment).
- **Outputs:** One row per interview saved to `public.intake_sessions` plus a downloadable summary attachment.

## Highlights

- Dynamic interview: pages, questions, and options load live from Postgres.
- One-command bootstrap: `docker compose up -d` brings the full stack online.
- Responses persist to `intake_sessions` and generate a downloadable summary.
- CI smoke (`.github/workflows/smoke.yml`) seeds the DB and runs loader tests on every push.

## Next Steps

- Extend rules mapping for complex branching or page logic (see rules catalog).
- Replace the Markdown summary with branded DOCX/PDF output.
- Harden credentials, add PG 12 compatibility checks, and increase rule coverage in CI.

---

Built for the MentalkB migration feasibility study.
>>>>>>> eec956d (0Dv1.00)
