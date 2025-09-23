# 🚀 MentalkB Docassemble PoC
> **Proof-of-concept:** migrating MentalkB wizard flows from Catalyst into [docassemble](https://docassemble.org/).

_For the detailed walkthrough with screenshots, see [docs/setup-guide.md](docs/setup-guide.md)._ 

# ⚡ ## Quick Start

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
