# Baseline experiment

This directory contains the zero-shot baseline evaluation for the ArkTS
code retrieval benchmark.

## Model

The main baseline uses:

- **Model:** EmbeddingGemma-300M
- **Maximum sequence length:** 512 tokens
- **Training:** none

The pretrained model is evaluated directly on the ArkTS test set.

## Evaluation

The test set contains 2,446 docstring–function pairs.

The following metrics are reported:

- Recall@1
- Recall@5
- MRR
- NDCG@5

## Running the baseline

From the repository root:

```bash
python experiments/baseline/run_embeddinggemma.py \
  --output results/zero_shot.json
