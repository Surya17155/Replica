---
name: replica
description: Use when the user uploads a screenshot of a hero section or landing page (or a URL/description of one) and wants a copy-paste-ready developer prompt to recreate it exactly in a tool like Lovable, Bolt, Replit, or Cursor. Produces prompts with exact hex colors, Tailwind classes, animation timing tuples, and component structure — not vague descriptions.
license: MIT
---

# Design-to-Prompt — Hero Section & Full Landing Page Generator

## Overview

This skill turns a UI screenshot (hero section or full landing page) into a complete, copy-paste-ready **developer prompt** at the motionsites.ai level of detail — the kind a senior frontend engineer would write so that an agent (Lovable, Bolt.new, Cursor, Replit, v0, Claude Code) can rebuild the design exactly.

**Output quality is this (never vague):**
- Every color → hex code
- Every font → Google Fonts URL + weight + Tailwind alias
- Every animation → full Framer Motion `initial` / `animate` / `transition` block (delay, duration, ease)
- Every button → tailwind class string, multi-layer box-shadow, icon markup
- Every section → full component with file path

**The skill requires BOTH the screenshot AND any hosted asset URLs (images, videos visible in the design) to produce the final prompt.** It guides the user through generating + hosting those assets first, then embeds the URLs inline at the right places in the final output.

--- 

## HOW TO USE THIS SKILL

When the user uploads an image/design reference:

1. **Ask Hero vs Full Landing** (if not specified)
2. **Ask Brand Context** (if not provided; fall back to screenshot text)
3. **Run Image Analysis** (silently — internal checklist)
4. **Publish Asset Inventory** (image prompts + video workflow + URL requests)
5. **Wait for all asset URLs** before writing final prompt
6. **Write final code prompt** at motionsites.ai level of detail

---

## PART 1 — ASSET PREP WORKFLOW (before the final prompt)

This is the most important part of the skill. Before writing the final prompt, you must identify every external asset in the design and stop until the user provides hosted URLs.

### 1a — When to Ask for Assets

Scan the image for:

- **Background image/video** (not solid CSS/ gradient)
- **Product mockups** / hero images
- **Avatar images** (testimonial section)
- **Logo** (unless SVG text or simple)
- **Decorative 3D elements** (corner images, floating objects)
- **Any card/component with an embedded image'

### 1b — Image Inventory Format

Present to the user:

```
## ASSET INVENTORY

I can see [N] images/videos in this design that need hosted URLs.
For each one I've written a detailed generation prompt.
Upload to https://postimages.org after generating, then reply with the URLs.

### ASSET 1 — [Name / Position]
- Purpose: [where it goes in the design — hero background, features card left, testimonial avatar, etc.]
- Style: [matching the design aesthetic — dark glassmorphic, minimalist clean, vintage paper, etc.]
- Generation Prompt:
  [ultra-detailed prompt for Midjourney/DALL-E/Flux — describe content, mood, lighting, composition, colors, aspect ratio, and style reference]
```

For **any image** in the design, first produce a detailed image-generation prompt. If the user has provided brand context, include that context in the prompt. If not, describe what's visible in the screenshot and let the user adjust.

If the user replies with a URL — great, embed it. If they say "skip it" — use `[PLACEHOLDER_URL]` in the final prompt.

### 1c — Video Backgrounds (Simple)

If the hero uses a background video:

1. Detect the mood from the screenshot (dark cinematic, nature calm, futuristic neon, etc.)
2. Produce a descriptive prompt for Sora / Runway / Pika / Kling:
   ```
   Purpose: Full-bleed background behind hero headline
   Generated prompt: "A slow aerial drift over a misty forest at golden hour, warm amber light filtering through canopy, cinematic 24fps, smooth 10-second loop, 3840x2160, film grain, atmospheric haze"
   ```
3. Ask the user to generate, host, and return a URL

### 1d — Complex Motion Videos (scroll-driven / exploded view)

If the design depends on a scroll-driven motion effect (the main subject animates through frames as the user scrolls — popular in modern portfolio/marketing pages):

**STOP. Do not write the final prompt yet.** Present this workflow:

