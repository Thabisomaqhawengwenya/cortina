# Cortina — A Little Scoop of Happiness

> **Cortina** is an artisan ice cream brand digital experience produced by Kefalos in Zimbabwe, featuring kinetic physics, Lenis smooth scrolling, GSAP MorphSVG jelly CTAs, and interactive SVG lighting sticker peeling mechanics.

---

## Overview

Cortina is a high-craft culinary digital experience transformed for Zimbabwe's iconic ice cream brand by **Kefalos Cheese Products (Pvt) Ltd** (Harare, Zimbabwe).

### Core Features

- **Kinetic Physics & Organic Jelly CTAs:** GSAP `MorphSVGPlugin` with spring easing transforms CTA buttons into randomized fluid organic blobs on hover.
- **Deconstructed Sundae Sticker Peeling:** Interactive sticker peeling mechanics with hardware-accelerated SVG specular lighting (`<feSpecularLighting>`, `<fePointLight>`, and `<feComposite>`), automatically adapting to lightweight drop shadows on mobile.
- **Buttery 120fps Smooth Scrolling:** Powered by `@studio-freight/react-lenis` coupled directly to the `gsap.ticker`.
- **Directional Angle Eye Tracking:** Pointer vector math (`Math.atan2`) dynamically points eyes and directional badges toward the user's cursor with zero-latency GSAP `quickSetter`.
- **Authentic Kefalos Catalog:** Features Classic Cortina (Vanilla, Strawberry, Chocolate, Cherry Ripple), Cortina Shamiso, and Cortina Cool Dudes fruit ice lollies across standard Zimbabwe pack sizes (125ml, 300ml, 1L, 2L, 5L, and commercial soft-serve mixes).

---

## Brand Palette

- **Primary Green:** `#007A3D` (Kefalos Cortina Brand Green)
- **Secondary Yellow:** `#FFC72C` (Cortina Sun Yellow)
- **Vanilla Cream:** `#FBF6EA` (Smooth Dairy Background)
- **Chocolate Brown:** `#2E1810` (Rich Cocoa Text & Accents)

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
