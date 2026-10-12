# FE402 · Advanced UI: Animation, Graphics, WebGL and WebGPU

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [FE302](../../year_3/FE302_react_and_component_architecture/README.md) (and in practice [FE304](../../year_3/FE304_browser_internals_and_web_performance/README.md)) | [FE501](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md), [FE403](../FE403_ai_native_interfaces_streaming_generative_ui/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Frontend Engineering major](../../README.md). Uses the vectors, matrices and transformations of [FND113](../../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), FE304's rendering pipeline and frame budgets, and FE303's reduced-motion and contrast rules.

## Why this course matters now

Motion and graphics on the web have changed a lot since 2024:
- Same-document view transitions became Baseline in October 2025, and React 19.3 made `<ViewTransition>` stable in September 2026. Cross-document view transitions and scroll-driven animations are Interop 2026 focus areas but not yet Baseline.
- GSAP, including its formerly paid plugins, became 100% free with Webflow's backing.
- WebGPU now ships in Chrome (desktop since 113, Android 12+ since 121), Safari 26 and Firefox (Windows since 141), though Linux and some platforms are still in progress, so it is not Baseline.
- three.js offers a WebGPU renderer with WebGL 2 fallback.

Creative developers, design engineers and data-visualisation engineers are the people who make products feel fast and alive (see the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md)). AI assistants produce three.js scenes, shaders and D3 charts on request. They do not judge whether motion helps or distracts, whether a scene holds 60 fps on a budget phone's GPU, or whether a chart is readable by a screen-reader user. Those judgements, backed by measurement, are this course.

## Learning outcomes

By the end you can:

1. **Design** motion with intent (timing, easing, choreography) and **implement** reduced-motion alternatives that satisfy WCAG 2.2.2 and 2.3.3.
2. **Animate** at 60 fps on low-end devices by keeping work on the compositor, and **prove** it with frame timing in a trace.
3. **Build** page and element transitions with the View Transition API and React's `<ViewTransition>`, with fallbacks where support is missing.
4. **Choose** between CSS, the Web Animations API, Motion and GSAP for a given job, and **justify** the bundle and main-thread cost.
5. **Render** with SVG, Canvas 2D and OffscreenCanvas in workers, and **explain** when each beats the DOM.
6. **Program** the GPU with WebGL 2 (GLSL) and WebGPU (WGSL), including a compute shader, with feature detection and fallback.
7. **Build and optimise** three.js scenes (glTF, compressed textures, instancing, level of detail) to a stated frame and memory budget on mobile GPUs.
8. **Create** accessible, performant data visualisations with D3 and Observable Plot, scaling to large datasets with canvas or WebGL.

## Chapters and lessons

### Chapter 1 · Motion design and accessibility (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why motion | Feedback, continuity, attention, personality; when motion is noise | Critique motion in 5 apps; classify each animation by purpose |
| 1.2 Timing and easing | Durations by distance and size, cubic-bezier curves, the CSS `linear()` easing function, springs (stiffness, damping, mass) | Tune a sheet's open and close so they feel physical; compare spring and bezier |
| 1.3 Choreography | Staggering, shared elements, direction and hierarchy | Choreograph a list-to-detail transition on paper, then build it |
| 1.4 Motion accessibility | `prefers-reduced-motion`, vestibular triggers (parallax, zoom), WCAG 2.2.2 Pause/Stop/Hide, 2.3.1 Three Flashes, 2.3.3 Animation from Interactions | Ship reduced-motion variants of every animation in a sample app |

**Check your understanding:** What makes an animation feel "slow" even when it is short? Why is parallax a common accessibility complaint? What should replace a motion effect when reduced motion is on: nothing, a fade, or something else?

### Chapter 2 · CSS animation and the compositor (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Frame budgets | 16.7 ms at 60 Hz and 8.3 ms at 120 Hz; what consumes a frame (FE304) | Record an animation trace; find dropped frames and their cause |
| 2.2 Compositor-friendly properties | `transform` and `opacity`, layer promotion, `will-change` costs, GPU memory | Rewrite a width/height animation to `transform`; compare frame times |
| 2.3 The Web Animations API | `element.animate()`, timelines, playback control, `finished` promises, composite modes | Build a controllable animation sequence without a library |
| 2.4 FLIP | First, Last, Invert, Play for layout animations; measuring once, animating transforms | Animate a reorderable grid with FLIP at 60 fps on 4× CPU throttling |
| 2.5 Entry and exit | `@starting-style`, discrete property transitions, animating `display` and `<dialog>` | Animate a popover's entry and exit with no JavaScript |

