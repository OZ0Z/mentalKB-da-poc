# Migration Strategy: Java Rules → Docassemble YAML

**Goal**

Provide a repeatable approach to migrate MentalkB decision logic from the legacy Java application into Docassemble while keeping the database as the system of record for content.

---

## 1. Inputs reviewed

- **Postgres dump**: tables pages, pages_layout, questions, questions_options supply structure, prompts, option text, and ordering.
- **Java code**: UI controllers and helper classes encode visibility, routing, validation, computed fields, and list handling.

We treat **DB tables as content** and **Java code as rule definitions**.

---

## 2. Rule taxonomy (expected in Java)

1. **Visibility / gating** – show or hide pages/fields based on answers or flags.
2. **Branching / navigation** – next/previous page logic not expressible via simple ordering.
3. **Validation** – required-when conditions, format enforcement, and cross-field checks.
4. **Derived values** – compute age, totals, or derived booleans for later pages.
5. **Repeats / instances** – collections such as children, medications, agreements.
6. **Dynamic options** – option lists filtered by earlier answers or lookup tables.
7. **Localization** – swap label/phrases for ES/PT variants.

---

## 3. Translation patterns (Java → Docassemble)

| Rule type        | Java pattern                                      | Docassemble pattern |
|------------------|----------------------------------------------------|---------------------|
| Visibility       | if (hasAllergy) show("AnaphylaxisTreatment")    | show if: hasAllergy on the field |
| Branching        | if (hasAllergy) return Allergy_Treatment         | code: block setting 
ext_page |
| Validation       | if (end.before(start)) addError(field, msg)      | alidation_error("msg") inside code: |
| Computed         | ge = Period.between(dob, now)                   | code: compute ge variable |
| Repeatables      | loops over children[i]                           | Docassemble list syntax child[i].name |
| Dynamic options  | filter via Java service                            | Python helper ilter_options() returning list |
| Localization     | getLabelEs() / getLabelPt()                    | select alternate DB columns or phrase tables |

We keep YAML thin: data stays in Postgres, minimal code: blocks express rules, and reusable helpers go into ules.py (future).

---

## 4. Extraction workflow

1. **Locate rule sites** in Java
   - Grep/decompile for keywords: page, question_group, setVisible, 
ext, alidate, error, ddChild, etc.
2. **Catalog** each finding in docs/rules-catalog.md with: rule id, kind, scope, inputs, condition, Java location.
3. **Translate** using the table above; add references (# RULE: VIS-001) in YAML for traceability.
4. **Verify** behaviour via targeted scenarios (see runbook) and CI smoke tests.

---

## 5. Target architecture after migration

- **Database** continues to store page/question metadata and option text.
- **Docassemble YAML** orchestrates flow, referencing the DB loader for content.
- **Python helpers** encapsulate reusable predicates (e.g., is_minor(age)), keeping rules diff-able and testable.

This separation lets business users edit CSV/DB extracts while engineers maintain a compact rule library.

---

## 6. Example mapping

Legacy snippet (QuestionAnswers.java):

`java
public boolean isMatch() {
    if (match == null) {
        match = Boolean.valueOf(
            (!firstParentAnswer.isAnswered() && !secondParentAnswer.isAnswered())
            || firstParentAnswer.equalsOtherAnswer(secondParentAnswer)
        );
    }
    return match.booleanValue();
}
`

Docassemble implementation:

`yaml
code: |
  both_blank = not defined('first_parent_answer') and not defined('second_parent_answer')
  equal_answers = defined('first_parent_answer') and defined('second_parent_answer') and first_parent_answer == second_parent_answer
  answers_match = both_blank or equal_answers

  if not answers_match:
      validation_error("Both parent answers must match (or both be blank).")
`

Rule entry: CMP-112 in ules-catalog.md with references to the Java file and YAML line.

---

## 7. Outputs tracked

- Updated YAML with rule annotations (# RULE: …).
- docs/rules-catalog.md for traceability.
- CI smoke tests (pytest) to ensure loader contracts remain intact.
