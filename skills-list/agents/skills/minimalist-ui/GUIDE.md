---
name: minimalist-ui
description: Clean, warm editorial interfaces with monochrome palettes, typographic contrast, flat bento grids, and muted pastels. No gradients or heavy shadows.
---

# minimalist-ui

Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows.

## 1. Color Palette

- **Background:** `#fafaf9` (Stone-50) or `#f5f5f4` (Stone-100)
- **Text Primary:** `#1c1917` (Stone-900)
- **Text Secondary:** `#44403c` (Stone-700)
- **Border:** `#d6d3d1` (Stone-300) / `#e7e5e4` (Stone-200)
- **Accent:** `#292524` (Stone-800) or `#a8a29e` (Stone-400)
- **Muted:** `#78716c` (Stone-500)
- **Invert:** `#fafaf9` (Stone-50) on dark
- **UI surfaces:** `#ffffff` → `#f5f5f4` → `#e7e5e4`

## 2. Typography

- **Display / Hero:** `'DM Serif Display', 'Playfair Display', 'EB Garamond'` — 72-96px, 1.0 line-height
- **Headings (h2-h4):** `'Inter', 'SF Pro', system-ui sans` — 18-48px, 1.2 line-height
- **Body:** `'Inter', 'SF Pro', system-ui sans` — 15-16px, 1.5-1.6 line-height, 0 letter-spacing
- **Small / Meta:** System-ui sans — 12-13px, uppercase with tracking 0.08em
- **Mono (code/data):** `'JetBrains Mono', 'SF Mono'`

## 3. Spacing System (8px grid)

| Token | Value | Usage |
|-------|-------|-------|
| space-3xs | 4px | icon gaps, inline |
| space-2xs | 8px | tight elements |
| space-xs | 12px | \( \hat{ } \)  |
| space-sm | 16px | small cards |
| space-md | 24px | card padding |
| space-lg | 32px | sections |
| space-xl | 48px | section gap |
| space-2xl | 64px | major section |
| space-3xl | 96px | page sections |
| space-4xl | 128px | hero spacing |

## 4. Layout Principles

- **Max-width:** 72rem (1152px) for content; 90rem (1440px) for hero/full-bleed
- **Grid:** 12-column flex or CSS grid at ≥1024px; collapse to 1-2 cols at ≤768px
- **Padding:** `px-6 md:px-12 lg:px-24`
- **Bento grids:** "flat" mode — no gap on inner tiles, subtle 1px border between them
- **Negative space:** 30-40% whitespace per viewport

## 5. Key Components

### Navigation
```html
<nav class="fixed top-0 inset-x-0 h-16 flex items-center justify-between px-6 md:px-12 z-50 bg-[#fafaf9]/80 backdrop-blur-md border-b border-stone-200">
  <a class="text-sm font-medium tracking-tight" href="/">Studio</a>
  <div class="hidden md:flex items-center gap-8 text-sm text-stone-600">
    <a href="#work">Work</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
```

### Hero (Editorial)
```html
<section class="pt-32 pb-24 px-6 max-w-6xl mx-auto">
  <h1 class="text-6xl md:text-8xl font-serif leading-[1.0] tracking-tight text-stone-900 max-w-4xl">
    Design that
    <span class="italic">feels</span>
    like
    <br/>
    <span class="text-stone-400">nothing else.</span>
  </h1>
  <p class="mt-8 max-w-xl text-stone-500 leading-relaxed">
    We craft digital experiences that prioritize clarity, warmth, and lasting impression over fleeting trends.
  </p>
</section>
```

### Feature Grid (Bento)
```html
<section class="max-w-6xl mx-auto px-6 py-24">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 border-t border-stone-200">
    <div class="p-8 border-b border-r border-stone-200">
      <h3 class="text-sm font-medium text-stone-900 mb-2">Strategy</h3>
      <p class="text-sm text-stone-500 leading-relaxed">Research-driven positioning that aligns brand and product vision.</p>
    </div>
    <div class="p-8 border-b border-r border-stone-200">
      <h3 class="text-sm font-medium text-stone-900 mb-2">Design</h3>
      <p class="text-sm text-stone-500 leading-relaxed">Clean interfaces built on typographic hierarchy and intentional space.</p>
    </div>
    <div class="p-8 border-b border-stone-200">
      <h3 class="text-sm font-medium text-stone-900 mb-2">Develop</h3>
      <p class="text-sm text-stone-500 leading-relaxed">Performant front-end engineering with attention to every detail.</p>
    </div>
  </div>
</section>
```

### Card (Default)
```html
<article class="group cursor-pointer">
  <div class="aspect-[4/3] bg-stone-100 mb-4 overflow-hidden">
    <img src="https://picsum.photos/seed/project/800/600" alt="Project" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700" />
  </div>
  <h3 class="text-sm font-medium text-stone-900">Project Name</h3>
  <p class="text-xs text-stone-500 mt-1">Brand · Web · 2026</p>
</article>
```

### Footer
```html
<footer class="border-t border-stone-200 py-16 px-6 mt-24">
  <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-start gap-8">
    <div>
      <p class="text-sm text-stone-900 font-medium">Studio</p>
      <p class="text-xs text-stone-500 mt-1">© 2026 All rights reserved.</p>
    </div>
    <div class="flex gap-8 text-xs text-stone-500">
      <a href="#" class="hover:text-stone-900 transition-colors">Twitter</a>
      <a href="#" class="hover:text-stone-900 transition-colors">GitHub</a>
      <a href="#" class="hover:text-stone-900 transition-colors">Dribbble</a>
    </div>
  </div>
</footer>
```

## 6. Motion (Subtle)

- **Hover (card):** `transform: scale(1.02)` + `opacity: 0.9` over 700ms ease
- **Page load:** staggered fade-up on sections — `translateY(24px) → 0` + `opacity: 0 → 1`, 600ms each, 100ms stagger
- **Nav link:** color transition 200ms
- **No parallax, no spinning icons, no particle effects**

## 7. Typography Scale (Editorial)

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Hero display | 96px | 400 | 1.0 |
| h2 | 48px | 400 | 1.1 |
| h3 | 32px | 500 | 1.2 |
| h4 | 24px | 500 | 1.3 |
| Body | 16px | 400 | 1.6 |
| Small | 13px | 400 | 1.5 |
| Meta (uppercase) | 12px | 500 | 1.4 |

## 8. Responsive Breakpoints

- **Mobile:** ≤640px — single column, 16px padding, hero 48px
- **Tablet:** 768-1024px — 2 columns, 32px padding
- **Desktop:** ≥1024px — 3+ columns, 96px padding

## 9. Accessibility

- Color contrast ≥ 4.5:1 for text
- Focus-visible ring: `2px solid #292524` offset 2px
- Reduced motion: respect `prefers-reduced-motion`
- Labels on all form inputs
- Alt text on all images
