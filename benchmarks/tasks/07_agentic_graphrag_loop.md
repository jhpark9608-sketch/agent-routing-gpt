# Task 07 — Bounded Agentic GraphRAG Loop

Category: agentic RAG
Difficulty: hard
Expected routing: Terra → Sol Low

## Prompt

Implement a bounded retrieve → inspect evidence → reformulate → retrieve loop.

The agent may continue only when evidence is insufficient or contradictory.

Requirements:
- hard maximum step count
- explicit early-stop criteria
- trace of each retrieval decision
- detection of repeated or semantically equivalent queries
- no infinite loops
- no extra retrieval when evidence is already sufficient
- tests for early-stop, one-retry, contradictory-evidence, repeated-query prevention, and max-step termination

Acceptance:
- All loops terminate.
- Trace explains why another retrieval was or was not performed.
- Existing retrieval behavior remains available for non-agentic paths.