```
This design uses a scroll-driven motion effect. Here is a step-by-step plan:

**Step 1 — First Frame Prompt:**
[Detailed prompt describing the initial state of the animated subject]

**Step 2 — Last Frame Prompt:**
[Detailed prompt describing the final state of the animated subject]

**Step 3 — Interpolation:**
Use Luma Dream Machine or Kling AI "image-to-video" / "keyframes" mode.
- Upload the first frame as frame 1
- Upload the last frame as the final frame
- Set motion strength to [subtle / moderate / dramatic based on design]
- Export as MP4 at least 1080p, 8–15 seconds (it will become a shorter scroll animation)

**Step 4:**
Host the resulting MP4 on any CDN and reply with the URL.
Once I have it, I will embed it in the final prompt so the hero uses scroll-driven playback.
```

### 1e — Background That Is an Image (not CSS)

If the background is a real image/photo (not code-able CSS), produce a detailed image generation prompt for it and tell the user:

```
The background of this design is a photo/image that cannot be recreated with CSS.
Generate this image and host it:

**Background Image Prompt:**
[Full Midjourney/DALL-E/Flux prompt matching the screenshot's background]
```

---

## PART 2 — IMAGE ANALYSIS CHECKLIST (Hero)

Run this checklist internally (silently) on every hero image before writing the prompt. Check EVERY item.

### Layout & Frame
- [ ] Outer page background color (what surrounds the hero card, if any)
- [ ] Hero container shape — full-screen? padded/rounded card inside a wrapper?
- [ ] Exact border-radius of container (e.g., `rounded-3xl` = 24px, or `rounded-[40px]`)
- [ ] Overflow behavior (content bleeding off bottom edge? rounded clip?)
- [ ] z-layering (video → overlay → content?)

### Background
- [ ] Solid color, gradient, image, or video background?
- [ ] If video: describe motion, mood, color palette
- [ ] If gradient: direction, from-color, to-color
- [ ] Dark overlay on top? (e.g., `bg-black/20`)
- [ ] Texture / noise layer? (fixed, `mix-blend-mode`, opacity)
- [ ] Bottom fade-out gradient? (`bg-gradient-to-t from-[color] to-transparent`)

### Navbar
- [ ] Fixed/floating, sticky, or static?
- [ ] Pill/floating shape, or full-width bar?
- [ ] Background: transparent, glass (`backdrop-blur`), solid white, dark?
- [ ] Logo: text only, SVG icon, image? Font? Size? Color?
- [ ] Nav links: count, labels, color, font size, uppercase?
- [ ] Hover effects (opacity, color change, underline?)
- [ ] CTA button in navbar: text, shape, colors, icons inside?
- [ ] Mobile: hamburger menu? What appears when opened?
- [ ] Scroll behavior (shadow/bg change on `scrollY > threshold`)

### Hero Headline & Typography
- [ ] Main headline text (or placeholder like `[Product Name] tagline`)
- [ ] Font family (serif, sans-serif, monospace, display, grotesk?)
- [ ] Font weight (300/400/500/600/700/900)
- [ ] Font size as `clamp()`: `clamp(smallPx, Xvw, largePx)`
- [ ] Letter-spacing: tight (`-0.04em`), normal, wide (`0.1em`)?
- [ ] Line-height: tight (0.9–1.0), normal (1.2), relaxed (1.5)?
- [ ] Color: solid, or gradient (direction + hex stops)?
- [ ] Any italic/serif accent word mixed inside sans-serif headline?
- [ ] Any animated text (fade in, slide up, typewriter, character reveal)?
- [ ] Subheadline/tagline: size, color, font, opacity?

### Visual Focal Element
- [ ] Hero image/portrait/product mockup?
- [ ] Position (center, right side, absolute overlay?)
- [ ] Effects: magnetic hover, parallax, float animation?
- [ ] Decorative 3D objects / corner elements?
- [ ] Badge/pill/tag floating near headline ("New", "AI-powered", etc.)?

### CTA Buttons
- [ ] How many buttons? Labels?
- [ ] Primary: background (gradient/solid/glass), text color, shape, padding, shadow
- [ ] If gradient: gradient direction + hex stops
- [ ] Inner/outer box-shadow (exact multi-layer values)
- [ ] Icon inside button? (arrow, chevron, star, sparkle?)
- [ ] Secondary/ghost: border style, background, text color
- [ ] Hover animations: scale, glow, color change?

