---
title: "Professional Reference — Nova Hero Section (Interactive Portrait with Blob-Reveal)"
source: "external designer prompt (extracted from .docx)"
type: "reference"
date_extracted: 2026-06-24
use_as_template: true
notes: "Professional-grade prompt from a designer of one of the most viral interactive hero sections — use as a gold-standard structural template for our generated prompts"
---

# Professional Reference — Nova Hero Section (Interactive Portrait with Blob-Reveal)

> **Why this file exists:** This is the level of detail and structure our generated prompts must match. Every line below came from a real professional prompt that successfully replicated a Blob-reveal Three.js hero. Use this as the **structural template** when generating hero prompts for users.

> Source: external (extracted from `Prompt_Nova_Hero_Section_Interactive_Portrait_with_Blob-Reveal_Effect.docx` on 2026-06-24)

---

## Original Document

Prompt: Nova Hero Section (Interactive Portrait with Blob-Reveal Effect)

GET FREE CREDITS FOR MANUS HERE 👇

manus.im/redeem?c=otdhmdk

PROMPT START

Build me a full-screen interactive hero section for a React + Vite + TypeScript + Tailwind CSS v4 website. The hero section consists of 4 components that work together: a Preloader splash screen, a HeroSection scroll-driven wrapper, an InteractivePortrait Three.js canvas with a blob-reveal shader effect, and a SignatureMarqueeSection background text layer. Below is the exact specification for each.

Dependencies Required

npm install three @types/three framer-motion

Tailwind CSS v4 is used (imported via @import "tailwindcss" in CSS). The project uses Vite + React 19.

COMPONENT 1: Preloader (preloader.tsx)

A full-screen loading splash that appears for 3.5 seconds on page load, then slides up to reveal the hero.

Behavior:

On mount, lock body scroll (document.body.style.overflow = "hidden")

After 3500ms, set visibility to false and unlock body scroll

Uses Framer Motion AnimatePresence for exit animation

Exit animation: slides up (y: "-100%") over 0.8s with cubic-bezier easing [0.76, 0, 0.24, 1]

Visual Design:

Fixed overlay covering entire viewport, z-index: 9999

Background color: #e60000 (red)

Text color: white

Centered content with flexbox (column direction)

Content:

Main text: "NOVA" in a custom serif font called "Brier" (bold weight), sized text-6xl on mobile, text-8xl on tablet, text-9xl on desktop. Uppercase, tracking-tighter.

A small stylized lowercase "n" positioned absolutely above the "NOVA" text, centered horizontally (left-1/2), offset upward (-top-4 on mobile, -top-8 on tablet+). Same Brier font, sized text-2xl/text-4xl. It animates in with a spring animation after 0.5s delay (scale from 0 to 1).

The "NOVA" text fades in from below (opacity 0 to 1, y: 20 to 0) over 0.5s with 0.1s delay.

Bottom of screen: "LOAD NOVA" text in Oswald font (font-family: var(--font-oswald)), text-sm/text-base, bold, tracking-widest, uppercase. Positioned absolutely at bottom-12. Fades in after 0.6s delay.

Fonts needed:

"Brier" - a custom bold serif font. Load via @font-face from any CDN or local file. Use CSS variable --font-brier and Tailwind utility font-brier.

"Oswald" - Google Font. Load via Google Fonts CDN in index.html. Use CSS variable --font-oswald.

COMPONENT 2: SignatureMarqueeSection (signature-marquee-section.tsx)

An infinitely scrolling dual-line marquee text that sits behind the portrait.

Structure:

Full width/height container with flexbox centering, z-0, overflow-hidden

Two horizontal marquee rows stacked vertically with gap-4 (mobile) / gap-8 (desktop), py-10

All text is select-none and pointer-events-none

Top Row (moves left):

Framer Motion animate={{ x: [0, -1000] }} with repeat: Infinity, repeatType: "loop", duration: 20, ease: "linear"

4 duplicated <h2> elements for seamless looping

