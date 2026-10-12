# DLR302 · Computer Vision: From CNNs to Vision Transformers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS206](../../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) | [DLR402](../../year_4/DLR402_multimodal_models/README.md); taken alongside [DLR301](../DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR303](../DLR303_sequence_models_and_transformers/README.md); prepares for [DLR305](../DLR305_generative_models_vaes_gans_and_diffusion/README.md) |

## Why this course matters now

Vision models inspect crops, read documents, guide vehicles and screen medical images. The field changed shape twice in a decade: convolutional networks (AlexNet, 2012; ResNet, 2015) and then transformers and self-supervised learning (ViT, 2020; DINOv2, 2023). Today, pretrained foundation models do much of the work out of the box. Frozen DINOv3 features beat specialised systems on many dense tasks without fine-tuning (Siméoni et al., 2025). SAM 3 segments every instance of a concept named in a short phrase (Carion et al., 2025). CLIP-style models classify images they were never trained on. Coding assistants wire up a `timm` or Hugging Face fine-tuning script in minutes. What still needs a skilled human is everything the benchmark hides. A plant-disease model scored 99.35% on its held-out lab images but 31.4% on photos taken in other conditions (Mohanty et al., 2016). ImageNet models lost 11–14 percentage points on a carefully rebuilt test set (Recht et al., 2019). Building data that matches deployment, measuring shift, and knowing why a model is right are the skills this course trains.

## Learning outcomes

By the end you can:

1. **Implement** convolution (direct and `im2col`), pooling and their backward passes, and **verify** them against PyTorch.
2. **Explain** the design logic of LeNet, AlexNet, VGG, ResNet, EfficientNet and ConvNeXt, and **reproduce** a ResNet on CIFAR-10 to a stated accuracy.
3. **Design** data pipelines and augmentation, and **measure** distribution shift between training data and deployment data.
4. **Fine-tune** and **linear-probe** pretrained backbones (supervised, DINOv2/v3, CLIP/SigLIP) and **choose** among them under data and compute limits.
5. **Train and evaluate** detectors and segmenters, computing IoU, NMS and COCO mAP yourself.
6. **Implement** a Vision Transformer and **compare** its inductive biases and data needs with CNNs at equal compute.
7. **Explain** contrastive, self-distillation and masked-image self-supervised learning, and **evaluate** representations by linear probe and k-NN.
8. **Diagnose** shortcut learning and robustness failures with Grad-CAM, corruption benchmarks and slice analysis.

## Chapters and lessons

### Chapter 1 · Images as tensors and convolution (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Pixels and layouts | Channels, NCHW vs NHWC, normalisation by dataset statistics, colour spaces | Load and inspect 20 images; compute per-channel statistics |
| 1.2 The convolution operation | Sliding dot product, kernel, stride, padding, dilation, output-size formula | Implement `conv2d` with loops; match `F.conv2d` |
| 1.3 Why convolutions work | Locality, weight sharing, translation equivariance; receptive field growth | Compute receptive fields for a 5-layer net by hand |
| 1.4 `im2col` | Convolution as one big matrix multiply; memory trade-off | Vectorised `conv2d`; 100× speed-up over loops |

**Check your understanding:** Why is a convolution equivariant but not invariant to translation, and which layer adds invariance? How many parameters does a 3×3 conv from 64 to 128 channels have, with and without bias? Why does `im2col` use so much memory?

### Chapter 2 · The first CNNs (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Conv backward and pooling | Backward of convolution as a convolution; max and average pooling gradients | Gradcheck your conv and pooling |
| 2.2 LeNet-5 | LeCun et al. (1998): conv–pool stacks for digit recognition | LeNet on MNIST in PyTorch |
| 2.3 AlexNet | ReLU, dropout, data augmentation and GPUs (2012) | Small AlexNet-style net on CIFAR-10 |
| 2.4 VGG | Stacks of 3×3 convolutions (Simonyan and Zisserman, 2014); depth vs parameters | Count FLOPs and parameters of VGG-16 layer by layer |

**Check your understanding:** Why are two 3×3 convolutions preferred to one 5×5? Where are most of VGG-16's parameters, and what does that suggest? Why did ReLU speed up training compared with tanh?

