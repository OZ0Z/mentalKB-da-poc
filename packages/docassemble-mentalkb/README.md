# docassemble-mentalkb

Docassemble package that renders MentalkB interview flows directly from the MentalkB Postgres database.

## Features
- Loads pages, questions, and options via SQLAlchemy.
- Supports page-by-page wizard rendering inside docassemble.
- Persists responses to `intake_sessions` using a docassemble completion hook.
- Generates a Markdown summary attachment (swap for DOCX/PDF as needed).

## Installation
1. Ensure the MentalkB database is running (see repository root README).
2. In Docassemble, open **Package Management → Add a package → from GitHub** and provide this repository URL, or upload a built archive containing this package directory.
3. Launch the interview at `/interview?i=docassemble.mentalkb:data/questions/interview.yml`.

## Configuration
The package expects an environment variable `MENTALKB_DB_URL` inside the Docassemble runtime. The provided Docker Compose file/container sets this automatically.

## Development tips
- Update `loader.py` SQL statements if the underlying schema differs.
- Extend `util.save_session_results` to write to domain-specific tables.
- To rerun the loader locally, export `MENTALKB_DB_URL` and run `python -m docassemble.mentalkb.loader` for a quick smoke test.
