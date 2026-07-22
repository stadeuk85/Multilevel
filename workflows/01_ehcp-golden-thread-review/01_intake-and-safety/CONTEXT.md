# Stage 01: intake and safety

## Job

Confirm the review can proceed safely and define its boundaries.

## Inputs

- requested task;
- draft EHCP or relevant sections;
- document stage;
- evidence pack metadata;
- privacy and handling context.

## Load

- `identity.md`
- `rules.md`
- `reference/privacy-and-safety.md`
- `reference/ehcp-sections.md`

## Actions

1. Confirm England jurisdiction.
2. Record document stage and review scope.
3. Inventory supplied documents without reproducing unnecessary identifiers.
4. Flag missing sections, missing reports or unsafe data handling.
5. Record whether evidence comparison is complete, partial or unavailable.

## Output

Write `01_intake.json` containing jurisdiction, document stage, scope, supplied evidence IDs, limitations, privacy status and stage status.

## Completion gate

Proceed only when the requested plan text is available, material limitations are recorded and the handling context is acceptable. Otherwise stop with a clear limitation.
