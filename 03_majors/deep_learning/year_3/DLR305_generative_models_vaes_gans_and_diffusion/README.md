# DLR305 · Generative Models: VAEs, GANs and Diffusion

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS206](../../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md); in practice [DLR301](../DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR302](../DLR302_computer_vision_from_cnns_to_vision_transformers/README.md) | [DLR402](../../year_4/DLR402_multimodal_models/README.md), [DLR501](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md); taken alongside [DLR304](../DLR304_training_deep_networks_optimization/README.md) |

## Why this course matters now

Generative models now make images, video, speech, music, molecules and weather forecasts. One family of ideas sits underneath most of them: latent variables (VAEs), learned discrete tokens (VQ-VAE), adversarial training (GANs), and diffusion and flow matching. Stable Diffusion 3 trains rectified-flow transformers (Esser et al., 2024), and diffusion-style objectives now appear in language modelling too (LLaDA, 2025). Building a working pipeline is easy: Hugging Face `diffusers` fine-tunes a text-to-image model with LoRA in an afternoon, and coding assistants write the sampling loop. The hard problems are harder to see. Is the model better, or does FID just reward a quirk? FID can contradict human raters and change with sample size (Jayasumana et al., 2024). Is it memorising its training data? Diffusion models have been shown to emit training images, and researchers extracted over a thousand of them from state-of-the-art models (Carlini et al., 2023). Can its outputs be identified? The law now asks. The EU AI Act's Article 50 requires machine-readable marking of synthetic content from 2 August 2026, and India's amended IT Rules, in force since 20 February 2026, require labels and embedded provenance metadata for synthetically generated content. This course covers the mathematics, the training, the evaluation and the responsibility.

## Learning outcomes

By the end you can:

1. **Derive** the evidence lower bound, the reparameterisation trick, the GAN minimax objective, the change-of-variables formula, and the DDPM and flow-matching training objectives.
2. **Implement** a VAE, a VQ-VAE, a DCGAN with a gradient penalty, a RealNVP flow, a DDPM and a flow-matching model, from scratch in PyTorch.
3. **Explain** how score matching, SDEs, DDIM and flow matching relate, and **trade off** sampling steps against quality.
4. **Apply** conditioning and classifier-free guidance, and **measure** the fidelity–diversity trade-off.
5. **Fine-tune** an open latent diffusion model with LoRA on a licensed dataset, with a dataset card.
6. **Evaluate** generative models with likelihood, FID, precision/recall, CMMD, CLIPScore and human studies, and **state** each metric's failure modes.
7. **Audit** a model for memorisation, and **apply** watermarking and C2PA content credentials, testing their robustness.
8. **Explain** the legal duties for synthetic media in the EU and India and what they require of an engineer.

## Chapters and lessons

### Chapter 1 · What generative modelling is (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Density estimation vs sampling | Explicit likelihood, implicit samplers; the families at a glance | Fit a Gaussian mixture with EM; sample from it |
| 1.2 Maximum likelihood as KL | min KL(p_data ‖ p_θ) = max likelihood; mode-covering vs mode-seeking divergences | Fit a single Gaussian to a bimodal target with both KL directions |
| 1.3 Autoregressive models as generators | Exact likelihood; slow sequential sampling; link to [DLR303](../DLR303_sequence_models_and_transformers/README.md) | Pixel-level autoregressive model on binarised MNIST |
| 1.4 What "good" means | Fidelity, diversity, novelty, controllability, speed | Rank 4 sample grids by each criterion; compare with classmates |

**Check your understanding:** Why does forward KL produce blurry, mode-covering fits and reverse KL mode-seeking ones? Why is an autoregressive image model slow to sample? Why can a model have high likelihood and poor samples?

### Chapter 2 · Autoencoders and VAEs (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Autoencoders | Bottlenecks, denoising autoencoders, why a plain autoencoder is not a generator | Sample from a plain AE's latent space; see why it fails |
| 2.2 The ELBO | Derivation via Jensen's inequality; reconstruction plus KL (Kingma and Welling, 2013) | Derive the ELBO and its Gaussian closed-form KL |
| 2.3 Reparameterisation | z = μ + σ·ε; low-variance gradients through sampling | Compare with a score-function estimator's variance |
| 2.4 Failure modes | Blurry samples, posterior collapse, KL annealing, β-VAE | Train β-VAEs at β = 0.5, 1, 4; plot rate vs distortion |

**Check your understanding:** Why are VAE samples often blurry? What does posterior collapse look like in the KL term, and how do you detect it during training? What does β trade off?

