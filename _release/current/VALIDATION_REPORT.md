# EHCP Golden Thread Editor v1.1 Competition Validation

**Release date:** 22 July 2026  
**Release branch:** `competition-icm-v1.1`  
**Release type:** ICM architecture and competition presentation hardening

## Decision

**Candidate for competition submission, subject to the GitHub Actions validation workflow passing and final human review.**

This decision approves the public methodology package for demonstration. It does not approve production handling of identifiable EHCP material, automated statutory decisions or legal advice.

## Competition rubric alignment

| Judging question | Evidence in the repository |
|---|---|
| Does it critique rather than rewrite? | `rules.md` prohibits replacement text and `examples.md` contrasts critique with rewriting. |
| Is the domain specific? | `identity.md` limits the editor to draft EHCPs in England, especially Sections B, E and F. |
| Is the methodology clean? | The original five-part editor remains intact. ICM entry files, workflow folders and stage contracts add inspectable orchestration. |
| Can a stranger use it? | `README.md`, `SKILL.md`, `AGENTS.md`, the file map and the synthetic demo provide multiple clear entry points. |

## ICM architecture checks

- Root entry catalogue present.
- Workspace context router present.
- Eight numbered stage contracts present.
- Stable references separated from workflow sequence.
- Blank case-run template present.
- Case state represented by explicit stage artefacts.
- Public demonstration separated from the authoritative editor.
- Release evidence separated under `_release/`.

## Control checks

- England jurisdiction boundary.
- Critique-only and no-rewriting boundary.
- Exact quotation requirement.
- No invented facts or professional recommendations.
- Authority-type separation.
- Missing evidence and conflicts remain visible.
- Personal-data minimisation.
- Human review required before statutory use.
- Proposed reforms are not treated as current law.

## Machine contract checks

The response schema requires:

- versioned review identity;
- limitations and finding-count explanation;
- up to three material priority findings;
- stable finding IDs;
- authority provenance where relied upon;
- evidence recommendation locations;
- human review status;
- mandatory self-check controls.

A synthetic valid fixture is included under `evals/fixtures/`.

## Automated validation

Run:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_repo.py
```

GitHub Actions runs the same validation on pushes and pull requests.

## Known limitations

- The repository currently contains one contract fixture rather than a full benchmark suite.
- The demo illustrates the method but does not parse uploaded EHCP documents.
- The authority register is a controlled pointer to official sources, not a substitute for current-law verification.
- Human and specialist review remain necessary for contested legal, classification, placement, appeal or remedy questions.

## Human release check

Before merging to the public default branch, confirm:

1. GitHub Actions passes.
2. The README links resolve.
3. The demo opens without errors.
4. No real case information is present.
5. The public submission text accurately describes the editor.
6. The repository remains public.