### Chapter 3 · Going deep: residual networks (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The degradation problem | Deeper plain nets train worse, not just overfit | Train 20- and 56-layer plain nets; compare training loss |
| 3.2 ResNet | Identity shortcuts, basic and bottleneck blocks (He et al., 2015); pre-activation blocks | ResNet-18 on CIFAR-10 to ≥ 92% test accuracy |
| 3.3 Batch normalisation in CNNs | Per-channel statistics, train vs eval mode, small-batch problems, GroupNorm | Break a model by evaluating in train mode; fix it |
| 3.4 Efficient designs | Inception modules; depthwise separable convolutions; EfficientNet compound scaling (Tan and Le, 2019) | Compare accuracy per FLOP for three backbones |

**Check your understanding:** Why does an identity shortcut make the degradation problem disappear? What happens to BatchNorm at batch size 2, and what would you use instead? Why can a model with fewer FLOPs run slower on a GPU?

### Chapter 4 · Modern CNNs and training recipes (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 ConvNeXt | "A ConvNet for the 2020s" (Liu et al., 2022): borrowing ViT design choices into a CNN; ConvNeXt V2 | Read the paper's "modernisation roadmap" figure; reproduce two steps |
| 4.2 Recipes matter | AdamW, cosine schedules, label smoothing, stochastic depth, EMA weights | Ablate 5 recipe items on Imagenette |
| 4.3 Augmentation policies | Random-resized crop, flips, colour jitter, RandAugment, mixup, CutMix | Measure each augmentation's effect over 3 seeds |
| 4.4 The `timm` ecosystem | Pretrained weights, model cards, licences, reproducible configs | Fine-tune 3 `timm` backbones with one config file |

**Check your understanding:** How much of ConvNeXt's gain over ResNet came from the training recipe rather than the architecture, and why does that matter when reading papers? Why does mixup change the meaning of "label"? What should you check before using pretrained weights commercially?

### Chapter 5 · Data, augmentation and distribution shift (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Building a dataset | Collection, labelling guidelines, label noise, inter-annotator agreement, duplicates across splits | Find near-duplicates between train and test with perceptual hashing |
| 5.2 Shift you can measure | Lab vs field images; ImageNetV2's 11–14 point drop; ImageNet-C corruptions (Hendrycks and Dietterich, 2019) | Train on PlantVillage, test on PlantDoc field images; report the gap |
| 5.3 Shortcut learning | Texture bias in ImageNet CNNs (Geirhos et al., 2018); background and watermark shortcuts | Show a model using background rather than the object |
| 5.4 India-specific data | IDD (India Driving Dataset, IIIT Hyderabad) with unstructured roads; PlantVillage and PlantDoc for crops | Compare class distributions of IDD with a Western driving dataset |

**Check your understanding:** Why does a 99% held-out accuracy say little about field performance? How would you build a test set that predicts deployment accuracy for a crop app used across Indian states? Which augmentations help with lighting shift, and which can hurt?

### Chapter 6 · Transfer learning (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Linear probe vs fine-tune | Frozen features plus a linear head; full and partial fine-tuning; discriminative learning rates | Compare the three on a 1,000-image dataset |
| 6.2 Choosing a backbone | Supervised ImageNet, CLIP/SigLIP, DINOv2/DINOv3; resolution and patch size | Probe 4 backbones on the same task; plot accuracy vs inference cost |
| 6.3 Small data | Few-shot learning, k-NN on features, strong augmentation | 10-shot classification with k-NN on DINOv2 features |
| 6.4 Forgetting and robustness | Fine-tuning can reduce robustness to shift; weight averaging as a remedy | Measure field-image accuracy before and after full fine-tuning |

**Check your understanding:** When does a linear probe beat full fine-tuning? Why might a self-supervised backbone transfer better than a supervised one to satellite or medical images? How do you choose a learning rate for a pretrained backbone compared with a new head?

### Chapter 7 · Object detection (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Boxes and metrics | IoU, non-maximum suppression, precision–recall, COCO mAP@[.5:.95] | Implement NMS and mAP; match `pycocotools` on a toy set |
| 7.2 Two-stage detectors | Region proposals, anchors, Faster R-CNN (Ren et al., 2015), feature pyramids (FPN) | Fine-tune torchvision Faster R-CNN on a small dataset |
| 7.3 One-stage detectors | YOLO (Redmon et al., 2015), RetinaNet and focal loss for class imbalance | Compare speed and mAP of a one-stage and a two-stage model |
| 7.4 Detection as set prediction | DETR: transformer decoder, object queries, Hungarian matching loss (Carion et al., 2020) | Trace Hungarian matching on 3 predictions and 2 targets |

**Check your understanding:** Why does mAP@[.5:.95] reward tight boxes more than mAP@0.5? What problem does focal loss solve that plain cross-entropy does not? Why does DETR not need NMS?

