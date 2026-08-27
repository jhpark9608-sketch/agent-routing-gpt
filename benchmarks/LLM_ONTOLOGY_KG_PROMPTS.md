# LLM + Ontology + Knowledge Graph Experiment Prompts

These prompts are designed for Codex A/B testing with the same starting repository and the same prompt under two conditions:

- Baseline: Sol Medium
- Routing: agent-routing-gpt

They also reflect active 2025–2026 directions in LLM systems: Agentic RAG, GraphRAG, ontology-grounded retrieval, open-world entity resolution, structured outputs, tool use, provenance, and graph-native multi-agent reasoning.

## Prompt 1 — Architecture analysis: Agentic GraphRAG

> Inspect the target repository and identify the full path from user query to retrieval to graph reasoning to answer generation. Produce a concise architecture map. Do not modify code. Identify which components are deterministic, which invoke an LLM, which use graph traversal, and where provenance is lost. Limit exploration to files needed to establish the execution path.

Purpose: tests whether cheap discovery can be delegated without spending Sol on broad repository exploration.

## Prompt 2 — Structured entity and relation extraction

> Implement structured entity/relation extraction for the ingestion pipeline. The output schema must include canonical entity id, surface form, entity type, relation type, source document id, evidence span, and confidence. Invalid or incomplete records must fail validation rather than silently entering the graph. Add focused tests and preserve existing behavior outside the extraction path.

Purpose: structured outputs + reliable KG construction.

## Prompt 3 — Ontology-grounded triple validation

> Add an ontology validation layer that checks extracted triples against allowed classes, relation types, domain/range constraints, and cardinality rules where available. Do not automatically delete invalid triples: classify them as valid, repairable, or rejected and preserve the reason. Add tests for valid, invalid-domain, invalid-range, unknown-class, and unknown-relation cases.

Purpose: ontology as an explicit semantic constraint instead of relying only on LLM judgment.

## Prompt 4 — Open-world entity resolution

> Improve entity linking so the system can handle aliases, ambiguous names, and entities that do not yet exist in the graph. Use a staged strategy: exact/canonical match, alias match, candidate ranking, then unresolved/open-world fallback. Never fabricate an existing graph id. Return confidence and evidence for the chosen resolution. Add tests for collisions and unseen entities.

Purpose: open-world KG-RAG and robust entity linking.

## Prompt 5 — Hybrid vector + graph retrieval

> Implement a hybrid retriever that combines semantic/vector candidates with graph-neighborhood evidence. Normalize scores before fusion, expose the contribution of each retrieval source, and avoid returning duplicate evidence. Include a deterministic fallback when graph evidence is unavailable. Add tests showing cases where vector-only and graph-only retrieval each miss useful evidence but hybrid retrieval succeeds.

Purpose: hybrid RAG / GraphRAG retrieval.

## Prompt 6 — Query router and multi-step planner

> Add a query router that chooses among local semantic retrieval, local graph traversal, global/community retrieval, and multi-hop planning. The router must emit a structured plan before executing tools. Plans must include selected strategy, subqueries, stopping condition, and expected evidence type. Add tests for at least four query patterns and keep the plan auditable.

Purpose: agentic retrieval planning + tool calling.

## Prompt 7 — Bounded Agentic GraphRAG loop

> Implement a bounded retrieve → inspect evidence → reformulate → retrieve loop. The agent may continue only when evidence is insufficient or contradictory. Add a hard step limit, explicit stopping criteria, and a trace of each retrieval decision. Prevent infinite loops and avoid repeating semantically identical queries. Add tests for early-stop, one-retry, and max-step cases.

Purpose: Agentic RAG with bounded autonomy rather than uncontrolled loops.

## Prompt 8 — Provenance and claim verification

> Add claim-level provenance to generated answers. Each factual claim must map to at least one source span or graph path. Unsupported claims must be marked unsupported rather than presented as grounded. Add a verification pass that checks claim/evidence consistency and produces a machine-readable result. Include tests for supported, partially supported, contradictory, and unsupported claims.

Purpose: hallucination control, provenance, and verifiable multi-step workflows.

## Prompt 9 — Ontology induction and alignment

> Given the repository's sample corpus and current schema, design and implement a candidate ontology-induction pipeline. Extract recurring concepts and relations, propose class/property mappings to the existing ontology, detect naming conflicts and near-duplicates, and output a reviewable migration proposal. Do not mutate the production ontology automatically. Include confidence, supporting examples, and conflict reasons.

Purpose: LLM-assisted ontology construction while retaining human review.

## Prompt 10 — End-to-end evaluation

> Build an evaluation harness for the ontology-aware GraphRAG pipeline. Measure retrieval recall, graph-path validity, ontology-constraint violations, answer faithfulness/provenance coverage, latency, and model/token usage where available. Separate retrieval failures from reasoning failures. Produce a machine-readable results file and a concise Markdown report. Do not hard-code expected answers into the evaluator.

Purpose: measures whether the system is actually better rather than merely more complex.

---

## Suggested research/design prompt

For a higher-level architecture experiment:

> Design an ontology-aware Agentic GraphRAG system for a domain corpus. Use a hybrid vector + graph retriever, structured entity/relation extraction, explicit ontology constraints, open-world entity resolution, a bounded query-planning agent, and claim-level provenance. First identify which components should be deterministic and which genuinely need an LLM. Then propose the smallest viable architecture, failure modes, evaluation plan, and ablation study. Avoid adding agents when a deterministic component is sufficient.

## Suggested ablation prompt

> Design an ablation study that isolates the value of (1) vector retrieval, (2) graph retrieval, (3) ontology constraints, (4) agentic query planning, and (5) claim verification. Define datasets, metrics, controls, expected failure modes, and statistical reporting. The experiment must distinguish retrieval quality from generation quality and must record token/credit cost per condition.

## Suggested ontology-vs-no-ontology prompt

> Compare two GraphRAG pipelines that are identical except that one uses an explicit ontology for entity types, relation constraints, and validation. Define hypotheses, implementation differences, evaluation metrics, and error categories. Pay particular attention to invalid triples, entity-type drift, relation ambiguity, multi-hop answer correctness, and retrieval coverage.
