# DLR402 · Multimodal Models

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [DLR302](../../year_3/DLR302_computer_vision_from_cnns_to_vision_transformers/README.md); in practice also [DLR303](../../year_3/DLR303_sequence_models_and_transformers/README.md) and [DLR305](../../year_3/DLR305_generative_models_vaes_gans_and_diffusion/README.md) | [DLR501](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md); taken alongside [DLR401](../DLR401_large_language_models_pretraining_fine_tuning/README.md) |

## Why this course matters now

Frontier models now take in text, images, audio and video together, and many also produce speech or images. Each step there has a public paper. CLIP aligned images and text through contrastive learning (2021). LLaVA showed that a projector and visual instruction tuning turn a language model into a vision–language model (VLM) (2023). Whisper reached robust speech recognition by training on 680,000 hours of weakly supervised audio (2022). Moshi casts spoken dialogue as full-duplex speech-to-speech generation (2024). Qwen2.5-Omni's "Thinker–Talker" design produces text and streaming speech from a single end-to-end model (2025). Open data now matters as much as open weights. Molmo's PixMo datasets were "collected without the use of external VLMs" (Deitke et al., 2024). India's linguistic diversity makes this practical, not academic. IndicVoices gathered 7,348 hours of speech from 16,237 speakers in 145 districts and 22 languages (Javed et al., 2024). Vistaar collects 59 benchmarks for Indian-language speech recognition (Bhogale et al., 2023). AI tools now caption, transcribe and answer questions about images out of the box. Multimodal engineers are hired for what those tools get wrong: hallucinated objects, weak low-resource speech, unreliable grounding, token budgets that explode with video, and evaluation that hides all of this.

## Learning outcomes

By the end you can:

1. **Represent** images, audio and video as tensors and tokens (patches, log-mel features, neural-codec tokens), and **calculate** each modality's token budget.
2. **Train and evaluate** contrastive image–text models, including multilingual retrieval for Indian languages.
3. **Build** a LLaVA-style VLM (vision encoder, projector, language model), train it in two stages, and **ablate** its design choices.
4. **Implement** grounding outputs (boxes and points as tokens) and **evaluate** them with IoU-based metrics.
5. **Fine-tune and evaluate** speech recognition for Indian languages and code-switched speech with WER/CER and speaker-disjoint splits.
6. **Explain** speech generation with neural codecs, full-duplex dialogue, video understanding, and unified any-to-any architectures, with their trade-offs.
7. **Measure** multimodal hallucination, bias and safety failures, and **design** evaluations that catch them.

## Chapters and lessons

### Chapter 1 · Modalities as tensors and tokens (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Images | Patches, resolution, aspect ratio, tiling; tokens per image | Count tokens for a 1344×896 image at patch sizes 14 and 16 |
| 1.2 Audio | Sampling rate, STFT, log-mel spectrograms, frame rates | Compute log-mel features; tokens per second at 3 frame rates |
| 1.3 Neural codecs | Residual vector quantisation; SoundStream (Zeghidour et al., 2021), EnCodec (Défossez et al., 2022) | Encode and decode speech with EnCodec at 3 bitrates; listen and measure |
| 1.4 Video | Frames, fps, spatio-temporal patches; why video breaks token budgets | Token budget for 1 minute of video under 3 sampling schemes |

**Check your understanding:** Why does doubling image resolution roughly quadruple a VLM's cost? Why do audio language models use codec tokens rather than raw samples? What sampling rate of frames is enough to recognise "pouring water" vs "drinking water"?

### Chapter 2 · Contrastive alignment (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 CLIP and ALIGN recap | InfoNCE over image–text pairs; noisy web data at scale (Jia et al., 2021) | Implement the symmetric contrastive loss; check with a toy batch |
| 2.2 SigLIP and SigLIP 2 | Pairwise sigmoid loss; multilingual training and better localisation (Tschannen et al., 2025) | Fine-tune a small SigLIP on 20k captioned images |
| 2.3 Retrieval evaluation | Recall@K in both directions; hubness; bootstrap intervals | Image–text retrieval in English, Hindi and Tamil |
| 2.4 Audio–text alignment | Contrastive audio–text models; zero-shot audio classification | Zero-shot classification of environmental sounds |

