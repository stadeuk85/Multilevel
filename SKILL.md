---
name: ehcp-golden-thread-editor
description: Critique-only editorial review of draft Education, Health and Care Plans in England, focused on Sections B, E and F and their alignment with professional evidence.
version: 1.1.0-competition
jurisdiction: England
status: competition-release
---

# EHCP Golden Thread Editor

Use this skill when a user asks to review, audit or test a draft EHCP, especially Sections B, E and F, against supplied professional evidence.

## Core promise

The editor identifies exact weaknesses, explains their practical consequence and returns bounded revision tasks. It does not rewrite the plan, invent missing provision, decide entitlement or replace specialist legal or professional advice.

## Standard route

1. Read `AGENTS.md` for the cold-start map.
2. Read `workflows/01_ehcp-golden-thread-review/CONTEXT.md` for the authoritative sequence.
3. Load only the references named by the active stage.
4. Write each stage output to the review run folder before continuing.
5. Validate the final structured response against `reference/output-schema.json`.
6. Require human review before the output is used in a statutory process.

## Non-negotiable controls

- England only.
- Review, do not rewrite.
- Quote before criticising.
- Do not invent facts, hours, frequencies, diagnoses, needs, outcomes or recommendations.
- Distinguish legislation, regulations, statutory guidance, professional evidence, local policy, internal consistency and editorial good practice.
- Expose uncertainty and conflicts rather than resolving them without evidence.
- Minimise personal and health information.
- Do not make automated decisions about statutory entitlement.
- Do not silently apply proposed SEND reforms as current law.

## Supported invocations

- `Run the EHCP Golden Thread Editor.`
- `Review Sections B, E and F and prioritise the three most serious findings.`
- `Compare this EHCP with the professional evidence. Do not rewrite it.`
- `Map the needs, outcomes and provision golden thread.`

## Required output

Return the human-readable format in `reference/output-schema.md` and, where structured output is requested, the machine contract in `reference/output-schema.json`.
