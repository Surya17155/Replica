# Typewriter Effect (Character Reveal)

**Visual cue:** Text that appears character by character, like a typewriter.

**Implementation: Character-split + stagger:**

```tsx
const text = "Transform your workflow";
const characters = text.split("");

return (
  <motion.h1 initial="hidden" animate="visible"
    variants={{
      visible: { transition: { staggerChildren: 0.03 } }
    }}>
    {characters.map((char, i) => (
      <motion.span key={i}
        variants={{
          hidden: { opacity: 0, filter: "blur(4px)" },
          visible: { opacity: 1, filter: "blur(0px)" }
        }}
      >{char}</motion.span>
    ))}
  </motion.h1>
);
```

**Performance:** ✅ Good for headlines (< 50 chars). Bad for paragraphs (DOM overhead).

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