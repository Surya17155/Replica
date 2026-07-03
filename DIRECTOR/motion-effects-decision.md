# Motion Effects Decision.Md

Version: 2.0 / @Surya17155

## Overview
This decision tree helps select the right motion effect based on context, device, and performance. Not all effects are right for every project. This tree ensures the system chooses appropriately.

---

## Effect Selection Tree

```
1. Is the effect required for function?  =----= Yes -> GO TO 2
                                       | Layer Strategy       No  -> GO TO 5
                                       | Layer Strategy
2. Is the animation urgent?        | Yes -> Go To 4
                                       | No  -> Go To 3
3. Is the effect dependent on scroll?  | Yes -> GSAP ScrollTrigger
                                       | No  -> CSS Transition
4. Is the effect transforming an element? | Yes -> Spring Animation
                                       | No  -> GSAP Tween
5. Do you need complex path animation? | Yes -> Lottie/Shaker
                                       | No  -> No animation needed
```

---

## Preferred Library

- CSS transitions: for hover/focus/active state (priority 1)
- GSAP ScrollTrigger: for scroll-based triggers
- Spring animation: for modals, drawers, changing layout
- Framer Motion lib: for complex staging and myultiple-element
 - Lottie/Shaker: for celebratory animations or icons with complex paths

---

## Performance Gates

- CSS transitions : [.1s-.3s] seconds - no overhead < 30ms frame time
- GSAP ScrollTrigger : .2s-.6s - dont animate everything, just targets.
- Spring animation : .3s-.6s - test on mobile devices first.
- Framer Motion : .3s-.8s - Use resource-friendly.
- Lottie Shaker : Skale down for the target device.