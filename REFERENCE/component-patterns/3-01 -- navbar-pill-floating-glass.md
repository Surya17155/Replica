# Navbar — Pill / Floating Glass

```tsx
// src/components/Navbar.tsx
export default function Navbar() {
  return (
    <nav className="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-auto max-w-5xl">
      <div className="flex items-center justify-between px-8 py-3 rounded-full
                      bg-white/[0.04] backdrop-blur-[20px] border border-white/[0.08]
                      shadow-[0_8px_32px_rgba(0,0,0,0.12)]">
        <Logo />
        <ul className="hidden md:flex items-center gap-8 text-sm text-white/80">
          <li className="hover:text-white transition-colors">Link</li>
        </ul>
        <CTABookDemo />
        <Hamburger className="md:hidden" />
      </div>
    </nav>
  );
}
```

### 3.02 Navbar — Full-Width Transparent (Dark)

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
