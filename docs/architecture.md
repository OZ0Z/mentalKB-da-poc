# Architecture Notes

## Data sources
- **pages**: defines section titles and ordering (`id`, `title`, `sort`).
- **questions**: mapped to docassemble fields (`id`, `page_id`, `type`, `question`, `required`, `sort`).
- **options**: response choices for radio/checkbox style controls (`id`, `question_id`, `label`, `value`, `sort`).

Adjust the SQL in `loader.py` if the actual dump uses different table or column names.

## Flow
1. `loader.KB` connects via `MENTALKB_DB_URL` and caches page/question/option metadata.
2. The interview YAML iterates through pages in sort order and renders each question with the correct docassemble datatype and options.
3. On completion, `util.save_session_results` persists a JSON snapshot to `intake_sessions` (auto-created when missing).
4. A Markdown attachment (`templates/summary.md`) summarizes answers; swap for DOCX/PDF as needed.

## Extension points
- Implement branching by evaluating stored rule expressions before rendering questions.
- Populate additional exports (DOCX, PDF) using docassemble templates.
- Replace Markdown summary with official document templates.
- Integrate authentication by deriving `user_email` from docassemble user sessions.

## Limitations
- Assumes flat page order; no conditional jumps implemented yet.
- Loader performs read-only queries; ensure DB user has appropriate permissions.
- Seeding relies on docker volume reset; provide migration scripts for production.
