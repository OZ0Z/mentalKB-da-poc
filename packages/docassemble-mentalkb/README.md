# docassemble-mentalkb

Docassemble package that renders a MentalkB interview using the MentalkB CSV exports.
It bundles the loader, interview driver, and CSV files so the interview runs inside a Docassemble server.

## Installation

1. Push this folder to a GitHub repository (public or private).
2. In Docassemble Package Manager choose **Add from GitHub** and point it at the repo, or upload a wheel/zip built from this package.
3. After installation, open `/interview?i=docassemble.mentalkb:data/questions/interview.yml` to launch the demo driver.
4. To make it the default landing page, add `default interview: docassemble.mentalkb:data/questions/interview.yml` to `config.yml`.

## Data assumptions

- `data/static/public_questions.csv` provides the base question metadata (id, type, text, optional page id).
- Option files (e.g., `public_questions_options_part1.csv`) contain rows with `id`, `question_id` or `qid`, `label`/`text`, and optional `value`.
- Add any extra CSV extracts to `data/static/` and update the loader ordering if needed.

## What ships

- `loader.py` converts the CSVs into `Question` and `Option` objects for use inside Docassemble.
- `interview.yml` is a thin driver that renders the first loaded question and its choices as a proof of concept.
- `MANIFEST.in` ensures the interview YAML and CSVs are packaged.

## Limitations / TODO

- Page ordering is a placeholder: replace the `first_qid` logic with page sequencing from `public_pages.csv` or your layout rules.
- No skip logic or branching yet; extend the driver YAML or loader to encode conditions.
- No automated tests; consider adding lightweight pytest coverage for a couple of representative question/option rows.

## License

MIT (adjust `setup.py` if you need a different license).
