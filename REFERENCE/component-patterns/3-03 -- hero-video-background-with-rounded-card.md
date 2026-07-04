# Hero — Video Background with Rounded Card

```tsx
<div className="bg-[#F5F5F0]">
  <div className="max-w-7xl mx-auto px-6 pt-24 pb-16">
    <div className="rounded-[40px] overflow-hidden relative h-[85vh] min-h-[600px]">
      <video autoPlay muted loop playsInline className="absolute inset-0 w-full h-full object-cover">
        <source src={heroVideo} type="video/mp4" />
      </video>
      <div className="absolute inset-0 bg-gradient-to-t from-[#F5F5F0] via-black/20 to-transparent" />
      <div className="relative z-10 flex flex-col justify-end h-full p-12">
        <h1 className="text-5xl md:text-8xl font-bold text-white tracking-[-0.04em] leading-[0.9]">
          Headline
        </h1>
      </div>
    </div>
  </div>
</div>
```

### 3.04 Hero — Full-Screen Dark with 3D Portrait + Magnet

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
