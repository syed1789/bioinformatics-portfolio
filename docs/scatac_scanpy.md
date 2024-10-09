# Single-cell ATAC-seq Analysis (Scanpy)

This module provides functionality for analyzing single-cell ATAC-seq data using the Scanpy package in Python.

## Overview

The scATAC-seq analysis with Scanpy includes:
1. Data loading and preprocessing
2. Normalization and feature selection
3. Dimensionality reduction (PCA and UMAP)
4. Clustering
5. Visualization

## Main Functions

- `process_scatac_scanpy(adata)`: Processes scATAC-seq data using Scanpy.
- `visualize_results(adata)`: Visualizes the results of the analysis.

## Usage

```python
from src.scatac_scanpy.scatac_scanpy import main

main('path/to/your/scatac/data.h5ad')
```

This will process the scATAC-seq data using Scanpy and generate visualizations.
