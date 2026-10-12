# MOB402 · Labs and projects

Every AI result in this course is reported with its device, OS version, model version, precision and runtime, and every quality number comes from a versioned evaluation set. "On-device" claims must be backed by a network capture showing no inference traffic. Supported devices for Gemini Nano and Apple Foundation Models are limited: the course lends supported devices, and every project must also run its fallback path on an unsupported one. Safety testing targets only your own apps. Labs 2 and 8 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Placement map and cost model | Classify 10 features as on-device, hybrid or cloud; estimate cloud cost for 1 million users | Decision memo with assumptions | 3 h |
| 2 · Runtimes and accelerators (no AI) | Convert one model to LiteRT and Core ML; run on CPU, GPU and NPU or Neural Engine; predict LLM decode speed from bandwidth | Latency table; your prediction vs measurement with an explanation of the gap | 6 h |
| 3 · Quantization and distillation | Post-training int8, int4 weight-only for a small LLM, and a distilled classifier under 5 MB | Accuracy-vs-size plot; slice where quantization hurts most | 7 h |
| 4 · Camera pipeline and custom model | CameraX or AVFoundation pipeline with backpressure; a planted preprocessing bug to find | Frame-rate and dropped-frame log; the bug and fix | 6 h |
| 5 · Gemini Nano | ML Kit GenAI summarization and the Prompt API; availability, download states, every error code; cloud fallback via Firebase AI Logic | Tests for each documented error; video on a supported and an unsupported phone | 6 h |
| 6 · Foundation Models | Streaming session, `@Generable` output, a read-only tool, availability handling; switch to a cloud model via the Language Model protocol | Zero parse failures over 100 runs; configuration-only provider switch | 6 h |
| 7 · Open model and delivery | An open model through LiteRT-LM, llama.cpp or MLX on both platforms; download after install with integrity check | Install size unchanged; corrupted-model test rejected; memory-warning survival | 7 h |
| 8 · Safety and Indian-language eval (no AI) | 30 adversarial inputs against your own feature; a 100-item eval set in two Indian languages | Red-team report; eval set with rubric and agreement check | 5 h |
| 9 · Benchmark harness and thermal soak | Time to first token, tokens/s, peak memory, energy, 10-minute soak on two devices | Harness code; throttling curves | 6 h |
| 10 · Federated simulation | Federated averaging over partitioned data with and without differential-privacy noise | Accuracy vs privacy-budget plot | 4 h |

## Projects

### P1 · Offline bilingual document scanner (L1, ~6 hours)

**Real-world inspiration:** shop bills, printed forms and medicine strips in India mix English and Devanagari text, and many users scan them where connectivity is poor. ML Kit's on-device text recognition supports Devanagari. Avoid government ID documents in your test data.

**What to build:** a scanner that captures a page, corrects perspective, recognises text (Latin and Devanagari) and barcodes on device, lets the user edit, and exports text. Images are deleted after export unless the user saves them.

**Acceptance criteria:**
- **Quality:** character error rate reported separately for 25 Latin and 25 Devanagari test images you captured, with the ground truth files included.
- **Speed:** recognition p50 under 300 ms per page on a mid-range phone (release build, 20 runs).
- **Offline proof:** works in airplane mode; a proxy capture of a full session shows no image or text leaving the device.
- **Privacy:** images are removed from app storage after export (automated check).

**Stretch goals:** Tamil or Bengali scripts where supported; table detection for bills; a Vision-framework version on iOS with a side-by-side error comparison.

**What it proves to an employer:** you can ship an on-device ML feature, measure its quality honestly by script and prove your privacy claim.

### P2 · Leaf-disease classifier, quantized for two platforms (L2, ~15 hours)

**Real-world inspiration:** agritech apps let farmers photograph a diseased leaf and get a likely diagnosis offline in the field. The public PlantVillage dataset (Hughes and Salathé, 2015) is the usual starting point; it was photographed in controlled conditions, so field accuracy is lower. Your app is an illustrative scenario and must not present results as expert advice.

