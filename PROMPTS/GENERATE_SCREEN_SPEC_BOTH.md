# Prompt Template: Generate Both Companion Specifications (`SCREEN_SPEC_XX.md` + `SCREEN_SPEC_XX_READABLE.md`)

> **File:** `PROMPTS/GENERATE_SCREEN_SPEC_BOTH.md`  
> **Role:** Replica Dual-Spec Engine v2.0 (Architect & Auditor)  
> **Target Outputs:**  
> 1. `specs/SCREEN_SPEC_[ID].md` (Deterministic Code Generation Contract)  
> 2. `specs/SCREEN_SPEC_[ID]_READABLE.md` (Human-Readable UI & Style Inventory)  
> **Input Required:** Screenshot of the UI screen + Screen ID & Name (optional brand context)

---

## Agent Instructions

You are acting as the **Replica Dual-Spec Generation Engine**.
Analyze the attached visual screenshot and generate **BOTH** complementary specification files for the given screen.

Both files must be saved under the `specs/` directory:
1. `specs/SCREEN_SPEC_[ID].md`
2. `specs/SCREEN_SPEC_[ID]_READABLE.md`

### Critical Consistency Rule:
Both files must be in **100% mutual alignment**:
- The class names in `SCREEN_SPEC_[ID].md` must match the classes documented in `SCREEN_SPEC_[ID]_READABLE.md`.
- The Hex codes, color tokens, and font sizes must be identical across both documents.
- Every button cataloged in the readable spec must exist in the DOM structure and CSS of the code spec.

---

## Specification 1: Deterministic Code Generation Contract (`specs/SCREEN_SPEC_[ID].md`)

Follow the instructions in `PROMPTS/GENERATE_SCREEN_SPEC.md`:
- **Section 1: Metadata & Layout Architecture:** Screen ID, route, shell layout, target viewports (Desktop 1440px+, Tablet 768px-1024px, Mobile <768px).
- **Section 2: Component & DOM Hierarchy:** Complete semantic HTML5 tree with all container classes, text strings, and inline SVG paths.
- **Section 3: Explicit CSS Specifications:** Fully written, uncompressed CSS rules with exact Hex colors, Flexbox/Grid definitions, paddings, borders, shadows, `:hover`, `:active`, transitions, and media queries.
- **Section 4: Typography & Color Mapping Table:** Structured table with element mapping, font-family, sizes, weights, line-heights, and Hex codes.
- **Section 5: Assets, Icons & Micro-Copy:** Icon names, dimensions, image aspect ratios, and micro-copy strings.
- **Section 6: Responsive Breakpoints & Mobile Adaptations:** Layout shift rules across viewport thresholds.

---

## Specification 2: Human-Readable UI & Component Style Inventory (`specs/SCREEN_SPEC_[ID]_READABLE.md`)

Follow the instructions in `PROMPTS/GENERATE_SCREEN_SPEC_READABLE.md`:
- **Section 1: Buttons & Interactive Elements Catalog:**
  - 1.1 Action Buttons Table (Element, Visual Type, Position, Default Style, Hover/Active States, CSS/Tailwind class strings).
  - 1.2 Navigation Links & CTAs Table (Label, Variant, Destination/Role, Typography, Hover State, Transitions).
- **Section 2: Headers & Typography Catalog:**
  - Mermaid hierarchy diagram of textual elements.
  - 2.1 Typography Hierarchy Table (Text Content, Tag/Role, Font Family, Fluid clamp() Size, Weight, Line Height, Color/Treatment).
- **Section 3: CSS System & Visual Tokens:**
  - 3.1 Color Palette Tokens Table (Background, Surfaces, Borders, Text tiers, Accent Hex codes).
  - 3.2 Visual Effects & Glassmorphism (Backdrop blur, shadow elevations, diffuse glows).
- **Section 4: Layout & Spacing Matrix:**
  - Container Table (Section/Container, Layout Model Flex/Grid, Alignments, Paddings, Gaps, Max-Widths).
- **Section 5: Assets, Icons & Media Inventory:**
  - Categorized breakdown of all SVG icons (with px dimensions), avatars, product stills, and logos.

---

## Quality Bar Checklist
- [ ] Are BOTH files generated and saved directly to the `specs/` directory?
- [ ] Are class names, tokens, and CSS properties 100% consistent between both files?
- [ ] Is there zero vague text (e.g. no "approximately", "placeholder styles", or truncated blocks)?
- [ ] Does the code spec have complete, copy-paste ready HTML & CSS?
- [ ] Does the readable spec have all Markdown tables fully populated?
