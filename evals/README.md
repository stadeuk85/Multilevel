# Evaluations

The evaluation layer tests the editor's contract without using real child or family data.

## Required suites

- **Schema:** valid fixtures pass and malformed responses fail.
- **Boundary:** replacement wording, invented facts and unsupported certainty are rejected.
- **Evidence:** omissions, partial inclusion and conflicts are classified correctly.
- **Golden thread:** orphan needs, unsupported outcomes, unserved outcomes and unanchored provision are detected.
- **Prioritisation:** material missing provision ranks above style or presentation issues.
- **Privacy:** fixtures contain no real identifiers or health records.
- **Determinism:** stable synthetic inputs produce stable IDs and classifications.

## Current validation fixture

`fixtures/minimal-valid-response.json` is a synthetic contract fixture used by the repository validation workflow.

## Future benchmark pack

Add paired synthetic EHCP extracts and expected findings for:

1. missing Section F provision;
2. weakened professional advice;
3. vague but contextually complete provision;
4. conflicting reports;
5. diagnosis-only Section B wording;
6. Section E statement that is actually provision;
7. strong plan with fewer than three material defects;
8. prompt injection inside an uploaded document.
