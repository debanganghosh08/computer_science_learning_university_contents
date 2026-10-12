# FE402 · Labs and projects

Performance evidence in this course is frame timing: a DevTools trace or `requestAnimationFrame` frame-time log, at least 60 seconds long. It is recorded both at 4× CPU throttling on a laptop and on a real low-cost Android phone. Every animation needs a reduced-motion variant, and every chart needs a text alternative. The raw WebGL lab is done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Motion audit | Classify animations in 5 apps by purpose; add reduced-motion variants to a sample app | Audit table; reduced-motion demo video | 3 h |
| 2 · Compositor and FLIP | Convert layout animations to transforms; FLIP grid reorder | Traces showing zero layout during animation; 60 fps at 4× CPU | 4 h |
| 3 · View transitions | Shared-element card-to-detail transition (same-document); cross-document with fallback; React `<ViewTransition>` tabs | Demo in Chrome, Safari and Firefox with documented fallbacks | 4 h |
| 4 · Libraries compared | The same scroll story in CSS/WAAPI, Motion and GSAP; one Lottie and one Rive asset | Table of bundle bytes, main-thread time and INP while scrolling | 5 h |
| 5 · SVG | Scalable icon set; hand-written path; stroke and morph animation; forced-colours support | Icons at 16–256 px; forced-colours screenshots | 4 h |
| 6 · Canvas in a worker | Interactive node graph on `OffscreenCanvas` in a worker, keyboard-accessible | Trace showing main-thread savings; screen-reader demo | 5 h |
| 7 · Raw WebGL (no AI) | Triangle → transformed cube → textured, lit cube → 10,000 instances | Code from a blank file; draw-call comparison | 8 h |
| 8 · Three.js assets and mobile soak | Compress a glTF model with Draco and KTX2; WebGPU renderer with fallback; 5-minute soak on a phone | Size and quality comparison; frame-time chart over 5 minutes | 6 h |
| 9 · WebGPU compute | 100,000-particle compute simulation with a WebGL 2 fallback and device-loss handling | Demo on two browsers; recovery from a simulated device loss | 6 h |
| 10 · D3 and maps | Bar chart race and a district-level choropleth from public Indian data, normalised correctly | Charts with text summaries and data tables; legend and source notes | 5 h |

## Projects

### P1 · Micro-interaction kit (L1, ~6 hours)

**Real-world inspiration:** product teams keep motion consistent through a small set of documented patterns. Large design systems publish their motion guidelines, for example in the motion sections of Material Design 3 and IBM Carbon.

**What to build:** a documented kit of 8 interactions for a design system:
- button press, toggle, toast enter/exit, dialog open/close;
- list add/remove, list reorder (FLIP), tab switch (view transition) and skeleton-to-content.

Each interaction comes with motion tokens (durations, easings), a reduced-motion variant and usage guidance.

**Acceptance criteria:**
- **Frames:** each interaction holds 60 fps at 4× CPU throttling (trace attached); zero layout or paint during transform-based animations.
- **Accessibility:** all variants honour `prefers-reduced-motion`; nothing flashes more than 3 times per second; focus is never delayed by an animation (tested with keyboard).
- **Tokens:** durations and easings come from tokens shared with FE303's token pipeline; no raw values in component CSS (lint check).
- **Size:** the kit adds at most 4 KB gzipped of JavaScript in total (CSS/WAAPI only, no library).
- **Documentation:** each interaction has a "when to use / when not to" note and a demo.

**Stretch goals:** a spring easing generated with CSS `linear()`; Motion or GSAP versions of two interactions, with a cost comparison.

**What it proves to an employer:** you can design and engineer motion as a system, with taste and with numbers.

### P2 · Scrollytelling data story: India's monsoon (L2, ~15 hours)

**Real-world inspiration:** newsrooms publish interactive, scroll-driven explainers built on public data. The India Meteorological Department's rainfall records, published as datasets on [data.gov.in](https://www.data.gov.in/), cover more than a century of sub-divisional monsoon rainfall.

**What to build:** a scroll-driven story showing:
- long-term monsoon rainfall and departures from normal;
- a sub-divisional or district map with year selection;
- a small-multiples view of extreme years;
- an explorable chart where readers pick a region.

Use D3 7 or Observable Plot, CSS scroll-driven animations with a JavaScript fallback, and an accessible alternative for every visual.

**Acceptance criteria:**
- **Data integrity:** every number traces to a dataset file and version listed in a sources section; a script regenerates all derived data; one reviewer checks 10 random figures against the source.
- **Accessibility:** each step has a text summary; each chart has a keyboard-navigable data view with announced values; colour-blind-safe palettes with patterns or labels; axe zero.
- **Performance:** scrolling holds 60 fps at 4× CPU throttling; INP at most 200 ms when switching regions; LCP at most 2.5 s on the FE304 baseline profile.
- **Progressive enhancement:** in browsers without scroll-driven animations the story still works, using IntersectionObserver.
- **Maps:** boundaries follow the Survey of India's official depiction; choropleths are normalised (rainfall departure, not raw totals by area).
- **Mobile:** fully usable at 360 px width and 200% font scale.

**Stretch goals:** Hindi version with localised number formats; an audio summary of each chart.

**What it proves to an employer:** you can turn data into an honest, accessible, fast interactive story, a skill valued in media, analytics and product teams.

### P3 · 3D product configurator with WebGPU and WebGL fallback (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** vehicle and furniture brands use web 3D viewers so buyers can change colours and parts before buying. The product here, an electric scooter, is an **illustrative scenario**. Use your own or a properly licensed model, and credit it.

**What to build:** a configurator with:
- a glTF model compressed with Draco and KTX2, with progressive loading and a poster fallback;
- colour, material and accessory options with smooth transitions, plus a shared-element transition from a product grid into the 3D view;
- a GPU particle effect (for example, an exploded-parts view) driven by a WebGPU compute shader, with a WebGL 2 fallback path;
- screenshot export, and a non-3D accessible mode (image gallery plus a specifications table);
- English and Hindi labels.

**Acceptance criteria:**
- **Budget:** initial transfer at most 3 MB including the model, measured on the network panel; the poster appears with LCP at most 2.5 s on the FE304 baseline profile.
- **Frames:** at least 30 fps sustained for 5 minutes on a low-cost Android phone (Helio G99-class or similar), and at least 60 fps on a mid-range laptop; frame-time charts attached. No frame-loop allocations (heap stays flat).
- **Fallback:** the same experience runs on WebGPU and on WebGL 2 (forced via a flag), with documented differences; device loss is recovered without a reload.
- **Interaction:** INP at most 200 ms when changing options.
- **Accessibility:** all options are reachable by keyboard and announced; the non-3D mode gives the same information; reduced motion disables camera fly-throughs and particles.
- **Engineering write-up:** what you cut to meet the mobile budget, with before/after measurements, and the AI-generated code you rejected and why.

**Stretch goals:** an augmented-reality preview through WebXR where supported (preview of FE501); a React Three Fiber version, with a comparison of frame times.

**What it proves to an employer:** you can deliver high-end 3D on the web that still works on budget phones and for users who cannot use 3D. That combination is rare in creative-developer portfolios.

## Feeds into

- [FE501 Frontier Seminar](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md): WebXR and spatial interfaces build on the 3D and WebGPU work.
- [FE403 AI-Native Interfaces](../FE403_ai_native_interfaces_streaming_generative_ui/README.md): motion and visualisation for streaming and agent progress, and WebGPU for on-device inference.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): graphics and visualisation capstones.
