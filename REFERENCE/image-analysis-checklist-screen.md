---
tags: [reference, checklist, image-analysis, screen-spec]
---

# Image Analysis Checklist — Screen Specification

Run this comprehensive checklist silently on every screen screenshot before generating the screen specification. Check every category to ensure 100% extraction of layout, CSS, tokens, and micro-interactions.

---

## 1. Frame, Layout Shell & Container Architecture
- [ ] **Viewport & Container Structure**:
  - Is the content contained in a full-width viewport or a centered constrained container (`max-width: 1280px / 1440px / 1600px`)?
  - Does this screen extend a standard App Shell (Top Navigation + Sidebar Drawer), or is it a standalone fullscreen/modal view?
- [ ] **Multi-Column Division**:
  - Count columns (e.g., Single Column Feed, Two-Column Main + Secondary Sidebar, Three-Column Grid, Bento Grid).
  - Explicit flex / grid metrics: What is the flex-basis or fixed pixel width of side columns (e.g., `width: 380px` or `400px`)?
  - Gap spacing between columns: 16px, 20px, 24px, or 32px?
- [ ] **Padding & Insets**:
  - Outer page container padding: Top, Bottom, Left, Right (e.g., `24px` horizontal padding).

---

## 2. Color Sampling & Token Alignment
- [ ] **Sample Base Background Hex**:
  - Sample background color: Matches `--color-bg-base` (`#0f0f0f`), dark gray, pure black (`#000000`), or white?
- [ ] **Sample Card & Container Surface Colors**:
  - Elevating surface hex: Is it `#181818`, `#212121`, `#272727`?
  - Border colors and opacity: e.g., `rgba(255, 255, 255, 0.1)`.
- [ ] **Sample Typography Colors**:
  - Primary headline color: `#ffffff` or `#f1f1f1`?
  - Secondary metadata color: `#aaaaaa` or `#888888`?
  - Accent color: Brand red (`#ff0000`), blue (`#3ea6ff`), green, etc.?

---

## 3. Typography & Hierarchy Decomposition
For every text element in the screenshot:
- [ ] **Font Family**: Sans-serif (Roboto, Inter), Serif, Monospace, or Display?
- [ ] **Font Size in Pixels**: Sample size (e.g., 20px headline, 16px section title, 14px body/action, 12px caption/meta).
- [ ] **Font Weight**: 400 (regular), 500 (medium), 600 (semi-bold), 700 (bold).
- [ ] **Line Height & Letter Spacing**: Tight (1.2) for headlines, normal (1.4–1.5) for body.
- [ ] **Text Clipping**: Does text truncate with an ellipsis (`text-overflow: ellipsis; overflow: hidden; white-space: nowrap`) or multi-line clamp (`-webkit-line-clamp: 2`)?

---

## 4. Component Primitives & Explicit CSS
- [ ] **Buttons & CTAs**:
  - Button height: 32px (small), 36px (standard), 40px, or 48px?
  - Border radius: Fully rounded pill (`border-radius: 9999px`) or rounded rectangle (`border-radius: 8px`)?
  - Internal padding: `padding: 0 16px`?
  - Background & Hover: Translucent overlay `rgba(255, 255, 255, 0.1)` hovering to `0.2`?
- [ ] **Media & Thumbnails**:
  - Aspect ratio: `16 / 9`, `4 / 3`, `1 / 1`?
  - Border radius on media containers: `8px`, `12px`, `16px`?
  - Overlay badges (e.g., duration badge `12:45` in bottom right): Background `#000000` with 80% opacity, font size 12px, border-radius 4px.
- [ ] **Avatars & Badges**:
  - Dimensions: 24x24, 36x36, 40x40, or 48x48?
  - Shape: 100% circular (`border-radius: 50%`)?
- [ ] **Dividers & Borders**:
  - Are there horizontal dividers between sections? 1px solid `rgba(255, 255, 255, 0.1)`.

---

## 5. Micro-Interactions & Interactive States
Identify every interactive element visible or implied:
- [ ] Buttons: `:hover` brightness/overlay change, `:active` scale down (`transform: scale(0.98)`).
- [ ] Clickable Cards / List Items: Hover background shift (e.g. from transparent to `rgba(255,255,255,0.05)`).
- [ ] Tabs / Filter Chips: Distinct `active` state (inverted white background with dark text) vs `idle` state.
- [ ] Input / Search fields: Focus outline ring or border glow (`outline: 2px solid var(--color-accent-blue)`).

---

## 6. Icons & Asset Extraction
- [ ] Identify all visible icons and match them to exact [Lucide](https://lucide.dev/) or standard SVG names (e.g., `Search`, `Bell`, `ThumbsUp`, `Share2`, `MoreVertical`).
- [ ] Transcribe all readable text verbatim for micro-copy and titles.
