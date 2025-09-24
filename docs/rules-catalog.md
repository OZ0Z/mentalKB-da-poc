# Rules Catalog (traceability)

> Inventory of legacy rules and their Docassemble implementation status. Update as new rules are identified.

| ID      | Kind        | Scope  | Inputs                               | Condition / Description                                                 | Docassemble mapping                                | Status |
|---------|-------------|--------|--------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------|--------|
| VIS-001 | visibility  | field  | hasAllergy                           | Show Anaphylaxis treatment fields only when hasAllergy == true.        | show if: hasAllergy on naphylaxis_treatment.   | ✅ Demo |
| BR-010  | branching   | page   | hasAllergy                           | Navigate to Allergy_Treatment page if allergy confirmed, else general. | code: block sets 
ext_page based on answer.     | ⏳ TODO |
| VAL-020 | validation  | field  | start_date, end_date                 | End date must be on or after start date.                                | alidation_error() check in page code: block.   | ✅ Demo |
| CMP-112 | computed    | field  | first_parent_answer, second_parent_answer | Answers match when both blank or equal (see QuestionAnswers.java). | YAML code: computes nswers_match, raises error. | ✅ Demo |
| REP-040 | repeat      | group  | child[i]                             | Allow multiple child entries with per-child validation.                 | Docassemble repeat syntax child[i].*.            | ⏳ TODO |
| DYN-050 | options     | field  | prior selections                     | Filter option list based on earlier answers.                            | Python helper ilter_options() feeding choices. | ⏳ TODO |

_Status legend: ✅ Demo (implemented in PoC), ⏳ TODO (identified, implementation pending)._ 
