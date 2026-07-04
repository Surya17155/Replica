---
tags: [reference, checklist, landing-page, analysis]
---

# Image Analysis Checklist — Full Landing Page

Run [[image-analysis-checklist-hero]] first, every single item. Then add the items below for the full page.

---

## Section Inventory
- [ ] List every section from top to bottom (Hero, Marquee, About, Services, Projects, Pricing, FAQ, Footer, ...)
- [ ] Order they appear
- [ ] Background changes per section (dark → light → dark?)
- [ ] Corner transitions between sections (e.g., `rounded-t-[60px] -mt-14 z-10`)
- [ ] Approx padding/min-height per section

## Marquee / Ticker Section
- [ ] Scrolling logos, images, or text?
- [ ] Direction: left or right
- [ ] Speed + scroll-reactivity (CSS animation vs. scroll-driven)
- [ ] Items: image tiles, logo text, or mixed
- [ ] Border-radius per tile
- [ ] Pause on hover?

## Content / About / Info Section
- [ ] Heading style (same gradient as hero? different?)
- [ ] Animated paragraph (character-by-character reveal? opacity-scroll?)
- [ ] Decorative corner images or 3D objects
- [ ] CTA button repeated?

## Services / Features Section
- [ ] List or grid format
- [ ] Numbered items? Icons?
- [ ] Divider borders between items
- [ ] Item: name + description layout
- [ ] Background: light (white) or dark

## Projects / Portfolio / Works Section
- [ ] Card layout: grid, bento, stacked sticky
- [ ] Stacking card effect (scale-down as scroll, sticky top)
- [ ] Card content: number, category, title, CTA, image grid layout
- [ ] Image grid column split (e.g., 40% / 60%)
- [ ] Image border-radius (heavy = `rounded-[40px]`)
- [ ] Card border style, background
- [ ] Featured / highlighted card variant?

## Pricing Section
- [ ] Card styles: dark vs. light cards
- [ ] Price display, plan names, descriptions
- [ ] Button styles per card
- [ ] Featured plan treatment
- [ ] Toggle (monthly / yearly)?

## Testimonials
- [ ] Static quotes or carousel
- [ ] Card style, avatar shape, author info
- [ ] Scroll or auto-advance behavior
- [ ] Avatar images (gather URLs)

## FAQ Section
- [ ] Accordion collapsible items
- [ ] Plus/minus or chevron icons
- [ ] Border treatment between items
- [ ] Animation on open/close

## Footer / Contact Section
- [ ] Layout: columns, links, social icons
- [ ] CTA in footer (email input, button)
- [ ] Copyright bar
- [ ] Fixed bottom navigation?
- [ ] GSAP marquee text at bottom
- [ ] Social icons (Twitter, LinkedIn, GitHub, etc.)

---

## Asset Inventory Cross-Reference

For each section that contains an image, list:
- Section name + position
- Image content (what does it show)
- Asset role (hero, card, avatar, decoration, background)
- Required hosted URL

See [[asset-inventory]] — full workflow for gathering these URLs.

---

## Output Is Fed Into

→ [[prompt-output-template-landing-page]]

---

## Related
- [[image-analysis-checklist-hero]]
- [[asset-inventory]]
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
- [[motion-effects/_index]]
- [[component-patterns/_index]]
- [[prompt-output-template-landing]]