---
name: redesign-existing-projects
description: Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS.
---

# redesign-existing-projects

Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS.

## 1. The Audit Process

### Phase 1: Visual Audit

Run through this checklist against the existing codebase:

**Typography**
- [ ] Does it use a system-ui stack or default fonts? (bad)
- [ ] Are font sizes too uniform? (all text same size = bad)
- [ ] Is line-height below 1.5 for body text? (bad, too cramped)
- [ ] Are there more than 2 font families? (bad, inconsistent)
- [ ] Is letter-spacing at 0 for all text? (bad, misses hierarchy)
- [ ] Does body copy exceed 75 characters per line? (bad, hard to read)

**Spacing**
- [ ] Is spacing inconsistent? (e.g., 15px, 17px instead of 8px grid)
- [ ] Are sections too close together? (< 80px between sections = bad)
- [ ] Are elements touching or overlapping unintentionally? (bad)
- [ ] Is padding uniform for all containers? (excessive padding everywhere = bad)

**Color**
- [ ] Are there more than 4 colors in the palette? (bad)
- [ ] Is the primary color too bright or saturated? (bad, looks cheap)
- [ ] Are shadows visible and generic? (box-shadow with full black = bad)
- [ ] Is there an unused color lingering in the codebase? (bad)
- [ ] Are success/error/warning colors the default browser palette? (bad)

**UI Components**
- [ ] Are buttons using default browser styles or <Button> without customization? (bad)
- [ ] Are cards using the default shadows and borders? (bad, generic)
- [ ] Are inputs still using default border color? (bad, gray #ccc)
- [ ] Are modals showing without animation? (bad, jarring)
- [ ] Are navigation items too far apart or too close together? (bad)
- [ ] Are dropdowns using browser default styling? (bad)
- [ ] Are table headers using default browser styling? (bad)

**Images & Media**
- [ ] Are images not optimized (large file sizes without lazy loading)? (bad)
- [ ] Is there no loading skeleton or spinner for images? (bad UX)
- [ ] Are icons using multiple styles (filled + outlined)? (bad, inconsistent)
- [ ] Are icons raster instead of SVG? (bad, blurry on retina)

**Animations**
- [ ] Are there no micro-interactions on hover/focus? (bad, feels dead)
- [ ] Are page transitions hard cut (no fade or slide)? (bad, feels cheap)
- [ ] Are loading states using text "Loading..." instead of skeleton/spinner? (bad)
- [ ] Is the animation timing arbitrary (non-standard durations)? (bad, feels off)
- [ ] Are animations disabled on reduced-motion without fallback? (bad, accessibility issue)

### Phase 2: Brand & Identity Audit
- [ ] Is there a defined color palette in CSS custom properties? (if not, add one)
- [ ] Are there custom properties for spacing? (if not, add 8px-based system)
- [ ] Are font faces loaded properly? (if not, add @font-face or import)
- [ ] Is there a consistent border-radius across elements? (if not, standardize to 3 values)
- [ ] Are shadows defined as custom properties? (if not, define 3 levels)
- [ ] Is animation timing defined as custom properties? (if not, define fast/base/slow)

## 2. The Upgrade Playbook

### Typography Overrides
```css
/* BEFORE (generic) */
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }

/* AFTER (premium) */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300..700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

:root {
  --font-body: 'Inter', system-ui, sans-serif;
  --font-display: 'Playfair Display', 'Georgia', serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;
}
```

### Spacing Standardization
```css
:root {
  --space-xs: 0.25rem;  /* 4px */
  --space-sm: 0.5rem;   /* 8px */
  --space-md: 1rem;     /* 16px */
  --space-lg: 2rem;     /* 32px */
  --space-xl: 4rem;     /* 64px */
  --space-2xl: 6rem;    /* 96px */
  --space-3xl: 8rem;    /* 128px */
}
```

### Shadow Overrides
```css
:root {
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 6px -2px rgba(0,0,0,0.05), 0 12px 16px -4px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 24px -6px rgba(0,0,0,0.08), 0 20px 32px -8px rgba(0,0,0,0.12);
}
```

### Animation Overrides
```css
:root {
  --ease-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 3. The 10-Minute Quick Fix

When time is limited, apply these 5 changes for maximum visual impact:

1. **Add a premium font** (Inter + Playfair Display or Space Grotesk)
2. **Fix spacing** — add 6rem (96px) between sections, use 8px grid
3. **Reduce color palette** — pick 3 colors max and stick to them
4. **Standardize shadows** — use 3 levels only
5. **Add micro-interactions** — hover states on buttons/links/cards with 200ms transition

## 4. CSS Framework Specific Notes

### Tailwind CSS
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        display: ['Playfair Display', 'Georgia', 'serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        '30': '7.5rem',
      },
      boxShadow: {
        'premium': '0 4px 6px -2px rgba(0,0,0,0.05), 0 12px 16px -4px rgba(0,0,0,0.1)',
      }
    }
  }
}
```

### Chakra UI / shadcn
- Override `theme` or `cssVariables` with the tokens above
- Replace default `borderRadius` with custom `--radius` tokens
- Replace default shadows with premium shadows

## 5. Anti-Patterns to Remove

| Cheap Pattern | Premium Replacement |
|--------------|-------------------|
| `box-shadow: 0 2px 10px rgba(0,0,0,0.1)` | Layered shadows with 0.05 opacity max |
| `border-radius: 10px` | Standardize to 4px / 8px / 16px only |
| `font-weight: 600` everywhere | Use 300/400 for body, 600/700 for headers |
| Full black `#000000` or `rgba(0,0,0,*)` | Use dark gray `#1A1A1A` or `#333` |
| Full white `#FFFFFF` background | Use off-white `#FAFAFA` or `#F5F5F5` |
| `transition: all 0.3s` | Specific properties + custom timing |
| Default blue link color | Use brand accent color + underline on hover |

## 6. Quality Checklist (Final)