---
name: industrial-brutalist-ui
description: Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints.
---

# industrial-brutalist-ui

Raw mechanical interfaces blending Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type-scale contrast, utilitarian color, analog degradation. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints.

## 1. Color Palette

- **Background:** `#0D0D0D` (near-black) or `#F5F5F0` (aged paper)
- **Text:** `#E5E5D9` (off-white on dark) or `#1A1A1A` (near-black on light)
- **Accent:** `#CC3333` (signal red), `#3399FF` (terminal blue), `#E5B800` (caution amber)
- **Muted:** `#666666` (gray terminals), `#999988` (faded ink)
- **Surface:** `#1A1A1A` (dark cards), `#E8E8E0` (light cards)
- **Border:** `#333333` (dark), `#CCCCC0` (light)
- **Overlay:** `#FF0000` at 8% opacity (scanline simulation)

## 2. Typography

- **Display:** `'Syne', 'Archivo Black', 'Arial Black'` — Ultra-bold, 16px-120px, 0.8-0.9 line-height
- **Mono/Data:** `'JetBrains Mono', 'IBM Plex Mono', 'Courier New'` — All data, nav, body copy
- **Body (alternative):** `'Inter', 'Space Grotesk', system-ui` — 14-16px, 1.4 line-height
- **Micro:** `'JetBrains Mono'` — 10-11px, uppercase tracking 0.15em
- **Weights:** 800 for headings, 400 for body, 500 for interactive
- **No italic, no decorative faces**

## 3. Layout Grid

- **Base grid:** 8px; sub-units at 4px for micro adjustments
- **Max-width:** `1440px` (dashboard-style full width) or `960px` (editorial)
- **Columns:** 12-column rigid grid with 16px or 8px gutter
- **Grid lines:** visible 1px border (`#333` or `#CCC`) — "blueprint" aesthetic
- **Padding:** tight — `24px` edge, `12-16px` between elements
- **No rounded corners** (except `2px` for input fields where necessary)

## 4. Components

### Terminal-Style Navbar
```html
<nav class="fixed top-0 inset-x-0 h-12 bg-[#0D0D0D] border-b border-[#333] flex items-center px-6 z-50">
  <span class="text-[#CC3333] text-xs font-mono tracking-wider uppercase">SYS::ROOT</span>
  <div class="ml-auto flex gap-6 text-xs font-mono text-[#999]">
    <a href="#" class="hover:text-[#E5E5D9] transition-colors">_work</a>
    <a href="#" class="hover:text-[#E5E5D9] transition-colors">_about</a>
    <a href="#" class="hover:text-[#E5E5D9] transition-colors">_contact</a>
  </div>
</nav>
```

### Hero (Blueprint)
```html
<section class="min-h-screen bg-[#0D0D0D] flex items-center border-b border-[#333]">
  <div class="max-w-[1440px] mx-auto px-6 py-24 w-full">
    <div class="grid grid-cols-12 gap-4">
      <div class="col-span-8">
        <p class="text-[#CC3333] text-xs font-mono tracking-[0.2em] uppercase mb-4">// 01_about</p>
        <h1 class="text-7xl md:text-9xl font-bold text-[#E5E5D9] leading-[0.85] tracking-tighter uppercase">
          INDUSTRIAL<br/>
          <span class="text-[#666]">BRUTALISM</span>
        </h1>
        <p class="mt-8 max-w-lg text-sm font-mono text-[#999] leading-relaxed">
          [RAW MECHANICAL INTERFACES] — Where Swiss typographic precision meets military-grade utility.
        </p>
      </div>
      <div class="col-span-4 border-l border-[#333] pl-4">
        <div class="text-xs font-mono text-[#666] space-y-2">
          <p>STATUS: <span class="text-[#33CC33]">OPERATIONAL</span></p>
          <p>VERSION: 2.4.1</p>
          <p>BUILD: 2026.06</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Dashboard Metric Block
```html
<div class="border border-[#333] p-4">
  <p class="text-[#666] text-[10px] font-mono tracking-[0.15em] uppercase">Total Requests</p>
  <p class="text-4xl font-bold text-[#E5E5D9] font-mono mt-1">2,847,392</p>
  <div class="flex gap-2 mt-2">
    <span class="text-[#33CC33] text-xs font-mono">↑ +12.4%</span>
    <span class="text-[#999] text-xs font-mono">vs last period</span>
  </div>
</div>
```

### Data Table
```html
<table class="w-full font-mono text-xs text-left border-collapse">
  <thead>
    <tr class="border-b border-[#333] text-[#666] uppercase tracking-[0.1em]">
      <th class="py-2 pr-4">Endpoint</th>
      <th class="py-2 pr-4">Status</th>
      <th class="py-2 pr-4">Latency</th>
      <th class="py-2">Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr class="border-b border-[#333]/50 hover:bg-white/5">
      <td class="py-2 pr-4 text-[#E5E5D9]">/api/v1/users</td>
      <td class="py-2 pr-4 text-[#33CC33]">200</td>
      <td class="py-2 pr-4">24ms</td>
      <td class="py-2">1.2k/s</td>
    </tr>
  </tbody>
</table>
```

## 5. Special Effects (Analog Degradation)

- **Scanlines:** repeating-linear-gradient overlay at 2px/50% opacity black on dark themes
- **Noise:** CSS `background-image` SVG noise at 0.5% opacity
- **Chromatic aberration (glitch):** `text-shadow` with red and cyan offsets on hover (only for special elements)
- **Ink bleed:** simulate with feather/gaussian blur on text-shadows in light mode
- **Crt curvature:** optional `border-radius: 2% / 4%` on full-page container (subtle)

### Scanline Overlay CSS
```css
.scanlines {
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 1px,
    rgba(0, 0, 0, 0.05) 1px,
    rgba(0, 0, 0, 0.05) 2px
  );
  pointer-events: none;
}
```

## 6. Motion (Minimal, Purposeful)

- **Duration:** fast — 100-200ms transitions
- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` (mechanical feel)
- **Hover:** immediate color swap, no scale
- **Page load:** instant paint, no fade-in. Data populates after render (skeleton state as empty dashes `--`)
- **No parallax, no marquee, no decorative animation**

## 7. Accessibility

- High contrast mode: use `#FFFFFF` on `#000000` as fallback
- Focus-visible: `2px solid #CC3333` (red) for dark, `2px solid #000` for light
- Respect `prefers-reduced-motion`: zero transitions
- All data visualization has text equivalents
- Monospace font ensures code-like clarity for screen readers
