# EHCP Golden Thread Editor v1.1 Competition Validation

**Release date:** 22 July 2026  
**Release branch:** `competition-icm-v1.1`  
**Release type:** ICM architecture and competition presentation hardening

## Decision

**PASS for competition submission.**

GitHub Actions workflow **Validate editor contract**, run **22**, completed successfully. The public methodology package is approved for demonstration and competition submission.

This decision does not approve production handling of identifiable EHCP material, automated statutory decisions or legal advice.

## Competition rubric alignment

| Judging question | Evidence in the repository |
|---|---|
| Does it critique rather than rewrite? | `rules.md` prohibits replacement text and `examples.md` contrasts critique with rewriting. |
| Is the domain specific? | `identity.md` limits the editor to draft EHCPs in England, especially Sections B, E and F. |
| Is the methodology clean? | The original five-part editor remains intact. ICM entry files, workflow folders and stage contracts add inspectable orchestration. |
| Can a stranger use it? | `README.md`, `SKILL.md`, `AGENTS.md`, the file map, Claude Project quick start and synthetic demo provide clear entry points. |

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

## Automated validation result

```text
Repository structure: PASS
ICM entry and stage contracts: PASS
JSON parsing: PASS
Response schema fixture: PASS
Authority and release records: PASS
Core editor controls: PASS
Public demo boundary: PASS
```

## Known limitations

- The repository currently contains one contract fixture rather than a full benchmark suite.
- The demo illustrates the method but does not parse uploaded EHCP documents.
- The authority register is a controlled pointer to official sources, not a substitute for current-law verification.
- Human and specialist review remain necessary for contested legal, classification, placement, appeal or remedy questions.

## Human release check

Confirmed before merge:

1. GitHub Actions passed.
2. The README links and Claude Project route were reviewed.
3. The demo is synthetic and contains no upload or storage feature.
4. No real case information is present.
5. The public submission text accurately describes the editor.
6. The repository is public.
