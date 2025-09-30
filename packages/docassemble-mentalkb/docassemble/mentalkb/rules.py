"""Rule helpers for MentalkB docassemble package."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from .loader import KB, Page, Question, Option


KEYWORDS = {
    "visibility": ["setvisible", " visible", "show(", "hide("],
    "branching": ["next", "previous", "navigate", "route", "switch", "case "],
    "validation": ["required", "validate", "validation", "error", "adderror", "pattern.compile", "matches("],
    "computed": ["equals", "compareto", "isafter", "isbefore", "age", "difference"],
    "options": ["options", "choices", "list", "lookup", "filter"],
}


def classify(snippet: str, current: str) -> str:
    if current and current != "unknown":
        return current
    s = snippet.lower()
    for kind, tokens in KEYWORDS.items():
        if any(token in s for token in tokens):
            return kind
    return "unknown"


def _filter_options(question: Question, options: Iterable[Option], answers: Dict[str, object]) -> List[List[str]]:
    option_pairs: List[List[str]] = []
    selected_agreements = answers.get("selected_agreements")
    for opt in options:
        if selected_agreements and "agreement" in (question.prompt or "").lower():
            if opt.value and opt.value not in selected_agreements:
                continue
        option_pairs.append([opt.label, opt.value or opt.label])
    return option_pairs


def build_fields(kb: KB, questions: Iterable[Question], answers: Dict[str, object]) -> List[Dict[str, object]]:
    fields: List[Dict[str, object]] = []
    for q in questions:
        field: Dict[str, object] = {
            "label": q.prompt,
            "field": f"q_{q.id}",
            "required": bool(q.required),
            "datatype": kb.da_datatype_for(q.kind),
        }
        if kb.has_options(q.id):
            field["choices"] = _filter_options(q, kb.options_for(q.id), answers)
        visibility = visibility_expression(q)
        if visibility:
            field["show if"] = visibility
        fields.append(field)
    return fields


def visibility_expression(question: Question) -> Optional[str]:
    prompt = (question.prompt or "").lower()
    if "parent" in prompt and "has" not in prompt:
        return "has_parental_rights"
    return None


def resolve_next_page(kb: KB, pageset_name: Optional[str], current_page: Page, visited: List[str]) -> Optional[Page]:
    if current_page.next_name:
        candidate = kb.pages.get(current_page.next_name)
        if candidate and candidate.visible and candidate.name not in visited:
            return candidate
    sequence = kb.get_page_sequence(pageset_name)
    try:
        idx = next(i for i, page in enumerate(sequence) if page.name == current_page.name)
    except StopIteration:
        idx = -1
    for page in sequence[idx + 1 :]:
        if page.visible and page.name not in visited:
            return page
    return None

