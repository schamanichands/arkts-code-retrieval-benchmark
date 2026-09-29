# Fine-tuning experiments

This directory contains experiments on domain-specific fine-tuning of
EmbeddingGemma-300M for ArkTS code retrieval.

## Objective

The experiments investigate how fine-tuning on ArkTS-specific
docstring–function pairs affects retrieval quality and how the amount of
training data influences the resulting benchmark performance.

## Model

All controlled experiments use:

- **Model:** EmbeddingGemma-300M
- **Maximum sequence length:** 512 tokens
- **Loss:** Multiple Negatives Ranking Loss
- **Batch size:** 4
- **Learning rate:** 1e-5
- **Epochs:** 2
- **Warm-up ratio:** 10%
- **Mixed precision:** disabled
- **Random seed:** 42

## Training data

The experiments use subsets of the ArkTS-CodeSearch training split.

| Configuration | Training examples |
|---|---:|
| 25% | 4,890 |
| 50% | 9,780 |
| 100% | 19,561 |

The validation and test sets remain unchanged.

## Evaluation

All trained models are evaluated on the same test set containing 2,446
examples.

The following retrieval metrics are reported:

- Recall@1
- Recall@5
- MRR
- NDCG@5

## Reproducibility

Training configurations are stored together with the corresponding
experiment results.

Model checkpoints are not stored in the Git repository because of their
size.