### Floating / Overlay Cards
- [ ] Any stat cards, info panels, floating UI elements?
- [ ] Position (bottom-left, bottom-right, absolute?)
- [ ] Background: glass/blur, solid white, dark?
- [ ] Content: text, numbers, icons?
- [ ] Cutout/mask effect for corner integration?

### Animations & Motion
- [ ] Entrance animations (fade in / slide up / scale in on load)?
- [ ] Stagger order: navbar → headline → subtext → button?
- [ ] Scroll-driven effects (parallax, opacity fade on scroll)?
- [ ] Magnetic / mouse-following effects?
- [ ] CSS keyframe animations (pulse, float, spin, scroll-down indicator)?

### Color & Aesthetic System
- [ ] Primary background hex
- [ ] Primary text hex
- [ ] Secondary/muted text hex (with opacity)
- [ ] Accent color(s) hex
- [ ] Overall aesthetic: dark, light, glassmorphic, neon, minimal, fintech, creative?

### Fonts
- [ ] Identify ALL font families visible
- [ ] Map each to a Google Fonts name or infer closest match
- [ ] Determine if loaded via Google Fonts URL or `@font-face`

---

## PART 3 — IMAGE ANALYSIS CHECKLIST (Full Landing Page)

Run ALL of the Hero checklist first, then additionally scan for:

### Section Inventory
- [ ] List every section from top to bottom (Hero, Marquee, About, Services, Projects, Pricing, FAQ, Footer…)
- [ ] Order they appear
- [ ] Background changes? (dark → light → dark alternating?)
- [ ] Corner transitions between sections (e.g. `rounded-t-[60px] -mt-14`)?

### Marquee / Ticker
- [ ] Scrolling logos, images, or text?
- [ ] Direction: left or right?
- [ ] Speed + scroll-reactivity (CSS animation vs. scroll-driven)?
- [ ] Items: image tiles (border-radius?), logo text, or mixed?

### Content / About / Info Section
- [ ] Heading style (same gradient as hero, or different?)
- [ ] Animated paragraph (character-by-character reveal? opacity scroll?)
- [ ] Decorative corner images or 3D objects?
- [ ] CTA button repeated?

### Services / Features Section
- [ ] List or grid format?
- [ ] Numbered items? Icons?
- [ ] Divider borders between items?
- [ ] Item name + description layout
- [ ] Background: light (white) or dark?

### Projects / Portfolio / Works Section
- [ ] Card layout: grid, bento, stacked sticky?
- [ ] Stacking card effect (scale down as scroll, sticky top)?
- [ ] Card content: number, category, title, CTA, image grid?
- [ ] Image grid column split (e.g. 40%/60%)?
- [ ] Image border-radius (heavy = `rounded-[40px]`)?
- [ ] Card border style, background

### Pricing Section
- [ ] Cards: dark vs. light cards?
- [ ] Price display, plan names, descriptions
- [ ] Button styles per card

### Testimonials
- [ ] Static quotes or carousel?
- [ ] Card style, avatar, author info
- [ ] Scroll/auto-advance behavior?

### Footer / Contact Section
- [ ] Layout: columns, links, social icons
- [ ] CTA in footer (email, button)?
- [ ] Copyright bar?
- [ ] Fixed bottom navigation?
- [ ] GSAP marquee text?

---

## PART 4 — FINAL PROMPT OUTPUT (Hero Section)

Use this exact structure. Write in second-person imperative ("Build...", "Create...", "Use...").

