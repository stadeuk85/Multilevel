#!/usr/bin/env python3
"""Validate the competition repository structure and response contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit("Install development dependencies with: pip install -r requirements-dev.txt") from exc

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "AGENTS.md",
    "CONTEXT.md",
    "FILE-MAP.md",
    "COMPETITION_SUBMISSION.md",
    "identity.md",
    "rules.md",
    "examples.md",
    "reference/CONTEXT.md",
    "reference/output-schema.md",
    "reference/output-schema.json",
    "reference/authority-register.json",
    "reference/privacy-and-safety.md",
    "workflows/01_ehcp-golden-thread-review/CONTEXT.md",
    "templates/CONTEXT.md",
    "templates/review-run-template/README.md",
    "templates/review-run-template/STATUS.json",
    "evals/CONTEXT.md",
    "evals/README.md",
    "evals/fixtures/minimal-valid-response.json",
    "demo/CONTEXT.md",
    "demo/index.html",
    "_release/CONTEXT.md",
    "_release/current/RELEASE_MANIFEST.json",
    "_release/current/VALIDATION_REPORT.md",
]

STAGES = [
    "01_intake-and-safety",
    "02_evidence-register",
    "03_section-extraction",
    "04_golden-thread-mapping",
    "05_evidence-alignment",
    "06_priority-findings",
    "07_human-review",
    "08_final-output",
]


def load_json(relative_path: str) -> object:
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require_phrases(path: str, phrases: list[str], errors: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8").lower()
    for phrase in phrases:
        if phrase.lower() not in text:
            errors.append(f"{path} is missing required phrase: {phrase}")


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    for stage in STAGES:
        contract = ROOT / "workflows/01_ehcp-golden-thread-review" / stage / "CONTEXT.md"
        if not contract.is_file():
            errors.append(f"Missing stage contract: {contract.relative_to(ROOT)}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    try:
        schema = load_json("reference/output-schema.json")
        fixture = load_json("evals/fixtures/minimal-valid-response.json")
        status_template = load_json("templates/review-run-template/STATUS.json")
        authority_register = load_json("reference/authority-register.json")
        release_manifest = load_json("_release/current/RELEASE_MANIFEST.json")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"JSON parsing failed: {exc}", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validation_errors = sorted(validator.iter_errors(fixture), key=lambda item: str(list(item.path)))
    if validation_errors:
        for error in validation_errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"Schema validation failed at {location}: {error.message}", file=sys.stderr)
        return 1

    if not isinstance(status_template, dict) or len(status_template.get("stages", {})) != 8:
        errors.append("STATUS.json must contain all eight workflow stages")

    if not isinstance(authority_register, dict) or not authority_register.get("last_reviewed"):
        errors.append("Authority register must contain a review date")

    if release_manifest.get("workflow", {}).get("stage_count") != 8:
        errors.append("Release manifest stage count must equal eight")

    require_phrases(
        "SKILL.md",
        ["Review, do not rewrite", "Do not invent facts", "Human review", "England only"],
        errors,
    )
    require_phrases(
        "README.md",
        ["identity.md", "rules.md", "examples.md", "reference/", "editor, not a rewriter"],
        errors,
    )
    require_phrases(
        "rules.md",
        ["Editor, not rewriter", "Quote before criticising", "No invented evidence"],
        errors,
    )

    demo_text = (ROOT / "demo/index.html").read_text(encoding="utf-8").lower()
    if "uploads and stores nothing" not in demo_text or "synthetic" not in demo_text:
        errors.append("Public demo must state its synthetic, no-upload boundary")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("Repository structure: PASS")
    print("ICM entry and stage contracts: PASS")
    print("JSON parsing: PASS")
    print("Response schema fixture: PASS")
    print("Authority and release records: PASS")
    print("Core editor controls: PASS")
    print("Public demo boundary: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
