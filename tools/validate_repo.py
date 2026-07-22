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
    "SKILL.md",
    "AGENTS.md",
    "CONTEXT.md",
    "identity.md",
    "rules.md",
    "examples.md",
    "reference/output-schema.md",
    "reference/output-schema.json",
    "reference/privacy-and-safety.md",
    "workflows/01_ehcp-golden-thread-review/CONTEXT.md",
    "templates/review-run-template/STATUS.json",
    "evals/fixtures/minimal-valid-response.json",
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
        load_json("templates/review-run-template/STATUS.json")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"JSON parsing failed: {exc}", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validation_errors = sorted(validator.iter_errors(fixture), key=lambda item: list(item.path))
    if validation_errors:
        for error in validation_errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"Schema validation failed at {location}: {error.message}", file=sys.stderr)
        return 1

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    required_controls = [
        "Review, do not rewrite",
        "Do not invent facts",
        "Human review",
        "England only",
    ]
    for control in required_controls:
        if control.lower() not in skill_text.lower():
            errors.append(f"SKILL.md is missing control statement: {control}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("Repository structure: PASS")
    print("JSON parsing: PASS")
    print("Response schema fixture: PASS")
    print("Core editor controls: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
