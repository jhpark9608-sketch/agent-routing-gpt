# Task 09 — Ontology Induction and Alignment

Category: ontology
Difficulty: hard
Expected routing: Terra → Sol Low or Sol Medium for methodology-critical judgment

## Prompt

Design and implement a candidate ontology-induction and alignment workflow using the repository's sample corpus and existing schema.

Requirements:
- extract recurring candidate concepts and relations
- propose mappings to existing classes/properties
- detect near-duplicates and naming conflicts
- preserve supporting examples/evidence
- assign confidence
- generate a reviewable migration proposal
- do not automatically mutate the production ontology
- separate observed corpus evidence from LLM-proposed interpretation

Add focused tests for duplicate concepts, conflicting mappings, unsupported proposed relations, and clean alignments.

Acceptance:
- Proposed ontology changes are reviewable before application.
- Conflicts are not silently resolved.
- Evidence and confidence are preserved.
