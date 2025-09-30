# MentalkB Docassemble PoC

**Proof-of-concept:** migrating MentalkB wizard flows from Catalyst into [docassemble](https://docassemble.org/).

_For the detailed walkthrough with screenshots, see [docs/setup-guide.md](docs/setup-guide.md)._ 

## Quick Start

1. Copy `.env.example` to `.env` and customize secrets if needed.
2. Place the sanitized MentalkB dump at `db-init/001_mentalkb.sql` (optional bootstrap table runs from `000_bootstrap_intake_sessions.sql`).
3. Start the stack with `docker compose up -d` or simply run `make up`.
4. Wait for containers to report healthy, then open <http://localhost:8080>.
5. Log in with the credentials from `.env`, install the `docassemble-mentalkb` package from this repo, and browse to `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.

## Project Layout

```
mentalkb-da-poc/
├── docker-compose.yml            # Stack: Docassemble + Postgres + pgAdmin
├── .env.example                  # Copy to .env; carries credentials + DB URL
├── db-init/
│   ├── 000_bootstrap_intake_sessions.sql
│   └── 001_mentalkb.sql          # Sanitized dump (not committed)
├── packages/docassemble-mentalkb/
│   ├── docassemble/mentalkb/
│   │   ├── loader.py             # SQLAlchemy loader for pages/questions/options
│   │   ├── rules.py              # Branching/visibility helpers (BR-010, VIS-001)
│   │   ├── util.py               # `save_session_results` DB hook
│   │   ├── data/questions/interview.yml  # Driver using the rule helper
│   │   └── templates/summary.md
│   ├── tests/                    # pytest smoke + rule tests
│   ├── setup.py / MANIFEST.in
│   └── README.md
├── docs/
│   ├── setup-guide.md            # How to run + screenshots
│   ├── architecture.md           # DB mapping & extension points
│   ├── migration-strategy.md     # Java → Docassemble playbook
│   ├── rules-catalog.md          # Traceability table (manual curation)
│   ├── rules-digest.md           # Auto-generated summary from the miner
│   ├── limitations.md            # Known gaps / risks
│   └── runbook.md                # Operational commands
├── tools/rule-miner/             # Java rule extraction + summary scripts
├── .github/workflows/smoke.yml   # CI seeding + loader smoke tests
└── Makefile                      # up/down/logs/psql/smoke helpers
```

## Documentation

- Migration strategy: [docs/migration-strategy.md](docs/migration-strategy.md)
- Rules catalog & traceability: [docs/rules-catalog.md](docs/rules-catalog.md)
- Rule miner digest: [docs/rules-digest.md](docs/rules-digest.md)
- Runbook: [docs/runbook.md](docs/runbook.md)
- Limitations & risks: [docs/limitations.md](docs/limitations.md)

## Highlights

- Dynamic interview pulls content straight from Postgres (records answers to `intake_sessions`).
- YAML driver now uses helper rules for page branching and field visibility.
- Rule miner scripts inventory Java rule sites and produce a digest for planning.
- `make smoke` / CI run a minimal Postgres seed + pytest to keep the loader/rules wired up.

## Next Steps

- Wire remaining branching/validation cases from the catalog into `rules.py` / YAML.
- Replace the Markdown summary with branded DOCX/PDF output.
- Broaden CI (e.g., Postgres 12 matrix, additional rule tests) and harden credentials for production.

Built for the MentalkB migration feasibility study.
