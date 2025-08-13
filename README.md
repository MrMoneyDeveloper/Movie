# Impossible Movie

A single-page cinematic playground that embraces deliberate glitches in physics, state, and narration. No build step is needed; open the page and the experience begins.

## Running

1. Clone this repository.
2. Open `index.html` in a modern browser. For best results, launch a local server to bypass cross-origin limits:

   ```bash
   python3 -m http.server
   ```

   Then visit `http://localhost:8000` and load the page.
3. Click anywhere in the page once to unlock audio.

## Architecture

- **ES modules only.** All third-party libraries (Three.js, GSAP, Matter.js, XState, RxJS, Tone.js) load directly from CDNs via `import` statements.
- **Event bus.** RxJS subjects coordinate world and narration channels.
- **Entity–Component–System.** Entities own `Transform` and `Mesh` components; systems update motion and rendering each frame.
- **State machine director.** XState orchestrates beats: `intro → roam → violation → stutter` with timed transitions.
- **Audio timelines.** Tone.js loops drive percussion and pads, synced to the global clock.

## Highlights

- Gravity inversion pulses that flip the Matter.js simulation and tween entity velocity.
- Time-stutter effect that freezes rendering for several frames.
- Narrator speaks to the user with speech synthesis and captions, remembering visit count via `localStorage`.
- Orbit controls, multi-zone floor grid, and a background particle field.

## Credits

All libraries are loaded from CDNs with version pins:

- [Three.js](https://threejs.org/) – `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js`
- [GSAP](https://greensock.com/gsap/) – `https://cdn.jsdelivr.net/npm/gsap@3.12.5/index.js`
- [Matter.js](https://brm.io/matter-js/) – `https://cdn.jsdelivr.net/npm/matter-js@0.19.0/+esm`
- [XState](https://xstate.js.org/) – `https://cdn.jsdelivr.net/npm/xstate@4/es/index.js`
- [RxJS](https://rxjs.dev/) – `https://cdn.jsdelivr.net/npm/rxjs@7.8.1/+esm`
- [Tone.js](https://tonejs.github.io/) – `https://cdn.jsdelivr.net/npm/tone@14.8.49/+esm`

