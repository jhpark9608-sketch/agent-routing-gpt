# Task 08 — Provenance and Claim Verification

Category: verification
Difficulty: hard
Expected routing: Terra → Sol Low; Sol Medium only for unresolved high-impact design questions

## Prompt

Add claim-level provenance and verification to answer generation.

Requirements:
- Decompose the final answer into factual claims.
- Map each claim to one or more source spans or graph paths.
- Mark unsupported claims as unsupported.
- Detect evidence that contradicts a claim.
- Produce a machine-readable verification object.
- Preserve human-readable citations/provenance.
- Add tests for supported, partially supported, contradictory, and unsupported claims.

Acceptance:
- A factual claim cannot be labeled grounded without evidence.
- Graph-derived evidence includes the path or relation chain.
- Verification output is machine-readable and testable.
