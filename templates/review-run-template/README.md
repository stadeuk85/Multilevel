# Review run template

Copy this folder into an approved private working location for each EHCP review. Do not commit real case material to the public repository.

## Expected artefacts

```text
review-run/
├── STATUS.json
├── 01_intake.json
├── 02_evidence-register.json
├── 02_evidence-register.md
├── 03_items.json
├── 04_golden-thread-map.json
├── 04_golden-thread-map.md
├── 05_evidence-alignment.json
├── 05_evidence-alignment.md
├── 06_findings.json
├── 06_findings.md
├── 07_human-review.json
├── 08_final-review.json
└── 08_final-review.md
```

## Rules

- Keep source documents in an approved secure store, not in this repository.
- Use evidence IDs and minimum necessary quotations.
- Never replace source documents with model summaries.
- Record unresolved matters and human decisions explicitly.
- A missing stage artefact means that stage is incomplete unless `STATUS.json` records it as not applicable with a reason.
