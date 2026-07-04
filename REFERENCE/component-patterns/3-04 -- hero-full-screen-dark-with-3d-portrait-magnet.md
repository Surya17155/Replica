# Hero — Full-Screen Dark with 3D Portrait + Magnet

```tsx
<div className="bg-[#0C0C0C] h-screen relative overflow-hidden flex flex-col justify-center items-center">
  <Navbar />
  <div className="relative z-10 text-center px-4">
    <p className="text-white/60 text-sm uppercase tracking-[0.3em] mb-8">Badge text</p>
    <h1 className="text-clamp(3rem, 15vw, 160px) font-bold tracking-[-0.04em] leading-[0.85]
                   bg-gradient-to-r from-white via-white/80 to-white/40 bg-clip-text text-transparent">
      Product Name
    </h1>
    <p className="text-white/50 text-lg mt-6 max-w-xl mx-auto">Supporting text</p>
    <div className="flex gap-4 justify-center mt-10">
      <PrimaryButton />
      <SecondaryButton />
    </div>
  </div>
  <Magnet padding={150} strength={3}>
    <img src="/portrait.png" className="absolute left-1/2 -translate-x-1/2 bottom-0 z-10
                                        w-[280px] lg:w-[520px]" />
  </Magnet>
</div>
```

### 3.05 Card — Sticky Stacking Card (Portfolio/Projects)

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
