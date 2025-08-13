# Impossible Movie


A single-page cinematic playground that embraces deliberate glitches in physics, state, and narration. No build step is needed; open the page and the experience begins.

## Running

1. Clone this repository.

2. Run the setup script:

   ```bash
   python manage.py
   ```

   It installs npm dependencies and starts a dev server.
3. The script opens your default browser to the demo; if it doesn't, visit `http://localhost:5173` manually.
4. Click anywhere in the page once to unlock audio.

See [COMMANDS.md](COMMANDS.md) for additional invocation options.

## Architecture

 - **ES modules only.** Third-party libraries (Three.js, GSAP, Matter.js, XState, RxJS, Tone.js) are installed via npm and bundled by Vite.
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

All libraries are used with version pins:

- [Three.js](https://threejs.org/) – `0.160.0`
- [GSAP](https://greensock.com/gsap/) – `3.12.5`
- [Matter.js](https://brm.io/matter-js/) – `0.19.0`
- [XState](https://xstate.js.org/) – `4`
- [RxJS](https://rxjs.dev/) – `7.8.1`
- [Tone.js](https://tonejs.github.io/) – `14.8.49`

