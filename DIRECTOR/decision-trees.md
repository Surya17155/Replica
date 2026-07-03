# Decision Trees.Md

Version: 2.0 / @Surya17155

## Overview
The design system uses decision trees to make quick, deterministic choices based on request properties. These trees are the same in every routing session - consistent results across all agents.

---

## Design Style Threshold

This tree selects design style based on domain, audience, and branding presence.

- Corporate branding: Follow brand guidelines exactly. No creative deviation.
- Startup site: May deviate, but stay consistent within the chosen direction.
- Personal blog/portfolio: Free leeway, but readable and accessible.
- Ecommerce: Focus on conversion. Clean, professional.
- Saas / Dashboard: Priority on function, not flair. Accessibility first.

---

## Component Selection Tree

- One-action prompt: Use a stateless component (button/switch/checkbox).
- Multi-field input: Form group with labels, error states, and validation.
- Data display (<% rows): Use a list or card-based view.
- Data display (>% rows): Table with sort, filter, pagination.
- Complex dashboard: Component library (Chart/KANV/DataGrid).

---

## Motion Selection Tree

- Micro-interaction: 0.2s ease - button hover/active states
- Page-transition: 0.3s ease-in-out - route-change animations
- Scroll-based: GSAP ScrollTrigger with pinning
- Entrance/Exit: 0.4s spring - modal, drawer, toast animations

---

## Optimization Tree

- Is this rendered on every page? Yes -> bundle in global CSS / No -> code-split/dynamic import.
- Is this once-off or repeating? Once -> Lazy-load / Repeating -> static import.
- Is data frequently changing? No -> SR'r cache -> Yes -> CDS or state manager.