**Check your understanding:** Why is animating `transform` smooth while animating `top` is not? When does `will-change` make things worse? Why does FLIP measure layout only once?

### Chapter 3 · View transitions and scroll-driven animation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Same-document view transitions | `document.startViewTransition`, snapshots, `view-transition-name`, `view-transition-class` (Baseline October 2025), pseudo-element styling | Shared-element transition from a product card to its detail view |
| 3.2 Cross-document transitions | `@view-transition` for multi-page apps (in Interop 2026, not Baseline); progressive enhancement | Animate navigation in a multi-page site with a no-op fallback |
| 3.3 React integration | `<ViewTransition>` and `addTransitionType` (React 19.3); transitions tied to state updates | Directional tab transitions driven by transition types |
| 3.4 Scroll-driven animation | Scroll and view timelines in CSS (not Baseline; Interop 2026), JavaScript fallback with IntersectionObserver | A scroll progress indicator and reveal effects with a fallback |

**Check your understanding:** What does the browser snapshot during a view transition, and why does that limit interactivity during it? How do you ship a cross-document transition without breaking browsers that lack it? Why are scroll-driven CSS animations cheaper than scroll event handlers?

### Chapter 4 · Animation libraries (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Motion | Declarative animations, layout animations, gestures, springs for React, Vue and vanilla JS | Rebuild the FLIP grid with Motion; compare code and bundle size |
| 4.2 GSAP | Timelines, ScrollTrigger, SplitText (free since Webflow's support), main-thread cost | A scroll-told product story with GSAP; measure INP while scrolling |
| 4.3 Designer-authored animation | Lottie (JSON from After Effects) and Rive (state machines, runtime interactivity); file sizes and rendering cost | Integrate one Lottie and one Rive animation; compare bytes and CPU time |
| 4.4 Choosing | A decision table: CSS/WAAPI first, libraries for orchestration and physics, designer tools for illustration | Write the motion guidelines section of a design system |

**Check your understanding:** When does a library's bundle cost pay for itself? Why can a GSAP scroll story hurt INP, and how do you prevent it? What does Rive's state machine give you that a Lottie file cannot?

### Chapter 5 · SVG in depth (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Coordinate systems | `viewBox`, `preserveAspectRatio`, transforms, user units | Make an icon set that scales cleanly from 16 to 256 px |
| 5.2 Paths | Line, cubic and quadratic Bézier commands, arcs; path data by hand | Hand-write the path for a logo shape; animate its stroke |
| 5.3 Animation and morphing | Stroke dash animation, path morphing (matching point counts), filters and masks | Animate a loading indicator that respects reduced motion |
| 5.4 Accessibility and icons | `role="img"` with `<title>`, decorative `aria-hidden`, icon systems, `currentColor` and forced colours | Audit an icon library for names and forced-colours behaviour |

**Check your understanding:** Why does an SVG icon disappear in forced-colours mode, and how do you fix it? When is SVG the wrong choice for many moving elements? How do you decide whether an SVG needs a name?

### Chapter 6 · Canvas 2D and off-main-thread rendering (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Immediate mode | The canvas state machine, paths, images, text; `devicePixelRatio` for crisp output | A crisp line chart at DPR 1, 2 and 3 |
| 6.2 Render loops | `requestAnimationFrame`, fixed vs variable time steps, dirty-rectangle redraws | A particle system at 60 fps with 5,000 particles |
| 6.3 Interaction | Hit testing (geometry, colour picking), pointer events, gestures | Draggable nodes on a canvas graph |
| 6.4 Workers | `OffscreenCanvas` in a worker, `ImageBitmap`, transfer costs | Move rendering into a worker; show main-thread time drop in a trace |
| 6.5 Accessibility of canvas | Fallback content, parallel DOM for focusable items, announcing state | Make the draggable graph operable by keyboard and screen reader |

**Check your understanding:** Why is a canvas blurry on a phone, and what is the fix? When does canvas beat SVG, and when does it lose? What must you add so a canvas-based UI is accessible?

### Chapter 7 · GPU fundamentals and WebGL 2 (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The graphics pipeline | Vertices, primitive assembly, rasterisation, fragments, depth testing, blending | Draw a triangle in raw WebGL 2 with no library (no AI) |
| 7.2 Shaders in GLSL | Vertex and fragment shaders, attributes, uniforms, varyings, precision on mobile GPUs | A fragment shader that draws a gradient and a circle by maths |
| 7.3 Transformations | Model, view and projection matrices; homogeneous coordinates; cameras | Rotate a cube with your own matrix code from FND113 |
| 7.4 Textures and lighting | Texture sampling, mipmaps, Lambert and Phong lighting | Textured, lit cube with correct mipmapping |
| 7.5 Performance | Draw calls, batching, instancing, overdraw, GPU memory on Mali- and Adreno-class phone GPUs | Draw 10,000 instances in one call; compare with 10,000 draw calls |

**Check your understanding:** Why do draw calls cost more than triangles in many scenes? What is the difference between a vertex shader's and a fragment shader's job? Why must you think about `mediump` precision on phones?

### Chapter 8 · Three.js and 3D on the web (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Scene graph | Scenes, meshes, cameras, materials (physically based), lights, shadows and their cost | A lit product turntable |
| 8.2 Assets | glTF 2.0, Draco geometry and KTX2/Basis texture compression, loading progress and streaming | Cut a model's transfer size by 70% with Draco and KTX2; compare visual quality |
| 8.3 Interaction and React | Raycasting, orbit controls, React Three Fiber 9; keeping React re-renders out of the frame loop | Click-to-select parts of a model in React Three Fiber |
| 8.4 WebGPU renderer and TSL | three.js `WebGPURenderer` with WebGL 2 fallback; Three Shading Language for node-based materials | Port the turntable to the WebGPU renderer with fallback |
| 8.5 Mobile performance | Level of detail, frustum culling, texture budgets, pixel-ratio caps, thermal throttling over minutes | Hold 30 fps for 5 minutes on a low-cost Android phone; report frame times |

**Check your understanding:** Why can a scene run at 60 fps for 30 seconds and then drop to 20? Which costs more on a budget phone, triangles or texture memory, and how do you find out? Why must the frame loop live outside React's render cycle?

### Chapter 9 · WebGPU basics (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The API | Adapters, devices, queues, command encoders, swap chains; how it differs from WebGL's global state | Render a triangle in raw WebGPU |
| 9.2 WGSL and pipelines | Render pipelines, bind groups, buffers and alignment rules | A textured quad with a uniform buffer |
| 9.3 Compute shaders | Workgroups, storage buffers, dispatch; particles and image filters on the GPU | A 100,000-particle simulation in a compute shader |
| 9.4 Support and fallback | Platform status (Chrome, Safari 26, Firefox on Windows and Apple-silicon macOS), feature detection, limits, device loss | Ship with WebGPU-first and a WebGL 2 fallback; handle device loss |

**Check your understanding:** What does WebGPU give you that WebGL 2 cannot, and when does that matter? Why is device loss something every WebGPU app must handle? Why is WebGPU not Baseline yet, and what does that mean for a product decision?

### Chapter 10 · Data visualisation with D3 (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Visual encoding | Position, length, colour, area; perceptual accuracy; choosing a chart for the question | Redesign 5 misleading charts |
| 10.2 D3 core | Scales, axes, data joins (`join`), transitions, shapes and layouts (hierarchy, force) | A bar chart race of state-wise data with smooth transitions |
| 10.3 Maps | Projections, GeoJSON and TopoJSON, choropleths; maps of India should follow the Survey of India's official boundary depiction | A district-level choropleth from public data with a correct legend |
| 10.4 Quick charts | Observable Plot for exploratory charts; when to stop hand-coding | Rebuild a D3 chart in 15 lines of Plot |

**Check your understanding:** Why is a pie chart with 12 slices a poor encoding? What does the data join's enter/update/exit pattern solve? Why must a choropleth be normalised by population?

### Chapter 11 · Accessible, performant visualisation and production graphics (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Accessible charts | Text summaries, data tables, keyboard navigation of data points, colour-blind-safe palettes, patterns as well as colours | Make a line chart navigable by keyboard with announced values |
| 11.2 Large data | Canvas and WebGL rendering for 100,000+ points (uPlot, deck.gl), downsampling, web workers | Plot 1 million points interactively; keep INP under 200 ms |
| 11.3 Real-time charts | Streaming updates, ring buffers, throttled rendering | A live chart at 10 updates per second with stable memory |
| 11.4 Production concerns | Loading strategies for heavy graphics, poster fallbacks, battery, visual regression for canvas | Add visual regression tests to a WebGL scene |

**Check your understanding:** What does a screen-reader user need from a chart: every point, a summary, or both? When should you downsample, and how do you avoid hiding important outliers? How do you test a WebGL scene in CI?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Motion audit | Reduced-motion variants |
| 2 | 2 | Lab 2 · Compositor and FLIP | 60 fps trace; **P1 starts** |
| 3 | 3 | Lab 3 · View transitions | Shared-element transition with fallback |
| 4 | 4 | Lab 4 · Libraries compared | Bundle and CPU table; **P1 due** |
| 5 | 5 | Lab 5 · SVG | Icon set and stroke animation |
| 6 | 6 | Lab 6 · Canvas in a worker | Accessible draggable graph |
| 7 | 7 | Lab 7 · Raw WebGL (no AI) | Triangle to lit cube; mid-term (AI off) |
| 8 | 7 | Lab 7 (cont.) · Instancing | Draw-call comparison |
| 9 | 8 | Lab 8 · Three.js assets | Compressed model; **P2 due** |
| 10 | 8 | Lab 8 (cont.) · Mobile soak | 5-minute frame-time report |
| 11 | 9 | Lab 9 · WebGPU compute | Particle simulation with fallback |
| 12 | 10 | Lab 10 · D3 and maps | Choropleth; **P3 starts** |
| 13 | 11 | Accessible, large-data charts | Keyboard chart; 1M points |
| 14 | 11 | Production graphics | **P3 due** |
| 15 | Review | P3 demo on a budget phone | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of shaders and three.js setup; explaining WebGPU validation errors; generating easing curves to compare; converting D3 v3–v5 examples to v7; writing visual regression harnesses.
- **Do without AI (drills):** raw WebGL from a blank file; matrix maths; FLIP from memory; hand-writing an SVG path; the mid-term (explain a frame trace and a shader on paper) and final.
- **Verify AI output by:** frame-time traces on a real budget phone, not only on your laptop; GPU validation layers and the WebGPU error scopes; visual comparison against a reference render; accessibility checks on every chart (keyboard, screen-reader summary, contrast); checking feature support against Baseline data.
- **Where AI still fails here (collect your own evidence):** look for generated animations that animate layout properties, ignore `prefers-reduced-motion`, or allocate objects every frame (garbage-collection stutter). Look for shaders that compile on desktop but fail on mobile precision, three.js code using APIs removed in recent releases, WebGPU code with misaligned buffers, and charts with misleading scales or colour-only encodings. Keep a log with the trace or screenshot that proves each failure.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h) and P3 demo on a budget phone | 20% |

