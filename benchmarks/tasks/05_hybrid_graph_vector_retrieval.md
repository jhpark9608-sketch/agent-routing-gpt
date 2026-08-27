# Task 05 — Hybrid Graph + Vector Retrieval

Category: retrieval
Difficulty: medium
Expected routing: Terra

## Prompt

Implement or improve a hybrid retriever that combines semantic/vector retrieval with graph-neighborhood evidence.

Requirements:
- Normalize component scores before fusion.
- Make fusion weights configurable.
- Preserve the individual vector and graph score contributions.
- Deduplicate equivalent evidence.
- Provide deterministic fallback when graph evidence is unavailable.
- Do not silently favor one retrieval source because its raw score range is larger.
- Add tests where vector-only misses useful graph evidence, graph-only misses semantically relevant evidence, and hybrid retrieval recovers both.

Acceptance:
- Score fusion is inspectable.
- Duplicate evidence is removed.
- Fallback works.
- Targeted tests and existing tests pass.
