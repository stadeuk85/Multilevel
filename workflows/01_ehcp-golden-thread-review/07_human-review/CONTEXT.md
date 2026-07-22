# Stage 07: human review

## Job

Require a human to review the evidence trail, priorities and limitations before release.

## Inputs

- all completed analytical stage outputs;
- draft final response.

## Review questions

- Are the quoted passages exact and correctly located?
- Are the three priorities genuinely the highest-impact concerns?
- Is every evidence-based statement supported by supplied material?
- Are authority types accurately distinguished?
- Are conflicts and limitations visible?
- Has the editor avoided replacement wording and invented facts?
- Is personal information minimised?
- Does any issue require specialist legal or professional review?

## Output

Write `07_human-review.json` containing reviewer role, review date, decision, required corrections, unresolved matters and release status.

Allowed decisions:

- `approved_for_editorial_use`;
- `return_for_correction`;
- `specialist_review_required`;
- `do_not_use`.

## Completion gate

Only `approved_for_editorial_use` permits Stage 08. Approval does not convert the output into legal advice or an entitlement decision.
