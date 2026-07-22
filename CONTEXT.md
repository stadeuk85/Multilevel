# Repository context

## One repository, one job

This repository defines a governed editorial workflow for reviewing draft EHCPs in England. It separates stable editorial knowledge from case-specific working artefacts.

## Workspace map

| Area | Job |
|---|---|
| `workflows/` | Authoritative review sequence and stage contracts |
| `reference/` | Stable legal, editorial and evidence-review guidance |
| `templates/` | Blank case-run structures copied for each review |
| `evals/` | Synthetic fixtures and contract tests |
| `demo/` | Public, non-case-specific demonstration |
| `_release/` | Manifest, validation evidence and release notes |

## Active workflow

Use `workflows/01_ehcp-golden-thread-review/CONTEXT.md`.

## Architecture boundary

The reusable repository must not contain real EHCPs, identifiable child information or mutable production case records. A live review should be instantiated from `templates/review-run-template/` in an approved private environment.

## State model

The workflow state is represented by completed stage artefacts in the copied review-run folder. A later reviewer should be able to identify what has been completed, what remains unresolved and what human decision is required without reconstructing hidden model reasoning.

## Release boundary

The public release demonstrates method, governance, structured output and workflow design. It is not a statutory decision system, legal service or production personal-data platform.