**Check your understanding:** Why does batch size matter so much for softmax contrastive losses and less for sigmoid losses? Why can retrieval in Hindi be poor even with a multilingual text encoder? What does a retrieval gap between languages tell you about the training data?

### Chapter 3 · Vision–language model architectures (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Cross-attention designs | Flamingo's perceiver resampler and gated cross-attention (Alayrac et al., 2022) | Diagram Flamingo's data flow; count added parameters |
| 3.2 Query transformers | BLIP-2's Q-Former bridging frozen encoders and frozen LLMs (Li et al., 2023) | Compare token counts entering the LLM for Q-Former vs projector |
| 3.3 Projector designs | LLaVA and LLaVA-1.5: MLP projector plus visual instruction tuning (Liu et al., 2023) | Build a LLaVA-style VLM: frozen SigLIP + MLP + 0.5–1.5B language model |
| 3.4 Resolution handling | Dynamic resolution and tiling (Qwen2.5-VL, 2025); what matters when building VLMs (Laurençon et al., 2024) | Ablate image resolution vs accuracy on a document task |

**Check your understanding:** Why do most open VLMs now use a simple projector rather than a Q-Former? What do you lose by freezing the vision encoder? Why does OCR quality depend more on resolution than on model size?

### Chapter 4 · Training VLMs (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Stage 1: alignment | Caption pretraining with only the projector trained | Train stage 1 on 100k captions |
| 4.2 Stage 2: instruction tuning | Mixed visual QA, OCR, charts and conversation data; interleaved image–text data (OBELICS) | Stage 2 with 3 data mixtures; compare |
| 4.3 Open data | PixMo's human-collected captions and pointing data; why distilling from closed VLMs is a dead end for openness (Deitke et al., 2024) | Audit the licences and origins of your training data |
| 4.4 Evaluation during training | Held-out VQA, captioning metrics and their limits | Track 3 metrics per checkpoint; find where they disagree |

**Check your understanding:** Why train only the projector first? How can an instruction-tuning mix make a VLM worse at OCR? What licence and terms-of-service questions arise from using another model's outputs as training data?

### Chapter 5 · Grounding (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Locations as tokens | Boxes as text or special tokens (Kosmos-2, Peng et al., 2023); points (Molmo) | Add box outputs to your VLM |
| 5.2 Open-vocabulary detection | OWL-ViT (Minderer et al., 2022), Grounding DINO (Liu et al., 2023), MDETR | Compare two detectors on 20 free-text queries |
| 5.3 Segmentation from language | SAM 3 concept prompts; combining a VLM with a segmenter | "Point to every leaf with a lesion" pipeline |
| 5.4 Metrics | IoU, referring-expression accuracy, pointing accuracy | Evaluate grounding on a RefCOCO subset |

**Check your understanding:** Why are coordinates as text tokens fragile, and how do models mitigate that? Why does a VLM that describes an object correctly often fail to localise it? How would you evaluate pointing when objects have no crisp boundary?

### Chapter 6 · Documents, charts and Indian scripts (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 OCR-free understanding | DocVQA (Mathew et al., 2020), ChartQA (Masry et al., 2022); layout vs text | Evaluate a VLM on 100 DocVQA questions |
| 6.2 Indic scripts | Conjuncts, matras, mixed-script documents; low-resource OCR | Build a 200-image test set of printed Hindi and Bengali pages |
| 6.3 Classic OCR vs VLMs | Tesseract and specialised OCR models vs general VLMs | Character error rate for 3 systems on your set |
| 6.4 Structured extraction | Forms and tables into JSON; confidence and abstention | Extract fields from 50 public-domain forms; measure field accuracy |

**Check your understanding:** Why does a VLM sometimes "read" text that is not in the image? Which errors matter most when extracting fields from official documents? How would you build a test set that represents real Indian documents without using private data?

### Chapter 7 · Speech recognition (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Objectives | CTC, attention encoder–decoder, transducers; Conformer encoders (Gulati et al., 2020) | Implement CTC greedy decoding |
| 7.2 Self-supervised speech | wav2vec 2.0 (Baevski et al., 2020), HuBERT (Hsu et al., 2021) | Probe wav2vec 2.0 layers for phone information |
| 7.3 Weak supervision at scale | Whisper's 680,000 hours; multitask tokens; failure modes (hallucinated text in silence) | Find Whisper hallucinations on 20 silent or noisy clips |
| 7.4 Indian-language ASR | IndicVoices, Vistaar benchmarks, IndicWhisper, IndicConformer; code-switching | Fine-tune Whisper-small on one Indian language; WER on speaker-disjoint test |
| 7.5 Metrics and splits | WER vs CER, normalisation rules, speaker and district leakage | Recompute WER under 3 normalisation rules; show the spread |

