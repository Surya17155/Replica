---
name: frontend-design
description: Anthropic's frontend design skill for creating intuitive, polished, and on-brand user interfaces.
---

# frontend-design

Anthropic's frontend design skill for creating intuitive, polished, and on-brand user interfaces.

## Core Principles

1. **Start with a blueprint** — layout, hierarchy, and spacing before colors and polish
2. **Typography is the UI** — 70% of a well-designed interface is text treatment
3. **Consistency over novelty** — new patterns should earn their place
4. **Reduce, reuse, respect** — remove clutter, reuse components, respect constraints
5. **Performance is part of design** — a beautiful slow page is ugly

## 1. Typography

### Font Stack

```css
--font-body: 'Inter', system-ui, -apple-system, sans-serif;
--font-display: 'Space Grotesk', 'Inter', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', 'SF Mono', monospace;
```

### Scale

| Token | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `text-xs` | 0.75rem (12px) | 400/500 | 1.5 | Labels, captions |
| `text-sm` | 0.875rem (14px) | 400/500 | 1.5 | Secondary text |
| `text-base` | 1rem (16px) | 400 | 1.6 | Body paragraphs |
| `text-lg` | 1.125rem (18px) | 500 | 1.5 | Large body |
| `text-xl` | 1.25rem (20px) | 600 | 1.4 | Subheadings |
| `text-2xl` | 1.5rem (24px) | 600 | 1.3 | Section headings |
| `text-3xl` | 1.875rem (30px) | 600 | 1.2 | Major headings |
| `text-4xl` | 2.25rem (36px) | 600/700 | 1.1 | Display heading |
| `text-5xl` | 3rem (48px) | 600/700 | 1.0 | Hero display |
| `text-6xl` | 3.75rem (60px) | 600/700 | 1.0 | Large hero |

## 2. Color

### Palette Structure

```css
:root {
  --bg-primary: #FAFAFA;
  --bg-secondary: #F5F5F5;
  --bg-tertiary: #E8E8E8;
  
  --text-primary: #0A0A0A;
  --text-secondary: #525252;
  --text-tertiary: #A3A3A3;
  
  --accent: #0066FF;
  --accent-hover: #0052CC;
  --accent-soft: #E8F0FE;
  
  --border: #E5E5E5;
  --border-hover: #D4D4D4;
  
  --success: #16A34A;
  --warning: #F59E0B;
  --error: #DC2626;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #0A0A0A;
    --bg-secondary: #141414;
    --bg-tertiary: #1F1F1F;
    --text-primary: #F5F5F5;
    --text-secondary: #A3A3A3;
    --text-tertiary: #666666;
    --border: #2A2A2A;
    --border-hover: #404040;
  }
}
```

## 3. Spacing

8px base grid:

| Token | Value |
|-------|-------|
| `space-1` | 4px |
| `space-2` | 8px |
| `space-3` | 12px |
| `space-4` | 16px |
| `space-5` | 20px |
| `space-6` | 24px |
| `space-8` | 32px |
| `space-10` | 40px |
| `space-12` | 48px |
| `space-16` | 64px |
| `space-20` | 80px |
| `space-24` | 96px |

## 4. Border Radius

| Token | Value |
|-------|-------|
| `radius-sm` | 4px |
| `radius-md` | 8px |
| `radius-lg` | 12px |
| `radius-xl` | 16px |
| `radius-full` | 100% |

## 5. Shadows

```css
:root {
  --shadow-sm: 0 1px 2px 0 rgba(0,0,0,0.04);
  --shadow-md: 0 4px 6px -2px rgba(0,0,0,0.04), 0 10px 15px -4px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 24px -6px rgba(0,0,0,0.04), 0 20px 32px -8px rgba(0,0,0,0.08);
}
```

## 6. Animation

```css
:root {
  --ease-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
}
```

## 7. Layout Principles

- Max content width: 1200px
- Grid: 12-column with 24px gap
- Responsive: 1→2→3 columns at 640/768/1024px
- Padding: `clamp(1rem, 4vw, 3rem)`
- 3-tier section spacing: 48px (tight), 96px (default), 128px (generous)

## 8. Component Presets

### Button
```html
<button class="inline-flex items-center justify-center gap-2 px-5 py-2.5 text-sm font-medium 
  bg-[var(--accent)] text-white rounded-lg 
  hover:bg-[var(--accent-hover)] transition-colors duration-150">
  Get Started
  <svg>...</svg>
</button>
```

### Card
```html
<article class="bg-[var(--bg-primary)] border border-[var(--border)] rounded-xl p-6 
  hover:shadow-md transition-shadow duration-250">
  <h3 class="text-lg font-semibold text-[var(--text-primary)]">Title</h3>
  <p class="mt-2 text-sm text-[var(--text-secondary)] leading-relaxed">Description</p>
</article>
```

### Input
```html
<input class="w-full px-4 py-2.5 text-sm bg-[var(--bg-primary)] border border-[var(--border)] 
  rounded-lg placeholder:text-[var(--text-tertiary)]
  focus:outline-none focus:border-[var(--accent)] focus:ring-2 focus:ring-[var(--accent-soft)]
  transition-colors duration-150" />
```

## 9. Responsive Breakpoints

| Breakpoint | Width |
|------------|-------|
| `sm` | 640px |
| `md` | 768px |
| `lg` | 1024px |
| `xl` | 1280px |
| `2xl` | 1536px |

## 10. Accessibility

- All interactive elements have visible focus states
- Color combinations pass WCAG AA (4.5:1 contrast)
- `prefers-reduced-motion` respected
- Alt text on all meaningful images
- Form labels associated with inputs