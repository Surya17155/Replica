---
tags: [reference, checklist, hero, analysis]
---

# Image Analysis Checklist — Hero Section

Run **silently** before producing any hero prompt. Tick every box. These items become the output spec.

---

## Layout & Frame
- [ ] Outer page background color (what surrounds the hero card, if any)
- [ ] Hero container shape — full-screen OR padded/rounded card inside a wrapper?
- [ ] Exact border-radius of container (`rounded-3xl` = 24px, `rounded-[40px]`, `rounded-[60px]`, etc.)
- [ ] Overflow behavior (does content bleed off bottom edge?)
- [ ] z-layering — animation/illustration stack order (video → overlay → content?)

## Background
- [ ] Solid color, gradient, image, or video?
- [ ] If video: motion, mood, color palette
- [ ] If gradient: direction, from-color (hex), to-color (hex)
- [ ] Dark overlay on top? (`bg-black/20`, `bg-black/40`)
- [ ] Texture or noise layer? (fixed, `mix-blend-mode`, opacity, background-size)
- [ ] Bottom fade-out gradient? (`bg-gradient-to-t from-[color] to-transparent`, height)

## Navbar
- [ ] Fixed/floating, sticky, or static?
- [ ] Pill/floating shape, or full-width bar?
- [ ] Background: transparent, glass (`backdrop-blur`), solid white, dark?
- [ ] Logo: text only, SVG icon, image? Font? Size? Color?
- [ ] Nav links: count, labels, color, font size, uppercase?
- [ ] Hover effects (opacity, color, underline?)
- [ ] CTA button in nav: text, shape, colors, icon inside?
- [ ] Mobile: hamburger menu? What appears when opened?
- [ ] Scroll behavior (shadow/bg change at `scrollY > threshold`)

## Hero Headline & Typography
- [ ] Main headline text (or placeholder if illegible)
- [ ] Font family (serif, sans-serif, monospace, display, grotesk?)
- [ ] Font weight (300/400/500/600/700/900)
- [ ] Font size as `clamp()`: `clamp(smallPx, Xvw, largePx)`
- [ ] Letter-spacing: tight (`-0.04em`), normal, or wide (`0.1em`)
- [ ] Line-height: tight (0.9–1.0), normal (1.2), relaxed (1.5)
- [ ] Color: solid or gradient (direction + hex stops)
- [ ] Italic/serif accent word mixed inside sans-serif headline?
- [ ] Animated text (fade in, slide up, typewriter, character reveal)?
- [ ] Subheadline/tagline: size, color, font, opacity?

## Visual Focal Element
- [ ] Hero image / portrait / product mockup?
- [ ] Position (center, right side, absolute overlay)
- [ ] Special effects: magnetic hover, parallax, float animation?
- [ ] Decorative 3D objects / corner elements?
- [ ] Badge / pill / tag floating near headline ("New", "AI-powered", etc.)?

## CTA Buttons
- [ ] How many buttons? Labels?
- [ ] Primary: background (gradient/solid/glass), text color, shape, padding, shadow
- [ ] If gradient: gradient direction + hex stops
- [ ] Inner/outer box-shadow (exact multi-layer values)
- [ ] Icon inside button (arrow, chevron, star, sparkle)
- [ ] Secondary/ghost: border, background, text color
- [ ] Hover animations: scale, glow, color change?

## Floating / Overlay Cards
- [ ] Stat cards, info panels, floating UI?
- [ ] Position (bottom-left, bottom-right, absolute)
- [ ] Background (glass/blur, solid white, dark)
- [ ] Content (text, numbers, icons)
- [ ] Cutout/mask effect for corner integration?

## Animations & Motion
- [ ] Entrance animations (fade in / slide up / scale in on load)?
- [ ] Stagger order: navbar → headline → subtext → button?
- [ ] Scroll-driven effects (parallax, opacity on scroll)?
- [ ] Magnetic / mouse-following effects?
- [ ] CSS keyframe animations (pulse, float, spin, scroll indicator)?

## Color & Aesthetic System
- [ ] Primary background hex
- [ ] Primary text hex
- [ ] Secondary/muted text hex (with opacity)
- [ ] Accent color(s) hex
- [ ] Overall aesthetic: dark, light, glassmorphic, neon, minimal, fintech, creative → see [[quick-aesthetic-guide]]

## Fonts
- [ ] Identify ALL font families visible
- [ ] Map each to a Google Fonts name (or infer)
- [ ] Loaded via Google Fonts URL or `@font-face`

---

## Output Is Fed Into

→ [[prompt-output-template-hero]] — exact structure the output uses

---

## Related
- [[image-analysis-checklist-landing-page]] — extra items for full page
- [[motionsites-ai]] — quality bar
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