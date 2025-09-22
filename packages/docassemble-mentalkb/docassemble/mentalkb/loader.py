# docassemble/mentalkb/loader.py
import csv
from importlib import resources
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Option:
    id: str
    question_id: str
    label: str
    value: str | None = None

@dataclass
class Question:
    id: str
    kind: str
    prompt: str
    page_id: str | None = None

class KB:
    def __init__(self):
        self.questions: Dict[str, Question] = {}
        self.options_by_qid: Dict[str, List[Option]] = {}
        self._load()

    def _read_csv(self, fname: str):
        with resources.files("docassemble.mentalkb.data.static").joinpath(fname).open("r", encoding="utf-8") as f:
            yield from csv.DictReader(f)

    def _load(self):
        for row in self._read_csv("public_questions.csv"):
            self.questions[row["id"]] = Question(
                id=row["id"],
                kind=row.get("type", "text").strip() or "text",
                prompt=row.get("question", "").strip(),
                page_id=row.get("page_id") or None
            )

        option_files = [
            "public_questions_options_part1.csv",
            "public_questions_options_part2.csv",
            "public_questions_options_interact.csv",
            "public_questions_options_auto.csv",
        ]
        for of in option_files:
            try:
                for row in self._read_csv(of):
                    qid = row.get("question_id") or row.get("qid") or ""
                    opt = Option(
                        id=row.get("id") or "",
                        question_id=qid,
                        label=(row.get("label") or row.get("text") or "").strip(),
                        value=row.get("value") or None
                    )
                    self.options_by_qid.setdefault(qid, []).append(opt)
            except FileNotFoundError:
                pass

    def get_question(self, qid: str) -> Question | None:
        return self.questions.get(qid)

    def get_options(self, qid: str) -> List[Option]:
        return self.options_by_qid.get(qid, [])
