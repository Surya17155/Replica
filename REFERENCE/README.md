# REFERENCE — Central Hub

> **This README is the central hub for ALL design references in the brain corpus.**
> Every reference file points here. This README points to every reference file.
> When the LLM loads SKILL.md, it eventually reaches this hub and gets full access to the entire knowledge base.

## Wiring Path (how you got here)

```
00-brain-index
  └─→ 02-References/
        └─→ REFERENCE/README.md  ← YOU ARE HERE
              ├─→ motion-effects/_index.md (13 files)
              ├─→ css-presets/_index.md (7 files)
              ├─→ component-patterns/_index.md (6 files)
              ├─→ aesthetic-cards/_index.md (6 files)
              ├─→ pinterest-doc/_index.md (8 files)
              └─→ (root files below)
```

**Upward links:**
- Parent: [[../README|02-References]]
- Root: [[../../README|00-brain-index]]
- Director: [[../DIRECTOR/rules-engine|DIRECTOR/rules-engine]] (workflow rules)
- Skill router: [[../ultra-prompt-generator/DESIGNER/skill-router|skill-router]] (which skill to use)

Total reference files: **46** + this README

---

## 1. Motion Effects — [[motion-effects/_index|Index]] (13 files)

Scroll-driven animation specs. Each is a copy-paste JSX hook + Tailwind class cluster.

- [[1-01— stagger-fade-in-page-load-entrance.md]]
- [[1-02— scroll-triggered-reveal-whileinview.md]]
- [[1-03— parallax-scroll-multi-speed-layers.md]]
- [[1-04— sticky-card-stacking-scale-down-on-scroll.md]]
- [[1-05— magnetic-mouse-follow-magnet-component.md]]
- [[1-06— float-animation-continuous-up-down.md]]
- [[1-07— scroll-driven-marquee-infinite-logo-scroll.md]]
- [[1-08— hover-scale-glow-effect-micro-interaction.md]]
- [[1-09— counter-animation-number-scroll-up.md]]
- [[1-10— typewriter-effect-character-reveal.md]]
- [[1-11— svg-path-draw-line-animation.md]]
- [[1-12— cursor-trail-mouse-particles.md]]
- [[1-13— 3d-tilt-on-hover-perspective-transform.md]]

## 2. CSS Presets — [[css-presets/_index|Index]] (7 files)

Visual-effects CSS blocks ready to drop into @layer or :root.

- [[2-01— glassmorphism-dark-theme.md]]
- [[2-02— gradient-text.md]]
- [[2-03— multi-layer-button-shadow-premium-cta.md]]
- [[2-04— neon-glow-effect-nft-web3-dark-cyber.md]]
- [[2-05— noise-grain-texture-overlay.md]]
- [[2-06— section-transition-rounded-top-pull-up.md]]
- [[2-07— scroll-driven-fade-out-bottom-of-hero.md]]

## 3. Component Patterns — [[component-patterns/_index|Index]] (6 files)

Component-level architecture specs — props, classes, behavior.

- [[3-01— navbar-pill-floating-glass.md]]
- [[3-02— navbar-full-width-transparent-dark.md]]
- [[3-03— hero-video-background-with-rounded-card.md]]
- [[3-04— hero-full-screen-dark-with-3d-portrait-magnet.md]]
- [[3-05— card-sticky-stacking-card-portfolioprojects.md]]
- [[3-06— marquee-logo-ticker.md]]

## 4. Aesthetic Cards — [[aesthetic-cards/_index|Index]] (6 files)

Visual identity presets — single-page aesthetic with full color/type/spacing spec.

- [[4-01— glassmorphism.md]]
- [[4-02— dark-portfolio.md]]
- [[4-03— fintechsaas.md]]
- [[4-04— nftweb3.md]]
- [[4-05— creative-studio.md]]
- [[4-06— modern-agency.md]]

## 5. Pinterest Templates — [[pinterest-doc/_index|Index]] (8 files)

Verified full prompts reverse-engineered from Pinterest reference images.

- [[pinterest-template-01.md]]
- [[pinterest-template-02.md]]
- [[pinterest-template-03.md]]
- [[pinterest-template-04.md]]
- [[pinterest-template-05.md]]
- [[pinterest-template-06.md]]
- [[pinterest-template-07.md]]
- [[pinterest-template-08.md]]

---

## Root Files (top-level)

These sit at `REFERENCE/` directly — used by ALL flow types.

- [[image-analysis-checklist-hero.md]]
- [[image-analysis-checklist-landing-page.md]]
- [[motionsites-ai.md]]
- [[prompt-output-template-hero.md]]
- [[prompt-output-template-landing-page.md]]
- [[quick-aesthetic-guide.md]]

---

## Backlinks (this README is referenced from)

Every file in this folder links back to this hub via its `_index.md` or footer.
Cross-references go through this hub so every file remains reachable from the brain index.

## How to Use

1. AI reads SKILL.md → activates skill-router → finds the relevant reference file here
2. Reference files inline-link back here, so context navigates naturally
3. No file is unreachable — every orphan has either a backlink or sits in a ro   ot file linked below

---

## 🔌 Connected From (every layer above reaches this README)

**This README is the central vocabulary hub. It is reached from:**

| Source | Hops | Purpose |
|--------|------|---------|
| [[../../SKILL\|ultra-prompt-generator/SKILL.md]] | 1 | Main skill, includes router block, finds this README |
| [[../DIRECTOR/rules-engine\|DIRECTOR/rules-engine]] | 1 | Workflow points to vocab before generating |
| [[../DESIGNER/skill-router\|skill-router]] | 1 | When a skill is selected, it pulls vocabulary from here |
| [[../DESIGNER/skill-decision-engine\|skill-decision-engine]] | 1 | Algorithm signals reference aesthetic / motion categories here |

**This README points to:**

- All 5 subfolder hubs (`_index.md` files)
- [[../SKILL\|SKILL.md]] (back to entry)
- [[../DIRECTOR/rules-engine\|DIRECTOR rules-engine]] (workflow that consumes this vocab)

> **Note:** Worth skimming this file when using one of the supplementary design skills, to keep vocabulary consistent — not a strict requirement.

*Last wired: full corpus wiring pass — every file now reaches root.*