```
Build a [adjective] hero section for "[Product Name]" using [Tech Stack: React + TypeScript + Vite + Tailwind CSS + Framer Motion + Lucide React].

---

## Page Frame

Outer wrapper: [Tailwind classes for the outermost div]
Hero container: [Tailwind classes, border-radius, overflow-hidden, background]

---

## Background

[Describe the background layer: solid color / video / image / gradient]
[If video: URL, autoPlay muted loop playsInline, object-cover absolute inset-0 w-full h-full]
[Any overlay: absolute inset-0 bg-black/X or gradient]
[Any texture: fixed z-50 pointer-events-none, mix-blend-mode, opacity, background-size]
[Bottom fade: h-XX bg-gradient-to-t from-[color] to-transparent]

---

## Global Styles

### Fonts
[Font name, weights, import method (Google Fonts URL or @font-face with src)]
[Map to Tailwind: --font-X: 'Font Name', fallback → tailwind font-X]

### CSS Custom Properties
[All CSS variables: --bg, --text, --accent, --surface in HSL or hex]

### CSS Utility Classes
[Any special classes: .liquid-glass, .hero-heading, .accent-gradient etc.]
[Include full CSS for each class]

### CSS Animations
[@keyframes definitions for any custom animations]

---

## Navbar

[Position: fixed/static/absolute, wrapper classes]
[Inner pill/bar: classes, background, blur, border, shadow]
[Logo: markup, font, size, color, SVG path if custom icon]
[Nav links: flex gap, text size, color, uppercase, hover effect, active state]
[CTA button: gradient, shadow, icon, full class string]
[Mobile: hamburger logic, dropdown menu structure]
[Scroll behavior: class changes on scrollY > threshold]

---

## Hero Content

### Badge / Eyebrow
[If present: classes, background, text, icon, animation]

### Headline
[Tag: h1, exact text with line breaks]
[Tailwind: text-size (clamp or responsive), font-weight, color (or gradient class), tracking, leading]
[Any mixed font (italic serif word inside sans-serif headline)]
[Animation: initial state, animate state, transition, delay]

### Subheadline
[Tag, text, Tailwind classes, animation]

### CTA Buttons
[Button 1 — Primary: full class string + exact multi-layer box-shadow + icon markup]
[Button 2 — Secondary: full class string, hover border gradient]

### Hero Visual Element
[Image/portrait: position, size classes, src URL from user's hosted link]
[Special effect: Magnet component (mouse-follow), parallax settings]
[Decorative elements: each with position and animation]

---

## Floating Cards (if present)

### [Card Name] — Bottom-[Left/Right]
[Position: absolute bottom-X left-X / right-X]
[Background: glass/blur/solid, border-radius]
[Content: markup — headline number, label, button]
[Animation: initial, animate, transition values]
[Corner mask (if cutout): exact SVG path + positioned div]

---

## Animations Reference

| Element | Library | initial | animate | delay | duration |
|---------|---------|---------|---------|-------|----------|
| Navbar | Framer | opacity:0, y:-20 | opacity:1, y:0 | 0s | 0.6s |
| Headline | Framer | opacity:0, y:40 | opacity:1, y:0 | 0.15s | 0.8s |
| Subheadline | Framer | opacity:0, y:30 | opacity:1, y:0 | 0.35s | 0.7s |
| CTA Button | Framer | opacity:0, y:20 | opacity:1, y:0 | 0.55s | 0.6s |
| Hero Image | Framer | scale:0.9, opacity:0 | scale:1, opacity:1 | 0.7s | 0.9s |

[All eases use: ease: [0.25, 0.1, 0.25, 1] or custom cubic-bezier]

---

## Reusable Components

### [ComponentName] ([filename].tsx)
[Props, behavior, full class list, any special logic]

---

## Dependencies

[Package list: react, react-dom, framer-motion, lucide-react, tailwindcss, etc. with versions]

---

## File Structure

src/components/[ComponentName].tsx
src/styles/index.css
src/App.tsx
index.html
...
```

---

## PART 5 — FINAL PROMPT OUTPUT (Full Landing Page)

Use this structure:

```
Build a [adjective] [page type] landing page for "[Product Name]" using [Tech Stack: React + TypeScript + Vite + Tailwind CSS + Framer Motion + Lucide React].

---

## Global Design System

### Tech Stack
[Exact frameworks and libraries]

### Fonts
[All fonts, import method, weights, Tailwind aliases]

### Color System
[All colors as CSS variables or Tailwind config extensions]
[Format: --bg: #XXXXXX; --text: #XXXXXX; etc.]

### Global CSS
[Body/html resets, overflow-x hidden, box-sizing]
[Tailwind custom theme extension]
[All CSS utility classes with full CSS]
[All @keyframes animations]

### Tailwind Config Extensions
[Custom colors, fonts, animations, borderRadius tokens]

---

## SECTION ORDER

1. [SectionName] — [brief description]
2. [SectionName] — [brief description]
...

---

## 1. [SECTION NAME] SECTION

[Section-level specs: background, min-height, padding, z-index, overflow]

[Subsection A — e.g., Navbar]
[Subsection B — e.g., Hero Headline]
[Subsection C — e.g., CTA Buttons]

[If this section has an asset URL, embed it inline here:
  e.g. For the hero image: `src="[USER'S HOSTED IMAGE URL]"` ]

---

## 2. [SECTION NAME] SECTION

[Background, transition from previous section — rounded top + negative margin pull-up]
[Full section spec...]

[Continue for every section...]

---

## REUSABLE COMPONENTS

### [ComponentName] ([filename].tsx)
[Description, props, full class string, special behavior]

---

## ANIMATIONS

### Entrance (on page load)
[Table: Element / Library / initial / animate / delay / duration / easing]

### Scroll Animations
[Scroll-driven effects: IntersectionObserver, Framer whileInView, GSAP ScrollTrigger]

### Continuous Animations
[Marquees, floating elements, magnetic effects, parallax columns]

---

## DEPENDENCIES

[Full npm package list]

---

## FILE STRUCTURE

[Complete src/ directory with all component files]
```

