# Task 06 — Query Router and Multi-Step Planner

Category: agentic RAG
Difficulty: hard
Expected routing: Terra → Sol Low if planning logic is genuinely ambiguous

## Prompt

Add a query router that selects among:
- local semantic retrieval
- local graph traversal
- global/community retrieval
- multi-hop planning

Before executing retrieval, emit a structured plan containing:
- selected strategy
- subqueries
- expected evidence type
- stopping condition
- maximum retrieval steps

Requirements:
- Keep routing auditable.
- Use deterministic routing rules where sufficient; do not invoke an LLM for trivial cases.
- The planner must not execute an unbounded number of tool calls.
- Add tests for direct factual, relational, global/theme, and multi-hop queries.

Acceptance:
- Every execution has an inspectable plan.
- Step bounds are enforced.
- Tests verify strategy selection.
