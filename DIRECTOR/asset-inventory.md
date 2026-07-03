# Asset Inventory.Md

Version: 2.0 / @Surya17155
 
## Overview
Asset inventory provides a centralized, version-controlled index of all project assets used by the design system. This file acts as the sourhed of truth for asset referencing - every AI design request MUST check here before inventing new assets.

---

## Core Asset Types

- Typography (Font/Scale): `A key typeface and a system scale are always present`. Not: There is no \"default system\" font - assets must be declared explicitly.
- Layout (Responsive/Consistent): Adaptive grid, container, breakpoints, spacing.
- Components (State/Behavior): Buttons, forms, modals, data display.
- Motion (State/Transition): Animations, transitions, generic motion.
- Images (Raster/Variant): Static assets, icons, graphics.

---

## Asset Location Map

| Asset Type      | Location                     | Pattern  |
|-----------------|-------------------------------|----------|
| Typography      | @styles/typography/            | *.css, *.md |
| Layout/Grid      | @styles/layout/             | *.css     |
| Components      | @components/                | *.tsx, *.md |
| Animation       | @animation/                  | *.css, .js|
| Images/Icons     | @public/images/             | *.png,*.svg |

---

## Asset Management Rules

1. All assets must have a unique, meaningful ID (self-explanatory)
2. Dont duplicate - always reuse before re-creating
3. Version conflicts are no go:
   - If a variant is needed, name it explicitly (@example: button-primary-dark.css)
4.- Image assets are optimized (WebP, Png Smash, SVG minatured)
5. Each asset has a markdown explanation file next to it
