# Single-cell RNA-seq Analysis (Scanpy)

This module provides functionality for analyzing single-cell RNA sequencing data using the Scanpy package in Python.

## Overview

The scRNA-seq analysis with Scanpy includes:
1. Data loading and preprocessing
2. Normalization and feature selection
3. Dimensionality reduction (PCA and UMAP)
4. Clustering
5. Visualization

## Main Functions

- `process_scrna_scanpy(adata)`: Processes scRNA-seq data using Scanpy.
- `visualize_results(adata)`: Visualizes the results of the analysis.

## Usage

```python
from src.scrna_scanpy.scrna_scanpy import main

main('path/to/your/10x/data')
```

This will process the scRNA-seq data using Scanpy and generate visualizations.
