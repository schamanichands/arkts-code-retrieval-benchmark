# Experiments

This directory contains the experiments conducted for the ArkTS benchmark.

The experiments investigate semantic code retrieval for ArkTS and the effect
of domain-specific fine-tuning and training data size.

## Experimental setup

The main experiments use:

- **Model:** EmbeddingGemma-300M
- **Task:** docstring-to-function retrieval
- **Maximum sequence length:** 512 tokens
- **Loss:** Multiple Negatives Ranking Loss
- **Batch size:** 4
- **Learning rate:** 1e-5
- **Epochs:** 2
- **Warm-up ratio:** 10%
- **Random seed:** 42

The controlled data-efficiency experiments use the same training
configuration while varying the amount of training data.

## Experiment groups

### Baseline

Zero-shot evaluation of pretrained embedding models on the ArkTS test set.

See:

`baseline/`

### Fine-tuning

Domain-specific fine-tuning of EmbeddingGemma-300M on ArkTS
docstring–function pairs.

The main controlled experiments use:

- 25% of the training data — 4,890 examples
- 50% of the training data — 9,780 examples
- 100% of the training data — 19,561 examples

See:

`fine_tuning/`

### Transfer

The repository reserves this directory for experiments involving transfer
from TypeScript to ArkTS.

The TypeScript-to-ArkTS transfer experiment is not part of the main
experimental series of this research project.

See:

`transfer/`

## Evaluation

All fine-tuned models are evaluated on the same fixed test set containing
2,446 examples.

The main retrieval metrics are:

- Recall@1
- Recall@5
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG@5)

Experimental results are stored in:

`../results/`

and evaluation utilities are documented in:

`../evaluation/`
