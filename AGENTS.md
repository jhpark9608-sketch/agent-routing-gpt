# Agent Routing Policy

Optimize for correctness while minimizing unnecessary Sol usage.

## Default
- Use `terra_high` for normal engineering, implementation, integration, debugging, and testing.
- Use `luna_max` for bounded search, discovery, repetitive edits, log extraction, boilerplate, and simple tests.
- Use Sol only after the problem has been narrowed.
- Large task size alone is not a reason to use Sol.

## Escalation
Prefer:

`luna_max` → `terra_high` → `sol_low` → `sol_medium`

Escalate Luna → Terra when requirements are ambiguous, components interact, or correctness needs engineering judgment.

Escalate Terra → Sol Low only when a diagnosis fails verification, evidence is contradictory, multiple credible root causes remain, or deeper reasoning is materially useful.

Escalate Sol Low → Sol Medium only when the issue remains unresolved or the decision is architecture-critical, research-critical, or otherwise high-impact.

## Sol Token Firewall
Before spawning any Sol agent, prepare a compact evidence packet:
1. exact question
2. observed behavior
3. expected behavior
4. minimum relevant files/symbols
5. minimal log/error excerpt
6. tests already performed
7. current hypotheses

Do not ask Sol to rediscover the whole repository when Luna/Terra can gather the evidence more cheaply.

## Ownership
- Luna: discovery and mechanical work
- Terra: implementation, integration, and testing
- Sol: difficult reasoning and review

After Sol returns a diagnosis, hand routine implementation back to Terra whenever practical.

## Parallelism
- Parallelize only independent tasks.
- Prefer cheap read-heavy parallel work over multiple expensive reasoning agents.
- Avoid simultaneous edits to overlapping files.
- Do not spawn multiple Sol agents for the same problem unless an independent high-impact review is justified.
- Return concise summaries rather than large raw outputs.

## Research-critical work
Keep these separate:
- implementation correctness
- data correctness
- methodological validity
- scientific interpretation

Successful execution alone is not evidence of scientific validity.
