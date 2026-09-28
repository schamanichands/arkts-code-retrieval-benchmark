# Fine-Tuning Experiments

This directory contains experiments on fine-tuning embedding models using
ArkTS docstring–function pairs.

The main experiment uses **EmbeddingGemma-300M** and investigates whether
domain-specific training on ArkTS improves code retrieval performance.

The main training configuration includes:

- maximum sequence length: 512;
- Multiple Negatives Ranking Loss;
- learning rate: 2e-5;
- 2 training epochs;
- mixed-precision training.

Detailed experiment configurations and results are documented alongside
the corresponding scripts.
