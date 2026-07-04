---
name: design-skills-index
description: All 25 design skills registered to Hermes for ultra-prompt-generator. Split into DESIGN (17) + GSAP (8).
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [rag, design, gsap, scroll-trigger, motion, scroll-effects, hero, landing]
---

# 00-design-skills-index

> **All 25 design skills** registered in this skill's `skills list/.agents/skills/` directory. Load via `skill_view(name="...")`.

## Where This Index Lives

This is the **physical** index mirrored from the brain corpus at `00-skills-index.md`. When ultra-prompt-generator activates, the LLM pulls THIS file for the canonical skill list.

## How to Load

```python
skill_view(name="brainstorming")           # always first
skill_view(name="gsap-scrolltrigger")      # for scroll-driven heroes
skill_view(name="design-taste-frontend")   # for landing pages
```

Each `skill_view` returns the skill's SKILL.md + linked files.

---

## Bundle A — Design Skills (17 skills)

- [[brainstorming/SKILL|brainstorming]]
- [[design-taste-frontend/SKILL|design-taste-frontend]]
- [[design-taste-frontend-v1/SKILL|design-taste-frontend-v1]]
- [[emil-design-eng/SKILL|emil-design-eng]]
- [[frontend-design/SKILL|frontend-design]]
- [[gpt-taste/SKILL|gpt-taste]]
- [[high-end-visual-design/SKILL|high-end-visual-design]]
- [[image-to-code/SKILL|image-to-code]]
- [[imagegen-frontend-mobile/SKILL|imagegen-frontend-mobile]]
- [[imagegen-frontend-web/SKILL|imagegen-frontend-web]]
- [[impeccable/SKILL|impeccable]]
- [[industrial-brutalist-ui/SKILL|industrial-brutalist-ui]]
- [[minimalist-ui/SKILL|minimalist-ui]]
- [[redesign-existing-projects/SKILL|redesign-existing-projects]]
- [[stitch-design-taste/SKILL|stitch-design-taste]]
- [[ui-ux-pro-max/SKILL|ui-ux-pro-max]]
- [[web-design-guidelines/SKILL|web-design-guidelines]]

---

## Bundle B — GSAP Skills (8 skills, from `npx skills add greensock/gsap-skills`)

- [[gsap-core/SKILL|gsap-core]]
- [[gsap-frameworks/SKILL|gsap-frameworks]]
- [[gsap-performance/SKILL|gsap-performance]]
- [[gsap-plugins/SKILL|gsap-plugins]]
- [[gsap-react/SKILL|gsap-react]]
- [[gsap-scrolltrigger/SKILL|gsap-scrolltrigger]]
- [[gsap-timeline/SKILL|gsap-timeline]]
- [[gsap-utils/SKILL|gsap-utils]]

---

## Backlinks

- [[../../SKILL|ultra-prompt-generator/SKILL.md]]
- [[../../DESIGNER/skill-router|skill-router]]
- [[../../DIRECTOR/skill-decision-engine|skill-decision-engine]]

*Last update (2026-06-24): 8 GSAP skills added.*