### Chapter 3 · Discrete latents and learned tokenizers (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 VQ-VAE | Codebooks, nearest-neighbour quantisation, straight-through gradients, commitment loss (van den Oord et al., 2017) | VQ-VAE on CIFAR-10 |
| 3.2 Codebook health | Dead codes, utilisation, perplexity; reset and EMA updates | Plot codebook usage before and after fixes |
| 3.3 Why tokens matter | Latent spaces for diffusion; image and audio tokens for transformers ([DLR402](../../year_4/DLR402_multimodal_models/README.md)) | Train a small transformer prior over your VQ codes |
| 3.4 Codebook-free quantisation | Finite scalar quantisation: fixed per-dimension grids instead of a learned codebook (Mentzer et al., 2023) | Swap VQ for FSQ in your model; compare code utilisation and reconstruction |

**Check your understanding:** How does the straight-through estimator pass gradients through a non-differentiable lookup? Why do unused codes appear, and why do they hurt? Why does a good compression model make a generative model cheaper?

### Chapter 4 · Generative adversarial networks (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The game | Generator vs discriminator; minimax and non-saturating losses (Goodfellow et al., 2014) | 1-D GAN fitting a mixture; watch it oscillate |
| 4.2 DCGAN | Convolutional design rules (Radford et al., 2015) | DCGAN on Oxford Flowers-102 at 64×64 |
| 4.3 Stabilising GANs | Mode collapse; Wasserstein GAN; gradient penalty (Gulrajani et al., 2017) using `create_graph=True` | Add WGAN-GP; compare mode coverage on a 25-Gaussian grid |
| 4.4 Style-based generators | Mapping network, style modulation, progressive ideas (StyleGAN) | Read StyleGAN; reproduce its latent-interpolation figure at small scale |
| 4.5 GANs today | Adversarial losses inside autoencoders and codecs; adversarial distillation of diffusion samplers | Add a patch discriminator to your VQ-VAE |

**Check your understanding:** Why does the original minimax loss give weak gradients early in training? What does a gradient penalty enforce, and why does it need a second-order gradient? Why are GANs fast at sampling, and why did diffusion still replace them for most image generation?

### Chapter 5 · Normalising flows, briefly (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Change of variables | log p(x) = log p(z) + log \|det ∂z/∂x\| | Derive it for a 1-D affine map |
| 5.2 Coupling layers | RealNVP's cheap triangular Jacobians (Dinh et al., 2016); Glow's 1×1 convolutions | RealNVP on 2-D moons; exact likelihood |
| 5.3 Limits and legacy | Architectural constraints; flows as the bridge to continuous-time models | Compare bits per dimension of your flow and VAE on MNIST |
| 5.4 Continuous normalising flows | Neural ODEs and the instantaneous change of variables (Chen et al., 2018); why they were slow to train before flow matching | Train a tiny continuous flow on 2-D data; time it against RealNVP |

**Check your understanding:** Why must flow layers be invertible with a tractable determinant? Why are flows rarely used for large images today? What idea from flows survives in flow matching?

### Chapter 6 · Diffusion I: DDPM (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The forward process | Gaussian noising, closed-form q(xₜ \| x₀), signal-to-noise ratio | Visualise noising at 10 timesteps with linear and cosine schedules |
| 6.2 The training objective | Predicting noise ε; link to the ELBO and denoising score matching (Ho et al., 2020) | Derive the simplified loss |
| 6.3 The denoiser | U-Net with time embeddings and attention; ε, x₀ and v parameterisations | Implement a small U-Net |
| 6.4 Sampling | Ancestral sampling; variance choices; improved schedules (Nichol and Dhariwal, 2021) | DDPM on MNIST, then on CIFAR-10 at 32×32 |

**Check your understanding:** Why can training pick a random timestep per example instead of running the whole chain? What changes between predicting ε, x₀ and v? Why does the cosine schedule help at low resolution?

### Chapter 7 · Diffusion II: scores, ODEs and fast sampling (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Score matching | ∇ₓ log p(x); denoising score matching; Langevin dynamics | Sample a 2-D distribution with Langevin dynamics from a learned score |
| 7.2 The SDE view | Forward and reverse SDEs; the probability-flow ODE (Song et al., 2020) | Re-derive DDPM as a discretised SDE |
| 7.3 DDIM | Deterministic, non-Markovian sampling with fewer steps (Song, Meng and Ermon, 2020) | FID vs number of steps (10, 25, 50, 250) for DDPM and DDIM samplers |
| 7.4 Design space | EDM's choices for noise levels, preconditioning and solvers (Karras et al., 2022) | Swap in a second-order solver; compare at equal network evaluations |

