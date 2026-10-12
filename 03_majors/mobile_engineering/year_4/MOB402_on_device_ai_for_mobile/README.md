# MOB402 · On-Device AI for Mobile

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [MOB302](../../year_3/MOB302_ios_with_swift_and_swiftui/README.md) | [OV09](../../../../04_overlaps/OV09_edge_ai_secure_iot/README.md), [MOB501](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Mobile Engineering major](../../README.md). The catalog lists MOB302; the course covers Android and iOS equally, so [MOB301](../../year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md) is strongly recommended as well. [CS214 Machine Learning Foundations](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) supplies the ML background. Students who want more depth on compression can add [MLE404 Efficient Inference](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md).

## Why this course matters now

Both mobile platforms now ship a language model inside the operating system. Android runs Gemini Nano in the AICore system service; apps reach it through the ML Kit GenAI APIs (summarization, proofreading, rewriting and image description in beta, a Prompt API in beta, speech recognition in alpha), only while in the foreground and within per-app quotas. Apple's Foundation Models framework exposes its roughly 3-billion-parameter on-device model, compressed with 2-bit quantization-aware training, with guided generation and tool calling. iOS 27 adds image input, free Private Cloud Compute access for small developers, a protocol that lets the same code call Claude or Gemini in the cloud, and Core AI, a framework for running your own models on device. Google's LiteRT (formerly TensorFlow Lite) runs custom models on CPU, GPU and NPU, and LiteRT-LM runs open models such as Gemma. On-device AI promises privacy, offline use, low latency and no per-request cost. It is limited by memory, battery, heat, device support and model quality, especially for Indian languages. AI coding tools can wire up any of these APIs in minutes. Deciding what runs where, measuring quality, latency and energy honestly, and telling users the truth about their data remain engineering work.

## Learning outcomes

By the end you can:

1. **Decide** between on-device, hybrid and cloud inference for a feature, using latency, privacy, cost, device coverage and quality evidence.
2. **Explain** model formats, runtimes and accelerators (CPU, GPU, NPU, Apple Neural Engine) and why LLM decoding on phones is limited by memory bandwidth.
3. **Quantize and compress** models (int8, int4 weight-only, palettization, distillation) and **measure** the accuracy cost.
4. **Build** vision and text features with ML Kit, Vision and custom LiteRT or Core ML models in real camera pipelines.
5. **Integrate** Gemini Nano and Apple Foundation Models with availability checks, structured output, tools and cloud fallback.
6. **Run** open models on device with LiteRT-LM, llama.cpp, MLX or ExecuTorch, and **deliver** models without bloating the app.
7. **Evaluate** AI features with test sets, latency and energy measurements, thermal soak tests and device matrices.
8. **Design** AI features that are safe, honest about data use and compliant with store rules and India's DPDP Rules.

## Chapters and lessons

### Chapter 1 · Why and when on-device (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The trade-off space | Latency, privacy, offline, cost per request vs model size, quality, device coverage, update speed | Place 10 features on an on-device/hybrid/cloud map |
| 1.2 Device realities | RAM tiers, storage, thermal throttling, battery; what fails on a 3 GB phone | Profile available memory on three devices |
| 1.3 Hybrid patterns | On-device first with cloud fallback; cloud first with on-device privacy filter; Firebase AI Logic hybrid routing; Apple's on-device and Private Cloud Compute tiers | Design fallback logic for an unsupported device |
| 1.4 Cost model | Cloud token cost vs zero marginal cost on device; download cost of models; engineering cost | Estimate monthly cloud cost of a feature for 1 million users |

**Check your understanding:** When is on-device inference more expensive than the cloud? Which users does an on-device-only feature exclude? What privacy claim can you make for a hybrid feature?

### Chapter 2 · Formats, runtimes and accelerators (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Graphs and formats | LiteRT `.tflite`, Core ML `.mlpackage`, ONNX, ExecuTorch `.pte`; operator support gaps | Convert one PyTorch model to two formats; list failed ops |
| 2.2 Runtimes | LiteRT CompiledModel vs Interpreter APIs; Core ML compute units; ONNX Runtime Mobile | Run the same model through two runtimes |
| 2.3 Accelerators | GPU delegates, NPUs (Google Tensor, Qualcomm, MediaTek, Samsung), Apple Neural Engine; fallbacks to CPU | Measure latency per accelerator on two devices |
| 2.4 Why decoding is memory-bound | Prefill vs decode; bytes moved per token; tokens per second from bandwidth and model size | Predict tokens/s for a 1B and a 3B model; then measure |

**Check your understanding:** Why might a model run slower on a GPU than a CPU on a given phone? What does an unsupported operator do to latency? Why does halving weight precision roughly double decode speed?

