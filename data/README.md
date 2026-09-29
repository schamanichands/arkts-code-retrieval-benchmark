# Dataset

This directory contains documentation related to the dataset used in the
benchmark experiments.

## ArkTS-CodeSearch

The benchmark is based on the **ArkTS-CodeSearch** dataset:

https://huggingface.co/datasets/hreyulog/arkts-code-docstring

The dataset contains **24,452 ArkTS function–documentation pairs**.

| Split | Examples |
|-------|---------:|
| Train | 19,561 |
| Validation | 2,445 |
| Test | 2,446 |
| **Total** | **24,452** |

The dataset was collected from public GitHub and Gitee repositories and
processed using an ArkTS parsing and extraction pipeline.

## Data splits

The benchmark uses the original dataset split:

- **Train:** 19,561 examples
- **Validation:** 2,445 examples
- **Test:** 2,446 examples

The test set is kept fixed across experiments.

## Training subsets

For data-efficiency experiments, subsets of the training split are created
using a fixed random seed.

The planned configurations are:

- **25%:** 4,890 examples
- **50%:** 9,780 examples
- **100%:** 19,561 examples

The validation and test sets are not reduced.

## Original preprocessing pipeline

The original ArkTS dataset construction and preprocessing pipeline are
available in the collaborative project:

https://github.com/hreyulog/arkts-codesearch

This repository does not duplicate the original dataset construction
pipeline. It focuses on benchmark experiments, evaluation, and
reproducibility.
