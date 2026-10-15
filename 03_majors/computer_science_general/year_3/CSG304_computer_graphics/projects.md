# CSG304 · Labs and projects

Write CPU code in C++ or Rust (Python with NumPy is allowed for Labs 1–2), GPU code in WebGPU/WGSL (preferred, runs in a browser) or Vulkan. Every image-quality claim is measured against a reference (Mitsuba 3, pbrt or a provided image) with a stated metric; every performance claim uses GPU timestamps or RenderDoc/Nsight captures on a stated GPU. Capture only objects and places you have permission to scan, and never people without their consent.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Software rasterizer (core AI off) | Edge functions, top-left rule, depth buffer, perspective-correct interpolation | Renders of 5 test scenes matching references (PSNR ≥ 40 dB); a test showing no gaps or double coverage on a shared edge | 6 h |
| 2 · Cameras and scene graphs | Orbit camera, transform hierarchy, quaternion slerp | Video or GIF of the animated hierarchy; unit tests for matrix and quaternion code | 4 h |
| 3 · WebGPU mesh viewer | Load glTF, MVP uniforms, depth, basic lighting in WGSL | Hosted page or build; frame time at 1080p for 3 sample assets | 5 h |
| 4 · Textures and mipmaps | Mipmap generation (compute shader), bilinear/trilinear/anisotropic sampling | Side-by-side shimmering comparison; cost of each filter in ms | 4 h |
| 5 · PBR shading and the AI shader audit | GGX + Schlick + Smith shading, image-based lighting; white-furnace test; audit two AI-written shaders | Sphere grid render; furnace test results; audit table of AI shader errors with screenshots | 6 h |
| 6 · Shadows and many lights | Cascaded shadow maps with PCF; clustered forward shading with 1,000 lights | Frame-time breakdown per pass; artefact gallery (acne, peter-panning) with fixes | 6 h |
| 7 · BVH (build AI off) | SAH BVH build and traversal; robust ray–triangle intersection | Speed-up over brute force on a 1M-triangle model; node visits per ray histogram | 5 h |
| 8 · Path tracer | NEE, BRDF sampling, MIS, Russian roulette | Cornell box and one glossy scene; error vs samples plot against a Mitsuba 3 reference | 7 h |
| 9 · Mesh processing | Half-edge structure, Loop subdivision, QEM simplification | Simplified meshes at 3 levels with Hausdorff error and frame time | 4 h |
| 10 · Gaussian splatting | COLMAP poses, gsplat training on your own capture, held-out evaluation | PSNR/SSIM/LPIPS on held-out views, training time, artefact gallery | 5 h |
| 11 · Profiling | Capture and optimise your P3 renderer's worst frame | Before/after captures, the change, and the measured gain | 3 h |

## Projects

### P1 · A software rasterizer that matches the GPU (L1, ~6 hours)

**Real-world inspiration:** software rasterizers are still used as reference implementations and fallbacks (for example in browser and driver test suites), and writing one is the fastest way to understand what the hardware does.

**What to build:** a CPU rasterizer that loads an OBJ model with a texture, applies model-view-projection, clips against the near plane, rasterizes with edge functions, interpolates perspective-correctly, depth-tests, samples the texture bilinearly, applies Lambert lighting in linear space, and writes an sRGB PNG.

**Acceptance criteria:**
- Five provided scenes match reference images with PSNR ≥ 40 dB.
- A watertight-mesh test: every pixel inside the silhouette is covered exactly once.
- A triangle crossing the near plane renders without artefacts.
- A 100,000-triangle model renders at 1920×1080 in under 1 second on a stated CPU (C++ or Rust), with a profile of where the time goes.

**Stretch goals:** 4× MSAA; multithreaded tiled rasterization; SIMD edge evaluation.

**What it proves to an employer:** you understand the pipeline below the API, which graphics, driver and engine teams test for.

### P2 · A physically based path tracer verified against a reference (L2, ~15 hours)

**Real-world inspiration:** film and product-visualization renderers are physically based path tracers; their teams spend much of their effort proving images are unbiased and converge.

**What to build:** a path tracer in C++ or Rust with a SAH BVH, Lambertian and GGX microfacet materials (conductor and dielectric), area lights, next-event estimation, BRDF sampling with multiple importance sampling, Russian roulette, an HDR output and optional Open Image Denoise.

**Acceptance criteria:**
- White-furnace test passes for every material (energy within 1% of expected, or the loss explained).
- On 3 scenes (Cornell box, a glossy scene, a scene with a small bright light), root-mean-square error against a 16,384-spp Mitsuba 3 reference falls as 1/√N within measurement noise, shown on a log–log plot.
- An unbiasedness check: the mean of 256 independent 4-spp renders matches the reference within the expected standard error.
- MIS lowers error at equal time against both BRDF-only and light-only sampling on the glossy scene.
- BVH speed-up of at least 50× over brute force on a 1M-triangle model.

**Stretch goals:** spectral rendering; a GPU (WebGPU compute) version; ReSTIR-style direct lighting for 1,000 lights.

**What it proves to an employer:** you can build a renderer whose correctness is measured, not assumed, which offline-rendering and simulation teams value most.

### P3 · A real-time web viewer for a captured scene (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** mapping, real-estate, heritage and e-commerce products increasingly show captured 3D scenes on the web; Gaussian splats are becoming a standard asset type (the Khronos glTF extension reached release-candidate stage in 2026). A heritage-site viewer is used here as an **illustrative scenario**; capture only places you are allowed to.

**What to build:** capture a scene (an object, a room or a permitted outdoor space), recover poses with COLMAP, train 3D Gaussian Splatting with gsplat, then write **your own** WebGPU renderer for the trained splats (projection of 3D Gaussians to 2D, GPU depth sort, tile-based or per-pixel alpha compositing, spherical-harmonic colour), combined with conventional PBR meshes (for example labels or furniture) in the same frame with correct depth.

**Acceptance criteria:**
- At least 60 fps at 1920×1080 on a stated laptop-class GPU for a scene of at least 1 million Gaussians, measured with GPU timestamps; a frame-time breakdown (sort, raster, composite).
- Image quality on held-out views within 0.5 dB PSNR of the training codebase's own rasterizer for the same model.
- Correct occlusion between splats and meshes, demonstrated on a test view.
- Loads PLY and at least one compressed or glTF-based splat format; progressive loading so the first frame appears in under 3 seconds on a 50 Mbit/s connection (measured with throttling).
- Runs in two different browsers; a README documents capture, training, conversion and deployment so a classmate can reproduce it.
- A written capture and consent policy.

**Stretch goals:** level of detail for splats; relighting experiments; a VR mode via WebXR; contribute a fix or example to an open-source splat viewer.

**What it proves to an employer:** you can take a research technique to a fast, shippable product on the modern web GPU stack, which graphics, mapping and AR/VR teams hire for.

## Feeds into

- [CSG404 Programming Language Theory and Type Systems](../../year_4/CSG404_programming_language_theory_and_type_systems/README.md): the catalog sequence; shading languages (WGSL, Slang) are a live application of type systems.
- [DLR404 Efficient Deep Learning and GPU Programming](../../../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) and [DLR402 Multimodal Models](../../../deep_learning/year_4/DLR402_multimodal_models/README.md): GPU skills and neural scene representations continue there.
- [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): differentiable rendering is a scientific-ML tool.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a natural thesis seed (compression, relighting, evaluation of neural rendering).