---

## PART 6 — CRITICAL RULES FOR GENERATING PROMPTS

Always follow every one of these:

1. **Never say "a nice button" — say the exact classes.** Bad: "a gradient button". Good: `bg-gradient-to-r from-[#18011F] via-[#B600A8] to-[#7621B0] text-white rounded-full px-10 py-3.5 font-medium uppercase tracking-widest shadow-[0px_4px_4px_rgba(181,1,167,0.25),4px_4px_12px_#7721B1_inset] outline outline-2 outline-white -outline-offset-[3px]`

2. **Always use hex codes, never color names.** Bad: "dark background". Good: `bg-[#0C0C0C]`

3. **Always define font sizes with `clamp()` for fluid scaling.** Bad: "big heading". Good: `fontSize: clamp(3rem, 12vw, 160px)`

4. **Every animation gets all 4 values: initial, animate, delay, duration.** Bad: "fades in". Good: `initial={{ opacity: 0, y: 30 }}, animate={{ opacity: 1, y: 0 }}, transition={{ duration: 0.7, delay: 0.35, ease: [0.25, 0.1, 0.25, 1] }}`

5. **Glassmorphism includes the full CSS block** — backdrop-filter, background-blend-mode, box-shadow, and the `::before` gradient border pseudo-element with `mask-composite`.

6. **Buttons include their box-shadow** (multi-layer shadows are the signature of premium UI).

7. **Videos include all 5 attributes:** `autoPlay muted loop playsInline` + `object-cover`.

8. **Section transitions specify** rounded top corner class + negative margin pull-up (e.g., `rounded-t-[60px] -mt-14 z-10`).

9. **Marquees specify** direction (translateX negative = left), speed (seconds), and CSS keyframes vs. GSAP vs. scroll-driven.

10. **Cards with image grids specify** the exact column width split (e.g., `w-[40%]` / `w-[60%]`) and image heights via `clamp()`.

11. **Component names are PascalCase** and match a file path (e.g., `src/components/HeroSection.tsx`).

12. **Responsive breakpoints use Tailwind mobile-first** (base → sm: → md: → lg:) with explicit values at each breakpoint.

13. **Decorative elements include** exact position classes, width at each breakpoint, and FadeIn animation values.

14. **Custom fonts include** the `@font-face` block with `src` URL (or note as local file like `/fonts/PPMondwest-Regular.woff2`).

15. **Scroll animations specify** the offset (e.g., `['start 0.8', 'end 0.2']` for Framer Motion `useScroll`).

---

## PART 7 — QUICK AESTHETIC IDENTIFICATION GUIDE

Use these visual cues to identify the design aesthetic and apply matching defaults:

