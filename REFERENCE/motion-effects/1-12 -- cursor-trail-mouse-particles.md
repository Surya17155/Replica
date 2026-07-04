# Cursor Trail (Mouse Particles)

**Visual cue:** Small dots or elements follow the mouse cursor with a trailing delay.

**Implementation:** Use RAF and array of positions:

```tsx
const trail = useRef([]);
const [dots, setDots] = useState([]);

const handleMouseMove = (e) => {
  trail.current.push({ x: e.clientX, y: e.clientY, id: Date.now() });
  if (trail.current.length > 20) trail.current.shift();
  setDots([...trail.current]);
};

return (
  <div onMouseMove={handleMouseMove} className="relative">
    {dots.map((dot, i) => (
      <div
        key={dot.id}
        className="fixed w-2 h-2 rounded-full bg-accent pointer-events-none"
        style={{
          left: dot.x, top: dot.y,
          opacity: i / dots.length,
          transform: `scale(${i / dots.length})`,
          zIndex: 9999
        }}
      />
    ))}
  </div>
);
```

**Performance:** ⚠️ Limit to 20 dots. Use CSS `will-change: none` on dots.

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