Text: "REDEFINING LIMITS" repeated 4 times per element

Font: Brier (font-[family-name:var(--font-brier)])

Size: text-[12vw] mobile, text-[8vw] desktop

Color: #D1FF1C (neon yellow-green)

leading-[0.9], tracking-tight, px-4

Bottom Row (also moves left, slower):

Same animation but duration: 25

Text: "FIGHTING FOR VICTORIES" repeated 4 times per element

Font: Oswald (font-[family-name:var(--font-oswald)]), bold, uppercase

Size: same responsive sizing

Color: white (text-white)

leading-[0.9], tracking-tighter, px-4

COMPONENT 3: HeroSection (hero-section.tsx)

A scroll-driven wrapper that creates a shrinking portrait effect with parallax text.

Structure:

<section> with h-[300vh] (3x viewport height for scroll distance), bg-[#1a1f1a]

Inside: a sticky top-0 h-screen container with overflow-hidden, centered with flexbox, bg-background

Scroll Animations (using Framer Motion useScroll + useTransform + useSpring):

scrollYProgress tracks the section's scroll from "start start" to "end end"

Smoothed with useSpring (stiffness: 100, damping: 30, restDelta: 0.001)

Animation | Scroll Range | Transform
Portrait scale | 0 → 0.4 | 1 → 0.45
Text opacity | 0 → 0.2 | 0 → 1
Exit translateY | 0.85 → 1 | "0%" → "-100%"
Exit opacity | 0.9 → 1 | 1 → 0

Layer Order:

Background layer (z-0): Contains SignatureMarqueeSection. Has exitY and exitOpacity applied. The marquee starts invisible and fades in as user scrolls (controlled by textOpacity).

Foreground layer (z-10): Contains InteractivePortrait. Has scale, exitY, and exitOpacity applied. The portrait starts full-screen and shrinks to 45% as user scrolls, revealing the marquee text behind it.

Timing: The InteractivePortrait is conditionally rendered only after a 2600ms delay (to wait for the Preloader to finish).

COMPONENT 4: InteractivePortrait (interactive-portrait.tsx) — THE CORE COMPONENT

A full-screen Three.js canvas that displays two image layers with an organic blob-reveal shader effect on mouse hover.

Concept: The user sees a base portrait image (Layer 1). When they move their mouse over the canvas, an organic, amorphous blob shape follows the cursor. Inside this blob, a different image (Layer 2) is revealed along with an animated liquid texture background. The blob has soft, organic edges that undulate with procedural noise, creating a living, breathing reveal effect.

Container:

<div> with ref, className="fixed inset-0 w-full h-full bg-[#1a1f1a] cursor-crosshair overflow-hidden", style={{ touchAction: "none" }}

Contains a small badge image in the bottom-left corner: absolute bottom-4 left-4 z-10 pointer-events-none, max-width 120px

Three.js Setup:

Scene with white background (0xffffff)

Orthographic camera (sized to container dimensions, positioned at z=1)

WebGLRenderer with antialias: true, alpha: true, pixel ratio capped at 2

Image Layers (3 planes stacked by z-position):

Layer | Z-Position | Content
baseImage | 0.0 | Base portrait (woman without helmet) — always visible
bgPlane | 0.05 | Animated liquid texture background — only visible inside blob
helmetImage | 0.1 | Helmet overlay portrait — only visible inside blob

Image URLs (replace with your own):

Layer 1 (base, no helmet): https://res.cloudinary.com/dn5e7ch16/image/upload/v1776746155/wo_helmet_d3ibwz.png

Layer 2 (with helmet): https://res.cloudinary.com/dn5e7ch16/image/upload/v1776746558/Untitled_design_20_v6crga.png

Both textures use THREE.SRGBColorSpace. The TextureLoader has crossOrigin = "anonymous" set.

Image Sizing: On load (and on resize), the base image's natural aspect ratio is calculated. The planes are sized to fit the container using "contain" logic: if the image is wider than the container, it fills width; if taller, it fills height. Both baseImage and helmetImage share the same plane geometry dimensions.

The Blob System (internal class Blob):

The blob is a feedback-loop shader that creates a persistent, fading mask texture.

Uniforms:

pointer: Vector2 — mouse position in NDC (-1 to 1), defaults to (10, 10) (off-screen)

pointerDown: 1 (always active — the blob appears on hover, not click)

pointerRadius: 0.35 — base radius of the blob

pointerDuration: 2.5 — controls how fast the blob fades when mouse moves away

Mouse tracking:

On mousemove: convert mouse position to NDC coordinates relative to the container

On mouseleave: set pointer to (10, 10) (far off-screen, effectively hiding the blob)

Blob Shader (fragment shader, injected via onBeforeCompile on a MeshBasicMaterial):*

// Noise functions

float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123); }

