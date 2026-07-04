---
tags: [reference, aesthetic, guide, taxonomy]
---

# Quick Aesthetic Identification Guide

Match the screenshot's visual cues to a known aesthetic → apply matching CSS patterns + tech choices. This is how you pick defaults when writing the prompt.

---

## The 6 Core Aesthetics

### 1. Glassmorphism
**Cues:** Dark bg, blur panels, frosted glass, soft transparency borders
**Stack:** Tailwind + custom `.liquid-glass` class
**Key patterns:**
- `backdrop-blur-X` on all panels
- `rgba(255,255,255,0.01)` background
- `::before` gradient border pseudo-element with `mask-composite: exclude`
- Multi-color blurred "light blob" backgrounds
- Layered translucent cards stacking

See: [[05-Aesthetics/glassmorphism]] for details

### 2. Dark Portfolio
**Cues:** Black/near-black bg, gradient text, heavy display font
**Stack:** Tailwind + Framer Motion + Google Fonts (high weights)
**Key patterns:**
- `text-clamp(3rem, 12vw, 160px)` typography
- `bg-clip-text text-transparent bg-gradient-to-r from-X via-Y to-Z` for headline
- Tight `tracking-[-0.04em]`
- Framer Motion entrance: stagger fade-up
- Often yellow/white accent + lots of black

See: [[05-Aesthetics/dark-portfolio]]

### 3. Fintech / SaaS
**Cues:** Light gray bg, video hero inside rounded card, clean typography
**Stack:** Tailwind + Framer Motion + Lucide + (often Playwright mocked-up UI inside)
**Key patterns:**
- Rounded card hero: `rounded-[40px]` outside a `bg-[#F5F5F5]` page
- Negative letter-spacing on display: `tracking-[-0.04em]`
- Fonts: TT Norms, Inter, SF Pro, Geist
- Product UI image inside hero card
- Tab/badge UI elements that pop
- Trusted-by logo strip below hero

See: [[05-Aesthetics/fintech-saas]]

### 4. Creative Studio
**Cues:** White bg, serif+sans mix, column-based layout
**Stack:** Tailwind + custom fonts (PP Mondwest, Instrument Serif)
**Key patterns:**
- Italic serif accent word inside otherwise sans-serif headline
- Heavy use of static imagery (no video)
- Marquee logo strip
- Project cards with stacked layout
- Lots of typography as design

See: [[05-Aesthetics/creative-studio]]

### 5. NFT / Web3
**Cues:** Space theme, neon accents (mint / green / magenta), monospace text
**Stack:** Tailwind + Framer Motion + custom fonts (usually Anton or Space Grotesk)
**Key patterns:**
- Anton or Space Mono font
- Neon accents: `#6FFF00`, `#00FFFF`, `#FF00FF`
- Liquid-glass + animated noise
- Video backgrounds (3D-rendered)
- High-contrast dark + neon

See: [[05-Aesthetics/nft-web3]]

### 6. Modern Agency
**Cues:** Minimal white, mid-clamp typography, pill buttons, fixed bottom nav
**Stack:** Tailwind + Framer Motion + Intersection Observer fade-ins
**Key patterns:**
- White page with subtle noise overlay
- Big `clamp()` typography
- Pill-shaped buttons
- `tracking-[-0.04em]`
- Sticky bottom nav (a la Vercel)
- Subtle hover micro-interactions

See: [[05-Aesthetics/modern-agency]]

---

## How to Choose Between Aesthetics

When in doubt:

1. **Background color** — dark vs. light = #1 filter
2. **Effect density** — lots of blur/transparency = glassmorphism; clean = fintech / modern agency
3. **Typography mix** — italic serif accent = creative studio; monolithic display = dark portfolio
4. **Accent color style** — neon = web3; gradient text = dark portfolio
5. **Asset strategy** — heavy video = web3 / glassmorphism; static photography = creative studio

---

## Related
- [[motionsites-ai]] — quality bar across all aesthetics
- [[02-References#aesthetics|all 6 aesthetic notes]]
- [[conversational-workflow]] — when to apply these defaults

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
- [[aesthetic-cards/_index]]
- [[css-presets/_index]]
- [[prompt-output-template-hero]]
