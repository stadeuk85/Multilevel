# Stage 03: section extraction

## Job

Extract stable, reviewable items from the EHCP without changing the wording.

## Inputs

- completed intake;
- draft EHCP text;
- evidence register, where available.

## Load

- `reference/section-b-needs-checklist.md`
- `reference/section-e-outcomes-checklist.md`
- `reference/section-f-provision-checklist.md`
- `reference/ehcp-sections.md`

## Actions

1. Assign `B-##` to each distinct Section B need.
2. Assign `E-##` to each distinct Section E outcome.
3. Assign `F-##` to each distinct Section F provision.
4. Assign `A-##` to aspirations used in outcome mapping where relevant.
5. Preserve exact text and page, paragraph, table row or other stable location.
6. Separate bundled items only for analysis. Do not rewrite them.

## Output

Write `03_items.json` containing stable IDs, exact quotations, locations and item types.

## Completion gate

Every in-scope B, E and F passage has been accounted for, or an extraction limitation is recorded.
