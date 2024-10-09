# File: src/scatac_signac/scatac_signac.py

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas DataFrames
pandas2ri.activate()

# Import R packages
signac = importr('Signac')
seurat = importr('Seurat')
base = importr('base')

def process_scatac_signac(counts_path, fragments_path):
    r_code = f"""
    library(Signac)
    library(Seurat)
    
    # Load data
    counts <- Read10X_h5("{counts_path}")
    fragments <- CreateFragmentObject(path = "{fragments_path}", cells = colnames(counts))
    
    # Create Seurat object
    assay <- CreateChromatinAssay(counts = counts, fragments = fragments)
    object <- CreateSeuratObject(assay, assay = "peaks")
    
    # Preprocess data
    object <- NucleosomeSignal(object)
    object <- TSSEnrichment(object)
    
    # Normalize and find variable features
    object <- RunTFIDF(object)
    object <- FindTopFeatures(object, min.cutoff = "q0")
    
    # Dimension reduction and clustering
    object <- RunSVD(object)
    object <- RunUMAP(object, dims = 2:50, reduction = "lsi")
    object <- FindNeighbors(object, dims = 2:50, reduction = "lsi")
    object <- FindClusters(object, resolution = 0.5, algorithm = 3)
    
    # Return processed data
    list(
      umap = Embeddings(object, "umap"),
      clusters = Idents(object),
      counts = GetAssayData(object, slot = "counts", assay = "peaks")
    )
    """
    
    result = ro.r(r_code)
    return result

def main(counts_path, fragments_path):
    result = process_scatac_signac(counts_path, fragments_path)
    print("scATAC-seq analysis with Signac completed.")

if __name__ == "__main__":
    main('path/to/your/counts.h5', 'path/to/your/fragments.tsv.gz')
