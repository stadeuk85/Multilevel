# Stage 05: evidence alignment

## Job

Compare each material professional recommendation with the draft EHCP.

## Inputs

- evidence register;
- extracted B, E and F items;
- golden-thread map.

## Load

- `reference/evidence-alignment-checklist.md`
- `reference/source-hierarchy.md`
- relevant B, E or F checklist.

## Actions

For every material recommendation:

1. quote the recommendation and source location;
2. identify corresponding draft text;
3. compare each material delivery or outcome element;
4. classify treatment as included, partially included, omitted, contradicted or unclear;
5. explain the practical consequence;
6. return a human revision, clarification or decision task.

## Output

Write `05_evidence-alignment.json` and `.md`.

## Completion gate

Every material recommendation is classified or the audit is explicitly marked incomplete because evidence is absent or conflicting.
