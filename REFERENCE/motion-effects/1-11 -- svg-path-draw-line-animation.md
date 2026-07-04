# SVG Path Draw (Line Animation)

**Visual cue:** A decorative line or illustration draws itself in as the user scrolls.

**Implementation:** Map `scrollYProgress` to `strokeDashoffset`:

```tsx
const { scrollYProgress } = useScroll({ target: containerRef, offset: ["start 0.8", "end 0.2"] });
const pathLength = useTransform(scrollYProgress, [0, 1], [0, 1]);

return (
  <motion.path
    d="M0,100 C100,0 200,200 300,100"
    stroke="currentColor"
    strokeWidth={2}
    fill="none"
    style={{ pathLength }}
  />
);
```

**Performance:** ✅ Good. SVG draw is very GPU-light.

---

### 1.12 — Cursor Trail (Mouse Particles)

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
