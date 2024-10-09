File: docs/variant_analysis.md
Variant Analysis Pipeline
This module provides functionality for analyzing genetic variants from VCF files.
Overview
The variant analysis pipeline includes the following steps:

Loading VCF files
Annotating variants with additional information
Filtering variants based on specific criteria (e.g., minor allele frequency)

Main Functions

load_vcf(file_path): Loads a VCF file into a pandas DataFrame.
annotate_variants(vcf_df): Annotates variants with additional information.
filter_variants(annotated_df, maf_threshold=0.01): Filters variants based on minor allele frequency.

Usage
pythonCopyfrom src.variant_analysis.variant_analysis import main

main("path/to/your/vcf/file")
This will process the VCF file, annotate variants, apply filtering, and output the results.