### Chapter 3 · Quantization and compression (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Integer quantization | Scales and zero points, post-training int8, calibration data, per-channel vs per-tensor (Jacob et al., 2018) | Quantize a classifier; plot accuracy vs calibration size |
| 3.2 Low-bit weights for LLMs | Weight-only int4, GPTQ, AWQ; KV-cache size and quantization | Compare int8 and int4 variants of a small LLM on your eval set |
| 3.3 Quantization-aware training | Why QAT recovers accuracy; Apple's 2-bit QAT as a case | Fine-tune with fake-quant nodes; compare with post-training |
| 3.4 Palettization, pruning, distillation | Weight clustering in coremltools, sparsity, teacher–student training | Distil a large classifier into a model under 5 MB |
| 3.5 Measuring the cost | Accuracy by slice (language, lighting, device), not just overall | Find the slice where quantization hurts most |

**Check your understanding:** Why does calibration data matter, and what happens if it is unrepresentative? Why can overall accuracy hide a large drop for Hindi inputs? When is distillation worth more than quantization?

### Chapter 4 · Vision and text pipelines (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Camera pipelines | CameraX `ImageAnalysis` and AVFoundation; frame rates, backpressure, dropping frames, rotation | Run a model at a steady rate without stalling the preview |
| 4.2 Ready-made APIs | ML Kit (barcode, text recognition including Devanagari, face detection), Apple Vision | Scan Indian documents in Latin and Devanagari script |
| 4.3 Custom models | A custom LiteRT or Core ML image classifier end to end | Train, convert, quantize and ship a leaf-disease classifier |
| 4.4 Pre- and post-processing | Resizing, normalisation, colour spaces, non-maximum suppression; where bugs hide | Find a planted preprocessing bug from wrong outputs |
| 4.5 Audio and text | On-device speech recognition, keyword spotting, text classification | Offline voice command for three actions |

**Check your understanding:** Why does a model that scores 95% offline perform worse on camera frames? Where should frames be dropped, and why? How do you test OCR on scripts your team cannot read?

### Chapter 5 · Gemini Nano on Android (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 AICore and ML Kit GenAI | Summarization, proofreading, rewriting, image description, speech recognition; feature status | Summarise a chat thread on a supported device |
| 5.2 The Prompt API | Text and multimodal prompts, system instructions, structured output (alpha), sampling settings | Extract structured fields from a receipt photo |
| 5.3 Availability and download | Supported device lists, model download states, checking before showing UI | Build a feature flag driven by real availability |
| 5.4 Platform limits | Foreground-only inference, `BUSY` and per-app battery quotas, backoff | Handle every documented error code in tests |
| 5.5 Hybrid fallback | Firebase AI Logic routing to cloud Gemini when Nano is unavailable; App Check | Same feature on a supported and an unsupported phone |

**Check your understanding:** Why does Android block on-device GenAI inference from a background service? What should the UI do while the model downloads? What changes in your privacy notice when the cloud fallback runs?

### Chapter 6 · Apple Foundation Models and Core AI (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Sessions | `LanguageModelSession`, instructions vs prompts, streaming responses, availability checks | A streaming summariser with clear unavailable states |
| 6.2 Guided generation | `@Generable` and `@Guide` for typed output; why constrained decoding beats parsing text | Generate a typed itinerary with zero parse failures |
| 6.3 Tool calling | Defining tools, letting the model call app functions, guarding side effects | A tool that reads (never writes) calendar data |
| 6.4 iOS 27 additions | Image input and Vision tools, Private Cloud Compute access, the Language Model protocol for other providers, Dynamic Profiles, the Evaluations framework | Switch one feature between on-device and a cloud model by configuration |
| 6.5 Own models | Core AI for bringing your own models; Core ML and coremltools | Run your Chapter 4 classifier through Core ML and Core AI; compare |

**Check your understanding:** Why does typed guided generation reduce bugs? What must a tool never do without user confirmation? When would you use your own model instead of the system model?

### Chapter 7 · Open models and model delivery (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Open small models | Gemma family via LiteRT-LM; Llama-family and other GGUF models via llama.cpp; MLX on Apple silicon; ExecuTorch | Run one open model on Android and iOS |
| 7.2 Constrained decoding and tools | Grammar- or schema-constrained output, tool calling in LiteRT-LM | Force JSON output that always validates |
| 7.3 Licences | Model licences and acceptable-use terms; what you may ship | Write a licence check for your chosen model |
| 7.4 Delivery | Download after install, asset packs, background downloads, integrity checks, storage budgets | Deliver a 500 MB model without increasing install size |
| 7.5 Memory tricks | Memory-mapped weights, loading on demand, unloading under memory pressure; "LLM in a flash" | Survive a memory-warning test without being killed |

