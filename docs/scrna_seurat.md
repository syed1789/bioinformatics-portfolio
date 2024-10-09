# Single-cell RNA-seq Analysis (Seurat)

This module provides functionality for analyzing single-cell RNA sequencing data using the Seurat package in R.

## Overview

The scRNA-seq analysis with Seurat includes:
1. Data loading and preprocessing
2. Normalization and feature selection
3. Dimensionality reduction (PCA)
4. Clustering
5. Visualization (UMAP)

## Main Functions

- `process_scrna_seurat(data_path)`: Processes scRNA-seq data using Seurat.

## Usage

```python
from src.scrna_seurat.scrna_seurat import main

main('path/to/your/10x/data')
```

This will process the scRNA-seq data using Seurat and output the results.
