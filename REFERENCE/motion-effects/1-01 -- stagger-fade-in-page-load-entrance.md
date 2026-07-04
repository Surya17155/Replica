# Stagger Fade-In (Page-Load Entrance)

**Visual cue:** Elements appear one after another — navbar first, then headline, then subtext, then CTA.

**Implementation: Framer Motion `staggerChildren` on a container:**

```tsx
<motion.div
  initial="hidden"
  animate="visible"
  variants={{
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.15, delayChildren: 0.2 }
    }
  }}
>
  <motion.h1 variants={{
    hidden: { opacity: 0, y: 40 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.25, 0.1, 0.25, 1] } }
  }}>
    Headline
  </motion.h1>
  <motion.p variants={{...}} />
  <motion.div variants={{...}} />
</motion.div>
```

**GSAP equivalent:** `gsap.from('.hero-element', { opacity: 0, y: 40, duration: 0.8, stagger: 0.15, ease: 'power3.out' })`

**CSS-only (simple):** `@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }` with `animation-delay` on each child.

**Performance:** ✅ Good — Framer Motion uses RAF and passes through to CSS transforms for GPU compositing.

---

## 🔗 ↑ Go Back Up

This file is part of **REFERENCE hub**. To navigate:

← Parent folder: [[../motion-effects|motion-effects]]
← Hub: [[../README|REFERENCE — Central Hub]]
← 02-References: [[../../README|02-References]]
← Brain root: [[../../README|00-brain-index]]

**Wired from:**
- [[../ultra-prompt-generator/DESIGNER/skill-router|skill-router]] (selection logic)
- [[../DIRECTOR/rules-engine|DIRECTOR rules engine]] (workflow)

*Every file in the corpus is reachable from the brain root in ≤5 hops.*