# Prompt Template: Generate Deterministic Code Specification (`SCREEN_SPEC_XX.md`)

> **File:** `PROMPTS/GENERATE_SCREEN_SPEC.md`  
> **Role:** Senior Frontend Architect & Design Systems Engineer  
> **Target Output:** `specs/SCREEN_SPEC_[ID].md`  
> **Input Required:** Screenshot of the UI screen + Screen ID & Name (optional brand context)

---

## Agent Instructions

You are acting as the **Replica Deterministic Screen Spec Generator**.
Analyze the attached visual screenshot and generate a complete, deterministic, production-grade **Code Generation Specification** contract.

Your output must be saved to:  
`specs/SCREEN_SPEC_[ID].md`

---

## Output Contract & Required Sections

The generated file must adhere strictly to the following 6-part schema:

```markdown
# Screen Spec: [Screen Name] ([SCREEN-ID])

> **Specification Type:** Deterministic Screen Specification (Replica Engine v2.0)  
> **Target Route:** `/[route-path]`  
> **Source Reference:** [Product / Brand Name]  
> **Design Aesthetic:** [e.g., High-Contrast Dark Theme, Frosted Glassmorphism, Clean Minimalist Light]  
> **Companion Spec:** `specs/SCREEN_SPEC_[ID]_READABLE.md`

---

## 1. Metadata & Layout Architecture

- **Screen ID:** `[SCREEN-ID]` (e.g., `SCR-WEBEX-002`)
- **Route:** `/[route-path]`
- **Shell Layout:** `[LayoutShellName]` (e.g., Fixed top navbar + hero canvas + multi-column grid)
- **Viewport Target:**
  - Desktop: `1440px+` (Max content container `[width]px` centered, columns/grid rules)
  - Tablet: `768px - 1024px` (Responsive collapses, horizontal scrolling or stacked layout)
  - Mobile: `<768px` (Single column, mobile navigation drawer/hamburger, full-width buttons)

---

## 2. Component & DOM Hierarchy

Provide the complete semantic HTML5 / JSX DOM tree for the entire viewport.
- Use semantic tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<aside>`, `<article>`, `<button>`).
- Include every container class name.
- Embed inline SVG paths/viewBox for all icons (or specify exact Lucide React icon names).
- Represent realistic copy and structural groupings.

Example:
```html
<div class="screen-root">
  <header class="global-navbar">...</header>
  <main class="content-container">
    <section class="hero-section">...</section>
    <section class="grid-section">...</section>
  </main>
</div>
```

---

## 3. Explicit CSS Specifications

Write **complete, uncompressed, production-grade CSS rules** covering all layout containers, cards, typography, and interactive components.

Rules:
- Never use vague placeholders like "add styling here" or "similar to above".
- Every color must be an exact Hex code (`#0c0f12`, `#00875a`) or CSS variable with fallback (`var(--color-bg, #0f0f0f)`).
- Explicitly define `display`, `flex-direction`, `grid-template-columns`, `gap`, `padding`, `margin`, `border-radius`, and `box-shadow`.
- Include full pseudo-classes for interactive elements: `:hover`, `:active`, `:focus-visible`, and transition properties (`transition: all 0.2s ease`).
- Include responsive media queries (`@media (max-width: 1024px)`, `@media (max-width: 768px)`).

---

## 4. Typography & Color Mapping Table

| Element / Role | Font Family | Size (px / clamp) | Weight | Line Height | Color (Hex) | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hero Headline (H1) | Inter / System | clamp(2.5rem, 5vw, 4rem) | 700 (Bold) | 1.1 | #ffffff | -0.02em |
| Section Title (H2) | Inter / System | 28px | 600 (Semibold)| 1.25 | #f1f1f1 | -0.01em |
| Body Text | Inter / System | 15px | 400 (Regular) | 1.5 | #94a3b8 | normal |
| Primary CTA Button | Inter / System | 14px | 600 (Semibold)| 1.2 | #ffffff | normal |
| Micro-copy / Meta | Inter / System | 12px | 400 (Regular) | 1.4 | #64748b | normal |

---

## 5. Assets, Icons & Micro-Copy

- **Icons Required:** Exact names, dimensions (width × height in px), and stroke/fill colors.
- **Images & Media:** Aspect ratios (16:9, 1:1, 4:3), dimensions, border-radius, background fills, or overlay masks.
- **Exact Micro-Copy Strings:** Exact text content for headlines, subtext, button labels, and badges.

---

## 6. Responsive Breakpoints & Mobile Adaptations

- **Desktop (>1024px):** Multi-column flex/grid layout, full navigation bar, fixed elements.
- **Tablet (768px - 1024px):** Layout reflow, grid collapse from 3/4 columns to 2 columns, overflow horizontal scrolling.
- **Mobile (<768px):** 100% width fluid stacking, hamburger drawer navigation, touch-friendly tap targets (minimum 44x44px).
```

---

## Quality Bar Checklist
- [ ] Are all hex colors exact (no generic "blue" or "gray")?
- [ ] Is the DOM structure 100% semantic and complete?
- [ ] Are all hover and active states explicitly written out in CSS?
- [ ] Are all responsive breakpoint adjustments clearly defined?
- [ ] Is the output saved directly to `specs/SCREEN_SPEC_[ID].md`?
