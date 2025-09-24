# Setup Guide
 >  **Goal**: be running an interview and see a saved row in *intake_sessions* in ~2 minutes.

## Prerequisites
- Docker & Docker Compose
- Sanitized MentalkB SQL dump (place at `db-init/001_mentalkb.sql`)

## 1. Configure environment
```bash
cp .env.example .env
# edit the file to adjust passwords if required
```

## 2. Start the stack
```bash
docker compose up -d
```
The first boot seeds Postgres using `db-init/001_mentalkb.sql`. To reseed, run `docker compose down -v` before starting again.
###### *After **docker compose up -d**, watch readiness if you want*:
> 1) docker compose logs -f postgres | sed -n '/database system is ready to accept connections/p'
> 2) docker compose logs -f docassemble | sed -n '/Starting web server/p'


## 3. Access services
- Docassemble: http://localhost:8080 (login with `DA_ADMIN_EMAIL` / `DA_ADMIN_PASSWORD`)
- pgAdmin: http://localhost:5050 (use `PGADMIN_EMAIL` / `PGADMIN_PASSWORD`)
  - Register a server with host `postgres`, port `5432`, and the MentalkB credentials from `.env`.

## 4. Install the package
Inside Docassemble:
1. Package Management → Add a package → from GitHub → paste this repo URL.
2. After installation, open `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.
3. Walk through the pages; on completion, an entry is written to `intake_sessions` and a summary attachment downloads(can and will soon be DocX template)

> 📸 Drop screenshots in `docs/img/` (e.g., `first-page.png`, `intake-sessions.png`) so reviewers can see both the rendered interview and the database row.

## 5. Verify database writes
In pgAdmin (or `docker compose exec mentalkb-postgres psql`):
```sql
SELECT id, created_at, user_email, data
FROM intake_sessions
ORDER BY id DESC
LIMIT 5;

SELECT id, created_at, user_email, jsonb_pretty(data) AS data
FROM intake_sessions
ORDER BY id DESC
LIMIT 5;

```
You should see the answers JSON recorded for the session.

## Troubleshooting
- Reseed Postgres: `docker compose down -v && docker compose up -d`
- Shell access: `docker compose exec -it mentalkb-postgres psql -U $MENTALKB_USER -d $MENTALKB_DB`
- Docassemble logs: `docker compose logs -f docassemble`
