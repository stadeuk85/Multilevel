# Stage 02: evidence register

## Job

Create a traceable register of the professional evidence supplied for the review.

## Inputs

- completed `01_intake.json`;
- supplied professional reports and advice.

## Load

- `reference/evidence-alignment-checklist.md`
- `reference/source-hierarchy.md`

## Actions

For each source, record:

- evidence ID;
- author or discipline;
- date;
- document type;
- relevant findings;
- distinct needs;
- distinct recommendations;
- intended effects or outcomes;
- limitations, uncertainty and conflicts.

Preserve exact quotations and source locations for material recommendations.

## Output

Write `02_evidence-register.json` and a human-readable `02_evidence-register.md`.

## Completion gate

Every supplied report has an evidence ID. Missing or referenced-but-unsupplied documents are listed. Conflicts are exposed, not resolved.
