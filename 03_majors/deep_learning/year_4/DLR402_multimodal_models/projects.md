# DLR402 · Labs and projects

Every lab and project ships with data cards (source, licence, consent where people's voices or faces are involved), disjoint splits (by speaker, document or location as appropriate), metrics with confidence intervals, and a gallery of failure cases. Never collect or use personal audio or images without informed consent.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Token budgets and codecs | Patch, mel-frame and codec-token counts for image, audio and video; EnCodec at 3 bitrates | Token-budget sheet; listening notes and an ASR-based intelligibility score per bitrate | 3 h |
| 2 · Multilingual retrieval | Image–text retrieval with SigLIP 2 in English, Hindi and Tamil (translated captions, with translation quality spot-checked) | Recall@1/5/10 both directions with bootstrap CIs; error taxonomy | 4 h |
| 3 · LLaVA-style VLM: alignment and instruction tuning | Frozen SigLIP + MLP projector + small LM; stage 1 caption alignment, then stage 2 instruction tuning with 3 mixtures (general, OCR-heavy, balanced) and a frozen vs unfrozen encoder | Training curves; captions on 30 held-out images; VQA and OCR accuracy per mixture; recommendation | 10 h |
| 4 · Grounding | Box tokens in your VLM; compare with Grounding DINO and OWL-ViT | IoU-based accuracy on a RefCOCO subset; 20 failure images | 4 h |
| 5 · Indic documents | 200-page printed Hindi/Bengali test set from public-domain sources; Tesseract vs a specialised OCR model vs a VLM | CER per system; error categories (conjuncts, matras, numerals) | 4 h |
| 6 · ASR fine-tuning | Whisper-small fine-tune on one Indian language from IndicVoices; silence-hallucination test | WER and CER (speaker-disjoint) before/after; hallucination rate on 50 silent/noisy clips | 6 h |
| 7 · Voice pipeline latency | Cascade ASR → LLM → TTS with streaming where possible | Latency breakdown (p50/p95) per stage; one optimisation and its effect | 3 h |
| 8 · Video understanding and generation | VideoMAE fine-tune on a UCF101 subset with accuracy vs frames sampled; short clips from an open video model with FVD and C2PA credentials | Accuracy–cost curve; 10 questions a single frame cannot answer; temporal-consistency notes; verified manifests | 7 h |
| 9 · Toy Transfusion | One transformer with next-token loss on labels and diffusion loss on MNIST images | Samples conditioned on labels; classification accuracy of the same model | 5 h |
| 10 · Hallucination audit | POPE-style probes on your VLM and one public VLM; 100-image India-specific probe set | Hallucination rates with CIs; categories of failure | 3 h |

## Projects

### P1 · Multilingual image–text retrieval audit (L1, ~6 hours)

**Real-world inspiration.** Product search, digital archives and accessibility tools need image search in the user's language. SigLIP 2 added multilingual training (Tschannen et al., 2025), but quality across Indian languages is rarely measured in public.

**What to build.** An evaluation of two open multilingual image–text encoders on 1,000 image–caption pairs with captions in English and at least two Indian languages (human-written where possible; machine-translated captions must be spot-checked by a fluent reader on 100 items).

**Acceptance criteria**
- Recall@1/5/10 in both directions per language and model, with bootstrap 95% CIs.
- The language gap (English minus each Indian language) is reported with its interval, and the 20 largest failures are shown and categorised.
- Translation quality on the 100 checked items is reported, and results are recomputed excluding bad translations.
- One improvement (prompt templates, transliteration, or a light fine-tune on 5,000 pairs) is tested with 3 seeds.

**Compute budget.** ≤ 3 GPU-hours (embeddings plus an optional light fine-tune).

**Stretch goals.** Add romanised Hindi queries; test text-to-image retrieval for culturally specific concepts (festivals, foods, clothing).

**What it proves to an employer.** You can measure multilingual multimodal quality honestly before anyone builds on it.

### P2 · Speech recognition for code-switched Indian speech (L2, ~15 hours)

**Real-world inspiration.** Indian speakers mix languages within sentences, and customer-service and voice-assistant products must handle this. IndicVoices records natural speech from 16,237 speakers in 145 districts (Javed et al., 2024), and Vistaar showed that fine-tuned IndicWhisper models had the lowest WER on 39 of 59 benchmarks (Bhogale et al., 2023).

**What to build.** Fine-tune Whisper-small (or an IndicConformer model) for one Indian language with a code-switched test subset you assemble (from consented or openly licensed recordings). Compare with the zero-shot model and with a published Indian-language checkpoint.

**Acceptance criteria**
- Speaker-disjoint train/validation/test splits; no speaker appears in two splits (verified by script).
- WER and CER with documented normalisation rules for all three systems, with bootstrap CIs; the fine-tuned model improves on zero-shot by a margin outside the interval.
- Separate results for monolingual and code-switched utterances, with 20 annotated errors from each.
- Real-time factor on a T4 and on CPU.
- A data card covering consent, licence, speaker demographics (where available) and known coverage gaps.
- Compute ≤ 12 GPU-hours.

**Stretch goals.** Language-model fusion or contextual biasing for domain terms (crop names, place names); a telephony-quality (8 kHz) robustness test.

**What it proves to an employer.** You can adapt speech models to real Indian conditions and evaluate them without leakage.

### P3 · A grounded bilingual crop-health assistant (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Field photos of diseased crops are hard for vision models (Mohanty et al., 2016: 99.35% on lab images, 31.4% on field-style images), and farmers need answers in their own language with an indication of where the problem is. The assistant here is illustrative and must not be used for real agronomic decisions without expert validation.

**What to build.** A small LLaVA-style VLM (frozen or partially tuned vision encoder, a 0.5–2B language model) that, given a leaf photo and a question in Hindi or English, names the likely condition, points to or boxes the affected region, says how confident it is, and refuses or abstains for non-plant images and unclear photos. Build instruction data from PlantVillage and PlantDoc labels with templated and model-paraphrased Q&A, checked by a human on a sample.

**Acceptance criteria**
- A field-image test set (PlantDoc test split plus at least 100 photos you or classmates collect with permission) is kept separate from all training data.
- Diagnosis accuracy on field images with bootstrap CIs, compared with (a) your DLR302 classifier and (b) a general-purpose open VLM prompted zero-shot.
- Grounding: pointing or box accuracy on 150 field images with hand-marked lesion regions.
- Hallucination: on 200 POPE-style probes ("Is there a pest on this leaf?") the false-yes rate is reported and is lower than the zero-shot VLM's.
- Abstention: on 100 non-plant or unusable images, the model abstains or refuses at least 90% of the time.
- Answers in Hindi are reviewed by a fluent reader on 50 items, with fluency and correctness scores reported.
- Compute ≤ 30 GPU-hours; image features are cached to save quota.

**Stretch goals.** Voice input through your P2 ASR model; a small on-device version quantised with the techniques from DLR404.

**What it proves to an employer.** You can build a multimodal system end to end: data, architecture, grounding, multilingual output and safety behaviour, all measured on realistic data.

## Feeds into

- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): interpretability of multimodal features and multimodal reasoning.
- [DLR404 Efficient Deep Learning and GPU Programming](../DLR404_efficient_deep_learning_and_gpu_programming/README.md): quantising and serving VLMs and speech models.
- [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): multimodal models for remote sensing, microscopy and scientific documents.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): Indian-language speech or document understanding as a thesis topic.
- [PRO301 Professional Practice](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md): consent and privacy for voice and image data.