**What to build:** fine-tune a small image model on PlantVillage; convert to LiteRT and Core ML; quantize to int8 (and palettize on iOS); a live camera classifier on both platforms with a confidence threshold and an "unsure" answer.

**Acceptance criteria:**
- **Compression:** at least 3.5× smaller than the fp32 model with no more than 1.5 percentage points lower top-1 accuracy on the held-out PlantVillage test split.
- **Reality check:** accuracy on a separate set of at least 50 field-style photos (captured by you or properly licensed) is reported next to the lab number, with an analysis of the gap.
- **Calibration:** below the confidence threshold the app answers "unsure"; report how often it is wrong when confident.
- **Performance:** latency per accelerator (CPU, GPU, NPU or Neural Engine) on two devices; camera preview keeps its frame rate while classifying.
- **Energy:** energy per inference and over a 10-minute session.

**Stretch goals:** distillation from a larger teacher; Hindi and Marathi result screens with a voice readout; on-device fine-tuning of the final layer with user-confirmed labels (never uploaded).

**What it proves to an employer:** you can take a model from training to two mobile runtimes, compress it with measured costs, and tell the truth about field performance.

### P3 · Private bilingual message assistant (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** both platforms now offer system language models for summarising and rewriting text on device. Long group chats and notes in English, Hindi and code-mixed Hinglish are an everyday use case in India. Your app is an illustrative scenario that works on text the user pastes or shares into it, never on other apps' data.

**What to build:**
- **Features:** summarise a long thread into key points and action items (typed, structured output), and suggest three replies in the thread's language and tone.
- **Android:** Gemini Nano through ML Kit GenAI (Summarization and Prompt APIs), with every documented error and quota handled.
- **iOS:** Foundation Models with `@Generable` output and a read-only tool (for example, looking up dates mentioned in the thread).
- **Fallback:** a cloud path (Firebase AI Logic or the Language Model protocol) used only after explicit, revocable consent, with a different on-screen label.
- **Safety:** defences against instructions embedded in the pasted text; output length and content limits.
- **Evaluation:** a versioned 200-item eval set (100 English or Hinglish, 100 Hindi) with a scoring rubric.

**Acceptance criteria:**
- **Structure:** at least 99% of outputs across the eval set parse into the expected typed structure.
- **Quality:** rubric scores per language; two raters score 50 items independently and their agreement is reported.
- **Speed:** time to first token p50 under 1 second and tokens/s reported on each supported device; a 10-minute thermal soak curve.
- **Fallback:** the full feature works, or clearly declines, on an unsupported device; this path is tested automatically.
- **Privacy proof:** in on-device mode, a proxy capture shows no thread content leaving the phone; in cloud mode, the consent screen appears first and can be revoked.
- **Safety:** results of 30 prompt-injection cases hidden in pasted threads, each with the observed behaviour and the defence that applied.
- **Platform rules:** inference never runs in the background on Android; a written check against Apple guideline 5.1.2 and a DPDP-style notice.

**Stretch goals:** Tamil or Bengali eval sets; a LoRA adapter on iOS for reply tone; comparing an open model (LiteRT-LM) on the same eval set.

**What it proves to an employer:** you can build an on-device generative AI feature that is measured, safe, honest about data and works for users whose phones cannot run it. That combination is what AI product teams struggle to hire for.

## Feeds into

- [OV09 Edge AI and Secure IoT](../../../../04_overlaps/OV09_edge_ai_secure_iot/README.md): the same compression and measurement methods on embedded devices.
- [MOB501 Frontier Seminar](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md): multimodal assistants on glasses and watches.
- [MOB404 Mobile Analytics, Experimentation and Growth Engineering](../MOB404_mobile_analytics_experimentation_and_growth/README.md): experiments on AI features with quality guardrails.
- A [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) thesis on on-device model evaluation, and the [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