**Check your understanding:** Why is CER often more meaningful than WER for agglutinative languages? Why must test speakers be disjoint from training speakers? Why does Whisper sometimes produce fluent text for silence?

### Chapter 8 · Speech generation and spoken dialogue (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Text-to-speech | Text → acoustic tokens → codec decoder; AudioLM's semantic and acoustic tokens (Borsos et al., 2022) | Run an open TTS model; measure intelligibility with an ASR loop |
| 8.2 Full-duplex dialogue | Moshi's parallel streams for user and system speech (Défossez et al., 2024) | Measure response latency for a cascade (ASR → LLM → TTS) |
| 8.3 Omni models | Qwen2.5-Omni's Thinker–Talker; time-aligned multimodal RoPE | Diagram the streaming path; identify latency sources |
| 8.4 Voice risks | Voice cloning, consent, impersonation; watermarking audio | Write a consent and misuse policy for a voice feature |

**Check your understanding:** Where does latency come from in a cascaded voice assistant, and which parts can stream? What is lost when text is the only intermediate between listening and speaking? Why does voice cloning need consent controls by design?

### Chapter 9 · Video understanding (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Video encoders | ViViT factorised attention (Arnab et al., 2021); VideoMAE (Tong et al., 2022) | Fine-tune VideoMAE on a UCF101 subset |
| 9.2 Video in VLMs | Frame sampling, token merging, long-video memory | Accuracy vs frames sampled on 50 questions |
| 9.3 Temporal grounding | When did it happen? Timestamps as tokens | Evaluate temporal localisation on 30 clips |
| 9.4 Long and egocentric video | Hour-long inputs; frame retrieval and memory instead of encoding every frame | Answer 20 questions about a 30-minute video with a frame-retrieval pipeline |

**Check your understanding:** Why can a video QA model answer many questions from a single frame, and how do you build questions that need time? What is the cost trade-off between more frames and higher resolution? How would you evaluate a model's sense of "before" and "after"?

### Chapter 10 · Video and image generation in multimodal systems (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Video diffusion | Spatio-temporal latent patches; OpenAI's Sora technical report (2024) | Generate short clips with an open video model; measure temporal consistency |
| 10.2 Evaluation | FVD (Unterthiner et al., 2018), human preference, physics probes | Score 20 clips by FVD and by a 3-person rubric |
| 10.3 Provenance for video and audio | Watermarks, C2PA; India's labelling and metadata duties for synthetic audio-visual content | Attach credentials to generated clips |
| 10.4 Audio and music generation | Codec-token language models and diffusion for audio; consent and copyright for voices and music | Generate 10 clips with an open audio model; score prompt adherence with an audio–text contrastive model |

**Check your understanding:** Why is temporal consistency harder than per-frame quality? What does a low FVD fail to tell you? What must a product generating video in India now attach to its outputs?

### Chapter 11 · Unified any-to-any models (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Early fusion | Chameleon: one token stream for images and text (Chameleon Team, 2024) | Read the paper's stability fixes; list them |
| 11.2 Mixed objectives | Transfusion: next-token loss for text, diffusion loss for images in one model (Zhou et al., 2024) | Toy Transfusion on MNIST digits plus labels |
| 11.3 Everything as tokens | Emu3 (2024), AnyGPT (2024), Janus's decoupled encoders (2024) | Compare 3 designs in a one-page table |
| 11.4 Choosing an architecture | Late fusion vs early fusion vs mixed objectives, by task, data and compute | One-page decision memo for a speech-plus-vision assistant |

**Check your understanding:** Why might one model that both understands and generates images need different visual encoders for each task? What breaks in training when image tokens and text tokens have very different statistics? What is gained by early fusion over a bolted-on encoder?

