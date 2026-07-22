# Agent cold-start map

## Purpose

This repository contains a critique-only editor for draft Education, Health and Care Plans in England. Its primary review surface is the relationship between:

- Section B special educational needs;
- Section E outcomes;
- Section F special educational provision;
- supplied professional advice and recommendations.

## Read order

1. `SKILL.md`
2. `workflows/01_ehcp-golden-thread-review/CONTEXT.md`
3. the active stage contract
4. only the references named by that stage
5. `reference/output-schema.md`
6. `reference/output-schema.json` for structured output

## Authoritative files

- Identity and scope: `identity.md`
- Editorial constraints: `rules.md`
- Worked standard: `examples.md`
- Legal source order: `reference/source-hierarchy.md`
- Current authority summary: `reference/legal-authorities.md`
- Privacy and safety: `reference/privacy-and-safety.md`
- EHCP section map: `reference/ehcp-sections.md`
- B, E and F review criteria: `reference/section-*.md`
- Evidence comparison: `reference/evidence-alignment-checklist.md`
- Golden-thread mapping: `reference/golden-thread-checklist.md`
- Output contract: `reference/output-schema.md` and `.json`

## Stop conditions

Stop and state the limitation when:

- the document stage is unknown and materially affects the review;
- the plan text needed for the requested scope is absent;
- referenced professional evidence has not been supplied;
- a conflict cannot be resolved from the documents;
- personal data cannot be handled in an approved environment;
- the user asks the editor to make an entitlement, placement or legal remedy decision;
- the user asks for invented or replacement wording contrary to the editor remit.

## Completion standard

A review is complete only when:

- each material finding quotes the exact draft passage;
- evidence-based findings quote the relevant evidence;
- B, E and F items have stable IDs;
- link strength and uncertainty are explicit;
- the highest-impact findings appear first;
- no missing facts or provision have been invented;
- the final output follows the published contract;
- a human review status is recorded.