float noise(vec2 p) {
  vec2 i = floor(p); vec2 f = fract(p); f = f*f*(3.0-2.0*f);
  float a = hash(i); float b = hash(i + vec2(1.,0.));
  float c = hash(i + vec2(0.,1.)); float d = hash(i + vec2(1.,1.));
  return mix(mix(a,b,f.x),mix(c,d,f.x),f.y);
}

The shader logic (injected at #include <color_fragment>):

Read the previous frame's red channel from fbTexture (framebuffer feedback)

Subtract clamp(dTime / pointerDuration, 0., 0.05) — this makes the blob slowly fade

If pointer is active (pointerDown > 0.5):

Convert UV and mouse to aspect-corrected coordinates

Calculate angle and distance from cursor

Generate two layers of procedural noise based on angle and distance, animated by time

Create an organic radius variation: 0.7 + noiseVal*0.5 + noiseVal2*0.3

Multiply by pointerRadius to get the final organic radius

Use smoothstep to create a soft falloff from center to edge

Add this to the existing red value (accumulative, clamped 0-1)

Output the red channel value as the blob mask

Rendering pipeline:

Render the blob shader to a WebGLRenderTarget

Copy the framebuffer to a FramebufferTexture (this creates the feedback loop — each frame reads the previous frame's output)

Background Plane Shader (bgPlane):

This plane is only visible where the blob mask is active. It shows an animated liquid/organic texture.

Shader injection via onBeforeCompile:

Adds texBlob uniform (the blob's render target texture)

Adds time uniform

Modifies vertex shader to pass projected position as a varying (vPosProj)

Fragment shader logic:

Masking: Convert projected position to UV, sample texBlob. If red channel < 0.02, discard the pixel (invisible outside the blob).

Liquid animation (Domain Warping with fBm noise):

Three colors: colorBg = white (1.0), colorSoftShape = light gray (0.92), colorLine = medium gray (0.8)

Base UV scaled by 3.5

A distortion field (fbm at vUv * 2.0 + time * 0.2) creates slowly moving warping

Distortion strength: 0.7

The warped UV is fed into another fbm call to get the final noise value

Soft shapes are drawn using smoothstep(0.1, 0.9, sin(n * 3.0))

Fine lines are drawn using fract(n * 15.0) with a narrow smoothstep(0.49, 0.51, ...) band

Final color mixes background, soft shapes, and lines

fBm (Fractional Brownian Motion) function:

float fbm(vec2 p) {
  float value = 0.0;
  float amplitude = 0.5;
  for (int i = 0; i < 4; i++) {
    value += amplitude * noise(p);
    p *= 2.1;
    amplitude *= 0.3;
  }
  return value;
}

Helmet Image Shader (helmetImage):

Same masking logic as bgPlane — only visible inside the blob. Uses the same texBlob sampling and discard approach. No additional visual effects beyond the mask.

Animation Loop:

Uses THREE.Clock for delta time

Each frame: increment time, update uniforms, render blob, render scene

Uses requestAnimationFrame

Resize Handler:

Updates orthographic camera bounds

Updates aspect ratio uniform

Recalculates plane geometries based on new container size and image aspect ratio

Cleanup (on unmount):

Remove resize listener

Cancel animation frame

Remove renderer DOM element and dispose renderer

Traverse scene and dispose all geometries and materials

Dispose textures and render targets

CSS / Fonts Setup

In your global CSS file (index.css), you need:

@import "tailwindcss";

:root {
  --lorenzo-dark: #282c20;
  --background: #282c20;
  --font-oswald: "Oswald", sans-serif;
}

@font-face {
  font-family: "Brier";
  src: url("YOUR_BRIER_BOLD_FONT_URL") format("woff2");
  font-weight: bold;
  font-style: normal;
  font-display: swap;
}

@theme inline {
  --font-brier: "Brier", sans-serif;
  --font-oswald: var(--font-oswald);
  --color-background: var(--background);
}

@layer base {
  body {
    @apply bg-background text-foreground;
  }
}

In index.html, load Google Fonts:

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap" rel="stylesheet">

App-Level Integration

In your App.tsx:

import Preloader from "./components/preloader"
import Home from "./pages/Home"

function App() {
  return (
    <>
      <Preloader />
      <Home />
    </>
  )
}

In your Home.tsx, the HeroSection is the first section rendered:

import HeroSection from "../components/hero-section"

export default function Home() {
  return (
    <main className="relative">
      <HeroSection />
      {/* Other sections follow below */}
    </main>
  )
}

Summary of the Visual Effect

Page loads → Red splash screen with "NOVA" text animates in for 3.5 seconds, then slides up.

Hero revealed → Full-screen portrait of a woman (no helmet) on a white background fills the viewport. Cursor changes to crosshair.

Mouse hover → An organic, amorphous blob shape follows the cursor. Inside the blob, the viewer sees: (a) an animated liquid white/gray texture with flowing lines, and (b) the same woman but now wearing a helmet, layered on top of the liquid texture. The blob has soft, undulating edges that move organically due to procedural noise.

Mouse leaves → The blob slowly fades away over ~2.5 seconds, returning to the base portrait.

User scrolls → The portrait shrinks from 100% to 45% scale, revealing scrolling marquee text behind it ("REDEFINING LIMITS" in neon yellow-green, "FIGHTING FOR VICTORIES" in white). Eventually everything slides up and fades out to reveal the next section.

Output all 4 component files as complete, production-ready TypeScript React components. Do not omit any code. Include every shader line, every uniform, every animation parameter exactly as specified above.

PROMPT END

---

## Tools to Use (when generating similar prompts)

- **Frame-driven scroll video**: scroll-bound image-sequence playback
- **Three.js shader rigs**: blob-reveal, magnet, sticky-stack, etc.
- **GSAP ScrollTrigger**: scroll-driven image-sequence → see `skills-list/agents/skills/gsap-scrolltrigger/SKILL.md`
- **Image sequence generator**: insert image frames at every N px scroll, reverse on scroll-up

## Structural Pattern Discovered

The professional prompt has these layers (we mirror this in our generated prompts):

1. **Top-level goal in one sentence** (one-line brief)
2. **Tech stack + dependencies (npm install)** — explicit
3. **Components numbered separately**, each with:
   - Behavior (state, lifecycle, locks)
   - Visual design (colors, sizes, layout)
   - Content structure (sub-elements described individually)
   - Fonts (custom + Google Fonts)
4. **Per-section file paths** (`preloader.tsx`, etc.)
5. **Specific Tailwind classes** for everything

We adopt this structure for **every** hero/landing page prompt we generate — this is the motionsites.ai + professional-combination quality bar.

---

🧭 Navigation:
- [[../README|REFERENCE hub]]
- [[../_index|pinterest-doc index]]
- [[../../../../02-References/DIRECTOR/motion-effects-decision|motion-effects-decision]] (workflow rules this template implements)
- [[../../../../00-brain-index|00-brain-index]]
