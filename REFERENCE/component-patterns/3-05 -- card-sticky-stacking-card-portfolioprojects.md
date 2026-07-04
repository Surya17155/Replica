# Card — Sticky Stacking Card (Portfolio/Projects)

```tsx
// Each card is a sticky section that scales down as the next pushes up
<section className="relative h-[300vh]">
  <div className="sticky top-0 h-screen flex items-center justify-center">
    <motion.div style={{ scale }} className="w-full max-w-4xl mx-auto p-8 rounded-[40px] bg-[#1A1A1A]">
      <span className="text-white/30 text-sm">01</span>
      <h2 className="text-4xl font-bold text-white mt-2">Project Title</h2>
      <p className="text-white/50 mt-4">Description</p>
      <div className="flex gap-4 mt-8">
        <div className="w-[60%] h-[300px] rounded-3xl overflow-hidden">
          <img className="w-full h-full object-cover" />
        </div>
        <div className="w-[40%] h-[300px] rounded-3xl overflow-hidden">
          <img className="w-full h-full object-cover" />
        </div>
      </div>
    </motion.div>
  </div>
</section>
```

### 3.06 Marquee / Logo Ticker

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
