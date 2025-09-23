# docassemble-mentalkb

Docassemble package that renders MentalkB interview flows directly from the database seeded in this PoC.

## What it does

- `loader.py` reads `pages`, `pages_layout`, `questions`, and `questions_options` via SQLAlchemy.
- `data/questions/interview.yml` renders a page-by-page wizard, deferring control metadata to the DB.
- `util.py` persists each interview run into `public.intake_sessions` as JSON.
- `templates/summary.md` produces the downloadable summary (swap for DOCX when ready).

## Expected environment

Set `MENTALKB_DB_URL` inside the Docassemble runtime. The provided Docker Compose file injects it automatically.

## Developer map

```
docassemble-mentalkb/
├─ setup.py / MANIFEST.in        # packaging metadata and bundled assets
├─ tests/                        # loader smoke tests
└─ docassemble/mentalkb/
   ├─ __init__.py                # exports KB and save_session_results
   ├─ loader.py                  # DB → Question/Option/Page objects
   ├─ util.py                    # save_session_results hook
   ├─ data/questions/interview.yml  # primary interview driver
   └─ templates/summary.md       # export template
```

Adjust the SQL queries in `loader.py` if your schema names differ.