### Chapter 12 · Evaluation, hallucination and safety (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Benchmarks | MMMU (Yue et al., 2023) and their limits; contamination in multimodal benchmarks | Evaluate your VLM on an MMMU subset with CIs |
| 12.2 Hallucination | Object hallucination and the POPE protocol (Li et al., 2023); grounded answers | Measure your VLM's hallucination rate; reduce it |
| 12.3 Bias and coverage | Geographic and linguistic gaps; Indian contexts underrepresented in web data | Build a 100-image India-specific probe set |
| 12.4 Privacy and misuse | Faces, voices, location inference; refusing identification of people | Test and document your model's behaviour on identification requests |

**Check your understanding:** Why can a VLM score well on a benchmark while hallucinating often in use? How do you measure whether a model's answer is grounded in the image? Which multimodal capabilities need deliberate refusals, and how do you test them?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Token budgets and codecs | Token-budget sheet |
| 2 | 2 | Lab 2 · Multilingual retrieval | Recall@K by language |
| 3 | 3 | Lab 3 · LLaVA-style VLM: alignment and instruction tuning | — |
| 4 | 4 | Lab 3 (cont.) | **P1 due** |
| 5 | 5 | Lab 4 · Grounding | Grounding metrics |
| 6 | 6 | Lab 5 · Indic documents | CER comparison |
| 7 | 7 | Lab 6 · ASR fine-tuning | — |
| 8 | 8 | Lab 7 · Voice pipeline latency | Mid-term (AI off) |
| 9 | 9 | Lab 8 · Video understanding and generation | — |
| 10 | 10 | Lab 8 (cont.) | **P2 due** |
| 11 | 11 | Lab 9 · Toy Transfusion | Design comparison table |
| 12 | 12 | Lab 10 · Hallucination audit | — |
| 13 | 12 | Project studio | Safety and privacy tests |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** pre-labelling images and transcripts (as noisy labels to be checked); generating synthetic instruction data from existing labels; writing data loaders for audio and video formats; summarising architecture papers after you read them.
- **Do without AI (drills):** token-budget arithmetic for every modality; contrastive and CTC losses on paper; WER/CER by hand on short examples; designing speaker-disjoint and time-disjoint splits; both exams.
- **Verify AI output by:** (1) checking every AI-generated label set against a human-labelled sample of at least 100 items and reporting agreement; (2) listening to and viewing raw samples, not only metrics; (3) running hallucination probes (POPE-style yes/no questions about absent objects) on any VLM you use for labelling; (4) checking that speech test sets are speaker-disjoint.
- **Where AI still fails here:** gather evidence in Lab 10. Record the object-hallucination rate of an off-the-shelf VLM on your India-specific probe set, the WER of a general ASR model on code-switched Hinglish versus monolingual Hindi, and silence hallucinations from Whisper (Lab 6). These numbers, measured on your own data, guide what you build.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can: (1) with AI off, compute token budgets for a multimodal input, write the contrastive and CTC losses, and explain the LLaVA training stages; (2) build and train a small VLM or speech model whose gain over a zero-shot baseline is shown on a properly disjoint test set with confidence intervals; (3) present a hallucination or bias audit of your model and defend its limits orally.

## Industry reality

Multimodal models are documented in open reports and repositories: Qwen2.5-VL and Qwen2.5-Omni (2025), Molmo and PixMo (2024), PaliGemma (2024), SigLIP 2 (2025). Indian-language speech is an active area. AI4Bharat publishes IndicVoices, Vistaar and IndicConformer models, and the government's Bhashini platform offers language services (https://bhashini.gov.in/). Interviews for multimodal roles test architecture trade-offs, data design and evaluation.

**Interview questions from this course**

1. *Design a VLM for reading Indian government forms.* Strong answer: resolution and tiling for small text; vision encoder choice; OCR-heavy instruction data in the target scripts; structured JSON output with field-level confidence; evaluation by field accuracy on a realistic, privacy-safe test set; abstention.
2. *Why does a VLM hallucinate objects, and how do you measure and reduce it?* Strong answer: language priors overpower weak visual evidence; POPE-style probes; grounding outputs; better negatives in instruction data; preference tuning against hallucinated answers; measuring with CIs.
3. *Our ASR is good on read Hindi but poor on customer calls. What do you do?* Strong answer: domain and channel shift (8 kHz telephony, noise, code-switching); collect and label in-domain data with consent; speaker-disjoint evaluation; fine-tune; text normalisation for WER; consider CER; language-model fusion for domain terms.
4. *Cascade or end-to-end speech-to-speech for a voice assistant?* Strong answer: latency budget per stage; streaming; what the cascade loses (prosody, interruptions); end-to-end data needs and control; safety and auditability with text intermediates.
5. *How many tokens does a 2-minute video cost your model, and how would you cut that?* Strong answer: frames × patches arithmetic; lower fps; token merging or pooling; keyframe selection; resolution trade-offs; measure accuracy against the budget.

