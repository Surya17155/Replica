---
tags: [reference, prompt-template, landing-page, output-spec]
---

# Full Landing Page Prompt — Output Specification

When the user wants the **entire page top-to-bottom**, produce a prompt using this structure. The output is organized as numbered sections matching the page's actual top-to-bottom order.

---

## Structure (in this order)

```
Build a [adjective] [page type] landing page for "[Product Name]" using [Tech Stack].

---

## Global Design System

### Tech Stack
React + TypeScript + Vite + Tailwind CSS + Framer Motion + Lucide React
(+ GSAP if scroll-driven prompts; + Motion One for lowercase variants)

### Fonts
- Display: [name], weights [300, 400, 500, 600, 700, 900]
- Body:    [name], weights [400, 500]
- Mono:    [name] (if any)
[Google Fonts URL or @font-face]

Map to Tailwind in `tailwind.config.js`:
```js
fontFamily: {
  display: ['"PP Mondwest"', 'Inter', 'sans-serif'],
  body:    ['"Inter"', 'sans-serif'],
  mono:    ['"JetBrains Mono"', 'monospace'],
}
```

### Color System
CSS variables (added to `:root` in `index.css`):
```css
--bg:        #0A0A0A;
--text:      #F5F5F5;
--text-mute: rgba(245,245,245,0.6);
--accent:    #B600A8;
--accent-2:  #7621B0;
--surface:   #1A1A1F;
--border:    rgba(255,255,255,0.08);
```

Plus Tailwind theme extension for direct use:
```js
colors: {
  bg:       'var(--bg)',
  text:     'var(--text)',
  accent:   'var(--accent)',
}
```

### Global CSS
```css
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; overflow-x: hidden; background: var(--bg); color: var(--text); }
body { font-family: var(--font-body); -webkit-font-smoothing: antialiased; }
```

Custom utility classes (one block each):
- `.liquid-glass` (full CSS — see template below)
- `.hero-heading` (gradient text class)
- `.accent-gradient` (button gradient)
- `.text-stroke` (outlined text effect)

### Tailwind Config Extensions
```js
{
  extend: {
    colors: { /* see Color System */ },
    fontFamily: { /* see Fonts */ },
    borderRadius: { 'hero': '40px', 'pill': '999px' },
    animation: {
      'float':   'float 6s ease-in-out infinite',
      'pulse':   'pulse 2s ease-in-out infinite',
      'spin-slow': 'spin 8s linear infinite',
    },
    keyframes: { /* full @keyframes */ }
  }
}
```

---

## SECTION ORDER

1. Navbar — top floating pill or full bar
2. Hero — main above-the-fold
3. Marquee — logos / text ticker
4. About — context paragraph
5. Services / Features — grid or list
6. Projects / Portfolio — case studies
7. Pricing — tiered plans
8. Testimonials — quotes or carousel
9. FAQ — accordion
10. Footer — multi-column + CTA

(Only include sections actually visible. Order matters.)

---

## 1. NAVBAR SECTION

[Position: `fixed top-X left-1/2 -translate-x-1/2 z-50` for pill, or `absolute top-0 w-full` for full-bar]

Inner wrapper: `flex items-center justify-between rounded-full bg-black/30 backdrop-blur-xl border border-white/10 px-6 py-3`

Logo: `<svg>` markup or text `className="text-lg font-semibold tracking-tight"`

Nav links (4-7): flex with `gap-8 text-sm font-medium uppercase tracking-widest text-white/70 hover:text-white`

CTA button (right): full class + gradient + icon

Mobile: hamburger → menu opens below navbar

Scroll behavior: when `scrollY > 80`, increase bg opacity/glow.

[Embed any logo image URLs inline at the right place: `src="[USER_HOSTED_LOGO_URL]"`.]

---

## 2. HERO SECTION

[Follow [[prompt-output-template-hero]] — same level of detail]

---

## 3. MARQUEE SECTION

Background: `bg-[var(--surface)]` or transparent

Inner: `<div className="flex gap-12 animate-marquee">` or scroll-driven GSAP container

Items: image tiles, text logos, or mixed

Direction: left = `translateX(-100%)` to `translateX(0)` ; right = vice versa

Speed: `animation-duration: 30s` or scroll-velocity based

Optional: `pause on hover` via `group-hover:animation-play-state:paused`

---

## 4. ABOUT / INFO SECTION

Background: solid color, often white if hero was dark (with rounded-top transition: `rounded-t-[60px] -mt-14 z-10`)

Heading style: same gradient as hero? Or different? Specify.

Paragraph: animated reveal
- Option A: character-by-character (split into spans, stagger fade)
- Option B: opacity-driven scroll (`whileInView`)

Decorative corner images / 3D objects: each with position + FadeIn values

CTA button: optional repeat of hero CTA, maybe smaller variant

---

## 5. SERVICES / FEATURES SECTION

Layout: vertical list with dividers, OR 3-col grid, OR bento

Numbered items (e.g., 01, 02, 03): styled with mono font
- Item format: `[number] [icon] [item name] [description]`
- Dividers: `border-b border-white/10`

Background: light or dark (matches vertical rhythm)

[If items have images, embed URL inline: `<img src="[USER_HOSTED_FEATURE_URL]" />`.]

---

## 6. PROJECTS / PORTFOLIO SECTION

Layout: grid OR bento OR stacked sticky cards

Stacking card effect:
```js
// Each card sticky, scales down as next one scrolls over
useScroll({ offset: ['start start', 'end start'] })
// Card has transform: scale(0.95 - progress)
```

Card content:
- Number (e.g., "01") + category + title + CTA button
- Image grid: split (`w-[40%]` / `w-[60%]`)
- Image heights: `h-[clamp(240px, 40vw, 480px)]`
- Heavy rounding: `rounded-[40px]`

Card border: `border border-white/10`, background `bg-white/[0.02]`

[Embed image URLs inline.]

---

## 7. PRICING SECTION

Card variants: dark + light (often one is featured — highlighted)

Card structure: `<div className="rounded-3xl p-8 bg-[#111] border border-white/10">`

Per card: plan name, price (e.g., `$29`), description, feature list (×N), button

[Optional toggle: monthly/yearly — state via `useState`]

---

## 8. TESTIMONIALS SECTION

Variant A: carousel (`useMotionValue + transform`-driven slider)
Variant B: stacked static cards

Avatar: circular `rounded-full w-12 h-12 object-cover`
Author info: name + role/company

[Embed avatar URLs inline.]

---

## 9. FAQ SECTION

Accordion: each item toggleable via `useState`/`useAnimate`

Item structure:
```jsx
<button onClick={...} className="flex items-center justify-between w-full py-6 border-b border-white/10">
  <span className="text-lg font-medium">{question}</span>
  <Plus className={open ? 'rotate-45 transition-transform' : 'transition-transform'} />
