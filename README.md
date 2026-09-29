# ArkTS Benchmark for Generative Software Development

Research repository for the graduation research project:

> **Methods for constructing benchmarks for generative software development
> in low-resource programming languages**

The project focuses on **ArkTS** and investigates methods for constructing
and evaluating benchmarks for generative software development in a
low-resource programming language.

## Research context

This repository is based on the collaborative work behind:

> **ArkTS-CodeSearch: A Open-Source ArkTS Dataset for Code Retrieval**

The original dataset construction and ArkTS data-processing pipeline are
available in the collaborative project:

https://github.com/hreyulog/arkts-codesearch

This repository focuses on the **benchmark experiments, evaluation, and
reproducibility** aspects of the research project.

## Dataset

The benchmark uses the ArkTS-CodeSearch dataset containing **24,452
ArkTS functions** paired with corresponding documentation.

| Split | Examples |
|-------|---------:|
| Train | 19,561 |
| Validation | 2,445 |
| Test | 2,446 |
| **Total** | **24,452** |

The dataset was collected from public GitHub and Gitee repositories and
processed using an ArkTS parsing and extraction pipeline.

## Benchmark task

The primary task is **docstring-to-function retrieval**.

Given a natural-language description (docstring), the system retrieves
relevant ArkTS functions from a candidate collection.

Retrieval quality is evaluated using:

- Recall@1
- Recall@5
- MRR
- NDCG

The repository contains experiments with both lexical and semantic
retrieval approaches.

## Experiments

The experimental part of the project investigates the effect of
domain-specific training on ArkTS code retrieval.

## Main results

The independent NIR experiment evaluates the effect of specialized
ArkTS training data volume on EmbeddingGemma-300M.

| Training data | R@1 | R@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| Zero-shot | 0.5740 | 0.7416 | 0.6397 | 0.6653 |
| 25% | 0.6390 | 0.8115 | 0.7175 | 0.7338 |
| 50% | 0.6500 | 0.8209 | 0.7285 | 0.7448 |
| 100% | 0.6607 | 0.8361 | 0.7390 | 0.7568 |

The results show a consistent increase in all evaluated retrieval
metrics as the amount of specialized ArkTS training data increases.

![Effect of training data volume](figures/data_efficiency.png)

![Experimental results](figures/experiment_results_table.png)

### Baseline retrieval

Evaluation of pretrained embedding models on the ArkTS retrieval task
without ArkTS-specific fine-tuning.

### ArkTS fine-tuning

The main independent experiments fine-tune **EmbeddingGemma-300M**
on ArkTS docstring–function pairs.

The controlled experimental configuration is:

- **Batch size:** 4
- **Maximum sequence length:** 512
- **Loss:** Multiple Negatives Ranking Loss
- **Learning rate:** 1e-5
- **Training epochs:** 2
- **Warm-up ratio:** 10%
- **Random seed:** 42
- **AMP:** disabled

### Controlled data-efficiency experiment

The main independent experiment studies the effect of ArkTS-specific
training data volume.

EmbeddingGemma-300M is fine-tuned using:

- **25%** of the training data;
- **50%** of the training data;
- **100%** of the training data.

All other training parameters are kept fixed.

The repository also contains results reported in the joint
ArkTS-CodeSearch paper for contextual comparison. These results are
clearly separated from the independent work experiments.

## Repository structure

```bash
arkts-benchmark-nir/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── experiments/
│   ├── README.md
│   ├── baseline/
│   ├── fine_tuning/
│   ├── transfer/
│   └── analysis/
│       └── results_analysis.ipynb
│
├── evaluation/
│   └── README.md
│
├── results/
│   ├── README.md
│   └── raw/
│
└── figures/
    ├── data_efficiency.png
    ├── experiment_results_table.png
    ├── paper_model_comparison.png
    └── paper_transfer_results.png
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/schamanichands/arkts-benchmark-nir.git
cd arkts-benchmark-nir
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

The dataset and original preprocessing pipeline are available in the
collaborative ArkTS-CodeSearch project:

https://github.com/hreyulog/arkts-codesearch

See `data/README.md` for dataset preparation instructions.

### 5. Run the experiments

Experiment-specific instructions are provided in:

- `experiments/baseline/`
- `experiments/fine_tuning/`
- `experiments/transfer/`

The analysis notebook is available in:

`experiments/analysis/results_analysis.ipynb`

## Reproducibility

Experiments are organized to make the training and evaluation procedures
reproducible.

The repository separates:

1. Dataset and preprocessing work from the original collaborative project.
2. Benchmark preparation.
3. Model training.
4. Retrieval evaluation.
5. Experimental results and analysis.

Hardware and software configurations are documented alongside the
corresponding experiments.

## Attribution

This repository is part of a research project based on collaborative work.

The ArkTS-CodeSearch dataset and the original ArkTS data-processing
pipeline were developed as part of the joint research work and are
available in:

https://github.com/hreyulog/arkts-codesearch

The independent experiments in this repository focus on the evaluation
of EmbeddingGemma-300M and the effect of ArkTS-specific training data
volume using 25%, 50%, and 100% of the training data.

Results reported in the joint ArkTS-CodeSearch paper are stored
separately and explicitly marked as paper results.
