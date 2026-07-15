# Bioinformatics Portfolio

This repository showcases a comprehensive set of bioinformatics analyses and skills.

**Featured:** [Baseline CD8 exhaustion burden predicts checkpoint-blockade response](docs/scrna_icb_response.md) — end-to-end reanalysis of GSE120575 from raw GEO files. AUROC 0.86 (n=19), replicated across three independent parameterizations.

## Projects

1. Variant Analysis Pipeline
2. Sequencing Quality Control
3. Genomic Data Preparation
4. Single-cell RNA-seq Analysis (Seurat)
5. Single-cell RNA Sequencing Analysis (Scanpy)
6. Spatial Transcriptomics Analysis
7. Single-cell ATAC-seq Analysis (Signac/Seurat)
8. Single-cell ATAC-seq Analysis (Scanpy/Episcanpy)
9. ICB Response Biomarker: CD8 Exhaustion Predicts Checkpoint Blockade Response (GSE120575)

## Setup

1. Clone this repository
2. Install required Python packages: `pip install -r requirements.txt`
3. Install required R packages: `R -e "install.packages(readLines('r_requirements.txt'), repos='http://cran.rstudio.com/')"`
4. Run tests: `pytest tests/`

## Usage

Each analysis can be run independently. See individual documentation in the `docs/` directory for details.

## Documentation

Detailed documentation for each analysis can be found in the `docs` directory:

- [Variant Analysis](docs/variant_analysis.md)
- [Sequencing Quality Control](docs/quality_control.md)
- [Genomic Data Preparation](docs/data_preparation.md)
- [Single-cell RNA-seq Analysis (Seurat)](docs/scrna_seurat.md)
- [Single-cell RNA-seq Analysis (Scanpy)](docs/scrna_scanpy.md)
- [Spatial Transcriptomics Analysis](docs/spatial_transcriptomics.md)
- [Single-cell ATAC-seq Analysis (Signac)](docs/scatac_signac.md)
- [Single-cell ATAC-seq Analysis (Scanpy)](docs/scatac_scanpy.md)
- [ICB Response Biomarker — CD8 Exhaustion](docs/scrna_icb_response.md)


## Contact

Syed Nurul Hasan - [nayanchoto1789@gmail.com]

