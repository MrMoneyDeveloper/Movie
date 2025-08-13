# Impossible Movie

A single-page, physics-bending cinematic demo. Everything runs directly in the browser and all dependencies are loaded from CDNs.

## Running

1. Clone this repository.
2. Open `index.html` in any modern browser. No build step is required.
3. Optional: launch a local server to avoid browser security warnings:
   ```bash
   python3 -m http.server
   ```
   Then visit `http://localhost:8000` in your browser and open `index.html`.
4. Click once inside the page to enable audio.

## Features

- Letterboxed cinematic layout.
- Narrator addressing the viewer with speech synthesis and captions.
- Three physics-breaking effects: gravity inversion pulses, time stutter, and an impossible light that moves independent of the cube.

## Credits

All libraries are loaded from CDNs:
- [Three.js](https://threejs.org/) via jsDelivr.
- [GSAP](https://greensock.com/gsap/).
- [Matter.js](https://brm.io/matter-js/).
- [XState](https://xstate.js.org/).
- [RxJS](https://rxjs.dev/).
- [Tone.js](https://tonejs.github.io/).