**Check your understanding:** Why does the ODE view allow deterministic sampling and exact inversion? What is the cost of a sampling step, and how do solvers reduce the count? Why do fewer steps reduce diversity with some samplers?

### Chapter 8 · Flow matching and rectified flow (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Conditional flow matching | Regress a velocity field along simple probability paths (Lipman et al., 2022) | Flow matching on 2-D data in 50 lines |
| 8.2 Straight paths | Rectified flow and reflow (Liu et al., 2022); why straighter paths need fewer steps | Measure path curvature before and after one reflow |
| 8.3 Connections | Flow matching vs diffusion with v-prediction; same networks, different paths | Train both on CIFAR-10 with one shared U-Net |
| 8.4 At scale | Rectified-flow transformers in Stable Diffusion 3 (Esser et al., 2024); *Flow Matching Guide and Code* (Lipman et al., 2024) | Read the SD3 paper's timestep-sampling ablation |

**Check your understanding:** What exactly does a flow-matching network predict, and why is the loss simple regression? Why do straighter paths allow fewer integration steps? In what sense are diffusion and flow matching "the same model"?

### Chapter 9 · Conditioning and guidance (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Conditional models | Class embeddings; text encoders (CLIP, T5) through cross-attention | Class-conditional diffusion on CIFAR-10 |
| 9.2 Classifier guidance | Gradients from a noisy classifier (Dhariwal and Nichol, 2021) | Train a noisy classifier; guide your model |
| 9.3 Classifier-free guidance | Training with condition dropout; extrapolating between conditional and unconditional predictions (Ho and Salimans, 2022) | CFG scale sweep from 1 to 10 |
| 9.4 The trade-off | Fidelity vs diversity; oversaturation at high guidance | Plot FID and CLIPScore against guidance scale |

**Check your understanding:** Why does classifier-free guidance need condition dropout during training? Why does very high guidance reduce diversity and distort colours? What does a guidance scale of 1 mean?

### Chapter 10 · Latent diffusion and diffusion transformers (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Latent diffusion | Diffuse in an autoencoder's latent space (Rombach et al., 2021) | Encode and decode images; measure reconstruction error |
| 10.2 Diffusion transformers | Patchified latents, adaLN conditioning, scaling with Gflops (Peebles and Xie, 2022) | A small DiT on latent CIFAR-10 |
| 10.3 Few-step generation | Consistency models (Song et al., 2023); distillation of samplers | Compare 1-, 2- and 4-step sampling quality |
| 10.4 Fine-tuning in practice | LoRA, DreamBooth-style subject tuning, `diffusers` training scripts; licences of base checkpoints | LoRA fine-tune an open checkpoint on 200 openly licensed images |

**Check your understanding:** Why does latent diffusion cut compute so sharply, and what does it lose? Why did transformers replace U-Nets in the largest image models? What must you check in a base model's licence before fine-tuning for a product?

### Chapter 11 · Evaluating generative models (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Likelihood | Bits per dimension; why likelihood and sample quality can disagree | Compare bpd of your VAE, flow and diffusion models |
| 11.2 FID and its pitfalls | Fréchet distance on Inception features (Heusel et al., 2017); sample-size bias; resizing and compression effects | Show FID changing with sample size and JPEG quality; use `clean-fid` |
| 11.3 Beyond FID | Precision and recall (Kynkäänniemi et al., 2019); CMMD with CLIP embeddings (Jayasumana et al., 2024); CLIPScore for text alignment | Compute all metrics for 3 models; find a case where they disagree |
| 11.4 Human evaluation | Pairwise preference studies, rater instructions, inter-rater agreement | Run a 30-person blind pairwise study |
| 11.5 Memorisation | Nearest-neighbour search in feature space; extraction attacks on your own model (Carlini et al., 2023) | Train on a tiny dataset; measure how many samples are near-copies |

**Check your understanding:** Why should FID numbers computed with different sample counts or resizing code never be compared? What does high precision with low recall look like in samples? Why does a small or duplicated training set make memorisation more likely?

### Chapter 12 · Safety, provenance and law (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Watermarking | Invisible watermarks in latent diffusion (Stable Signature; Tree-Ring); text watermarking (SynthID, *Nature* 2024) | Watermark your model's outputs; test detection after crop, resize and JPEG |
| 12.2 Content credentials | C2PA manifests, signing, hard and soft bindings; specification 2.4 | Attach and verify a C2PA manifest with `c2patool` |
| 12.3 The law | EU AI Act Article 50 (machine-readable marking, from 2 Aug 2026); India's IT Rules amendment on synthetically generated information (notified 10 Feb 2026, in force 20 Feb 2026) | Write a one-page compliance note for your P3 model |
| 12.4 Misuse and consent | Non-consensual imagery, impersonation, voice cloning; consent and licensing of training data | Draft a dataset card and an acceptable-use policy |

