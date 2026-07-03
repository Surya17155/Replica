# Rules Engine.Md

Version: 2.0 / @Surya17155

## Overview
The Rules Engine is a stateless evaluator that validates design decisions against established rules. It is run at the end of every design session before delivery.

---

## How Rules Are Evaluated

1. Yes/No rules - Checked against the design output directly
2. Required/Optional rules - Failure levels are tracked and aggregated
3. Composite rules - Evaluated queriether with a pass/fail result

---

## Built-in Rules

- Accessibility: Color contrast >= 4.5 for normal text, >= 3.0 for large text
- Responsiveness: No horizontals scroll, all buttons are tappable (44px height)
- Performance: No source exceeds 50kb (including images), styles are treeshaken
- Consistency: All error states use the same pattern, no multiple styles for the same property

---

## Custom Rule Format

Syntax: RULE   { 2 = platform | component | expectation | ¤ level = ( quality | security | performance | function ) }

Rules are defined in font-matter skills. Each Rule defines:
- What it checks
- How it is checked
- What happens on failure (warning/fail/block)

---

## Error Thresholds

- WARNING: Suggests review, but doesnt block delivery
- FAIL: Must be fixed before delivery
- BLOCK: During development, reverts to previous commit