### Chapter 8 · Segmentation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Semantic segmentation | Fully convolutional nets, encoder–decoder, U-Net skip connections (Ronneberger et al., 2015) | U-Net on a satellite or medical dataset |
| 8.2 Instance and panoptic segmentation | Mask R-CNN (He et al., 2017); panoptic quality | Visualise masks and failure cases |
| 8.3 Losses and metrics | Pixel cross-entropy, Dice, mean IoU; boundary errors | Compare Dice vs cross-entropy on a small-object dataset |
| 8.4 Promptable segmentation | SAM (2023), SAM 2 for video (2024), SAM 3 concept prompts (2025) | Compare zero-shot SAM 3 masks with your U-Net on 50 images |

**Check your understanding:** Why does U-Net need skip connections? When is a zero-shot promptable segmenter good enough, and when must you train your own? Why can mean IoU look good while small objects are always missed?

### Chapter 9 · Vision Transformers (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 ViT | Patch embedding, class token, position embeddings, transformer encoder (Dosovitskiy et al., 2020) | ViT-Tiny from scratch on CIFAR-10 |
| 9.2 Data hunger and DeiT | Weaker inductive bias needs more data or stronger regularisation; distillation token (Touvron et al., 2020) | ViT vs ResNet-18 at equal GPU-hours |
| 9.3 Hierarchical ViTs | Swin Transformer's shifted windows; resolution and token count | Measure memory vs image size for ViT and Swin |
| 9.4 What attention looks at | Attention maps, attention rollout and their limits | Visualise attention maps; compare with Grad-CAM |

**Check your understanding:** Why does a ViT trained from scratch on CIFAR-10 underperform a ResNet, and what changes at a much larger scale? How does patch size trade accuracy against compute? Why are attention maps not explanations?

### Chapter 10 · Self-supervised vision (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Contrastive learning | SimCLR (augmentations, InfoNCE, projection head), MoCo (momentum encoder, queue) | SimCLR on STL-10 unlabeled; k-NN evaluation |
| 10.2 No negatives | BYOL; collapse and how predictor plus stop-gradient avoid it | Show collapse by removing the stop-gradient |
| 10.3 Self-distillation | DINO, DINOv2, DINOv3 (Gram anchoring for dense features) | Linear probe and k-NN with DINOv2 features |
| 10.4 Masked image modelling | MAE: 75% masking, asymmetric encoder–decoder (He et al., 2021); I-JEPA predicts in latent space | Small MAE on CIFAR-10; visualise reconstructions |
| 10.5 Evaluating representations | Linear probe, k-NN, fine-tune, dense probes; label efficiency curves | Accuracy at 1%, 10%, 100% labels for 3 backbones |

**Check your understanding:** Why do contrastive methods need strong augmentation, and what invariance does each augmentation teach? How does BYOL avoid collapse without negatives? Why does MAE mask so much more than BERT does?

### Chapter 11 · Vision–language: CLIP and SigLIP (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 CLIP | Contrastive image–text pretraining on 400M pairs; zero-shot classification by prompts (Radford et al., 2021) | Zero-shot classify Food-101 with prompt ensembles |
| 11.2 SigLIP and SigLIP 2 | Sigmoid pairwise loss; multilingual training and better localisation | Compare English and Hindi prompts with SigLIP 2 |
| 11.3 Biases and failure modes | Typographic attacks, dataset bias, poor counting and spatial reasoning | Build a 50-image probe set for counting and left/right |
| 11.4 From CLIP to multimodal models | Vision encoders inside VLMs; preview of [DLR402](../../year_4/DLR402_multimodal_models/README.md) | Linear-probe CLIP vs DINOv2 features on the same task |

**Check your understanding:** Why does contrastive pretraining give zero-shot classification "for free"? What changes when the softmax over the batch becomes a sigmoid per pair? Why does writing a word on an object fool CLIP?

### Chapter 12 · Robustness, explanation and deployment (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Explanations | Grad-CAM (Selvaraju et al., 2016), occlusion maps, their sanity checks | Use Grad-CAM to catch a shortcut in your P1 model |
| 12.2 Adversarial robustness | Small perturbations flip predictions; FGSM/PGD as robustness tests of your own model; adversarial training costs | Report accuracy under ε-bounded perturbations |
| 12.3 Calibration and abstention | Confidence thresholds, selective prediction, out-of-distribution detection | An "I don't know" option for non-plant images |
| 12.4 Shipping a vision model | ONNX export, latency on CPU and mobile, quantisation preview ([DLR404](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md)), monitoring drift | Export and benchmark your model on CPU |

