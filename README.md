# MentalkB Docassemble PoC

Proof-of-concept environment that demonstrates migrating MentalkB wizard flows from Catalyst into docassemble.

## Quick start

1. Copy `.env.example` to `.env` and customize secrets if desired.
2. Place the sanitized MentalkB dump at `db-init/001_mentalkb.sql`.
3. Run `docker compose up -d` (or `make up` if you use the optional Makefile).
4. Wait for the containers to become healthy, then open http://localhost:8080.
5. Log in with the credentials from `.env`, install the `docassemble-mentalkb` package from this repo, and run `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.

See `docs/setup-guide.md` for screenshots and the detailed walkthrough.

## Project layout

- `docker-compose.yml` – docassemble + Postgres + pgAdmin stack.
- `db-init/` – bootstrap SQL executed when Postgres starts the first time.
- `packages/docassemble-mentalkb/` – docassemble package with loader, YAML, and export template.
- `docs/` – setup instructions and architecture notes.

## Status

- Dynamic interview pulls pages/questions/options from Postgres.
- Responses persist to `intake_sessions` via docassemble hook.
- Generates a simple Markdown summary attachment (swap for DOCX as needed).

## Next steps

- Extend rules mapping for complex branching.
- Replace the summary template with branded DOCX/PDF output.
- Harden credentials and add CI checks when moving past the PoC stage.
