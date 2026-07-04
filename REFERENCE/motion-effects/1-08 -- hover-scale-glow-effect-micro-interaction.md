# Hover Scale + Glow Effect (Micro-Interaction)

**Visual cue:** Button or card enlarges slightly and gains a glow/shadow on hover.

**Implementation: Framer Motion `whileHover`:**

```tsx
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 300, damping: 15 }}
  className="transition-shadow duration-300 hover:shadow-[0_0_30px_rgba(181,1,167,0.4)]"
>
  Book Demo
</motion.button>
```

**Pure CSS:**
```css
.btn-primary {
  transition: transform 0.2s ease, box-shadow 0.3s ease;
}
.btn-primary:hover {
  transform: scale(1.02);
  box-shadow: 0 0 30px rgba(181,1,167,0.4);
}
```

**Performance:** ✅ Excellent.

---

### 1.09 — Counter Animation (Number Scroll-Up)

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
