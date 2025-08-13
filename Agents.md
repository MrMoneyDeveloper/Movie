# AGENTS.md — Brief for a Cinematic, Physics‑Breaking Static Website

**Status:** Draft v1.0\
**Owner:** Mohammed Farhaan (Lead Designer/Architect)\
**Goal:** Build a **single‑page, static** experience that blends cinema, game‑like open‑world systems, and deliberate **violations of physics** with explicit **fourth‑wall breaks**. **No local libraries or package installs.** All third‑party code must be referenced **via external **``**/**``** tags from CDNs** only. Complexity is a feature, not a bug.

---

## 1) Mission & North Star

Design a **watchable‑playable film**: a kinetic, interactive scene that **feels like a movie**, **behaves like a simulation**, and **talks to the viewer**. The world must occasionally **reject real‑world physics** (e.g., time glitches, impossible gravity, non‑Euclidean spaces) while an in‑world narrator **addresses the user directly**.

**Success looks like:**

- A seamless, cinematic loop (camera, score, choreography) that the user can interrupt and influence.
- Systemic interactions (entities, rules, economy) that create surprising outcomes.
- Timed, tasteful **fourth‑wall intrusions** that acknowledge the user’s presence/device/state.
- **Zero build step**: open `index.html` and the show begins.

---

## 2) Hard Constraints (Non‑negotiables)

1. **Static site only** (HTML/CSS/JS). Optional Service Worker is allowed but no server code.
2. **No packages, no local libraries.** All third‑party code via **CDN **``** or **`` only. Pin versions.
3. **Cinematic first.** Every system (physics, UI, audio) must support the filmic feel: framing, pacing, score.
4. **Complexity embraced**: layered systems, explicit state machines, ECS patterns; avoid trivial interactions.
5. **Accessibility**: fourth‑wall content must remain perceivable (captions/ARIA for meta‑narration).

---

## 3) Architecture (Browser‑Only)

- **Rendering Paths**: WebGL (primary via Three.js or PixiJS) → Canvas2D (fallback) → DOM (last resort).
- **Core Pattern**: **ECS** (Entity‑Component‑System) over a **state‑machine** director.
- **Event Bus**: RxJS subjects/observables for world events, camera cues, and UI diegesis.
- **Persistence**: IndexedDB or `localStorage` for run metadata (used by the fourth‑wall narrator).
- **Audio**: Procedural cues via WebAudio (Tone.js) synced to scene graph clocks.
- **Scheduling**: A scene **Director** orchestrates beats (enter, hold, exit) on a global timeline.

---

## 4) Agents & Responsibilities (ECS Roles)

- **Director** — Orchestrates scenes via state machines (intro ▶ open‑world ▶ set‑piece ▶ denouement). Owns tempo.
- **Cinematographer** — Controls camera rails, depth of field, dolly/handheld feel; enforces letterboxing.
- **World Architect** — Maintains **open‑world graph** (zones, portals, cells). Streams/instantiates entities on demand.
- **Physics Saboteur** — Intentionally violates physics rules (negative gravity pulses, time dilation, Escher rooms). Gatekept by timing & user actions.
- **Narrator (Fourth‑Wall)** — Breaks the wall respectfully: reads device/time/session state, speaks to the user, sometimes requests choices.
- **Choreographer** — Syncs motion (GSAP/Anime) to score and camera beats; handles bullet‑time, match cuts.
- **Foley/Score** — Generates/plays cues with Tone.js; ducking & side‑chain to narration.
- **UI–Diegesis Bridge** — Converts HUD to diegetic overlays; toggles debug monitors.
- **Archivist** — Persists run history, exposes it to Narrator for callbacks (“Welcome back at 10:04, Farhaan.”).
- **Performance Guardian** — Monitors FPS, heap, dropped frames; triggers adaptive quality.

---

## 5) Open‑World Systems Design (In a Single Page)

- **Graph of Zones**: Each zone = ruleset + ambiance + entity spawners.
- **Portals**: Spatial/non‑Euclidean transitions that defy physical continuity (e.g., door that returns older self).
- **Simulation Loop**: Fixed‑timestep tick; render interpolated. Systems run in priority bands (render > physics > AI > effects).
- **Economy of Weirdness**: Meter that governs frequency/intensity of physics breaks; reduces after big set‑pieces.
- **Diegetic UI**: Menus appear as in‑world objects (clapperboard, projector UI, slate cards).

---

## 6) Fourth‑Wall Playbook (Techniques)

- **Self‑awareness**: Read window size, timezone, language; acknowledge conditions (“Night shoot in Durban?”).
- **Temporal asides**: Narrator comments after user idle/return; uses Web Speech or caption overlay.
- **Debug Reveals**: Intentional peek at scene graph or event bus for one beat, then re‑diegetic fade.
- **Consent Gate**: Prompt before using mic/speech; always provide captions and mute.

---

## 7) Physics‑Breaking Catalogue (Implement at least 3)

1. **Gravity Inversion Pulses** — Entities float for a bar of the score; camera yaw locks to horizon.
2. **Escher Corridor** — Portal loop with changing field of view; spatial paradox via camera and scaled props.
3. **Time Stutter** — Frame duplication & variable playback rate; audio time‑stretch with grain.
4. **Impossible Light** — Shadows that move independent of sources; screen‑space decals faked in post.
5. **Klein Room** — Enter door A, exit rotated/reflected space; player position remapped.

Each violation is scripted by **Director** and enforced by **Physics Saboteur** with tunable intensity.

---

## 8) Interaction Model

- **Primary**: Mouse/trackpad orbit + keyboard WASD for drift; mobile: gyroscope parallax + tap holds.
- **Secondary**: Contextual prompts (diegetic devices). No menu overlays that break immersion.
- **Fail‑safes**: `Esc` toggles a minimal non‑diegetic control/help slate.

---

## 9) State & Dataflow

- **State Machines**: XState for Director & major sequences. Transitions tied to time/interaction/events.
- **Event Bus**: RxJS `Subject` channels: `world$`, `camera$`, `score$`, `narration$`, `weirdness$`.
- **Persistence**: `run_id`, `first_seen_at`, `zones_seen`, `violations_triggered`.

---

## 10) External Libraries (CDN‑Only; version‑pinned)

Use **one** rendering stack (Three *or* Pixi). Suggestion set:

**Rendering & Motion**

- Three.js — `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js`
- GSAP — `https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js`
- PixiJS (alternative to Three) — `https://cdn.jsdelivr.net/npm/pixi.js@8.2.1/dist/pixi.min.js`
- Anime.js (alternative motion) — `https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js`

**Physics & State**

- Matter.js — `https://cdn.jsdelivr.net/npm/matter-js@0.19.0/build/matter.min.js`
- XState — `https://cdn.jsdelivr.net/npm/xstate@4/dist/xstate.web.min.js`
- RxJS — `https://cdn.jsdelivr.net/npm/rxjs@7.8.1/dist/bundles/rxjs.umd.min.js`

**Audio**

- Tone.js — `https://cdn.jsdelivr.net/npm/tone@14.8.49/build/Tone.min.js`

**UI & Typography**

- Pico.css (lightweight) — `https://cdn.jsdelivr.net/npm/@picocss/pico@1.5.10/css/pico.min.css`
- Google Fonts (e.g., Inter, Cinzel) — standard fonts API link

> **Rule:** No bundlers. Only `<script src>` and `<link rel="stylesheet">`. Add SRI hashes when finalizing.

---

## 11) Example `index.html` Skeleton (CDN‑Only)

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Film • Simulation • Fourth Wall</title>
    <link rel="preconnect" href="https://cdn.jsdelivr.net" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1.5.10/css/pico.min.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;800&family=Cinzel:wght@400;700&display=swap" rel="stylesheet" />

    <!-- Rendering & Motion -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

    <!-- Physics & State -->
    <script src="https://cdn.jsdelivr.net/npm/matter-js@0.19.0/build/matter.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/xstate@4/dist/xstate.web.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/rxjs@7.8.1/dist/bundles/rxjs.umd.min.js"></script>

    <!-- Audio -->
    <script src="https://cdn.jsdelivr.net/npm/tone@14.8.49/build/Tone.min.js"></script>

    <style>
      :root { --film-black: #0a0a0a; --accent: #ffecd1; }
      body { background: var(--film-black); color: var(--accent); font-family: Inter, system-ui, sans-serif; }
      .letterbox { position: fixed; left: 0; right: 0; height: 6vh; background: #000; z-index: 10; }
      #topbar { top: 0; } #bottombar { bottom: 0; }
      canvas { display:block; width:100vw; height:100vh; }
      .slate { position: fixed; top: 1rem; left: 1rem; opacity: 0.8; }
    </style>
  </head>
  <body>
    <div id="topbar" class="letterbox"></div>
    <div id="bottombar" class="letterbox"></div>
    <main id="stage"></main>
    <aside class="slate" aria-live="polite" id="narration"></aside>

    <script>
      // Namespaces from UMD bundles
      const { gsap } = window;
      const { Matter } = window;
      const { XState } = window; // via xstate.web.min.js
      const { rxjs } = window; const { Subject } = rxjs;

      // Event bus
      const world$ = new Subject();
      const narration$ = new Subject();

      // Narrator (Fourth‑Wall) — minimal proof
      const say = (text) => {
        const el = document.getElementById('narration');
        el.textContent = text; // captions
        if ('speechSynthesis' in window) {
          const u = new SpeechSynthesisUtterance(text);
          u.rate = 1.0; window.speechSynthesis.speak(u);
        }
      };

      // Cold open
      say(`Fade in. ${new Date().toLocaleTimeString()} — you arrived.`);

      // TODO: mount Three.js scene, camera rails, physics sabotage, and state machines.
    </script>
  </body>
</html>
```

---

## 12) Experience Beats (Minimum Set‑Pieces)

1. **Cold Open:** Cinematographer locks shutter; letterbox bars slide; Narrator greets user by locale/time.
2. **Open‑World Drift:** Free roam through three zones; economy meter rises.
3. **First Violation:** Gravity inversion synchronized to score drop; particles swim upward.
4. **Fourth‑Wall Aside:** Debug overlay flashes; Narrator references the user’s return/idle.
5. **Set‑Piece:** Escher corridor + match cuts; time stutter on exit.
6. **Denouement:** Archivist saves run; Cinematographer executes a slow push‑in; fade to black.

---

## 13) Accessibility, Performance, Privacy

- **A11y**: All narrator content captioned; high‑contrast text; keyboard navigation available.
- **Perf**: Target 60 FPS; fall back to Canvas2D with reduced effects if < 45 FPS sustained.
- **Privacy**: No external analytics. Local storage only. Show a clear reset control.

---

## 14) Observability

- In‑world performance slate (FPS, frame time, active entities, GC events). Toggle with `~`.
- Log major transitions (zone enter/exit, violations triggered) to console and `localStorage` ring buffer.

---

## 15) Milestones (No Build Tools Required)

- **M0**: Skeleton loads; camera & narrator minimal (1 day)
- **M1**: Three zones + one physics violation + audio cue (2–3 days)
- **M2**: Fourth‑wall system + persistence + adaptive quality (2 days)
- **M3**: Two cinematic set‑pieces; polish pass; a11y & perf QA (2–3 days)

---

## 16) Risks & Mitigations

- **CDN reliability/version drift** → Pin versions; add SRI; provide two mirrors (jsDelivr + unpkg).
- **Mobile performance** → Early throttle detection; offer DOM/Canvas fallback scene.
- **A11y conflicts with diegesis** → Always duplicate in‑world speech with caption overlays.

---

## 17) Review Checklist

-

---

## 18) Open Questions (to sharpen the design)

- Which **two** violations are core to the identity (ship if only two make the cut)?
- Does the narrator’s **tone** break immersion or enhance it for your target audience?
- What is the minimum viable **zone graph** that still feels like an open world?
- Should music be **generative** (Tone) or **scored** (stems, licensed)?
- What **diegetic UI** objects best replace menus (slate, projector, clapperboard, CRT)?

---

## 19) License & Credits

- Attribute all libraries (Three.js, GSAP, Matter.js, RxJS, XState, Tone.js, Pico.css, Google Fonts).
- Provide links and versions in a dedicated `CREDITS.md`.

