# Lazy Loading Rule.Md

Version: 2.0 / @Surya17155

## Overview
The lazy loading rule ensures that the design system only loads the skills and resources needed for the current request. No asset or skill is loaded until it is explicitly referenced by the routing engine.

---

## Loading Behavior

1. Skills are stored as individual files - no monolithic load.
2. The routing response includes exact file paths for each skill.
3. The AI agent loads the primary skill file first, then secondary.
4. Group skill resources are loaded only when the routing response includes them.
5. After completion, all skill resources are unloaded from context.

---

## No-Preload Policy

This system DOES NOT preload skills or resources. Every skill is loaded on*emand. The routing engine is the only pre-loaded component. This maintains the system's footprint below context limits.

---

## Caching Strategy

1. Skill catalog is cached for the duration of the session
2. Skill fingerprints are cached until explicit invalidation
3. Active skill resources are cached only while the routing response is in use