**Check your understanding:** Why should a large model never ship inside the app bundle? What breaks if a downloaded model is corrupted or swapped? Which licence terms matter for a commercial app?

### Chapter 8 · Product, safety and Indian languages (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Latency UX | Streaming, skeleton states, cancel, progress; time to first token budgets | Redesign a feature so it feels fast at 3 tokens/s |
| 8.2 Safety and misuse | Prompt injection through content (summarising untrusted messages), harmful output, over-trust | Red-team your own feature with 30 adversarial inputs (your app only) |
| 8.3 Indian languages | Hindi, Bengali, Tamil and code-mixed "Hinglish"; scripts and transliteration; checking whether a model supports a language at all | Build a 100-item eval set in two Indian languages |
| 8.4 Honesty and consent | Telling users where data goes; Apple 5.1.2 (disclose and get permission for third-party AI); DPDP notice and consent | Write the user-facing data notice for your P3 |

**Check your understanding:** How can a message the user receives attack a summariser? What evidence do you need before launching a feature in Tamil? What may you claim as "on-device" if a fallback exists?

### Chapter 9 · Evaluation and measurement (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Quality | Task-specific test sets, golden outputs, rubric grading, LLM-as-judge and its biases | Build and version a 200-item eval set |
| 9.2 Performance | Time to first token, tokens per second, peak memory, model load time | Benchmark harness on two devices |
| 9.3 Energy and heat | Energy per inference, thermal soak (10 minutes continuous), throttling curves | Plot tokens/s over a 10-minute soak |
| 9.4 Device matrix | Coverage by device tier; supported vs fallback populations; regression testing when OS models update | Detect a quality change after a model update |

**Check your understanding:** Why can an OS update change your feature's behaviour without a release? What does a thermal soak reveal that a single run hides? When is LLM-as-judge acceptable evidence?

### Chapter 10 · Private learning and personalisation (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Federated learning | Federated averaging (McMahan et al., 2017); Gboard as a published case | Simulate federated training on partitioned data |
| 10.2 Differential privacy | Noise, privacy budgets, what DP does and does not promise | Add DP noise; measure accuracy loss |
| 10.3 On-device adaptation | Adapters (LoRA) for system models, on-device fine-tuning limits, data minimisation | Design a personalisation feature that never uploads raw text |

**Check your understanding:** What does federated learning protect, and what can still leak? Why do privacy budgets add up? When is personalisation not worth its privacy cost?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Placement map and cost model | Decision memo |
| 2 | 2 | Lab 2 · Runtimes and accelerators | Latency table |
| 3 | 3 | Lab 3 · Quantization | — |
| 4 | 3 | Lab 3 (cont.) · Distillation | **P1 due** |
| 5 | 4 | Lab 4 · Camera pipeline | — |
| 6 | 4 | Lab 4 (cont.) · Custom model | — |
| 7 | 5 | Lab 5 · Gemini Nano | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Foundation Models | — |
| 9 | 7 | Lab 7 · Open model on both platforms | — |
| 10 | 7 | Lab 7 (cont.) · Model delivery | **P2 due** |
| 11 | 8 | Lab 8 · Safety and Indian-language eval | — |
| 12 | 9 | Lab 9 · Benchmark harness | — |
| 13 | 9 | Lab 9 (cont.) · Thermal soak | — |
| 14 | 10 | Lab 10 · Federated simulation | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** conversion scripts (PyTorch to LiteRT or Core ML), boilerplate for availability checks and fallbacks, test-set expansion (then review every item), plotting benchmark results, explaining quantization papers.
- **Do without AI (drills):** the bandwidth arithmetic for tokens per second; reading an operator-support report; designing the eval set's slices; the safety red-team plan; the mid-term and final.
- **Verify AI output by:** (1) measuring on real devices of at least two tiers; (2) running your versioned eval set before and after every change; (3) checking API status (alpha, beta, stable) and device support on the official pages, which change monthly; (4) watching network traffic during "on-device" runs to prove nothing leaves the phone.
- **Where AI still fails here (collect your own evidence):** generated code often skips availability checks, runs GenAI inference from background work that Android blocks, parses free text where guided generation exists, quotes outdated API names, or claims "on-device" while calling a cloud endpoint. Log every case with the test or capture that exposed it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| Eval set and red-team report | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a device's memory bandwidth and a model's size and precision, estimate its decode speed within a factor of two and explain the gap after measuring; (2) design, on paper, a hybrid AI feature for 50 million Indian Android users, naming device coverage, fallback, privacy notice, quotas and metrics; (3) defend your P3 with quality, latency, memory, energy and thermal numbers from at least two devices.

