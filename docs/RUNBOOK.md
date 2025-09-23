# 🧯 Runbook

## Health checks
- Containers: `docker compose ps`
- Tail logs: `docker compose logs -f postgres` and `docker compose logs -f docassemble`
- DB ping: `psql "host=localhost port=5432 user=mentalkb dbname=mentalkb" -c "select 1"`

## Quick smoke (60–90s)
1) Open the interview, answer one page, finish.  
2) Verify writeback:
```sql
SELECT id, created_at, left(data::text, 200)
FROM public.intake_sessions
ORDER BY id DESC LIMIT 1;

````



## Common failures → fixes

**Docassemble cannot connect to DB**

**Symptom**: interview errors on load

**Fix**: confirm MENTALKB_DB_URL uses host postgres (Docker service name), and creds match .env

---

**No pages render**

**Symptom**: blank/empty interview

**Fix**: check page visibility flags (page_visible, pageset_visible); ensure pages_layout rows exist for the current pagename

---

**Restore/dump mismatch**

**Symptom**: Postgres init warnings or odd types

**Fix**: pin Postgres image (e.g., postgres:12) or re-dump/transform the SQL

---

## Useful commands

Bring up fresh: docker compose down -v && docker compose up -d

Connect inside the PG container: docker compose exec postgres psql -U mentalkb -d mentalkb

DB healthcheck (container): pg_isready -U mentalkb -d mentalkb -h localhost



