# Spatial Transcriptomics Analysis

This module provides functionality for analyzing spatial transcriptomics data.

## Overview

The spatial transcriptomics analysis includes:
1. Data loading and preprocessing
2. Normalization and feature selection
3. Dimensionality reduction and clustering
4. Spatial analysis
5. Visualization

## Main Functions

- `process_spatial_data(adata)`: Processes spatial transcriptomics data.
- `spatial_analysis(adata)`: Performs spatial analysis on the processed data.
- `visualize_results(adata)`: Visualizes the results of the analysis.

## Usage

```python
from src.spatial_transcriptomics.spatial_transcriptomics import main

main('path/to/your/visium/data')
```

This will process the spatial transcriptomics data, perform spatial analysis, and generate visualizations.
