# Scroll-Driven Marquee (Infinite Logo Scroll)

**Visual cue:** Logos / text scrolling horizontally in a continuous strip, often at different speeds per row.

**Implementation: Framer Motion with scrollY mapping:**

```tsx
const { scrollY } = useScroll();
const x1 = useTransform(scrollY, [0, 2000], [0, -800]);
const x2 = useTransform(scrollY, [0, 2000], [0, 800]);

return (
  <div className="overflow-hidden">
    <motion.div style={{ x: x1 }} className="flex gap-8 w-[200%]">
      {/* 3x repeated content */}
    </motion.div>
    <motion.div style={{ x: x2 }} className="flex gap-8 w-[200%]">
      {/* 3x repeated content */}
    </motion.div>
  </div>
);
```

**CSS-only (no scroll binding):**
```css
@keyframes marquee-left {
  from { transform: translateX(0%); }
  to { transform: translateX(-50%); }
}
.marquee-row { animation: marquee-left 30s linear infinite; }
.marquee-row-2 { animation-direction: reverse; animation-duration: 40s; }
```

**Performance:** ✅ CSS is best for continuous. Scroll-driven marquees need scroll event throttling (use `useTransform` with MotionValue).

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