| Visual Cues | Aesthetic | Key Patterns |
|-------------|-----------|-------------|
| Dark bg, blur panels, frosted glass | Glassmorphism | `backdrop-blur`, `rgba(...)`, `::before` gradient border mask |
| Black/near-black bg, gradient text, heavy font | Dark Portfolio | Gradient text class, `clamp()` huge typography, Framer entrances |
| Light gray bg, video hero inside rounded card | Fintech/SaaS | `clamp()`, negative letter-spacing, TT Norms / Inter, h-screen video card |
| White bg, serif+sans mix, column layout | Creative Studio | PP Mondwest / Instrument Serif italic accents, marquee, parallax image |
| Space theme, neon accents, monospace text | NFT/Web3 | Anton font, neon hex (#6FFF00), liquid-glass, video backgrounds |
| Minimal white, clamp typography, pill buttons | Modern Agency | `clamp()`, `-0.04em` letter-spacing, IntersectionObserver fade-in, fixed bottom nav |

---

## PART 8 — HANDLING EDGE CASES

### Low-Quality or Partial Image
- Still produce the prompt — infer missing values from visible design language.
- Mark inferred values with `[INFERRED: ...]` so the user knows to verify.
- Prioritize: colors → fonts → layout → animations (what you see clearly).
- If no image but user describes style (e.g., "glassmorphism dark SaaS hero"), generate from description using the same template.

### User Refuses to Provide Asset URLs
Say: "I'll use placeholder URLs `[PLACEHOLDER_URL]` in the prompt — just search-and-replace before pasting into your coding agent."

### User Refuses Brand Context
Keep text exactly as visible in the screenshot. Use `[PLACEHOLDER: describe what goes here]` for anything illegible.

### Multiple Images, Different Purposes
Ask: "Should I treat these as one design at different views, or separate designs?" If one design → merge all visible sections into a single prompt. If separate → ask which to process first.

### No Image Uploaded, Only Description
Generate a full prompt from the description using the same templates. Mark all values as `[INFERRED FROM DESCRIPTION: ...]`.

---

## TONE & FORMAT OF OUTPUT

- Write in second-person imperative: "Build...", "Create...", "Use...", "Place..."
- Use `##` headers for each major section
- Use backticks for all class strings and code values
- Use plain markdown tables for animation references (as shown in the animation table template above)
- Label every URL with what it's for (hero video, about section image, etc.)
- When uncertain, use `[PLACEHOLDER: describe what goes here]`
- **Do NOT** say "approximately" or "roughly" — commit to specific values
- The output must be copy-paste ready for Lovable, Bolt.new, Replit Agent, Cursor, or v0

---

## COMMON PITFALLS

1. **Skipping the asset inventory** — Most designs have external images. Always scan. Never write the final prompt until you have URLs or explicit user permission to use placeholders.

2. **Assuming the user will find their own image links** — Always generate the image prompt for them. Make it detailed enough to copy-paste into any image gen tool.

3. **Forgetting scroll-driven video workflow** — If the design looks like a scroll-motion page (product morphing, hero transforming through scroll), always use the two-frame workflow with Luma/Kling suggested.

4. **Writing "nice" or "good-looking" instead of exact classes** — This is the number one difference between motionsites.ai quality and amateur prompts. Be specific.

5. **Mixing up the hero vs full landing template** — Hero uses "Page Frame → Background → Global Styles → Navbar → Hero Content → Floating Cards → Animations". Full landing uses "Global Design System → SECTION ORDER → 1/2/3... sections → Reusable Components → Animations".

6. **Not asking for brand context first** — If the user has a brand, it changes the content. Ask early, before you commit to analyzing the image.

7. **Generating the final prompt before URLs are ready** — Embed the asset URLs INSIDE the sections where they belong. If you write the prompt first and add URLs later, the user has to manually edit it.

---

## VERIFICATION CHECKLIST

Before delivering the final prompt to the user:

- [ ] Did you ask Hero vs Full Landing (if not specified)?
- [ ] Did you ask about multiple images (if >1 uploaded)?
- [ ] Did you ask for brand context (if not provided)?
- [ ] Did you scan for ALL asset inventory (images/videos in the design)?
- [ ] Did you generate detailed image prompts for each needed asset?
- [ ] Did you provide the video workflow (first frame + last frame + interpolation) for complex motion designs?
- [ ] Did you WAIT for the user to return hosted URLs?
- [ ] Are all external asset URLs embedded INLINE at the correct sections (not at the end)?
- [ ] Is every color a hex code?
- [ ] Is every font identified by name + Google Fonts URL + weight?
- [ ] Does every animation have initial/animate/delay/duration?
- [ ] Are all button classes exact, including multi-layer box-shadows?
- [ ] Are all component names PascalCase and mapped to file paths?
- [ ] Is the output copy-paste ready for Lovable / Bolt / Replit / Cursor?
- [ ] If the user refused brand context: did you use text exactly as visible in the screenshot?
- [ ] If the user refused asset URLs: did you use `[PLACEHOLDER_URL]` placeholders?