## Industry reality

Platform documentation is explicit about limits: ML Kit GenAI inference "is permitted only when the app is the top foreground application", and apps may receive `BUSY` or per-app battery-quota errors. The supported-device lists name recent Pixel and Galaxy flagships plus selected models from other makers; check them against your own user base before building a feature that runs only on Gemini Nano. Apple's 2025 technical report describes its ~3B on-device model's KV-cache sharing and 2-bit quantization-aware training. Apple's guideline 5.1.2 now requires apps to disclose sharing personal data with third-party AI and get explicit permission. Google's published Gboard work is a well-known production example of federated learning.

**Interview questions from this course**

1. *Ship "summarise this conversation" to 50 million Android users in India, where only some devices support Gemini Nano.* Strong answer: availability-driven rollout; cloud fallback with consent and cost model, or no feature on unsupported devices; quotas and foreground limits; Indian-language quality evaluation; metrics for adoption, latency and failure.
2. *Why is LLM decoding on a phone memory-bandwidth bound, and what does that mean for quantization?* Strong answer: each token reads all weights; tokens/s ≈ bandwidth ÷ bytes of weights; lower precision raises speed and cuts memory but can hurt quality; KV cache grows with context.
3. *After int4 quantization, accuracy on Hindi inputs drops by 4 points. What next?* Strong answer: confirms with slice analysis and enough samples; better calibration data with Hindi; mixed precision for sensitive layers; QAT or a different method; decides with a product threshold.
4. *How do you measure the energy and thermal impact of an on-device model?* Strong answer: energy per inference with platform tools; 10-minute soak with throttling curve; device-tier matrix; foreground vs background conditions; compares with cloud round-trip energy.
5. *What can you truthfully tell users about where their data goes?* Strong answer: distinguishes on-device, Private Cloud Compute-style server processing and third-party cloud models; describes fallbacks; follows store disclosure rules and DPDP consent; verifies claims with traffic captures.

## Resources (free first)

- **Android:** Gemini Nano — https://developer.android.com/ai/gemini-nano ; ML Kit GenAI APIs — https://developers.google.com/ml-kit/genai ; ML Kit — https://developers.google.com/ml-kit ; LiteRT — https://developers.google.com/edge/litert ; Firebase AI Logic — https://firebase.google.com/docs/ai-logic
- **Apple:** Foundation Models — https://developer.apple.com/documentation/foundationmodels ; Core ML — https://developer.apple.com/documentation/coreml ; coremltools — https://apple.github.io/coremltools/ ; What's new in iOS 27 (Core AI) — https://developer.apple.com/ios/whats-new/ ; Apple Foundation Models tech report 2025 — https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
- **Open runtimes:** llama.cpp — https://github.com/ggml-org/llama.cpp ; MLX — https://github.com/ml-explore/mlx ; ExecuTorch — https://pytorch.org/executorch/ ; ONNX Runtime Mobile — https://onnxruntime.ai/docs/tutorials/mobile/
- **Papers:** Jacob et al., "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference" (arXiv 1712.05877) ; Frantar et al., GPTQ (arXiv 2210.17323) ; Lin et al., AWQ (arXiv 2306.00978) ; Alizadeh et al., "LLM in a flash" (arXiv 2312.11514) ; Liu et al., MobileLLM (arXiv 2402.14905) ; McMahan et al., federated averaging (arXiv 1602.05629) ; Hard et al., federated learning for Gboard (arXiv 1811.03604)
- **Data:** PlantVillage (Hughes and Salathé, arXiv 1511.08060)
- **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing — https://efficientml.ai/

## Sources

- Android Developers, Gemini Nano (AICore, hybrid inference) — https://developer.android.com/ai/gemini-nano (checked 2026-10)
- Google, ML Kit GenAI APIs (status, devices, quotas, foreground-only inference) — https://developers.google.com/ml-kit/genai (checked 2026-10)
- Google AI Edge, LiteRT (CompiledModel, NPU vendors, LiteRT-LM, platform minimums) — https://developers.google.com/edge/litert (checked 2026-10)
- Apple Machine Learning Research, Apple Intelligence Foundation Language Models Tech Report 2025 (Jul 2025) — https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025 (checked 2026-10)
- Apple, What's new in iOS 27 — https://developer.apple.com/ios/whats-new/ (checked 2026-10)
- Apple, App Review Guidelines 5.1.2 — https://developer.apple.com/app-store/review/guidelines/ (checked 2026-10)
- Press Information Bureau, DPDP Rules 2025 — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf (checked 2026-10)

_Last reviewed: 2026-10_
