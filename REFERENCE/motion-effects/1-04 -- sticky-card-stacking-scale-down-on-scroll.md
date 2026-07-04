# Sticky Card Stacking (Scale-Down on Scroll)

**Visual cue:** As user scrolls, cards at the top of a list shrink and "stack" while the next card pushes up from below.

**Implementation: Framer Motion `useScroll` + `useTransform` on each card:**

```tsx
const containerRef = useRef(null);
const { scrollYProgress } = useScroll({
  target: containerRef,
  offset: ["start start", "end end"]
});
const scale = useTransform(scrollYProgress, [0, 0.33, 0.66, 1], [1, 0.9, 0.8, 0.7]);
const opacity = useTransform(scrollYProgress, [0, 0.33], [1, 0]);

return (
  <div ref={containerRef} className="relative h-[300vh]">
    <div className="sticky top-0 h-screen flex items-center">
      <motion.div style={{ scale }} className="w-full max-w-4xl mx-auto">
        {/* Card content */}
      </motion.div>
    </div>
  </div>
);
```

**GSAP ScrollTrigger:** Use `pin: true` on the container, `scrub: 1` on the scale tween.

**Performance:** ✅ Good for up to ~5 cards. Uses GPU compositing for transform changes.

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