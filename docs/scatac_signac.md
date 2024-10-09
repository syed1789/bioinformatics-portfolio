# Single-cell ATAC-seq Analysis (Signac)

This module provides functionality for analyzing single-cell ATAC-seq data using the Signac package in R.

## Overview

The scATAC-seq analysis with Signac includes:
1. Data loading and preprocessing
2. Quality control
3. Dimensionality reduction (LSI)
4. Clustering
5. Visualization (UMAP)

## Main Functions

- `process_scatac_signac(counts_path, fragments_path)`: Processes scATAC-seq data using Signac.

## Usage

```python
from src.scatac_signac.scatac_signac import main

main('path/to/your/counts.h5', 'path/to/your/fragments.tsv.gz')
```

This will process the scATAC-seq data using Signac and output the results.
