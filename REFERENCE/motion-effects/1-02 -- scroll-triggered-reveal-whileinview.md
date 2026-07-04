# Scroll-Triggered Reveal (whileInView)

**Visual cue:** As user scrolls, elements slide/fade in as they enter the viewport.

**Implementation: Framer Motion `whileInView`:**

```tsx
<motion.div
  initial={{ opacity: 0, y: 60 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.7, ease: [0.25, 0.1, 0.25, 1] }}
>
  Content
</motion.div>
```

**GSAP ScrollTrigger:** Trigger with `start: 'top 80%'`, `end: 'bottom 20%'`, `scrub: 1`.

**CSS scroll-driven animation** (Chrome 115+): `@keyframes reveal { from { opacity: 0; transform: translateY(60px); } to { opacity: 1; transform: translateY(0); } }` with `animation-timeline: view()`, `animation-range: entry 0% entry 100%`.

**Performance:** ✅ Good. `whileInView` uses IntersectionObserver, which is off the main thread.

---

### 1.03 — Parallax Scroll (Multi-Speed Layers)

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
