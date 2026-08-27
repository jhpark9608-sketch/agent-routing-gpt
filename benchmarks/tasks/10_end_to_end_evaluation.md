# Task 10 — End-to-End Evaluation Harness

Category: evaluation
Difficulty: hard
Expected routing: Terra; Sol may review metric validity if needed

## Prompt

Build an evaluation harness for the ontology-aware GraphRAG pipeline.

Measure separately:
- retrieval recall
- graph-path validity
- ontology-constraint violations
- answer faithfulness / provenance coverage
- latency
- token/model usage where exposed by the system

Requirements:
- distinguish retrieval failure from reasoning/generation failure
- output machine-readable run results
- generate a concise Markdown summary
- do not hard-code benchmark answers into the evaluator
- make metric definitions explicit
- add tests for metric calculations

Acceptance:
- evaluator can compare at least two system configurations
- metrics are reproducible from saved run artifacts
- failures are categorized rather than collapsed into one score
