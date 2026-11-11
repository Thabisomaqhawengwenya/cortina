# Cortina — Artisan Gelato & Ice Cream Experience

> **Cortina** is an artisan gelato experience with kinetic physics, Lenis smooth scrolling, GSAP MorphSVG jelly CTA buttons, and interactive SVG lighting sticker peeling mechanics.

---

## Overview

Cortina is a high-craft culinary digital experience reimagined as an authentic Italian gelato and slow-churned ice cream brand (inspired by the heritage of Cortina d'Ampezzo).

### Core Features

- **Kinetic Physics & Organic Jelly CTAs:** GSAP `MorphSVGPlugin` with spring easing transforms CTA buttons into randomized fluid organic blobs on hover.
- **Deconstructed Sundae Sticker Peeling:** Interactive sticker peeling mechanics with hardware-accelerated SVG specular lighting (`<feSpecularLighting>`, `<fePointLight>`, and `<feComposite>`), automatically adapting to lightweight drop shadows on mobile.
- **Buttery 120fps Smooth Scrolling:** Powered by `@studio-freight/react-lenis` coupled directly to the `gsap.ticker`.
- **Directional Angle Eye Tracking:** Pointer vector math (`Math.atan2`) dynamically points eyes and directional badges toward the user's cursor with zero-latency GSAP `quickSetter`.
- **Complete Menu & Concept Checkout:** Interactive cart drawer with floating counter pill and toast notifications.

---

## Tech Stack

- **Framework:** Next.js App Router (Turbopack)
- **Styling:** Tailwind CSS v4 with CSS Custom Properties & Oklab color mixing
- **Animation:** GSAP 3 (`ScrollTrigger`, `MotionPathPlugin`, `MorphSVGPlugin`, `InertiaPlugin`)
- **Typography:** Google Fonts (`Modak`, `Mouse Memoirs`)
- **Smooth Scroll:** ReactLenis

---

## Getting Started

Start the local server:

```bash
npm start
```

Visit [http://localhost:3000](http://localhost:3000) in your browser.

---

## License

MIT © [Maqhawe T Ngwenya](https://github.com/Thabisomaqhawengwenya)
