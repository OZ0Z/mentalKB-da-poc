# Runbook

## Golden path smoke
1. make up
2. make smoke
3. Browse to <http://localhost:8080>, install package from GitHub, and open /interview?i=docassemble.mentalkb:data/questions/interview.yml.
4. Complete first section, download summary attachment.
5. make psql → SELECT * FROM intake_sessions ORDER BY id DESC LIMIT 5;.

## Reset environment
`ash
make reseed
`
(Stops containers, drops volumes, reseeds Postgres from db-init/.)

## CI failure triage
1. If smoke.yml fails seeding, inspect dump for new tables/privileges.
2. If loader tests fail, verify schema changes and update loader.py plus tests.
3. Re-run locally with MENTALKB_DB_URL=postgresql+psycopg2://mentalkb:mentalkb@localhost:5432/mentalkb pytest -q inside packages/docassemble-mentalkb.

## Rule mining refresh
`ash
cd tools/rule-miner
./mine.sh ../../legacy/java > sample-output/rules.csv
`
Review the CSV, update docs/rules-catalog.md, and commit artifact changes.

## Legacy Java sources
- Clone or symlink the Catalyst Java repo into `legacy/java/` (ignored by git).
  - Example symlink (PowerShell): `New-Item -ItemType SymbolicLink -Path legacy/java -Target "C:\\Users\\nerdy\\IdeaProjects\\CATALYST\\nlighen-master"`
  - Or `git clone https://.../nlighen-master.git legacy/java`
- Run `tools/rule-miner/mine.sh ../../legacy/java > tools/rule-miner/sample-output/rules.csv` to refresh the catalog.
- Commit only the generated CSV/notes; the legacy repo stays untracked.