**Check your understanding:** Why is a watermark that survives JPEG compression not necessarily robust to a determined remover? What does a C2PA manifest prove, and what does it not prove? Which duties fall on the model provider and which on the platform under India's amended rules?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · KL directions, autoregressive pixels and VAEs | — |
| 2 | 2 | Lab 1 (cont.) | Rate–distortion plot |
| 3 | 3 | Lab 2 · VQ-VAE and codebook health | — |
| 4 | 4 | Lab 3 · DCGAN and WGAN-GP | **P1 due** |
| 5 | 5 | Lab 4 · RealNVP | — |
| 6 | 6 | Lab 5 · DDPM from scratch | Samples and training curve |
| 7 | 7 | Lab 6 · Samplers and flow matching | FID-vs-steps plot |
| 8 | 8 | Lab 6 (cont.) | Mid-term (AI off) |
| 9 | 9 | Lab 7 · Guidance sweep | — |
| 10 | 10 | Lab 8 · DiT and LoRA fine-tuning | **P2 due** |
| 11 | 11 | Lab 9 · Metrics that disagree | — |
| 12 | 11 | Lab 9 (cont.) | Memorisation audit |
| 13 | 12 | Lab 10 · Watermarks and C2PA | Compliance note |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** `diffusers` and training boilerplate; checking algebra in a derivation you have already done; generating evaluation scripts (then testing them); drafting dataset cards and model cards for you to correct.
- **Do without AI (drills):** the ELBO, the DDPM loss, the flow-matching loss, the change-of-variables formula and the classifier-free guidance formula, each derived on paper in timed sessions; the mid-term and final.
- **Verify AI output by:** (1) checking sampling code against the paper's algorithm box line by line; (2) running a 2-D toy where the true density is known; (3) computing FID with a fixed, documented implementation (`clean-fid`) and sample count; (4) a nearest-neighbour memorisation check before showing any sample; (5) confirming licences of every base model and dataset yourself.
- **Where AI still fails here:** record evidence. Generated sampling loops often mix up timestep indexing and variance schedules (ᾱₜ vs αₜ); test them on a 2-D toy with a known answer and log any mismatch. Ask a vision-language model whether your generated images are synthetic and record its accuracy against the ground truth. Note any licence or legal claim an assistant makes that you cannot match to the actual text.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Derivation write-ups | 5% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 25% |

**Mastery gate.** You pass when you can: (1) with AI off, derive the ELBO, the DDPM objective and the conditional flow-matching objective, and write a DDPM sampling loop that runs correctly on a 2-D toy; (2) train a diffusion or flow-matching model from scratch whose FID (fixed implementation, stated sample count) improves steadily and beats your own GAN baseline at equal compute; (3) present a memorisation, watermark-robustness and licence audit of a fine-tuned model and defend it orally.

## Industry reality

Image and video generators in production are mostly latent diffusion or flow-matching transformers: Stability AI's SD3 paper describes rectified-flow transformers (2024), and open checkpoints are distributed through Hugging Face with `diffusers`. Provenance is now engineering work. C2PA publishes an open specification (version 2.4), Google DeepMind's SynthID watermarks AI outputs and its text method was published in *Nature* (2024), and both the EU and India impose labelling duties (sources below). Generative-model roles test derivations, sampling trade-offs and evaluation judgement.

**Interview questions from this course**

1. *Derive the VAE objective and explain the reparameterisation trick.* Strong answer: ELBO from Jensen's inequality or from KL to the true posterior; Gaussian KL in closed form; sampling moved outside the parameters so gradients flow; mentions posterior collapse.
2. *Explain diffusion training and sampling to an engineer who knows VAEs.* Strong answer: fixed forward noising with closed form; network predicts noise (or v); random timestep per example; iterative denoising; DDIM/ODE solvers for fewer steps; relation to hierarchical VAEs.
3. *Why use classifier-free guidance, and what does the scale do?* Strong answer: condition dropout trains conditional and unconditional modes together; the guided prediction extrapolates between them; higher scale raises prompt alignment and fidelity, lowers diversity, and eventually oversaturates.
4. *Our FID improved from 12 to 10. Should we ship?* Strong answer: checks the FID implementation, sample count, resizing and reference set; looks at precision/recall and CMMD; runs a human preference study; checks memorisation and safety; considers whether FID fits the domain at all.
5. *How would you make generated images identifiable?* Strong answer: invisible watermark at generation plus C2PA signed manifest; robustness tests against common edits; limits against determined removal; key management; legal duties under EU Article 50 and India's IT Rules.

