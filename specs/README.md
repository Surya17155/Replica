# Screen Specifications Directory (`specs/`)

This directory houses the **Dual-Spec Architecture** outputs, cleanly organized into dedicated folders for machine execution and human review.

```text
specs/
├── README.md
├── machine/                   # For AI Coding Agents (Claude, Antigravity, Copilot)
│   ├── 01_youtube_watch_view.md
│   ├── 02_channel_profile.md
│   ├── SCREEN_SPEC_02.md
│   └── SCREEN_SPEC_03.md
└── human/                     # For UI/UX Designers, PMs & Reviewers
    ├── SCREEN_SPEC_02_READABLE.md
    └── SCREEN_SPEC_03_READABLE.md
```

---

### Folder Breakdown

#### 1. `specs/machine/` (Deterministic Code-Gen Contracts)
- **Primary Consumer:** Autonomous AI coding agents (Claude, Antigravity, GitHub Copilot).
- **Format:** Strict, machine-parseable Markdown specifications adhering to `REFERENCE/spec-output-template-screen.md`.
- **Contents:**
  - Semantic HTML5 DOM tree (`<main>`, `<header>`, `<section>`, `<aside>`).
  - 100% explicit CSS rule blocks (exact px dimensions, hex/rgba values, flex/grid coordinates).
  - Explicit interactive states (`:hover`, `:active`, `:focus-visible`).
  - Responsive reflow rules for Desktop, Tablet, and Mobile viewports.

#### 2. `specs/human/` (Design Audit & UI Inventory)
- **Primary Consumer:** UI/UX Designers, Product Managers, QA Engineers, and Technical Leads.
- **Format:** High-level structured audit tables and catalogs.
- **Contents:**
  - **Buttons & Interactive Elements Catalog:** Table listing all buttons, links, icons, visual variants, and hover states.
  - **Headers & Typography Catalog:** Font families, weights, line heights, and responsive `clamp()` formulas.
  - **CSS System & Visual Tokens:** Color palette tokens, border radii, shadows, and frosted glass effects.
  - **Layout & Spacing Matrix:** Flexbox/grid alignment rules, container paddings, and section gaps.
  - **Assets & Media Inventory:** Icon names (Lucide/SVG), image ratios, and avatar assets.

---

### How AI Coding Agents Consume Machine Specs (Tier 3 Triplet)

When implementing any screen, pass this exact 3-part context to the agent:
1. **Global Tokens:** `GLOBAL_DESIGN_SYSTEM.md` (or master `README.md`)
2. **Machine Screen Spec:** `specs/machine/[SCREEN_SPEC_XX].md`
3. **Visual Reference:** `screenshots/[SCREEN_NAME].png`
