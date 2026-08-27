# Benchmark Guide

This benchmark is designed to test the central hypothesis of agent-routing-gpt:

> Expensive reasoning should be used only after cheaper agents have narrowed the problem.

The benchmark compares a single-agent Sol Medium baseline with the routing policy in this repository.

## 1. Conditions

### A — Baseline

Use GPT-5.6 Sol with Medium reasoning as the primary agent for the whole task.

Do not use the agent-routing-gpt routing files for this condition.

### B — Routing

Use this repository's routing configuration:

~~~text
Luna Max → Terra High → Sol Low → Sol Medium
~~~

The exact task prompt must be identical between A and B.

## 2. Why credits matter in addition to raw tokens

A routed run may use more raw tokens while still using fewer credits because the tokens are distributed across cheaper models.

Therefore report both:

- raw token usage
- credit usage
- task quality

The intended headline metric is **credit reduction at matched task quality**, not token reduction alone.

## 3. Usage capture

For each run, record:

- start and end time
- uncached input tokens
- cached input tokens
- output tokens
- credits
- wall-clock time
- Sol calls
- task success
- tests passed / total

Where available, use ChatGPT Desktop / Codex **Usage & billing** history because per-chat usage may not include every subagent or separately executed task.

Reference:
https://help.openai.com/en/articles/20001478

Allow usage reporting to refresh before recording the final value.

## 4. Experimental controls

Use the following controls for every task:

1. Same target repository.
2. Same starting commit.
3. Same prompt text.
4. Fresh session for every run.
5. Same permissions / sandbox policy.
6. Same test command.
7. Alternate A/B execution order.
8. Record cached and uncached input separately.
9. Prefer 3 repetitions or more.
10. Do not manually rescue one condition unless you apply the same rescue rule to both.

A simple counterbalanced order is:

~~~text
replicate 1: A → B
replicate 2: B → A
replicate 3: A → B
~~~

For even-numbered tasks, reverse the initial order.

## 5. Quality gates

A cheaper run is not a win if correctness falls.

Primary quality metrics:

- Task Success Rate
- Test Pass Rate

Secondary metrics:

- review acceptance
- number of unnecessary file edits
- regressions introduced
- unsupported assumptions

A benchmark result should only be described as a cost improvement if quality is equal or within a pre-declared acceptable margin.

## 6. Current experimental theme

The 10 included tasks use LLM + Ontology + Knowledge Graph engineering because the domain naturally mixes:

- cheap repository exploration
- structured extraction
- schema / ontology constraints
- multi-hop graph reasoning
- hybrid retrieval
- query planning
- agentic retrieval loops
- provenance and claim verification
- open-world entity resolution
- evaluation design

These are useful stressors for routing because some tasks should remain on Luna/Terra while others can legitimately trigger Sol.

Relevant current directions include Agentic RAG, GraphRAG, ontology-enhanced GraphRAG, graph-native agents, structured outputs, and tool-driven workflows.

Selected references:

- Microsoft GraphRAG: https://www.microsoft.com/en-us/research/project/graphrag/
- Agentic RAG survey, revised 2026: https://doi.org/10.48550/arXiv.2501.09136
- Agentic GraphRAG survey (2026): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6713979
- Ontology-enhanced GraphRAG (2026): https://doi.org/10.1007/978-3-032-29003-8_25
- Open-world KG-RAG multi-agent framework, WWW 2026: https://doi.org/10.1145/3774904.3792389
- OpenAI model guidance: https://developers.openai.com/api/docs/guides/latest-model

## 7. Running the benchmark

Choose a target codebase and freeze a start commit.

For each task:

1. Reset the target repository.
2. Run the Baseline condition.
3. Record results.
4. Reset again.
5. Run the Routing condition.
6. Record results.
7. Repeat according to the counterbalanced order.

Example reset:

~~~bash
git reset --hard <START_COMMIT>
git clean -fd
~~~

Use this only in a disposable benchmark checkout because it deletes uncommitted work.

## 8. Record results

Fill benchmarks/results.csv.

The template already includes 10 tasks × 2 conditions × 3 replicates.

Then generate the report:

~~~bash
python benchmarks/compare_results.py benchmarks/results.csv \
  --output benchmarks/BENCHMARK_RESULTS.md
~~~

## 9. Interpreting results

A strong result looks like:

- lower average credits
- equal or better task success
- equal or better test pass rate
- lower Sol-call rate
- no meaningful regression in runtime

Do not publish a percentage reduction until all planned paired runs are complete.