**Check your understanding:** Why can a Grad-CAM map look plausible for a wrong reason? Why is adversarial accuracy usually far below clean accuracy, and when does it matter in practice? What would you monitor after deploying a crop-disease model?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Convolution and classic CNNs | `conv2d` matching PyTorch |
| 2 | 2 | Lab 1 (cont.) | LeNet and AlexNet-style results |
| 3 | 3 | Lab 2 · ResNet reproduction | ResNet-18 ≥ 92% on CIFAR-10 |
| 4 | 4 | Lab 3 · Recipe ablation | **P1 due** |
| 5 | 5 | Lab 4 · Shift audit | Lab-to-field gap report |
| 6 | 6 | Lab 5 · Backbone bake-off | Probe vs fine-tune table |
| 7 | 7 | Lab 6 · Detection metrics and fine-tuning | mAP matching `pycocotools` |
| 8 | 8 | Lab 7 · Segmentation vs SAM 3 | Mid-term (AI off) |
| 9 | 9 | Lab 8 · ViT vs ResNet at equal compute | — |
| 10 | 10 | Lab 9 · Self-supervised pretraining | **P2 due** |
| 11 | 10 | Lab 9 (cont.) | Label-efficiency curves |
| 12 | 11 | Lab 10 · CLIP and SigLIP probes | Multilingual prompt report |
| 13 | 12 | Robustness clinic | Robustness report |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** boilerplate training loops and data loaders; converting annotation formats (COCO, YOLO, Pascal VOC); plotting; drafting augmentation pipelines; summarising papers after you have read them. Coding assistants (Claude Code, Cursor, GitHub Copilot) handle `timm`, torchvision and Hugging Face APIs well. Vision-language models (Claude, Gemini, GPT) can pre-label images, but treat their labels as noisy.
- **Do without AI (drills):** convolution output shapes and parameter counts; IoU, NMS and mAP by hand; receptive-field calculations; the InfoNCE loss on paper; the mid-term and final.
- **Verify AI output by:** (1) checking that metric code matches `pycocotools` or `torchmetrics` on a toy case with a known answer; (2) visualising 50 augmented images before training; (3) testing for duplicates across splits; (4) evaluating on a shifted test set, not only the random split; (5) running at least 3 seeds before claiming an improvement.
- **Where AI still fails here:** measure it yourself. Have a VLM label 200 images from PlantDoc or IDD and compare with ground truth by class; record the error rate and which classes fail. Ask an assistant to write mAP code and test it against `pycocotools` on edge cases (no predictions, duplicate detections, crowd annotations). Log every discrepancy; these logs feed P3's error analysis.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Paper-reading quizzes (ResNet, ViT, DINO, CLIP) | 5% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 25% |

**Mastery gate.** You pass when you can: (1) with AI off, implement a convolution layer with backward and a ResNet basic block, and compute NMS and AP on a small example by hand; (2) given an unfamiliar image dataset and 4 GPU-hours, deliver a model with a written deployment-shift analysis, a linear-probe baseline, and a fine-tuned model whose gain over that baseline is shown across 3 seeds; (3) explain in an oral exam why your model fails on its worst slice and what data you would collect to fix it.

## Industry reality

Self-supervised backbones are now standard starting points: Meta released DINOv3 as "a versatile vision foundation model" whose frozen features beat specialised systems across dense tasks (2025), and SAM 3 is open-sourced with a concept-segmentation benchmark (2025). Agricultural vision shows why evaluation matters. The PlantVillage model's accuracy fell from 99.35% on held-out lab images to 31.4% on field-style photos (Mohanty et al., 2016), and PlantDoc was built from internet field images to address the gap (Singh et al., 2019). India's unstructured traffic motivated the IDD dataset (Varma et al., 2018). Computer-vision engineers spend much of their time on data curation, labelling quality and evaluation design, which is also what interviewers probe.

**Interview questions from this course**

