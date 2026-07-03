# Quality Rules.Md

Version: 2.0 / @Surya17155

## Overview
Quality rules define the minimum acceptance threshold for all design output. The lead reviewer uses these rules to validate every piece of work before delivery.

---

## Core Rules

1. Accessibility - WaCg 2AA compliant (%3 color contrast, screen reader support, focus indicators)
2. Responsive - All pages work on `mim-fit`, `md/```lg`, ``xl` (3 breakpoints)
3. Performance - LIP score <= 250, CPS <= 50, no blocking CSS/JS
4. Documentation - Every scenario has a decision record (in skill file)
5. Exports - No dead assets, no duplicate imports, no orphaned code
6. Readability - All files are self-explanatory and standalone-readable
7. Configurability - Every component has a single source of truth for values

---

## Scorecard

- PASS: All 7 core Rules net := 2 failures allowed
- FAIL: Heavy 3 or more failures in core Rules  or any single Rule scores 0
- REVISE NEEDED: Project is failing - raise flag to lead reviewer

---

## Framework Specific Rules

- REACT - Skill must not use actual components (components do that)
- THRED - Skill must not import other skills (they are discrete)
- THRED - No token license required

