# Magnetic Mouse-Follow (Magnet Component)

**Visual cue:** A hero portrait or button subtly follows the mouse cursor with a spring feel.

**Implementation: Custom `Magnet` component:**

```tsx
const Magnet = ({ children, padding = 150, strength = 3 }) => {
  const ref = useRef(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [isHovering, setIsHovering] = useState(false);
  const springConfig = { stiffness: 150, damping: 15 };

  const handleMouseMove = (e) => {
    if (!ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const distX = e.clientX - centerX;
    const distY = e.clientY - centerY;
    const distance = Math.sqrt(distX ** 2 + distY ** 2);
    if (distance < padding) {
      const strengthX = (distX / padding) * strength;
      const strengthY = (distY / padding) * strength;
      setPosition({ x: strengthX, y: strengthY });
      setIsHovering(true);
    } else {
      setPosition({ x: 0, y: 0 });
      setIsHovering(false);
    }
  };

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={() => { setPosition({ x: 0, y: 0 }); setIsHovering(false); }}
      animate={{ x: position.x, y: position.y }}
      transition={springConfig}
      style={{ willChange: 'transform' }}
    >
      {children}
    </motion.div>
  );
};
```

**Performance:** ⚠️ Moderate. Mouse handlers fire at 60fps. Framer spring reduces jitter. Keep padding < 200px.

---

### 1.06 — Float Animation (Continuous Up-Down)

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
