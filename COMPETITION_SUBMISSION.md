# Weekly Comp 9 submission

## Recommended 2 to 3 sentence submission

The EHCP Golden Thread Editor is a specialist critique-only editor for parents reviewing draft Education, Health and Care Plans in England. It reviews Sections B, E and F, traces needs to outcomes and provision, compares the draft with professional evidence, and points to the exact wording that is unclear, unsupported or materially weakened. It does not rewrite the plan; it explains the defect, why it matters and the focused question or revision task the human author must resolve.

Repository: https://github.com/stadeuk85/EHCP-Golden-Thread-Editor

## Personal introduction

This was built from personal experience as a parent. My son has special needs, and like many families we were expected to understand and review a complex statutory document without specialist support. I wanted an editor that helps families see what has been written, what the professional evidence says and where the connection between need, outcome and provision may have broken, without pretending to replace the parent, professional or legal adviser.

## What changed after the competition began

The original five-part editor remains intact:

- `identity.md`
- `rules.md`
- `examples.md`
- `reference/`
- `README.md`

The later ICM Architect skill was then used to add filesystem orchestration around that editor: compact entry routing, folder contracts, eight numbered review stages, explicit hand-off artefacts, a copied private case-run template, a human release gate, schema validation and release evidence. These additions do not change the editor remit; they make the method easier to inspect, resume, test and govern.
