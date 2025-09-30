# Rules Catalog (traceability)

> Inventory of legacy rules and their Docassemble implementation status. Update as new rules are identified.
> See `docs/rules-digest.md` for auto-generated counts from the latest miner run.

| ID      | Kind        | Source (file:line)                                                                    | Scope  | Description                                                                                          | Docassemble mapping                                       | Status |
|---------|-------------|----------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------|
| VIS-001 | visibility  | legacy/java/src/main/java/com/incap/service/UserDataService.java:312                  | field  | Hide parental contact fields unless `hasParentalRights == true`.                                     | `show if: has_parental_rights` for related fields.        | ✅ Demo |
| BR-010  | branching   | legacy/java/src/main/java/com/incap/engine/EasyEngine.java:155                        | page   | Determine `nextPageName` using `lastPageSeen.getNextPageName()` with fallback to `findAdjacentPage`. | YAML `code:` sets `next_page` via helper `routing.next()`. | ⏳ TODO |
| BR-020  | branching   | legacy/java/src/main/java/com/incap/webapp/struts/action/ReportByAgreementAction.java:210 | page   | Redirect to summary page when report has no agreements.                                             | Add `if not agreements: next_page = 'ReportSummary'`.     | ⏳ TODO |
| VAL-020 | validation  | legacy/java/src/main/java/com/incap/webapp/struts/action/ParentingLongShortActionSub.java:118 | field  | Enforce that parenting plan start date precedes end date.                                           | `validation_error` in page `code:` comparing dates.       | ✅ Demo |
| CMP-112 | computed    | legacy/java/src/main/java/com/incap/model/report/comparison/QuestionAnswers.java:14   | field  | `AnswersMatch` when both blank or equal.                                                             | YAML `code:` computes `answers_match`, raises error.      | ✅ Demo |
| REP-040 | repeat      | legacy/java/src/main/java/com/incap/webapp/viewbean/ReportDataViewBean.java:162       | group  | Iterate over child agreements when building report tables.                                           | Use Docassemble list iteration (`agreements[i]`).         | ⏳ TODO |
| DYN-050 | options     | legacy/java/src/main/java/com/incap/service/MetadataService.java:245                  | field  | Filter option list by page/field metadata at runtime.                                                | Python helper `filter_options(page, field, answers)`.     | ⏳ TODO |

_Status legend: ✅ Demo (implemented in PoC), ⏳ TODO (identified, implementation pending)._ 
