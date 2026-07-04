# Marquee / Logo Ticker

```tsx
<div className="overflow-hidden py-16">
  <div className="flex gap-12 w-max animate-[marquee-left_40s_linear_infinite] hover:[animation-play-state:paused]">
    {/* 3x repeated content */}
    {[...logos, ...logos, ...logos].map((logo, i) => (
      <img key={i} src={logo} className="h-8 w-auto grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition-all" />
    ))}
  </div>
</div>
```

---

---

## 🔗 ↑ Go Back Up

This file is part of **REFERENCE hub**. To navigate:

← Parent folder: [[../component-patterns|component-patterns]]
← Hub: [[../README|REFERENCE — Central Hub]]
← 02-References: [[../../README|02-References]]
← Brain root: [[../../README|00-brain-index]]

**Wired from:**
- [[../ultra-prompt-generator/DESIGNER/skill-router|skill-router]] (selection logic)
- [[../DIRECTOR/rules-engine|DIRECTOR rules engine]] (workflow)

*Every file in the corpus is reachable from the brain root in ≤5 hops.*
