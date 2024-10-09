File: docs/scrna_scanpy.md
Single-cell RNA-seq Analysis (Scanpy)
This module provides functionality for analyzing single-cell RNA sequencing data using the Scanpy package in Python.
Overview
The scRNA-seq analysis with Scanpy includes:

Data loading and preprocessing
Normalization and feature selection
Dimensionality reduction (PCA and UMAP)
Clustering
Visualization

Main Functions

process_scrna_scanpy(adata): Processes scRNA-seq data using Scanpy.
visualize_results(adata): Visualizes the results of the analysis.

Usage
pythonCopyfrom src.scrna_scanpy.scrna_scanpy import main

main('path/to/your/10x/data')
This will process the scRNA-seq data using Scanpy and generate visualizations.
