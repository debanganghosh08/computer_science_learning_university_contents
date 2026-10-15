# CSG304 · Computer Graphics

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L4 | [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md); draws on [FND113](../../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) and [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) | [CSG404](../../year_4/CSG404_programming_language_theory_and_type_systems/README.md) (catalog sequence); electives [DLR404](../../../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md), [DLR402](../../../deep_learning/year_4/DLR402_multimodal_models/README.md); overlap [OV11](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). No earlier course in this university covers graphics, so the course starts from pixels and colour (L1) and ends with path tracing and neural rendering (L4). It uses linear algebra from FND113, probability from FND116 for Monte Carlo rendering, and the memory hierarchy from CS202 for GPU performance.

## Why this course matters now

Graphics is the most visible use of parallel computing, and it is changing fast. WebGPU, a modern GPU API with compute shaders, became available in all major browsers by November 2025 (Chrome 113 onward, Safari 26, Firefox 141 on Windows) ([web.dev](https://web.dev/blog/webgpu-supported-major-browsers)), so a renderer can now ship as a web page. 3D Gaussian Splatting (SIGGRAPH 2023) rendered captured scenes in real time at 1080p ([Kerbl et al.](https://arxiv.org/abs/2308.04079)), three years after NeRF showed neural scene representations ([Mildenhall et al., 2020](https://arxiv.org/abs/2003.08934)); by February 2026 Khronos had published a release candidate of a glTF extension for Gaussian splats ([Khronos](https://www.khronos.org/news/permalink/khronos-announces-gltf-gaussian-splatting-extension)). Game engines combine rasterization with virtualized geometry and real-time global illumination (Unreal Engine's [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine) and [Lumen](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine)), and offline film rendering is physically based path tracing, documented in the free 4th edition of *Physically Based Rendering* ([pbr-book.org](https://pbr-book.org/)). AI assistants write shader code quickly, but rendering bugs are often numerical and visual: wrong colour space, normals transformed by the wrong matrix, biased estimators that "look fine". The people hired for graphics roles can derive the maths, measure the frame, and prove an image is converging to the right answer.

## Learning outcomes

By the end you can:

1. **Explain** sampling, aliasing, colour spaces, gamma and tone mapping, and **fix** images that are too dark, banded or aliased.
2. **Derive and implement** model, view and projection transforms, quaternion rotation, and correct normal transformation.
3. **Implement** a software rasterizer with clipping, depth buffering and perspective-correct interpolation.
4. **Program** the GPU with WebGPU (WGSL) or Vulkan, and **explain** SIMT execution, occupancy and memory bandwidth limits.
5. **Implement** texturing with mipmaps and filtering, and physically based shading with microfacet BRDFs and image-based lighting.
6. **Build** real-time techniques (shadow maps, deferred and clustered shading, temporal anti-aliasing) and **profile** frames against a 16.6 ms budget.
7. **Build** a BVH ray tracer and an unbiased path tracer with importance sampling and multiple importance sampling, and **verify** it against a reference renderer.
8. **Train and render** neural scene representations (NeRF, 3D Gaussian Splatting) and **evaluate** them with PSNR, SSIM and LPIPS on held-out views.
9. **Use** AI tools for shader and tooling work while **catching** their typical numerical and colour-space errors.

## Chapters and lessons

### Chapter 1 · Images, colour and sampling (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Images as samples | Pixels as point samples of a continuous signal; the sampling theorem; aliasing and jaggies | Render a zone plate with 1 and 16 samples per pixel; explain the moiré |
| 1.2 Colour | Human vision, RGB primaries, sRGB vs linear light, the gamma curve, why averaging must happen in linear space | Blend two colours in sRGB and in linear space; show the dark fringe |
| 1.3 High dynamic range | Radiance values above 1, exposure, tone mapping (Reinhard, ACES-style filmic) | Tone-map an HDR image three ways and compare |
| 1.4 Image formats and displays | 8-bit vs 10-bit, banding and dithering, HDR displays | Show banding in an 8-bit gradient and remove it with dithering |

**Check your understanding:** (1) Why is anti-aliasing a sampling problem, not a "blur" problem? (2) Why do lighting calculations in sRGB space look wrong? (3) What information does tone mapping throw away, and why is that acceptable?

### Chapter 2 · Transforms and cameras (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Homogeneous coordinates | Points vs vectors (w = 1 vs 0), affine transforms as 4×4 matrices, composition order | Build a transform hierarchy (solar system) and animate it |
| 2.2 Projection | Perspective and orthographic projection, the view frustum, normalized device coordinates, depth precision and reversed-Z | Plot depth-buffer precision for near = 0.01 and 1.0 |
| 2.3 Normals | Why normals transform by the inverse transpose; non-uniform scaling | Break lighting with a non-uniformly scaled sphere, then fix it |
| 2.4 Rotations | Euler angles and gimbal lock; quaternions; slerp | Interpolate a camera orientation with Euler angles and with slerp; compare paths |
| 2.5 Cameras and scene graphs | Look-at matrices, field of view, scene graph traversal | Lab 2: an orbit camera and scene graph |

**Check your understanding:** (1) Why do vectors ignore translation? (2) Why is depth precision worst far from the camera with a standard projection? (3) When do you need slerp instead of linear interpolation?

### Chapter 3 · The rasterization pipeline (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Triangles and edge functions | Coverage tests, top-left fill rule, bounding-box traversal | Lab 1: rasterize triangles in software with no gaps or double-drawn pixels |
| 3.2 Barycentric interpolation | Barycentric coordinates; perspective-correct interpolation (divide by w) | Show the texture "swimming" bug without perspective correction, then fix it |
| 3.3 Visibility | Depth buffer, z-fighting, painter's algorithm and why it fails | Render intersecting triangles both ways |
| 3.4 Clipping and culling | Clipping against the near plane (Sutherland–Hodgman), back-face and frustum culling | Clip a triangle that crosses the near plane |
| 3.5 The hardware pipeline | Input assembly, vertex shading, rasterization, fragment shading, output merging; where each runs | Map every stage of your software rasterizer to the GPU stage |

**Check your understanding:** (1) Why must interpolation divide by w? (2) Why do adjacent triangles need a fill rule? (3) Why must clipping happen before the perspective divide?

### Chapter 4 · Programming the GPU (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 GPU architecture | SIMT, warps/wavefronts, divergence, occupancy, latency hiding, memory bandwidth vs compute | Estimate whether a full-screen shader is compute- or bandwidth-bound |
| 4.2 WebGPU and WGSL | Adapters, devices, buffers, bind groups, render and compute pipelines, command encoders | Lab 3: a WebGPU mesh viewer loading glTF |
| 4.3 Vulkan concepts | Explicit synchronization, render passes, descriptor sets, pipeline state; why explicit APIs exist | Read the triangle chapter of the Vulkan tutorial and annotate every object |
| 4.4 Compute shaders | Workgroups, shared memory, parallel reduction and prefix sum on the GPU | Implement a GPU prefix sum; compare with a CPU version |
| 4.5 Debugging and profiling | RenderDoc captures, GPU timestamps, overdraw views | Capture one frame and explain every draw call |

**Check your understanding:** (1) Why does branch divergence slow a shader? (2) What does high occupancy buy, and when does it not help? (3) Why do explicit APIs (Vulkan, WebGPU) push synchronization onto the programmer?

### Chapter 5 · Texturing (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Texture mapping | UV coordinates, wrapping modes, texture atlases | Map a texture onto a sphere and fix the seam |
| 5.2 Filtering | Magnification (bilinear), minification (mipmaps, trilinear), anisotropic filtering | Lab 4: show shimmering without mipmaps; measure the cost of each filter |
| 5.3 Detail maps | Normal maps and tangent space, displacement, parallax | Light a flat quad with a normal map |
| 5.4 Compression | Block compression (BC1–BC7, ASTC), memory and bandwidth savings | Compress three textures; report size and PSNR |

**Check your understanding:** (1) Why do mipmaps reduce aliasing *and* improve performance? (2) Why do normal maps need a tangent frame? (3) Why are GPU texture formats block-compressed rather than PNG-like?

### Chapter 6 · Shading and materials (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Radiometry | Radiant flux, irradiance, radiance, solid angle; the cosine term | Compute irradiance from a point light at three angles |
| 6.2 BRDFs | Definition, reciprocity, energy conservation; Lambertian; Blinn–Phong as an approximation | Numerically check energy conservation of Blinn–Phong; show where it fails |
| 6.3 Microfacet models | Cook–Torrance: distribution (GGX), Fresnel (Schlick), geometry term; roughness | Lab 5: GGX shading in WGSL with a roughness/metalness grid of spheres |
| 6.4 Image-based lighting | Environment maps, pre-filtered specular, irradiance maps, split-sum approximation | Light your spheres with an HDR environment map |
| 6.5 Material standards | Disney "principled" BRDF ideas; glTF metallic-roughness; physically based cameras | Render the glTF sample assets and compare with a reference viewer |

**Check your understanding:** (1) Why does a physically based BRDF need to integrate to at most 1? (2) What does roughness change in GGX, and why do rough surfaces look dimmer at the peak? (3) What does the split-sum approximation trade away?

### Chapter 7 · Real-time rendering techniques (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Shadows | Shadow maps, bias and peter-panning, PCF, cascaded shadow maps | Lab 6: cascaded shadows for a large outdoor scene |
| 7.2 Many lights | Forward, deferred and clustered (forward+) shading; G-buffers and bandwidth | Render 1,000 point lights with clustered shading; compare frame times |
| 7.3 Screen-space effects | SSAO, screen-space reflections and their failure cases | Show SSR failing at screen edges and explain why |
| 7.4 Temporal methods | Temporal anti-aliasing, history rejection, ghosting; temporal upscaling (the idea behind DLSS and FSR) | Implement TAA; produce and then reduce ghosting |
| 7.5 Geometry at scale | Level of detail, instancing, GPU-driven culling; virtualized geometry (Nanite) at the concept level | Instance 100,000 objects with GPU frustum culling |

**Check your understanding:** (1) Why does deferred shading struggle with transparency and MSAA? (2) Why does TAA ghost, and what signal tells you to reject history? (3) What is the frame-time cost of a 4-cascade shadow map at 1080p in your renderer?

### Chapter 8 · Ray tracing and acceleration structures (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Ray–primitive intersection | Ray–sphere, ray–triangle (Möller–Trumbore), numerical robustness and self-intersection | Build intersection tests with randomized checks against a brute-force reference |
| 8.2 BVH construction | Bounding volumes, median split vs surface area heuristic (SAH), binned SAH | Lab 7: SAH BVH; measure speed-up over brute force on a 1M-triangle mesh |
| 8.3 Traversal | Stack-based traversal, near-first ordering, packet and wide BVHs | Count node visits per ray for two split strategies |
| 8.4 Hardware ray tracing | BLAS/TLAS in DXR and Vulkan ray tracing; what RT cores accelerate | Map your BVH design to the two-level hardware model |

**Check your understanding:** (1) Why does SAH produce faster trees than median splits? (2) Why does a ray hit its own surface without an offset, and how do you fix it robustly? (3) Why are acceleration structures two-level in hardware APIs?

### Chapter 9 · Path tracing (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The rendering equation | Kajiya's equation; direct vs indirect light; why it needs integration | Write the equation for a Cornell box point and name each term |
| 9.2 Monte Carlo integration | Estimators, bias, variance, convergence rate 1/√N | Estimate an integral with uniform and importance sampling; plot variance |
| 9.3 Importance sampling and MIS | Cosine-weighted and BRDF sampling, light sampling, multiple importance sampling (Veach) | Lab 8: a path tracer with next-event estimation and MIS |
| 9.4 Unbiased and efficient | Russian roulette, the white-furnace test, reference comparisons | Pass the furnace test; compare with a Mitsuba 3 reference |
| 9.5 Real-time path tracing | Few samples per pixel, spatiotemporal resampling (ReSTIR), denoisers (Open Image Denoise) | Denoise a 4-spp image; measure error against 4,096 spp |

**Check your understanding:** (1) Why does halving noise cost four times the samples? (2) Why does MIS beat both of its component strategies on glossy surfaces with small lights? (3) Why can a denoised image look better but be more wrong?

### Chapter 10 · Geometry and animation (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Mesh data structures | Indexed meshes, half-edge structures, manifoldness | Build a half-edge mesh and walk the one-ring of every vertex |
| 10.2 Mesh processing | Loop subdivision, quadric error metric simplification | Lab 9: simplify a 1M-triangle mesh to 10k; report Hausdorff error |
| 10.3 Curves and surfaces | Bézier curves, de Casteljau, B-splines | Draw and subdivide a cubic Bézier |
| 10.4 Character animation | Skeletons, linear blend skinning and its candy-wrapper artefact, dual quaternion skinning | Skin an arm; show and fix the artefact |

**Check your understanding:** (1) Why does the half-edge structure make adjacency queries O(1)? (2) What does the quadric error metric measure? (3) Why does linear blend skinning collapse volume at twisted joints?

### Chapter 11 · Neural rendering (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 From photos to cameras | Structure from motion with COLMAP; camera intrinsics and poses | Capture 150 photos of an object or room you have permission to film; recover poses |
| 11.2 NeRF | Volume rendering as an integral, positional encoding, hierarchical sampling | Train a small NeRF with nerfstudio; render a held-out view |
| 11.3 Fast neural fields | Instant-NGP's multiresolution hash grid; why training dropped from hours to minutes | Compare training time and PSNR for two representations |
| 11.4 3D Gaussian Splatting | Anisotropic Gaussians, spherical-harmonic colour, sorting and alpha compositing, densification and pruning, differentiable rasterization | Lab 10: train 3DGS with gsplat on your capture |
| 11.5 Evaluation and formats | PSNR, SSIM, LPIPS on held-out views; floaters and view-dependent artefacts; PLY and the glTF splat extension | Report metrics and an artefact gallery for your scene |

**Check your understanding:** (1) Why is rasterizing Gaussians so much faster than marching rays through a neural field? (2) What does a high PSNR on training views fail to tell you? (3) Why must Gaussians be sorted per view, and what goes wrong if the sort is approximate?

### Chapter 12 · Graphics in production, with AI in the loop (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Frame budgets | 16.6 ms at 60 Hz and 11.1 ms at 90 Hz (VR); CPU-bound vs GPU-bound; draw-call and state-change costs | Lab 11: profile your P3 renderer and remove the top bottleneck |
| 12.2 Testing renderers | Golden images with tolerance, perceptual metrics, furnace and reciprocity tests | Add image-diff tests to CI |
| 12.3 AI in graphics work | Shader generation, upscaling networks, generative 3D assets; known failure modes | Run the AI shader audit (see below) |
| 12.4 Ethics of capture | Consent for scanning people and private places; synthetic media labelling | Write the capture policy for your P3 |

**Check your understanding:** (1) How do you tell whether a frame is CPU-bound or GPU-bound in one measurement? (2) Why are golden-image tests flaky across GPUs, and how do you make them robust? (3) What would you check first in an AI-written PBR shader?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Colour and sampling exercises | Image set with explanations |
| 2 | 2 | Lab 2 · Cameras and scene graphs | — |
| 3 | 3 | Lab 1 · Software rasterizer | **P1 starts** |
| 4 | 4 | Lab 3 · WebGPU mesh viewer | **P1 due** |
| 5 | 5 | Lab 4 · Textures and mipmaps | — |
| 6 | 6 | Lab 5 · PBR shading | **P2 starts** |
| 7 | 7 | Lab 6 · Shadows and many lights | Mid-term (AI off) |
| 8 | 8 | Lab 7 · BVH | — |
| 9 | 9 | Lab 8 · Path tracer | — |
| 10 | 9 | Path tracer (cont.) | **P2 due** |
| 11 | 10 | Lab 9 · Mesh processing | P3 capture and plan |
| 12 | 11 | NeRF with nerfstudio | — |
| 13 | 11 | Lab 10 · Gaussian splatting | P3 midpoint |
| 14 | 12 | Lab 11 · Profiling | **P3 due** |
| 15 | Review | Live debugging oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** WebGPU and Vulkan boilerplate (device setup, buffer layouts, bind groups); glTF and image loaders; UI for parameter tweaking; explaining a RenderDoc capture or an unfamiliar engine's code; first drafts of shaders that you then test; scripts for metrics (PSNR, SSIM, LPIPS) and plots.
- **Do without AI (drills):** derivations of projection matrices, normal transforms, perspective-correct interpolation and the Monte Carlo estimator; BRDF energy checks; the software rasterizer core and BVH build; hand-debugging a frame; the mid-term and final.
- **Verify AI output by:** furnace and reciprocity tests for BRDFs; comparison against Mitsuba 3 or pbrt reference images with a stated error threshold; checking colour space at every texture load and render-target write; unit tests for intersection code against brute force; GPU timestamps for any performance claim.
- **Where AI still fails here (show it):** in the AI shader audit (Lab 5 and Chapter 12), ask two assistants for a GGX shader, a normal-mapping shader and a TAA resolve, then run your tests. Look for these specific failures: lighting computed in sRGB space; normals multiplied by the model matrix instead of its inverse transpose; a GGX term missing its 1/π or cosine factor (fails the furnace test); TAA without history rejection (ghosting). Record each with a screenshot and the test that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + live debugging oral | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) derive the perspective projection and perspective-correct interpolation on a whiteboard and explain each term; (2) given a BRDF, check reciprocity and energy conservation numerically; (3) given a RenderDoc capture of a broken frame with two planted bugs (for example, a gamma error and a wrong normal transform), find and fix both within 30 minutes; and (4) demonstrate that your path tracer converges to a reference image, with a plot of error against samples.

## Industry reality

Graphics engineers work on game engines (Unreal, Unity, Godot and in-house engines), film and animation renderers, mapping and digital-twin products, AR/VR runtimes, CAD and design tools, browsers (WebGPU implementations) and GPU drivers. Neural rendering has moved from papers to products: Gaussian-splat support shipped in tools such as CesiumJS, Babylon.js and PlayCanvas ahead of final ratification of the Khronos extension (as reported by industry coverage of the release candidate, 2026). GPU skills transfer directly to ML systems work (see DLR404).

**Interview questions from this course**

1. *Walk me from a vertex in a mesh to a coloured pixel on screen.* Strong answer: vertex shader with MVP, clipping, perspective divide, viewport transform, rasterization with coverage and barycentrics, perspective-correct interpolation, fragment shading, depth test, blending, and where the GPU parallelises each stage.
2. *Why do normals use the inverse transpose of the model matrix?* Strong answer: normals must stay perpendicular to tangents; derive from n·t = 0; equal to the model matrix only for rotations and uniform scale; renormalise after.
3. *How would you make ray tracing a 10-million-triangle scene fast?* Strong answer: BVH with SAH (binned), two-level structures for instancing, traversal order, memory layout, ray coherence, hardware RT where available; how to measure node visits.
4. *A level runs at 40 fps instead of 60. What do you do?* Strong answer: measure first (CPU vs GPU timers, RenderDoc/Nsight/PIX); check draw calls, overdraw, shader cost, bandwidth, shadow cascades; fix the biggest item; verify with the same capture.
5. *NeRF or Gaussian splatting for a property-tour product?* Strong answer: capture pipeline, training time, rendering speed (rasterized splats run in real time on the web), memory/streaming size, editing and relighting limits, evaluation on held-out views, format support (PLY, the glTF extension).

## Resources (free first)

- **Books:** Pharr, Jakob and Humphreys, [Physically Based Rendering, 4th ed.](https://pbr-book.org/) (free online); Shirley et al., [Ray Tracing in One Weekend series](https://raytracing.github.io/); [Scratchapixel](https://www.scratchapixel.com/); [LearnOpenGL](https://learnopengl.com/); [WebGPU Fundamentals](https://webgpufundamentals.org/); [GPU Gems 3](https://developer.nvidia.com/gpugems/gpugems3) (free online); [Ray Tracing Gems](https://www.realtimerendering.com/raytracinggems/) (free PDFs).
- **Courses:** [CMU 15-462/662 Computer Graphics](http://15462.courses.cs.cmu.edu/); [Berkeley CS184/284A](https://cs184.eecs.berkeley.edu/); [MIT 6.837 (OCW)](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/); Dmitry Sokolov's [tinyrenderer](https://github.com/ssloy/tinyrenderer).
- **Specifications and APIs:** [WebGPU](https://www.w3.org/TR/webgpu/) and [WGSL](https://www.w3.org/TR/WGSL/) (W3C); [Vulkan tutorial](https://vulkan-tutorial.com/); [glTF](https://github.com/KhronosGroup/glTF) and [sample assets](https://github.com/KhronosGroup/glTF-Sample-Assets).
- **Papers and notes:** [Veach's thesis (MIS)](https://graphics.stanford.edu/papers/veach_thesis/); [Disney BRDF notes (Burley, 2012)](https://media.disneyanimation.com/uploads/production/publication_asset/48/asset/s2012_pbs_disney_brdf_notes_v3.pdf); [ReSTIR (2020)](https://research.nvidia.com/publication/2020-07_spatiotemporal-reservoir-resampling-real-time-ray-tracing-dynamic-direct); [NeRF](https://www.matthewtancik.com/nerf); [Instant-NGP](https://arxiv.org/abs/2201.05989); [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/).
- **Tools:** [RenderDoc](https://renderdoc.org/), [Mitsuba 3](https://www.mitsuba-renderer.org/), [Open Image Denoise](https://www.openimagedenoise.org/), [COLMAP](https://colmap.github.io/), [nerfstudio](https://docs.nerf.studio/), [gsplat](https://docs.gsplat.studio/), [3DGS reference code](https://github.com/graphdeco-inria/gaussian-splatting), [Blender](https://www.blender.org/), [McGuire Computer Graphics Archive (test scenes)](https://casual-effects.com/data/).
- **Paid, worth it:** Akenine-Möller et al., *Real-Time Rendering*, 4th ed. ([companion site](https://www.realtimerendering.com/)); Marschner and Shirley, *Fundamentals of Computer Graphics*.

## Sources

All checked 12 Oct 2026.

- web.dev, "WebGPU is now supported in major browsers" (25 Nov 2025) — https://web.dev/blog/webgpu-supported-major-browsers
- Kerbl, Kopanas, Leimkühler, Drettakis, "3D Gaussian Splatting for Real-Time Radiance Field Rendering" (SIGGRAPH 2023) — https://arxiv.org/abs/2308.04079
- Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis" (ECCV 2020) — https://arxiv.org/abs/2003.08934 ; Müller et al., "Instant Neural Graphics Primitives" (SIGGRAPH 2022) — https://arxiv.org/abs/2201.05989
- Khronos Group, "Khronos announces glTF Gaussian Splatting extension" (release candidate, 3 Feb 2026) — https://www.khronos.org/news/permalink/khronos-announces-gltf-gaussian-splatting-extension ; implementation status as reported by RadianceFields.com (2026) — https://radiancefields.com/platforms/the-khronos-group
- Epic Games, Nanite and Lumen documentation — https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine ; https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine
- Pharr, Jakob, Humphreys, *Physically Based Rendering*, 4th ed. (free online) — https://pbr-book.org/

_Last reviewed: 2026-10_
