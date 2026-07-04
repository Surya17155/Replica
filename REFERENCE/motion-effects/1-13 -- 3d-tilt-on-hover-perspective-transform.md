# 3D Tilt on Hover (Perspective Transform)

**Visual cue:** A card/image tilts slightly to follow the cursor in 3D space.

**Implementation:**

```tsx
const handleMouseMove = (e) => {
  const rect = ref.current.getBoundingClientRect();
  const x = (e.clientX - rect.left) / rect.width - 0.5;
  const y = (e.clientY - rect.top) / rect.height - 0.5;
  ref.current.style.transform = `perspective(1000px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`;
};
```

**Performance:** ⚠️ Avoid on mobile (no hover). Add `@media (hover: hover)` guard.

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