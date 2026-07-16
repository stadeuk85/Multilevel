# EHCP Golden Thread Editor

## What this editor does

This editor reviews a draft Education, Health and Care Plan under the framework for England. It concentrates on whether:

- Section B captures the special educational needs shown in the supplied evidence;
- Section E contains meaningful outcomes linked to those needs and the child or young person's aspirations;
- Section F specifies provision for every identified Section B need;
- professional recommendations have been included accurately or any departure is visible;
- the plan forms a coherent needs-to-outcomes-to-provision golden thread.

It identifies weaknesses and returns revision tasks. It does not write the corrected plan for you.

## Files in this editor

- `identity.md` defines who the editor is and its scope.
- `rules.md` defines the critique method and non-rewriting boundary.
- `examples.md` shows the required standard of feedback.
- `reference/` contains checklists, source hierarchy and the output contract.

## What to provide

Minimum:

- the draft EHCP text or document;
- the document stage, such as draft plan, amended draft, final plan under review or annual-review working copy.

Recommended:

- professional reports and advice used to prepare the plan;
- the date and author or discipline of each report;
- the user's review priority;
- the child or young person's age or phase, where relevant and safe to share.

Remove names, addresses, dates of birth, NHS numbers, school identifiers and other unnecessary personal information unless using an approved secure environment.

## Standard invocation

```text
Review this draft EHCP in editor mode.

Jurisdiction: England
Document stage: [draft / amended draft / annual review working copy]
Priority:
1. Evidence omitted from Section B
2. Weak or unmeasurable Section E outcomes
3. Section F provision that is vague, unquantified or weaker than the professional recommendations

Return the three most important findings first.
Quote the exact wording.
Explain the defect and its consequence.
Give me a revision task, not replacement wording.
State where the evidence is insufficient.
```

## Focused invocations

### Evidence audit

```text
Compare this draft EHCP against the supplied professional reports. Identify each material recommendation as included, partially included, omitted, contradicted or unclear. Quote both the report and the plan. Do not draft missing provision.
```

### Golden-thread review

```text
Map every Section B need to relevant Section E outcomes and Section F provision. Identify orphan needs, unsupported outcomes and provision without a stated need. Do not create missing links or wording.
```

### Section F specificity review

```text
Review Section F for missing type, frequency, duration, staffing, expertise, group size, delivery method, review mechanism or responsible party. Quote the exact phrase and ask the author to recover the missing detail from the evidence. Do not propose figures.
```

## Expected output

The editor follows `reference/output-schema.md`. It starts with three priority findings, then gives golden-thread breaks, evidence requiring clarification and strengths worth preserving.

## Limits

- Editorial support is not legal advice.
- A phrase is not automatically defective merely because it appears on a warning list. Context and evidence determine the finding.
- The editor cannot resolve conflicts in professional evidence. It exposes the conflict and asks for a human decision or further advice.
- The editor must not treat proposed SEND reforms as current law.
