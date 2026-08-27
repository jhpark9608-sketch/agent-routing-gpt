# Task 01 — Codebase Map

Category: discovery
Difficulty: easy
Expected routing: Luna → Terra

## Prompt

Inspect the target repository and identify the complete execution path for a user question through ingestion/retrieval/graph reasoning/answer generation.

Do not modify any files.

Requirements:
- Find only the files needed to establish the path.
- Identify entry points, major classes/functions, and data passed between stages.
- Mark which stages are deterministic, which invoke an LLM, and which access a graph/vector index.
- Identify where source provenance enters and where it can be lost.
- Return a concise architecture map plus the minimum set of relevant files.
- Do not perform repository-wide summarization unrelated to this path.

Acceptance:
- No code changes.
- Execution path is traceable from entry point to final answer.
- Findings cite exact file/function names.
- Output distinguishes retrieval, graph, LLM, and provenance stages.
