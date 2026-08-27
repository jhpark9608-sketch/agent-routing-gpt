# Task 03 — Ontology Validation

Category: implementation
Difficulty: medium
Expected routing: Terra

## Prompt

Add an ontology validation layer for extracted knowledge-graph triples.

Validate:
- allowed entity classes
- allowed relation types
- relation domain
- relation range
- cardinality constraints when represented by the existing ontology

Return one of:
- valid
- repairable
- rejected

For non-valid results preserve a machine-readable reason.

Requirements:
- Unknown classes/relations must not be treated as valid by default.
- Do not automatically mutate the production ontology.
- Keep the validator independently testable.
- Add tests for valid, invalid-domain, invalid-range, unknown-class, unknown-relation, and repairable cases.

Acceptance:
- Validator is deterministic for the same inputs.
- Reasons are inspectable.
- Existing ingestion behavior is preserved except where invalid triples are now classified.
