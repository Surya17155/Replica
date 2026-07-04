---
tags: [reference, motionsites, quality-benchmark]
---

# motionsites.ai — Quality Benchmark

The reference standard for prompts produced by the design-to-prompt skill. **Every output here must match this level of detail.**

## What motionsites.ai is

A premium library of "AI design prompts, hero sections, animated backgrounds, gradients, and templates" — marketed as one-click design superpowers for building AI-generated websites. Library is organized into:

- **Hero Prompts** — single-shot hero sections (above-the-fold)
- **Sections** (NEW) — reusable blocks like marquees, FAQs, pricing
- **Backgrounds** (NEW) — animated backgrounds
- **Full Landing Prompts** — entire pages top-to-bottom

Categories visible in the library: Interactive Discovery, Clarity Core, Dreamcore Landing, Organic Odyssey, Bold Studio, Pulse 3D, Prisma Creative Studio, Neural Interface, 3D Portfolio, 3D Story, Art Landing, Wellness Hero, Velorah, Cosmic, Web3 EOS Hero, Bloom, Aetheris Voyage, Future-State, CoderCrest, SaaS Value, VEX Ventures, Luxury Focus, SkyElite Private Jets, Synthesis, Urban Jungle, Conversion, Reveal Hero, Modern Agency, Cyberpunk Reveal, Liquid Glass Agency, Gateway Portal, Luxury Ecommerce Design, Audio Showcase, Grow AI Talent Platform, Luxury Real Estate, Aethera Studio, Glassmorphism Agency Hero, Mythic Naturecore, Asme, Cinematic Brand, Logoisum Video Agency Hero, 3D Collectible Hero, Innovation, Interstellar, Mango, Mystique, Enigma, Noir, Luma AI, Pixel Pioneers, Magnetic Dreams, Rive Forge, Aurora Pulse, Velocity Labs, Cyber Suite, Neon Matrix, Quantum Flux, Mirrors Edge, etc.

≈100+ prompt entries in total.

## What motionsites.ai Prompt Quality Looks Like

A motionsites.ai prompt is **not a description** — it is an engineering specification. It includes:

1. **Tech stack declaration** — usually React + Vite + TypeScript + Tailwind CSS + Framer Motion + Lucide React, but sometimes GSAP/Motion One. Specific package versions when relevant.

2. **Global design system** — fonts (with Google Fonts URLs), colors (CSS custom properties), `borderRadius`, custom theme extensions.

3. **Section-by-section structure** — every visible section ordered top-to-bottom, with:
   - Background color or gradient direction + stops
   - Section-to-section transition (rounded-top-class, negative margin pull-up)
   - Every component within it explicitly specified

4. **Component-level specificity:**
   - Fonts loaded from `https://fonts.googleapis.com/css2?...` URLs with all weights
   - `clamp()` responsive sizing everywhere (e.g., `clamp(3rem, 12vw, 160px)`)
   - Buttons: full tailwind class string + multi-layer box-shadow (`shadow-[0px_4px_4px_rgba(181,1,167,0.25),4px_4px_12px_#7721B1_inset]`)
   - Videos: full `<video autoPlay muted loop playsInline className="object-cover absolute inset-0 w-full h-full">`
   - Glassmorphism panels: full CSS including `::before` gradient border `mask-composite` pattern
   - Animations: full Framer Motion `initial / animate / transition` blocks with delay, duration, ease

5. **Animation reference table** — every animated element listed with `Element / Library / initial / animate / delay / duration / easing`.

6. **Reusable components** — each named (PascalCase) and mapped to a file path: `src/components/HeroSection.tsx`.

7. **File structure** — complete `src/` layout.

8. **Dependencies list** — npm packages with usage.

## The 15 Critical Rules (this skill's rules)

(See [[quick-aesthetic-guide]] for context)

1. **Exact classes, not adjectives** — never "nice button", always `bg-gradient-to-r from-[#18011F] via-[#B600A8] to-[#7621B0] text-white rounded-full px-10 py-3.5 font-medium uppercase tracking-widest ...`
2. **Hex codes, never color names** — `bg-[#0C0C0C]`, not "dark".
3. **`clamp()` for fluid typography** — `fontSize: clamp(3rem, 12vw, 160px)`.
4. **4-part animation tuple** — `initial`, `animate`, `delay`, `duration`. Every element.
5. **Glassmorphism CSS block is complete** — `backdrop-filter`, `background-blend-mode`, `box-shadow`, `::before` gradient border `mask-composite`.
6. **Buttons have box-shadow** — multi-layer. Premium.
7. **Videos: 5 attributes** — `autoPlay muted loop playsInline` + `object-cover`.
8. **Section transitions** — `rounded-t-[60px] -mt-14 z-10`.
9. **Marquees** — direction, speed, technique (CSS keyframes vs. GSAP vs. scroll-driven).
10. **Card image grids** — column width split (`w-[40%]` / `w-[60%]`) + image heights via `clamp()`.
11. **PascalCase components** — `src/components/HeroSection.tsx`.
12. **Tailwind mobile-first** — base → sm → md → lg with explicit values.
13. **Decorative elements** — explicit position classes + width per breakpoint + FadeIn animation values.
14. **Custom fonts** — `@font-face` block with src URL.
15. **Scroll offset** — `['start 0.8', 'end 0.2']` for `useScroll`.

## Why motionsites.ai Works

A user can copy one motion-site prompt, paste it into Lovable or Bolt.new, and the resulting build visually matches the screenshot to ≈95% fidelity. The remaining 5% is the user's choice of stock images, exact copy text, and one or two minor configuration knobs.

That is the bar. This brain exists to clear it.

## Related
- [[prompt-output-template-hero]] — our hero template (matched to this bar)
- [[prompt-output-template-landing-page]] — our full-landing template
- [[design-to-prompt-brain]] MOC

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

*Every file in the corpus is reachable from the root in ≤5 hops.*