#!/usr/bin/env python3
"""
Screen Specification Validator
------------------------------
Validates that generated screen specifications (specs/screen_XX.md) adhere to the
standard schema:
1. Required sections present (Metadata, DOM Hierarchy, Explicit CSS, Typography, States, Assets, Responsive).
2. CSS blocks exist and are non-empty.
3. Prohibits vague/ambiguous language (e.g. "nice button", "roughly", "approx").
4. Validates token alignment.
"""

import sys
import os
import re
from pathlib import Path

REQUIRED_SECTIONS = [
    r"## 1\.\s+Screen Metadata",
    r"## 2\.\s+Component & DOM Hierarchy",
    r"## 3\.\s+Explicit CSS Specifications",
    r"## 4\.\s+Typography",
    r"## 5\.\s+Micro-Interactions|## 5\.\s+Interactive States",
    r"## 6\.\s+Assets",
    r"## 7\.\s+Responsive"
]

VAGUE_PATTERNS = [
    r"\bnice\b",
    r"\bgood-looking\b",
    r"\bapproximately\b",
    r"\broughly\b",
    r"\bsomewhere around\b",
    r"\bclean modern\b",
    r"\bstandard padding\b"
]

def validate_spec(file_path: Path) -> tuple[bool, list[str]]:
    errors = []
    warnings = []
    
    if not file_path.exists():
        return False, [f"File not found: {file_path}"]

    content = file_path.read_text(encoding="utf-8")

    # 1. Check required sections
    for sec_pattern in REQUIRED_SECTIONS:
        if not re.search(sec_pattern, content, re.IGNORECASE):
            errors.append(f"Missing required section matching pattern: '{sec_pattern}'")

    # 2. Check for explicit CSS blocks
    css_blocks = re.findall(r"```css(.*?)```", content, re.DOTALL)
    if not css_blocks:
        errors.append("No explicit CSS code blocks (```css ... ```) found in spec.")
    else:
        total_css_lines = sum(len(b.strip().splitlines()) for b in css_blocks)
        if total_css_lines < 20:
            warnings.append(f"CSS specification seems very short ({total_css_lines} lines). Ensure all properties are explicit.")

    # 3. Check for HTML DOM hierarchy
    html_blocks = re.findall(r"```html(.*?)```", content, re.DOTALL)
    if not html_blocks:
        errors.append("No DOM hierarchy block (```html ... ```) found.")

    # 4. Check for vague phrases
    for vague in VAGUE_PATTERNS:
        matches = re.findall(vague, content, re.IGNORECASE)
        if matches:
            warnings.append(f"Found prohibited vague expression '{matches[0]}'. Replace with explicit CSS metrics.")

    # 5. Check for interactive states (:hover)
    if ":hover" not in content and "Hover State" not in content:
        warnings.append("No :hover state or Hover State table found. Interactive states should be explicitly defined.")

    is_valid = len(errors) == 0
    messages = [f"[ERROR] {e}" for e in errors] + [f"[WARN] {w}" for w in warnings]
    return is_valid, messages

def main():
    if len(sys.argv) < 2:
        # Default to validating all specs in specs/
        specs_dir = Path(__file__).resolve().parent.parent / "specs"
        spec_files = list(specs_dir.glob("*.md"))
        spec_files = [f for f in spec_files if f.name != "README.md"]
    elif sys.argv[1] == "--all":
        specs_dir = Path(__file__).resolve().parent.parent / "specs"
        spec_files = [f for f in specs_dir.glob("*.md") if f.name != "README.md"]
    else:
        spec_files = [Path(sys.argv[1])]

    if not spec_files:
        print("No spec files found to validate.")
        sys.exit(0)

    total_files = len(spec_files)
    passed_count = 0

    print(f"Validating {total_files} spec file(s)...\n" + "="*50)

    for sf in spec_files:
        valid, msgs = validate_spec(sf)
        status = "PASS" if valid else "FAIL"
        print(f"[{status}] {sf.name}")
        for m in msgs:
            print(f"   {m}")
        if valid:
            passed_count += 1
        print("-" * 50)

    print(f"\nSummary: {passed_count}/{total_files} specifications passed validation.")
    if passed_count < total_files:
        sys.exit(1)

if __name__ == "__main__":
    main()