## Resources (free first)

- **Courses:** Stanford CS236, Deep Generative Models — https://deepgenerativemodels.github.io/ ; MIT 6.S184, Introduction to Flow Matching and Diffusion Models — https://diffusion.csail.mit.edu/ ; Hugging Face Diffusion Models course — https://huggingface.co/learn/diffusion-course/unit0/1
- **Textbook:** Prince, *Understanding Deep Learning* (chapters on GANs, flows, VAEs and diffusion; free PDF) — https://udlbook.github.io/udlbook/
- **Guides:** Lipman et al., *Flow Matching Guide and Code* — https://arxiv.org/abs/2412.06264 ; Lilian Weng's blog posts on generative models — https://lilianweng.github.io/
- **Libraries:** `diffusers` — https://huggingface.co/docs/diffusers/index ; `clean-fid` — https://github.com/GaParmar/clean-fid ; `c2patool` — https://github.com/contentauth/c2patool
- **Key papers:** VAE https://arxiv.org/abs/1312.6114 ; VQ-VAE https://arxiv.org/abs/1711.00937 ; GAN https://arxiv.org/abs/1406.2661 ; WGAN-GP https://arxiv.org/abs/1704.00028 ; RealNVP https://arxiv.org/abs/1605.08803 ; DDPM https://arxiv.org/abs/2006.11239 ; DDIM https://arxiv.org/abs/2010.02502 ; score SDE https://arxiv.org/abs/2011.13456 ; EDM https://arxiv.org/abs/2206.00364 ; classifier-free guidance https://arxiv.org/abs/2207.12598 ; latent diffusion https://arxiv.org/abs/2112.10752 ; DiT https://arxiv.org/abs/2212.09748 ; flow matching https://arxiv.org/abs/2210.02747 ; rectified flow https://arxiv.org/abs/2209.03003 ; SD3 https://arxiv.org/abs/2403.03206 ; FID https://arxiv.org/abs/1706.08500
- **Provenance and law:** C2PA specifications — https://c2pa.org/specifications/specifications/2.4/index.html ; SynthID — https://deepmind.google/models/synthid/ ; EU AI Act Article 50 — https://artificialintelligenceact.eu/article/50/
- **Datasets:** Oxford Flowers-102 — https://www.robots.ox.ac.uk/~vgg/data/flowers/102/ ; Wikimedia Commons (check each file's licence) — https://commons.wikimedia.org/
- **Compute (free):** DDPM and flow matching at 32×32 fit Kaggle or Colab T4 sessions; LoRA fine-tuning of a 16 GB-class latent diffusion model fits a T4 in fp16 with small batches. Keep FID sample counts fixed across your experiments to save quota.

## Sources

- Esser et al., "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis" (2024) — https://arxiv.org/abs/2403.03206 (checked 2026-10)
- Nie et al., "Large Language Diffusion Models" (2025) — https://arxiv.org/abs/2502.09992 (checked 2026-10)
- Jayasumana et al., "Rethinking FID: Towards a Better Evaluation Metric for Image Generation" (2024) — https://arxiv.org/abs/2401.09603 (checked 2026-10)
- Carlini et al., "Extracting Training Data from Diffusion Models" (2023) — https://arxiv.org/abs/2301.13188 (checked 2026-10)
- EU AI Act, Article 50 (applies from 2 August 2026 under Article 113; amendments proposed in the Digital Omnibus, check the current text) — https://artificialintelligenceact.eu/article/50/ (checked 2026-10)
- Hogan Lovells, "India introduces mandatory labelling for AI and 3-hour takedown for illegal content" (Feb 2026; amendment G.S.R. 120(E) notified 10 Feb 2026, in force 20 Feb 2026) — https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content (checked 2026-10; secondary source, read the Gazette text for exact wording)
- Dathathri et al., "Scalable watermarking for identifying large language model outputs", *Nature* 634 (2024) — https://www.nature.com/articles/s41586-024-08025-4 (checked 2026-10)
- C2PA specification, version 2.4 (latest listed) — https://c2pa.org/specifications/specifications/2.4/index.html (checked 2026-10)

_Last reviewed: 2026-10_
