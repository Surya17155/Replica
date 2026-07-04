# Float Animation (Continuous Up-Down)

**Visual cue:** A floating 3D object, decorative element, or image gently bobs up and down.

**Implementation: CSS @keyframes:**

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
.float-animate {
  animation: float 6s ease-in-out infinite;
}
```

**Framer Motion:**
```tsx
<motion.div
  animate={{ y: [0, -20, 0] }}
  transition={{ duration: 6, repeat: Infinity, ease: "easeInOut" }}
/>
```

**Performance:** ✅ Excellent. Pure CSS is GPU-composited. Delay the start with `animation-delay` to avoid all elements moving in sync.

---

### 1.07 — Scroll-Driven Marquee (Infinite Logo Scroll)

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
