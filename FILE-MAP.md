# File map

This map lets a new reviewer locate the active workflow and its supporting material without searching the whole repository.

## ICM context layers

| Layer | Repository surface | Purpose |
|---|---|---|
| ICM-L0 | `SKILL.md`, `AGENTS.md` | Trigger, identity, controls and cold-start catalogue |
| ICM-L1 | root `CONTEXT.md` | Workspace router and architecture boundary |
| ICM-L2 | `workflows/**/CONTEXT.md` | Workflow and stage contracts |
| ICM-L3 | `identity.md`, `rules.md`, `examples.md`, `reference/` | Stable editorial and authority factory |
| ICM-L4 | copied `templates/review-run-template/` | Case-specific working artefacts and human decisions |

## Root entry files

- `README.md`: public explanation and competition entry page.
- `SKILL.md`: compact skill trigger and route.
- `AGENTS.md`: cold-start navigation and stop conditions.
- `CONTEXT.md`: repository workspace contract.
- `FILE-MAP.md`: this inventory.

## Original competition editor

- `identity.md`: who the EHCP editor is and what it reviews.
- `rules.md`: authoritative critique method and non-rewriting boundary.
- `examples.md`: the quality bar for useful feedback.
- `reference/`: checklists, source hierarchy, safety and output contracts.
- `README.md`: setup and use.

## Governed workflow

`workflows/01_ehcp-golden-thread-review/`

1. `01_intake-and-safety/`
2. `02_evidence-register/`
3. `03_section-extraction/`
4. `04_golden-thread-mapping/`
5. `05_evidence-alignment/`
6. `06_priority-findings/`
7. `07_human-review/`
8. `08_final-output/`

Each folder contains one `CONTEXT.md` stage contract.

## Stable references

- `reference/source-hierarchy.md`
- `reference/authority-register.json`
- `reference/legal-authorities.md`
- `reference/privacy-and-safety.md`
- `reference/ehcp-sections.md`
- `reference/section-b-needs-checklist.md`
- `reference/section-e-outcomes-checklist.md`
- `reference/section-f-provision-checklist.md`
- `reference/golden-thread-checklist.md`
- `reference/evidence-alignment-checklist.md`
- `reference/output-schema.md`
- `reference/output-schema.json`

## Assurance and public demonstration

- `evals/`: synthetic fixtures and evaluation plan.
- `tools/validate_repo.py`: structural and schema validator.
- `.github/workflows/validate.yml`: automated validation.
- `demo/`: public synthetic demonstration only.
- `_release/current/`: manifest, release notes and validation evidence.

## Runtime boundary

Do not store real EHCPs or identifiable case material in this repository. Copy the review-run template into an approved private environment and keep source documents in an approved secure store.
