# EHCP golden-thread review workflow

## Objective

Produce a traceable, critique-only review of a draft EHCP in England, focused on Sections B, E and F and their relationship to supplied professional evidence.

## Required inputs

- draft EHCP or relevant complete sections;
- document stage;
- requested review scope;
- supplied professional reports and advice, where evidence comparison is requested;
- safe handling context for personal data.

## Ordered stages

1. `01_intake-and-safety`
2. `02_evidence-register`
3. `03_section-extraction`
4. `04_golden-thread-mapping`
5. `05_evidence-alignment`
6. `06_priority-findings`
7. `07_human-review`
8. `08_final-output`

Do not skip a stage silently. Where a stage is not applicable, record `not_applicable` and the reason in the run status.

## Run folder

Copy `templates/review-run-template/` for each review. Keep source documents outside the public repository. Record only the minimum extracts and metadata required for traceability.

## Global controls

- No rewriting or invented detail.
- Exact quotations and stable locations.
- One principal defect per finding.
- Evidence and authority types remain distinguishable.
- Conflicts remain visible until a human resolves them.
- Human approval is mandatory before statutory use.

## Completion gate

The workflow is complete only when every stage status is recorded, the final output validates against the response schema, limitations are visible and the human-review record is complete.
