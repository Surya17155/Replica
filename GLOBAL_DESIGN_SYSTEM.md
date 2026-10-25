# Global Design System & Master Specifications (Tier 1)

> **Single Source of Truth (SSOT)** for project-wide styling, design tokens, layout shells, and shared component primitives. All screen specifications (`specs/screen_XX.md`) reference tokens and conventions defined here.

---

## 1. Tech Stack Conventions

- **Structure**: Semantic HTML5 (`<header>`, `<nav>`, `<aside>`, `<main>`, `<section>`, `<article>`).
- **Styling**: Standard CSS Custom Properties (CSS variables) + Vanilla CSS or Tailwind CSS utility classes.
- **Iconography**: [Lucide Icons](https://lucide.dev/) or inline SVG icons.
- **Font Delivery**: Google Fonts via `<link>` or `@import`.

---

## 2. Global Design Tokens

### 2.1 Color Tokens
All components should consume these CSS custom properties to ensure cross-screen coherence:

```css
:root {
  /* Surfaces & Backgrounds */
  --color-bg-base: #0f0f0f;            /* Deep black/gray app background */
  --color-bg-surface: #181818;         /* Card, container, and drawer background */
  --color-bg-surface-elevated: #272727;/* Hover states, popups, elevated chips */
  --color-bg-surface-highest: #383838; /* Dialogs, active chips, focused fields */
  
  /* Text Tiers */
  --color-text-primary: #f1f1f1;       /* 100% white/light primary headlines & body */
  --color-text-secondary: #aaaaaa;     /* Secondary subtitles, timestamps, view counts */
  --color-text-muted: #717171;         /* Placeholders, disabled text, meta labels */
  --color-text-inverse: #0f0f0f;       /* Text on primary accent buttons */

  /* Borders & Dividers */
  --color-border-subtle: rgba(255, 255, 255, 0.1);
  --color-border-strong: rgba(255, 255, 255, 0.2);

  /* Brand Accents & States */
  --color-primary: #ff0000;            /* Primary brand color (e.g. YouTube Red) */
  --color-primary-hover: #cc0000;
  --color-accent-blue: #3ea6ff;        /* Links, interactive tags, badges */
  --color-accent-blue-hover: #65b8ff;
  --color-danger: #ff4e45;
  --color-success: #2ba640;

  /* Interactive Overlays */
  --color-overlay-hover: rgba(255, 255, 255, 0.1);
  --color-overlay-active: rgba(255, 255, 255, 0.2);
}
```

### 2.2 Typography Scale
Primary font family: `'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.

```css
:root {
  --font-family-base: 'Roboto', sans-serif;

  /* Type Scale */
  --font-size-xs: 11px;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-md: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;
  --font-size-3xl: 28px;

  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.6;

  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
}
```

### 2.3 Spacing & Radius Scale
```css
:root {
  /* Spacing Scale */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;

  /* Radius Scale */
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;
}
```

---

## 3. Global App Shell & Layout Structure

Every screen in the application mounts inside the **Standard Application Shell**:

```html
<div class="app-layout">
  <!-- Top Navigation Bar (Fixed 56px height) -->
  <header class="app-header">
    <div class="header-start">...</div>
    <div class="header-center">...</div>
    <div class="header-end">...</div>
  </header>

  <!-- Content Body -->
  <div class="app-body">
    <!-- Collapsible Sidebar / Drawer -->
    <aside class="app-sidebar" data-state="expanded|mini|collapsed">
      ...
    </aside>

    <!-- Main Screen Viewport -->
    <main class="app-main-viewport" id="main-content">
      <!-- Screen-specific content renders here -->
    </main>
  </div>
</div>
```

```css
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: var(--color-bg-base);
  color: var(--color-text-primary);
  font-family: var(--font-family-base);
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
  padding: 0 var(--space-4);
  background-color: var(--color-bg-base);
  border-bottom: 1px solid var(--color-border-subtle);
}

.app-body {
  display: flex;
  flex: 1 1 0%;
  overflow: hidden;
}

.app-sidebar[data-state="expanded"] {
  width: 240px;
  flex-shrink: 0;
}

.app-sidebar[data-state="mini"] {
  width: 72px;
  flex-shrink: 0;
}

.app-main-viewport {
  flex: 1 1 0%;
  overflow-y: auto;
  min-height: calc(100vh - 56px);
}
```

---

## 4. Shared Atomic Components & CSS Classes

### 4.1 Button System

```css
/* Base Button reset */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  font-family: var(--font-family-base);
  font-weight: var(--font-weight-medium);
  font-size: var(--font-size-base);
  border: none;
  border-radius: var(--radius-full);
  cursor: pointer;
  padding: 0 var(--space-4);
  height: 36px;
  transition: background-color 0.2s ease, opacity 0.2s ease, transform 0.1s ease;
  user-select: none;
  white-space: nowrap;
}

.btn:active {
  transform: scale(0.98);
}

/* Variant: Solid White / Inverse Primary */
.btn-primary {
  background-color: var(--color-text-primary);
  color: var(--color-text-inverse);
}
.btn-primary:hover {
  opacity: 0.9;
}

/* Variant: Subtle Pill (Translucent surface) */
.btn-surface {
  background-color: var(--color-overlay-hover);
  color: var(--color-text-primary);
}
.btn-surface:hover {
  background-color: var(--color-overlay-active);
}

/* Variant: Icon-only Button */
.btn-icon {
  width: 40px;
  height: 40px;
  padding: 0;
  border-radius: var(--radius-full);
  background: transparent;
  color: var(--color-text-primary);
}
.btn-icon:hover {
  background-color: var(--color-overlay-hover);
}
```

### 4.2 Pill Chips / Filter Tags

```css
.filter-chip {
  display: inline-flex;
  align-items: center;
  height: 32px;
  padding: 0 var(--space-3);
  border-radius: var(--radius-sm);
  background-color: var(--color-bg-surface-elevated);
  color: var(--color-text-primary);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
  border: none;
  transition: background-color 0.15s ease;
}

.filter-chip:hover {
  background-color: var(--color-bg-surface-highest);
}

.filter-chip.active {
  background-color: var(--color-text-primary);
  color: var(--color-text-inverse);
}
```

---

## 5. Instructions for Coding Agents (Claude / Antigravity / Copilot)

1. **Always inherit from this master document**: Never hardcode colors when a CSS variable exists (e.g. use `var(--color-bg-base)` instead of hardcoding `#0f0f0f`).
2. **Follow the App Shell Layout**: All screens mount into `<main class="app-main-viewport">`. Do not recreate headers or sidebars unless explicitly directed in the screen spec.
3. **Respect Interactive States**: Include all `:hover`, `:active`, `:focus-visible`, and `transition` properties specified in the screen spec.
