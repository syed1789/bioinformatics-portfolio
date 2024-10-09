File: docs/quality_control.md
Sequencing Quality Control
This module provides functionality for performing quality control on sequencing data.
Overview
The quality control process includes:

Calculating various QC metrics
Visualizing the distribution of read qualities

Main Functions

calculate_qc_metrics(sequencing_data): Calculates quality control metrics for sequencing data.
plot_quality_distribution(sequencing_data): Plots the distribution of read qualities.

Usage
pythonCopyfrom src.quality_control.quality_control import main

main('path/to/your/sequencing_data.csv')
This will calculate QC metrics and generate a plot of the quality score distribution.
