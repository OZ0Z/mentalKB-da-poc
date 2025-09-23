"""Load MentalkB metadata from Postgres for use within docassemble."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Dict, List, Optional

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Row

DB_URL_ENV = "MENTALKB_DB_URL"


@dataclass
class Page:
    id: str
    title: str
    sort: int


@dataclass
class Question:
    id: str
    page_id: Optional[str]
    kind: str
    prompt: str
    required: bool
    sort: int


@dataclass
class Option:
    id: str
    question_id: str
    label: str
    value: Optional[str]
    sort: int


TYPE_MAP = {
    "text": "text",
    "textarea": "area",
    "integer": "number",
    "number": "number",
    "date": "date",
    "radio": "radio",
    "single_select": "radio",
    "select": "dropdown",
    "checkbox": "yesno",
    "multi_select": "checkboxes",
    "multiselect": "checkboxes",
}


class KB:
    """Read-only MentalkB knowledge base accessor."""

    def __init__(self, engine: Optional[Engine] = None):
        url = os.environ.get(DB_URL_ENV)
        if not url:
            raise RuntimeError(f"Environment variable {DB_URL_ENV} must be set for docassemble-mentalkb")
        self.engine: Engine = engine or create_engine(url, pool_pre_ping=True)
        self._pages: List[Page] = []
        self._questions_by_page: Dict[str, List[Question]] = {}
        self._options_by_question: Dict[str, List[Option]] = {}
        self._load_with_retry()

    # Public API ---------------------------------------------------------
    def pages(self) -> List[Page]:
        return self._pages

    def questions_for(self, page_id: Optional[str]) -> List[Question]:
        return self._questions_by_page.get(page_id or "_none", [])

    def options_for(self, question_id: str) -> List[Option]:
        return self._options_by_question.get(question_id, [])

    def has_options(self, question_id: str) -> bool:
        return bool(self.options_for(question_id))

    def da_datatype_for(self, kind: str) -> str:
        key = (kind or "").strip().lower()
        return TYPE_MAP.get(key, "text")

    # Internal helpers ---------------------------------------------------
    def _load_with_retry(self) -> None:
        last_error: Optional[Exception] = None
        for attempt in range(10):
            try:
                self._load()
                return
            except Exception as exc:  # pragma: no cover - defensive logging
                last_error = exc
                time.sleep(1 + attempt * 0.5)
        raise RuntimeError("Unable to load MentalkB metadata from Postgres") from last_error

    def _fetch(self, sql: str) -> List[Row]:
        with self.engine.connect() as conn:
            return list(conn.execute(text(sql)))

    def _load(self) -> None:
        self._pages = [
            Page(row.id, row.title, row.sort)
            for row in self._fetch(
                """
                SELECT id::text AS id,
                       COALESCE(title, '') AS title,
                       COALESCE(sort, 0) AS sort
                FROM pages
                ORDER BY sort, id
                """
            )
        ]

        questions = self._fetch(
            """
            SELECT id::text AS id,
                   page_id::text AS page_id,
                   COALESCE(type, 'text') AS kind,
                   COALESCE(question, '') AS prompt,
                   COALESCE(required, false) AS required,
                   COALESCE(sort, 0) AS sort
            FROM questions
            ORDER BY page_id, sort, id
            """
        )
        self._questions_by_page.clear()
        for row in questions:
            question = Question(
                id=row.id,
                page_id=row.page_id,
                kind=row.kind,
                prompt=row.prompt,
                required=bool(row.required),
                sort=row.sort,
            )
            key = row.page_id or "_none"
            self._questions_by_page.setdefault(key, []).append(question)

        options = self._fetch(
            """
            SELECT id::text AS id,
                   question_id::text AS question_id,
                   COALESCE(label, '') AS label,
                   value,
                   COALESCE(sort, 0) AS sort
            FROM options
            ORDER BY question_id, sort, id
            """
        )
        self._options_by_question.clear()
        for row in options:
            option = Option(
                id=row.id,
                question_id=row.question_id,
                label=row.label,
                value=row.value,
                sort=row.sort,
            )
            self._options_by_question.setdefault(row.question_id, []).append(option)
