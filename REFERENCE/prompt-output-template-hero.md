---
tags: [reference, prompt-template, hero, output-spec]
---

# Hero Section Prompt — Output Specification

When the user wants **only** the hero/above-the-fold section, produce a prompt using this exact structure. The output must read like a complete engineering specification, not a description.

---

## Structure (in this order)

```
Build a [adjective] hero section for "[Product Name]" using [Tech Stack].

---

## Page Frame
- Outer wrapper: [Tailwind classes for outermost div]
- Hero container: [classes, border-radius via rounded-Xxl or rounded-[Npx], overflow-hidden, background]

---

## Background
[One of these — be specific:]
- Solid color:  e.g. `bg-[#0A0A0A]`
- Gradient:     e.g. `bg-gradient-to-br from-[#0F0F1A] via-[#1A0B2E] to-[#2D0F4F]`
- Image:        `<img className="absolute inset-0 w-full h-full object-cover" src="..." />`
- Video:        `<video autoPlay muted loop playsInline className="absolute inset-0 w-full h-full object-cover" src="..." />`

Overlay (if any):
  `<div className="absolute inset-0 bg-black/30" />`  — or gradient

Texture (if any):
  fixed `z-50 pointer-events-none mix-blend-overlay opacity-[N]` with `background: url('/noise.png') ; background-size: 200px`

Bottom fade-out (if any):
  `<div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-[bg] to-transparent" />`

---

## Global Styles

### Fonts
[Font name, weights, Google Fonts URL or @font-face with src URL]
[Tailwind mapping: `--font-display: 'PP Mondwest', sans-serif;` in tailwind.config]

### CSS Custom Properties
[All CSS variables: --bg, --text, --accent, --surface in HSL or hex]

### CSS Utility Classes
[Any special classes — only when needed]
Example for liquid-glass:
```css
.liquid-glass {
  backdrop-filter: blur(20px) saturate(180%);
  background: rgba(255,255,255,0.01);
  border-radius: 24px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  position: relative;
}
.liquid-glass::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.05) 30%, transparent 60%);
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  pointer-events: none;
}
```

### @keyframes
[Any custom keyframes, e.g.]
```css
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(-12px); }
}
```

---

## Navbar

[Position: fixed / sticky / absolute, full description of wrapper + inner pill/bar classes]

Logo:
  - SVG icon, text, or image
  - Font, size, color, classes

Nav links (count, labels, classes, hover behavior)

CTA button (label, gradient, full class string with shadow, icon)

Mobile (hamburger logic, mobile menu structure)

Scroll behavior (what changes when `scrollY > threshold`)

---

## Hero Content

### Badge / Eyebrow
- Classes: `inline-flex items-center gap-2 px-3 py-1 rounded-full border border-white/15 bg-white/5 text-xs uppercase tracking-widest`
- Text (or placeholder)
- Icon (if any)
- Framer Motion: `initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.1 }}`

### Headline
- Tag: `<h1>`
- Text (with line breaks or placeholder)
- Tailwind: explicit `text-clamp(3rem, 12vw, 160px) font-bold tracking-[-0.04em] leading-[0.9]`
- Color: solid or class `bg-clip-text text-transparent bg-gradient-to-r from-[a] via-[b] to-[c]`
- Mixed font: italic serif accent word wrapped in `<span className="font-serif italic ...">`
- Animation

### Subheadline
- Tag: `<p>`
- Text + classes (`text-lg text-white/60 max-w-xl`)
- Animation

### CTA Buttons
- Primary: full class string with multi-layer box-shadow, icon markup
  - Example: `<motion.button whileHover={{ scale: 1.02 }} className="bg-gradient-to-r from-[#18011F] via-[#B600A8] to-[#7621B0] text-white rounded-full px-10 py-3.5 font-medium uppercase tracking-widest shadow-[0px_4px_4px_rgba(181,1,167,0.25),4px_4px_12px_#7721B1_inset] outline outline-2 outline-white -outline-offset-[3px]" />`
- Secondary: ghost button with hover border gradient

### Hero Visual Element
- Product image / portrait — position, size classes, src URL (from user's hosted link)
- Magnet (mouse-follow) effect — wrap in motion component with spring
- Parallax — `useScroll({ target, offset: ['start start', 'end start'] })` + transform.y
- Decorative 3D objects — each with position + width per breakpoint + FadeIn values

---

## Floating Cards (overlay on hero, if any)

For each card:
- Position: `absolute bottom-8 left-8` (or right)
- Background: `backdrop-blur-xl bg-white/10 border border-white/15`
- Content markup
- Animation values
- Corner cutout mask if applicable

---

## Animations Reference Table

| Element | Library | initial | animate | delay | duration |
|---------|---------|---------|---------|-------|----------|
| Navbar | Framer | opacity:0, y:-20 | opacity:1, y:0 | 0s | 0.6s |
| Badge | Framer | opacity:0, y:20 | opacity:1, y:0 | 0.10s | 0.6s |
| Headline | Framer | opacity:0, y:40 | opacity:1, y:0 | 0.15s | 0.8s |
| Subheadline | Framer | opacity:0, y:30 | opacity:1, y:0 | 0.35s | 0.7s |
| CTA Button | Framer | opacity:0, y:20 | opacity:1, y:0 | 0.55s | 0.6s |
| Hero Image | Framer | scale:0.9, opacity:0 | scale:1, opacity:1 | 0.7s | 0.9s |
| Floating Card 1 | Framer | opacity:0, y:20 | opacity:1, y:0 | 0.9s | 0.7s |
| (all easings) | ease: [0.25, 0.1, 0.25, 1] | | | | |

---

## Reusable Components

For each:
- Name (PascalCase) → file path (`src/components/HeroCard.tsx`)
- Props interface
- Behavior description
- Full class string
- Special logic (e.g., MagnetMouse wrapper, useScroll hook)

---

## Dependencies

```json
{
  "react": "^18.x",
  "react-dom": "^18.x",
  "framer-motion": "^11.x",
  "lucide-react": "^0.x",
  "tailwindcss": "^3.x"
}
```

(Dev deps: vite, typescript, @vitejs/plugin-react, @types/react, @types/react-dom, autoprefixer, postcss)

---

## File Structure

```
src/
├── components/
│   ├── HeroSection.tsx
│   ├── Navbar.tsx
│   ├── HeroHeadline.tsx
│   ├── HeroImage.tsx
│   ├── FloatingCard.tsx
│   └── DecorElement.tsx
├── styles/
│   └── index.css
├── App.tsx
└── main.tsx
index.html
package.json
vite.config.ts
tailwind.config.js
tsconfig.json
```

---

## Tone Rules

- Write in **second-person imperative**: "Build...", "Create...", "Use...", "Place..."
- Use `##` headers
- Backticks for class strings and code values
- Markdown tables for animation references
- Label every URL with what it's for
- `[PLACEHOLDER: ...]` for genuinely uncertain values
- **Never** "approximately" or "roughly"
- Output is copy-paste ready

## Related
- [[motionsites-ai]] — quality benchmark this spec is matched to
- [[image-analysis-checklist-hero]] — checklist before writing this prompt
- [[conversational-workflow]] — how we get to producing this prompt
- [[asset-inventory]] — required URLs to embed inline

---

## 🔗 ↑ Go Back Up

This file is part of **REFERENCE hub**. To navigate:

← Parent folder: [[../_root|_root]]
← Hub: [[../README|REFERENCE — Central Hub]]
← 02-References: [[../../README|02-References]]
← Brain root: [[../../README|00-brain-index]]

**Wired from:**
- [[../ultra-prompt-generator/DESIGNER/skill-router|skill-router]] (selection logic)
- [[../DIRECTOR/rules-engine|DIRECTOR rules engine]] (workflow)

*Every file in the corpus is reachable from the brain root in ≤5 hops.*

---

## 🧭 Navigation

← [[README|REFERENCE hub]]
← [[../README|02-References]]
← [[../../README|00-brain-index]]
← [[../DIRECTOR/rules-engine|DIRECTOR rules engine]]
← [[../ultra-prompt-generator/DESIGNER/skill-router|skill-router]]

**See also:**
- [[component-patterns/_index]]
- [[css-presets/_index]]
- [[prompt-output-template-hero]]
