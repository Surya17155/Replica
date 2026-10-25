---
tags: [reference, spec-template, screen, output-spec]
---

# Screen Specification Output Template (Standard Contract)

Use this exact structure whenever generating a specification from an uploaded UI screenshot. The output must be completely self-contained, deterministic, and unambiguous for autonomous coding agents (Claude, Antigravity, GitHub Copilot).

---

```markdown
# Screen Spec: [Screen Name] (Screen #[ID])

## 1. Screen Metadata & Environment
- **Screen ID**: `SCR-[ID]`
- **Route**: `/[route-path]`
- **Target Viewports**: 
  - Desktop: 1440px+ (Primary)
  - Tablet: 768px – 1024px
  - Mobile: < 768px
- **Parent Shell**: `AppLayout` (Sidebar state: `expanded` | `mini` | `hidden`)
- **Scroll Behavior**: Page-level vertical scroll / Isolated container scroll

---

## 2. Component & DOM Hierarchy
Outline the semantic HTML5 DOM structure. Every major container, section, and interactive control must be explicitly represented with its semantic tag, class name, and purpose:

```html
<main class="[screen-root-class]">
  <div class="[primary-layout-container]">
    <!-- Section 1 -->
    <section class="[section-class]">
      <header class="[header-class]">
        <h1 class="[headline-class]">[Exact Text / Placeholder]</h1>
        <div class="[actions-bar-class]">
          <button class="[btn-class]">...</button>
        </div>
      </header>
      <div class="[content-body-class]">...</div>
    </section>
  </div>
  <!-- Aside / Secondary Column (if present) -->
  <aside class="[secondary-column-class]">
    ...
  </aside>
</main>
```

---

## 3. Explicit CSS Specifications
Provide 100% complete CSS blocks. Do not summarize with phrases like "use proper padding" or "center the elements". Write the exact CSS rules:

```css
/* -------------------------------------------------------------
 * 1. Root & Layout Containers
 * ------------------------------------------------------------- */
.[screen-root-class] {
  display: flex;
  flex-direction: row; /* or column / grid */
  gap: var(--space-6, 24px);
  padding: var(--space-6, 24px);
  background-color: var(--color-bg-base, #0f0f0f);
  color: var(--color-text-primary, #f1f1f1);
  min-height: calc(100vh - 56px);
  box-sizing: border-box;
}

.[primary-layout-container] {
  flex: 1 1 0%;
  max-width: calc(100% - 424px);
  display: flex;
  flex-direction: column;
  gap: var(--space-4, 16px);
}

.[secondary-column-class] {
  width: 400px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-4, 16px);
}

/* -------------------------------------------------------------
 * 2. Cards, Surfaces & Sections
 * ------------------------------------------------------------- */
.[section-class] {
  background-color: var(--color-bg-surface, #181818);
  border: 1px solid var(--color-border-subtle, rgba(255, 255, 255, 0.1));
  border-radius: var(--radius-md, 12px);
  padding: var(--space-4, 16px);
}

/* -------------------------------------------------------------
 * 3. Typography & Text Elements
 * ------------------------------------------------------------- */
.[headline-class] {
  font-family: var(--font-family-base, 'Roboto', sans-serif);
  font-size: var(--font-size-xl, 20px);
  font-weight: var(--font-weight-bold, 700);
  line-height: var(--line-height-tight, 1.2);
  color: var(--color-text-primary, #f1f1f1);
  margin: 0;
}

/* -------------------------------------------------------------
 * 4. Interactive Components & States
 * ------------------------------------------------------------- */
.[btn-class] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2, 8px);
  height: 36px;
  padding: 0 var(--space-4, 16px);
  border-radius: var(--radius-full, 9999px);
  background-color: var(--color-overlay-hover, rgba(255, 255, 255, 0.1));
  color: var(--color-text-primary, #f1f1f1);
  font-size: var(--font-size-base, 14px);
  font-weight: var(--font-weight-medium, 500);
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

.[btn-class]:hover {
  background-color: var(--color-overlay-active, rgba(255, 255, 255, 0.2));
}

.[btn-class]:active {
  transform: scale(0.98);
}

.[btn-class]:focus-visible {
  outline: 2px solid var(--color-accent-blue, #3ea6ff);
  outline-offset: 2px;
}
```

---

## 4. Typography & Design Token Mapping Table

| UI Element | CSS Token / Selector | Font Family | Size | Weight | Line Height | Color (Hex / Token) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Screen Title | `.[headline-class]` | Roboto | 20px | 700 | 28px | `var(--color-text-primary)` (`#f1f1f1`) |
| Subtitle / Meta | `.[meta-class]` | Roboto | 12px | 400 | 18px | `var(--color-text-secondary)` (`#aaaaaa`) |
| Body Text | `.[body-class]` | Roboto | 14px | 400 | 20px | `var(--color-text-primary)` (`#f1f1f1`) |
| Button Label | `.[btn-class]` | Roboto | 14px | 500 | 20px | `var(--color-text-primary)` (`#f1f1f1`) |

---

## 5. Micro-Interactions & State Matrix

| Element | Idle State | Hover State | Active / Clicked | Disabled State |
| :--- | :--- | :--- | :--- | :--- |
| Primary CTA | `bg: #ffffff; text: #0f0f0f` | `opacity: 0.9` | `transform: scale(0.98)` | `opacity: 0.4; cursor: not-allowed` |
| Secondary Button | `bg: rgba(255,255,255,0.1)` | `bg: rgba(255,255,255,0.2)` | `transform: scale(0.98)` | `opacity: 0.3; cursor: not-allowed` |
| Interactive Card | `border: 1px solid transparent` | `border: 1px solid rgba(255,255,255,0.2)` | — | — |

---

## 6. Assets, Iconography & Exact Copy

### 6.1 Icons
- **Icon Library**: Lucide Icons (or SVG)
- **Mapping**:
  - `[Action 1]`: `<ThumbsUp size={18} />`
  - `[Action 2]`: `<Share2 size={18} />`
  - `[Action 3]`: `<MoreHorizontal size={18} />`

### 6.2 Images & Media
- **Primary Media Item**:
  - Aspect Ratio: `16 / 9`
  - Border Radius: `12px`
  - Object Fit: `cover`
- **User Avatar**:
  - Dimensions: `40px x 40px`
  - Border Radius: `50%`

### 6.3 Exact Visible Copy / Text Strings
- Main Header: `"[Exact text visible in screenshot]"`
- Action Buttons: `["Button Text 1", "Button Text 2", "Button Text 3"]`

---

## 7. Responsive Breakpoints & Reflow Rules

- **Desktop (1025px+)**: Two-column layout with fixed right column (`400px`) and flex-grow main content.
- **Tablet (768px – 1024px)**: Single-column layout. The secondary column reflows directly underneath the primary column with `width: 100%`.
- **Mobile (< 768px)**: Padding reduces to `12px`. Header action buttons collapse into a horizontal scroll strip or overflow menu.
```
