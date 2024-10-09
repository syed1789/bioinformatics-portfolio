# Variant Analysis Pipeline

This module provides functionality for analyzing genetic variants from VCF files.

## Functions

- `load_vcf(file_path)`: Load a VCF file.
- `annotate_variants(vcf_df)`: Annotate variants with additional information.
- `filter_variants(annotated_df)`: Filter variants based on specific criteria.

## Usage

```python
from src.variant_analysis.variant_analysis import main

main("path/to/your/vcf/file")
```
