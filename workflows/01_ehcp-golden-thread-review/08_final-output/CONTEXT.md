# Stage 08: final output

## Job

Produce the approved human-readable review and optional machine-readable response.

## Inputs

- approved human-review record;
- findings;
- golden-thread map;
- evidence-alignment audit;
- limitations and strengths.

## Load

- `reference/output-schema.md`
- `reference/output-schema.json`

## Actions

1. Assemble the review in the published order.
2. Preserve exact quotations and stable IDs.
3. Include material limitations and evidence gaps.
4. Include specific strengths worth preserving.
5. Complete the self-check.
6. Validate structured output against the JSON Schema.

## Outputs

- `08_final-review.md`
- `08_final-review.json`, where structured output is required
- completed `STATUS.json`

## Completion gate

The human decision is approved, the structured output validates, the critique-only boundary is intact and all limitations remain visible.