## Resources (free first)

- **Courses:** Stanford CS231n (vision–language lectures, Spring 2026) — https://cs231n.stanford.edu/ ; MIT 6.S191 Introduction to Deep Learning (2026 edition) — https://introtodeeplearning.com/ ; Hugging Face courses — https://huggingface.co/learn
- **Code and models:** OpenAI Whisper — https://github.com/openai/whisper ; AI4Bharat — https://ai4bharat.iitm.ac.in/ ; IndicVoices data — https://huggingface.co/datasets/ai4bharat/IndicVoices ; SAM 3 — https://github.com/facebookresearch/sam3
- **Key papers:** CLIP https://arxiv.org/abs/2103.00020 ; SigLIP 2 https://arxiv.org/abs/2502.14786 ; Flamingo https://arxiv.org/abs/2204.14198 ; BLIP-2 https://arxiv.org/abs/2301.12597 ; LLaVA https://arxiv.org/abs/2304.08485 ; LLaVA-1.5 https://arxiv.org/abs/2310.03744 ; Idefics2 ("What matters") https://arxiv.org/abs/2405.02246 ; Molmo/PixMo https://arxiv.org/abs/2409.17146 ; Qwen2.5-VL https://arxiv.org/abs/2502.13923 ; Kosmos-2 https://arxiv.org/abs/2306.14824 ; Grounding DINO https://arxiv.org/abs/2303.05499 ; Whisper https://arxiv.org/abs/2212.04356 ; wav2vec 2.0 https://arxiv.org/abs/2006.11477 ; EnCodec https://arxiv.org/abs/2210.13438 ; Moshi https://arxiv.org/abs/2410.00037 ; Qwen2.5-Omni https://arxiv.org/abs/2503.20215 ; Chameleon https://arxiv.org/abs/2405.09818 ; Transfusion https://arxiv.org/abs/2408.11039 ; VideoMAE https://arxiv.org/abs/2203.12602 ; POPE https://arxiv.org/abs/2305.10355 ; MMMU https://arxiv.org/abs/2311.16502
- **Indian-language resources:** IndicVoices https://arxiv.org/abs/2403.01926 ; Vistaar https://arxiv.org/abs/2305.15386 ; Bhashini — https://bhashini.gov.in/
- **Compute (free):** a LLaVA-style VLM with a frozen encoder and a 0.5–1.5B language model trains on Kaggle's 2× T4 within the weekly quota if you cache image features; Whisper-small fine-tuning fits a T4 in fp16. Video work should use short clips and low frame rates.

## Sources

- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper, 2022) — https://arxiv.org/abs/2212.04356 (checked 2026-10)
- Liu et al., "Visual Instruction Tuning" (2023) — https://arxiv.org/abs/2304.08485 (checked 2026-10)
- Défossez et al., "Moshi: a speech-text foundation model for real-time dialogue" (2024) — https://arxiv.org/abs/2410.00037 (checked 2026-10)
- Xu et al., "Qwen2.5-Omni Technical Report" (2025) — https://arxiv.org/abs/2503.20215 (checked 2026-10)
- Deitke et al., "Molmo and PixMo" (2024) — https://arxiv.org/abs/2409.17146 (checked 2026-10)
- Javed et al., "IndicVoices" (2024) — https://arxiv.org/abs/2403.01926 ; Bhogale et al., "Vistaar" (2023) — https://arxiv.org/abs/2305.15386 (checked 2026-10)
- OpenAI, "Video generation models as world simulators" (Feb 2024) — https://openai.com/index/video-generation-models-as-world-simulators/ (checked 2026-10)
- Hogan Lovells summary of India's IT Rules amendment on synthetically generated information (Feb 2026) — https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content (checked 2026-10)

_Last reviewed: 2026-10_
