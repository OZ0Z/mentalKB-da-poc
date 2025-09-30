"""Load MentalkB metadata from Postgres for use within docassemble."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Dict, List, Optional

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Row

DB_URL_ENV = "MENTALKB_DB_URL"


def _to_bool(value: Optional[str]) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


@dataclass
class Page:
    id: str
    name: str
    title: str
    header: Optional[str]
    pageset: Optional[str]
    order: int
    next_name: Optional[str]
    previous_name: Optional[str]
    visible: bool
    availability: Optional[str]
    page_type: Optional[str]


@dataclass
class Question:
    id: str
    page_id: Optional[str]
    group: Optional[str]
    field: Optional[str]
    kind: str
    prompt: str
    required: bool
    sort: int
    options_raw: Optional[str] = None


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
        self.pages: Dict[str, Page] = {}
        self._questions_by_page: Dict[str, List[Question]] = {}
        self._options_by_question: Dict[str, List[Option]] = {}
        self.questions_by_id: Dict[str, Question] = {}
        self._load_with_retry()

    def questions_for(self, page_id: Optional[str]) -> List[Question]:
        return self._questions_by_page.get(page_id or "_none", [])

    def options_for(self, question_id: str) -> List[Option]:
        return self._options_by_question.get(question_id, [])

    def has_options(self, question_id: str) -> bool:
        return question_id in self._options_by_question and bool(self._options_by_question[question_id])

    def da_datatype_for(self, kind: str) -> str:
        return TYPE_MAP.get(kind.lower(), "text")

    def get_page_sequence(self, pageset_name: Optional[str]) -> List[Page]:
        if pageset_name:
            return [
                page
                for page in self._pages
                if page.pageset == pageset_name and page.visible
            ]
        return [page for page in self._pages if page.visible]

    def _load_with_retry(self) -> None:
        last_error: Exception | None = None
        for attempt in range(10):
            try:
                self._load()
                return
            except Exception as exc:  # pragma: no cover - defensive
                last_error = exc
                time.sleep(1 + attempt * 0.5)
        raise RuntimeError("Unable to load MentalkB metadata from Postgres") from last_error

    def _fetch(self, sql: str) -> List[Row]:
        with self.engine.connect() as conn:
            return list(conn.execute(text(sql)))

    def _load(self) -> None:
        page_rows = self._fetch(
            """
            SELECT id::text AS id,
                   COALESCE(pagename, '') AS name,
                   COALESCE(page_title, '') AS title,
                   page_header,
                   pageset,
                   COALESCE(page_order, 0) AS order,
                   pagename_next,
                   pagename_previous,
                   page_visible,
                   page_availability,
                   page_type
            FROM pages
            ORDER BY pageset, page_order, id
            """
        )
        self._pages = [
            Page(
                id=row.id,
                name=row.name,
                title=row.title,
                header=row.page_header,
                pageset=row.pageset,
                order=int(row.order or 0),
                next_name=row.pagename_next,
                previous_name=row.pagename_previous,
                visible=_to_bool(row.page_visible) if row.page_visible is not None else True,
                availability=row.page_availability,
                page_type=row.page_type,
            )
            for row in page_rows
        ]
        self.pages = {page.name: page for page in self._pages if page.name}

        questions = self._fetch(
            """
            SELECT id::text AS id,
                   page_id::text AS page_id,
                   question_group,
                   question_field,
                   COALESCE(question_inputtype, 'text') AS kind,
                   COALESCE(question, '') AS prompt,
                   COALESCE(question_required, false) AS required,
                   COALESCE(question_order, 0) AS sort,
                   question_options
            FROM questions
            ORDER BY page_id, sort, id
            """
        )
        self._questions_by_page.clear()
        self.questions_by_id.clear()
        for row in questions:
            question = Question(
                id=row.id,
                page_id=row.page_id,
                group=row.question_group,
                field=row.question_field,
                kind=row.kind,
                prompt=row.prompt,
                required=_to_bool(row.required),
                sort=int(row.sort or 0),
                options_raw=row.question_options,
            )
            key = row.page_id or "_none"
            self._questions_by_page.setdefault(key, []).append(question)
            self.questions_by_id[question.id] = question

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
                sort=int(row.sort or 0),
            )
            self._options_by_question.setdefault(row.question_id, []).append(option)
