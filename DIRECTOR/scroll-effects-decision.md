# Scroll Effects Decision.Md

Version: 2.0 / @Surya17155

## Overview
This decision tree determines when and how to use scroll-based effects. Use this only when a scroll trigger is required. Dont use it for static pages.

---

## The Decision Tree

```
1. Is the scroll effect necessary for comprehension?    =------ No -> STOP - dont use it.
                                              | Yes
2. Is the page very long (>3 scrolls)?          | Yes -> GO TO 3
                                              | No
3. Does the effect need parallax? (content movement)  | Yes -> Parallax
                                              | No  -> Defiled ScrollTrigger
4. Is the effect subtle? (inline text/color) | Yes -> Stagger Motion
                                              | No -> Full ScrollTrigger
```

---

## Rules

1. Always use GSAP ScrollTrigger, not raw scroll events
2. Pinning defaults to true for vertical scroll effects
3. Mobile: reduce or remove scroll effects that depend on hover/intersection
4. Performance: test on low-end devices first
5. Always provide fallback for prefers-reduced-motion