</button>
<motion.div initial={false} animate={{ height: open ? 'auto' : 0 }} className="overflow-hidden">
  <p className="text-white/60 pb-6">{answer}</p>
</motion.div>
```

---

## 10. FOOTER

Layout: 4-column grid or 2-row flex

Columns: brand info, links, links, social

Copyright bar: bottom strip with `text-xs text-white/40`

Optional CTA (newsletter):
`<input className="..." /> <button>Subscribe</button>`

Optional GSAP marquee text (the brand name × large scale, scrolling)

---

## REUSABLE COMPONENTS

For each:
- `ComponentName (`{filename}.tsx`)` with PascalCase
- Props, behavior, full class string, any special logic

Common reusable bits in this stack:
- `<Magnetic>` — mouse-follow wrapper (Framer Motion spring)
- `<RevealOnScroll>` — opacity/translate-y whileInView wrapper
- `<AnimatedMarquee>` — generic marquee component

---

## ANIMATIONS

### Entrance (page-load)
[Same table format as hero template — Element / Library / initial / animate / delay / duration / easing]

### Scroll-driven
- IntersectionObserver triggers (`whileInView`)
- GSAP ScrollTrigger (for hero scroll-motion sites)
- Framer Motion `useScroll` + `useTransform`

### Continuous
- Marquee (`animation: marquee 30s linear infinite`)
- Float (`transform: translateY(-Npx)`, 6s ease-in-out infinite)
- Magnetic (mouse-follow spring)
- Parallax columns (translate y/x based on scroll position)

---

## DEPENDENCIES

```json
{
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "framer-motion": "^11.11.0",
    "lucide-react": "^0.451.0",
    "clsx": "^2.1.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.10",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.2",
    "typescript": "^5.6.0",
    "vite": "^5.4.0",
    "tailwindcss": "^3.4.13",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.47"
  }
}
```

(Add `gsap` if using GSAP, `@luma.gl/react` or similar if specialised)

---

## FILE STRUCTURE

```
src/
├── components/
│   ├── Navbar.tsx
│   ├── Hero.tsx
│   ├── Marquee.tsx
│   ├── About.tsx
│   ├── Services.tsx
│   ├── Projects.tsx
│   ├── Pricing.tsx
│   ├── Testimonials.tsx
│   ├── FAQ.tsx
│   ├── Footer.tsx
│   └── ui/
│       ├── Magnetic.tsx
│       ├── RevealOnScroll.tsx
│       └── AnimatedMarquee.tsx
├── hooks/
│   └── useMousePosition.ts
├── styles/
│   └── index.css
├── lib/
│   └── utils.ts
├── App.tsx
└── main.tsx
index.html
package.json
vite.config.ts
tailwind.config.js
tsconfig.json
```

---

## Related
- [[motionsites-ai]]
- [[prompt-output-template-hero]]
- [[image-analysis-checklist-landing-page]]
- [[conversational-workflow]]

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
- [[motion-effects/_index]]
- [[prompt-output-template-landing]]