**Mastery gate.** You pass when you can, with AI off, in 3 hours:
1. build a shared-element page transition and a reorderable list (FLIP), both holding 60 fps at 4× CPU throttling and both with reduced-motion variants;
2. write a WebGL 2 or WebGPU program from a blank file that renders an instanced, lit mesh;
3. make a provided D3 chart keyboard-navigable with a screen-reader summary.

You then explain one frame of your trace to an examiner.

## Industry reality

Product companies use motion to communicate state and brand. Data-heavy products (trading, analytics, logistics, maps) need engineers who can render large data fast. 3D product viewers and configurators appear in automotive and retail. The platform facts that shape those jobs in October 2026: WebGPU ships in all major engines on at least some platforms but is not Baseline; same-document view transitions are Baseline; GSAP is free; three.js renders through WebGPU with a WebGL fallback. Portfolios matter more here than anywhere else in frontend. A live, fast, accessible demo is the strongest application.

**Interview questions from this course**

1. *How would you animate a list when items are reordered?* A strong answer uses FLIP (or view transitions, or a library's layout animation), animates only transforms, handles interruptions, respects reduced motion, and explains why measuring layout once matters.
2. *This animation is janky on Android. How do you investigate?* A strong answer records a trace with CPU throttling or on a device, finds layout or paint work per frame, moves the animation to compositor properties, removes per-frame allocations, and checks main-thread work from other scripts.
3. *Canvas, SVG or WebGL for a chart with 500 points? With 500,000?* A strong answer picks SVG for 500 (accessible and stylable) and canvas or WebGL with downsampling for 500,000. It discusses hit testing, accessibility via summaries and tables, and memory.
4. *What is a draw call, and how would you make a three.js scene faster on mobile?* A strong answer defines a draw call as the CPU-to-GPU submission cost, then covers instancing and merging, texture compression (KTX2), level of detail, pixel-ratio caps, fewer lights and shadows, and frame-time measurement over minutes for thermal effects.
5. *How do you make a data visualisation accessible?* A strong answer gives a text summary of the insight, an accessible data table, keyboard navigation with announced values, palettes that do not rely on colour alone, sufficient contrast, and reduced-motion transitions. It tests with a screen reader.

## Resources (free first)

- **Animation:** [MDN Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API); [MDN View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API); [Chrome view transitions docs](https://developer.chrome.com/docs/web-platform/view-transitions); [React `<ViewTransition>`](https://react.dev/reference/react/ViewTransition); [Motion](https://motion.dev/); [GSAP](https://gsap.com/pricing/); [Lottie](https://airbnb.io/lottie/); [Rive](https://rive.app/); Josh Comeau's [CSS articles](https://www.joshwcomeau.com/css/).
- **Graphics:** [WebGL2 Fundamentals](https://webgl2fundamentals.org/); [WebGPU Fundamentals](https://webgpufundamentals.org/); [The Book of Shaders](https://thebookofshaders.com/); [three.js manual](https://threejs.org/manual/) and [docs](https://threejs.org/docs/); [WebGPU spec](https://www.w3.org/TR/webgpu/); [MDN WebGPU API](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API); [glTF](https://www.khronos.org/gltf/) and [KTX](https://www.khronos.org/ktx/).
- **Visualisation:** [D3](https://d3js.org/); [Observable Plot](https://observablehq.com/plot/); [uPlot](https://github.com/leeoniya/uPlot); [deck.gl](https://deck.gl/); public data from [data.gov.in](https://www.data.gov.in/); boundary guidance from the [Survey of India](https://surveyofindia.gov.in/).
- **Accessibility:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (2.2.2, 2.3.1, 2.3.3); [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/).

## Sources

All checked 12 Oct 2026.

- web.dev, "WebGPU is now supported in major browsers" (25 Nov 2025; per-browser versions and pending platforms) — https://web.dev/blog/webgpu-supported-major-browsers
- web.dev, "Same-document view transitions are now Baseline Newly available" (16 Oct 2025) — https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available
- Mozilla Hacks, "Launching Interop 2026" (cross-document view transitions and scroll-driven animations as focus areas) — https://hacks.mozilla.org/2026/02/launching-interop-2026/
- web-features 3.42.0 (WebGPU, scroll-driven animations, cross-document view transitions not Baseline; `view-transition-class` Oct 2025; Web Animations widely available) — https://web-platform-dx.github.io/web-features/
- React 19.3 (`<ViewTransition>` stable, `addTransitionType`) — https://react.dev/blog/2026/09/09/react-19-3
- GSAP pricing page ("GSAP is now 100% free for all users, thanks to Webflow's support") — https://gsap.com/pricing/
- npm registry versions on 12 Oct 2026: three 0.186.1, d3 7.9.0, motion 14.1.0, gsap 3.15.0, @react-three/fiber 9.8.1, pixi.js 8.22.0, @observablehq/plot 0.6.17 — https://registry.npmjs.org/

_Last reviewed: 2026-10_
