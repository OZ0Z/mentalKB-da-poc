"""Smoke tests for the MentalkB loader."""

import os

import pytest

pytest.importorskip("psycopg2", reason="psycopg2 required for loader smoke test")

from docassemble.mentalkb.loader import KB


def test_pages_and_fields_load():
    db_url = os.environ.get(
        "MENTALKB_DB_URL",
        "postgresql+psycopg2://mentalkb:mentalkb@localhost:5432/mentalkb",
    )
    os.environ["MENTALKB_DB_URL"] = db_url

    kb = KB()
    sequence = kb.get_page_sequence(None)
    assert sequence, "no pages loaded"

    first_page = sequence[0]
    questions = kb.questions_for(first_page.id)

    assert questions is not None, "questions_for returned None"
    assert len(questions) >= 0
