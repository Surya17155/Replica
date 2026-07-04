# Parallax Scroll (Multi-Speed Layers)

**Visual cue:** Background image/element moves slower than foreground when scrolling.

**Implementation: Framer Motion `useScroll` + `useTransform`:**

```tsx
import { useScroll, useTransform } from 'framer-motion';
const { scrollY } = useScroll();
const bgY = useTransform(scrollY, [0, 1000], [0, 200]); // bg moves 20% as fast
const fgY = useTransform(scrollY, [0, 1000], [0, -100]); // foreground moves opposite

return (
  <div className="relative h-screen overflow-hidden">
    <motion.div style={{ y: bgY }} className="absolute inset-0">
      <img src="/bg.jpg" className="w-full h-[120%] object-cover" />
    </motion.div>
    <motion.div style={{ y: fgY }} className="relative z-10">
      <h1>Hero Content</h1>
    </motion.div>
  </div>
);
```

**GSAP ScrollTrigger:** `gsap.to('.bg-layer', { y: 200, scrollTrigger: { trigger: '.section', start: 'top bottom', end: 'bottom top', scrub: 1 } })`

**Performance:** ⚠️ Use sparingly. Each parallax layer adds a composite layer. 2-3 layers is fine; 10+ layers will jank.

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