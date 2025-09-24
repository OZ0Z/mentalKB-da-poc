# Limitations & Architectural Considerations

1. **Legacy Java rules still under discovery**  
   The database captures structure but not all visibility/routing logic. We rely on the rule-miner inventory plus manual review to expose gaps. *Mitigation:* commit mined CSVs, expand docs/rules-catalog.md, and prioritize rule parity per page set.

2. **Postgres version drift**  
   The dump originated from PG 9.6; we currently run on PG 15. Minor type differences can surface. *Mitigation:* CI seeds on PG 15; add a PG 12 matrix job for legacy compatibility.

3. **Option linkage nuances**  
   Some extracts reference (question_group, question_field) instead of question_id. Loader already falls back, but cross-references should be monitored. *Mitigation:* add tests covering both shapes.

4. **Complex navigation paths**  
   Legacy may override next/previous dynamically (e.g., skip pages). Our base flow sorts by page_order. *Mitigation:* capture explicit routing rules in docs/rules-catalog.md and implement outing.py helpers when needed.

5. **Repeatable subforms**  
   While Docassemble supports repeats, nested validation/branching requires custom code: sections. *Mitigation:* provide reusable helpers and unit tests for representative repeats (children, medications, agreements).

6. **Localization strategy**  
   ES/PT labels exist in the dump. Docassemble needs a toggle strategy (language-specific phrase files or alternate DB columns). *Mitigation:* record locale rules, add YAML switches, and include in future sprint scope.

7. **Security / PII in dumps**  
   Ensure the SQL dump used for development is sanitized. *Mitigation:* document sanitization expectations in docs/setup-guide.md and provide tooling to mask PII before seeding.
