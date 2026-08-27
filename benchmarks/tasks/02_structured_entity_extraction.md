# Task 02 — Structured Entity and Relation Extraction

Category: implementation
Difficulty: medium
Expected routing: Terra, with Luna for discovery if useful

## Prompt

Implement structured entity/relation extraction in the target repository's ingestion pipeline.

Required output fields:
- canonical_entity_id
- surface_form
- entity_type
- relation_type
- source_document_id
- evidence_span
- confidence

Requirements:
- Use the repository's existing validation/model conventions.
- Invalid or incomplete extraction records must fail validation or be explicitly rejected.
- Do not silently coerce unknown entity/relation types into valid ones.
- Preserve behavior outside the extraction path.
- Add focused tests for valid extraction, missing required field, invalid type, and malformed relation.
- Keep changes minimal and explain any schema migration.

Acceptance:
- New tests pass.
- Existing tests pass.
- Invalid records cannot silently enter the graph.
- Source/evidence information survives extraction.
