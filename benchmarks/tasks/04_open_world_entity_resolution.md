# Task 04 — Open-World Entity Resolution

Category: reasoning + implementation
Difficulty: medium
Expected routing: Terra; Sol Low only if ambiguity remains after evidence gathering

## Prompt

Improve entity resolution for aliases, ambiguous names, and entities not already present in the knowledge graph.

Use a staged strategy:
1. canonical/exact match
2. alias match
3. candidate ranking
4. unresolved/open-world fallback

Requirements:
- Never fabricate an existing graph id.
- Return resolution status, selected id if any, confidence, candidate evidence, and reason.
- Handle collisions where two graph entities share a surface form.
- Preserve unresolved entities for later review instead of dropping them.
- Add tests for exact match, alias match, ambiguous collision, unseen entity, and low-confidence candidate.

Acceptance:
- Unseen entities cannot be falsely linked as known.
- Ambiguous cases are explicit.
- Tests cover both successful and unresolved resolution.
