# Genomic Data Preparation

This module provides functionality for preparing genomic data for downstream analyses.

## Overview

The data preparation process includes:
1. Loading and merging genetic and phenotype data
2. Handling missing values
3. Standardizing features

## Main Functions

- `load_and_merge_data(genetic_data_file, phenotype_data_file)`: Loads and merges genetic and phenotype data.
- `preprocess_data(data)`: Handles missing values and standardizes features.

## Usage

```python
from src.data_preparation.data_preparation import main

main('genetic_data.csv', 'phenotype_data.csv', 'preprocessed_data.csv')
```

This will load the data, preprocess it, and save the result to a new file.
