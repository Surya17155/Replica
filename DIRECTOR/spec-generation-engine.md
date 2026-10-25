---
tags: [director, rules, spec-engine, workflow]
---

# Screen Spec Generation Engine — Rules & Workflow

This document defines the decision logic and rules for converting UI screenshots into standardized Screen Specifications (`specs/screen_XX.md`).

---

## 1. Core Principles

### Rule 1: Never Describe When You Can Write Explicit CSS
- **Prohibited**: "Add a modern dark button with subtle padding and rounded corners."
- **Mandated**: 
  ```css
  .btn-pill {
    height: 36px;
    padding: 0 16px;
    border-radius: 9999px;
    background-color: rgba(255, 255, 255, 0.1);
    color: #f1f1f1;
    font-size: 14px;
    font-weight: 500;
    border: none;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
  }
  .btn-pill:hover { background-color: rgba(255, 255, 255, 0.2); }
  .btn-pill:active { transform: scale(0.98); }
  ```

### Rule 2: Token Alignment with `GLOBAL_DESIGN_SYSTEM.md`
Whenever a visual value matches a token in `GLOBAL_DESIGN_SYSTEM.md`:
- Always use the CSS custom property as the primary value with the fallback hex:
  `background-color: var(--color-bg-base, #0f0f0f);`
- This guarantees zero cross-screen style drift whether generating Screen #1 or Screen #100.

### Rule 3: Stateless & Isolated Screen Contracts
- Each screen spec must be self-contained. A coding agent should be able to build that screen using only:
  1. `GLOBAL_DESIGN_SYSTEM.md` (or Master README)
  2. `specs/screen_XX.md`
  3. The screenshot file

---

## 2. The 6-Phase Processing Workflow

When a screenshot is provided:

```
[Phase 1: Input Detection & ID Assignment]
                 ↓
[Phase 2: Visual Checklist Execution (Silently)]
                 ↓
[Phase 3: Global Token Mapping]
                 ↓
[Phase 4: DOM & CSS Generation]
                 ↓
[Phase 5: State Matrix & Asset Transcription]
                 ↓
[Phase 6: Quality Verification (10-Point Gate)]
```

### Phase 1: Input Detection & ID Assignment
- Determine Screen Name and Screen Number (e.g. `01_home_feed`, `02_watch_player`).
- Check if it belongs to an existing flow or new route.

### Phase 2: Visual Checklist Execution
- Execute `REFERENCE/image-analysis-checklist-screen.md`.
- Identify overall container, multi-column flex/grid properties, and interactive elements.

### Phase 3: Global Token Mapping
- Map detected colors to `--color-*` variables in `GLOBAL_DESIGN_SYSTEM.md`.
- Map detected typography to `--font-*` scale.

### Phase 4: DOM & CSS Generation
- Draft semantic HTML5 DOM tree structure.
- Write explicit CSS blocks for all containers, cards, text, and buttons.

### Phase 5: State Matrix & Asset Transcription
- Fill out the Micro-Interactions table (`:hover`, `:active`, `:focus-visible`).
- List Lucide icon equivalents and exact visible micro-copy.

### Phase 6: Quality Verification Gate
Before saving the spec, verify:
1. Are all hex colors exact or bound to tokens?
2. Are all button heights, paddings, and border-radiuses explicit?
3. Does every interactive element specify a `:hover` rule and transition?
4. Are all font sizes, line heights, and weights explicitly stated?
5. Is the DOM hierarchy valid semantic HTML5?