1. *Our defect detector is 98% accurate in testing but poor on the factory floor. What do you do?* Strong answer: checks whether the test split mirrors deployment (cameras, lighting, time); collects a field test set; inspects errors by slice; looks for shortcuts with Grad-CAM; proposes targeted data collection and augmentation; defines monitoring.
2. *Explain ResNet's key idea and why it works.* Strong answer: degradation problem; identity shortcuts make identity easy to learn and keep gradients flowing; bottleneck blocks; BatchNorm placement; mentions pre-activation variants.
3. *ViT or CNN for a 5,000-image medical dataset?* Strong answer: inductive bias vs data size; recommends a pretrained backbone (CNN or self-supervised ViT) with linear probe then fine-tune; evaluation with patient-level splits; compares at equal compute.
4. *Walk through how mAP is computed.* Strong answer: per-class precision–recall from score-sorted detections matched at an IoU threshold; interpolated AP; averaged over classes and IoU thresholds 0.5–0.95; pitfalls with duplicates and crowd boxes.
5. *How does CLIP do zero-shot classification, and where does it fail?* Strong answer: shared embedding space from contrastive training; class names turned into prompts; cosine similarity; prompt ensembles; failures on counting, spatial relations, fine-grained or rare classes, typographic attacks and dataset bias.

## Resources (free first)

- **Primary course:** Stanford CS231n, Deep Learning for Computer Vision (Spring 2026) — https://cs231n.stanford.edu/
- **Textbooks:** *Dive into Deep Learning*, chapters on CNNs and modern CNNs — https://d2l.ai/ ; Prince, *Understanding Deep Learning* (free PDF) — https://udlbook.github.io/udlbook/
- **Practical course:** fast.ai, Practical Deep Learning for Coders — https://course.fast.ai/
- **Libraries:** `timm` (PyTorch Image Models) — https://github.com/huggingface/pytorch-image-models ; DINOv3 — https://github.com/facebookresearch/dinov3 ; SAM 3 — https://github.com/facebookresearch/sam3
- **Datasets:** CIFAR-10/100 — https://www.cs.toronto.edu/~kriz/cifar.html ; ImageNet — https://www.image-net.org/ ; PlantVillage — https://github.com/spMohanty/PlantVillage-Dataset ; IDD — https://idd.insaan.iiit.ac.in/ ; EuroSAT — https://arxiv.org/abs/1709.00029
- **Key papers:** ResNet https://arxiv.org/abs/1512.03385 ; ConvNeXt https://arxiv.org/abs/2201.03545 ; ViT https://arxiv.org/abs/2010.11929 ; DeiT https://arxiv.org/abs/2012.12877 ; SimCLR https://arxiv.org/abs/2002.05709 ; MAE https://arxiv.org/abs/2111.06377 ; DINO https://arxiv.org/abs/2104.14294 ; DINOv2 https://arxiv.org/abs/2304.07193 ; CLIP https://arxiv.org/abs/2103.00020 ; SigLIP 2 https://arxiv.org/abs/2502.14786 ; DETR https://arxiv.org/abs/2005.12872 ; SAM https://arxiv.org/abs/2304.02643
- **Compute (free):** labs fit a free Colab GPU (12-hour maximum sessions, unpublished and fluctuating limits) or Kaggle's P100 / 2× T4 with a weekly quota shown in account settings. Pre-compute features once and probe on CPU to save quota.

## Sources

- Mohanty, Hughes and Salathé, "Using Deep Learning for Image-Based Plant Disease Detection" (2016) — https://arxiv.org/abs/1604.03169 (checked 2026-10)
- Singh et al., "PlantDoc: A Dataset for Visual Plant Disease Detection" (2019) — https://arxiv.org/abs/1911.10317 (checked 2026-10)
- Recht et al., "Do ImageNet Classifiers Generalize to ImageNet?" (2019) — https://arxiv.org/abs/1902.10811 (checked 2026-10)
- Siméoni et al., "DINOv3" (Aug 2025) — https://arxiv.org/abs/2508.10104 (checked 2026-10)
- Carion et al., "SAM 3: Segment Anything with Concepts" (Nov 2025) — https://arxiv.org/abs/2511.16719 (checked 2026-10)
- Varma et al., "IDD: A Dataset for Exploring Problems of Autonomous Navigation in Unconstrained Environments" (2018) — https://arxiv.org/abs/1811.10200 (checked 2026-10)
- Geirhos et al., "ImageNet-trained CNNs are biased towards texture" (2018) — https://arxiv.org/abs/1811.12231 ; Hendrycks and Dietterich, "Benchmarking Neural Network Robustness to Common Corruptions and Perturbations" (2019) — https://arxiv.org/abs/1903.12261 (checked 2026-10)
- Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (2021) — https://arxiv.org/abs/2103.00020 (checked 2026-10)
- Google Colab FAQ — https://research.google.com/colaboratory/faq.html ; Kaggle notebooks documentation — https://www.kaggle.com/docs/notebooks (checked 2026-10)

_Last reviewed: 2026-10_
