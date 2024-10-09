# File: src/scrna_seurat/scrna_seurat.py

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas DataFrames
pandas2ri.activate()

# Import R packages
seurat = importr('Seurat')
base = importr('base')

def process_scrna_seurat(data_path):
    r_code = f"""
    library(Seurat)
    
    # Load data
    data <- Read10X(data.dir = "{data_path}")
    
    # Create Seurat object
    seurat_object <- CreateSeuratObject(counts = data, project = "scRNA_project", min.cells = 3, min.features = 200)
    
    # Normalize data
    seurat_object <- NormalizeData(seurat_object)
    
    # Find variable features
    seurat_object <- FindVariableFeatures(seurat_object, selection.method = "vst", nfeatures = 2000)
    
    # Scale data
    all_genes <- rownames(seurat_object)
    seurat_object <- ScaleData(seurat_object, features = all_genes)
    
    # Perform PCA
    seurat_object <- RunPCA(seurat_object, features = VariableFeatures(object = seurat_object))
    
    # Find neighbors and clusters
    seurat_object <- FindNeighbors(seurat_object, dims = 1:10)
    seurat_object <- FindClusters(seurat_object, resolution = 0.5)
    
    # Run UMAP
    seurat_object <- RunUMAP(seurat_object, dims = 1:10)
    
    # Return processed data
    list(
      umap = Embeddings(seurat_object, "umap"),
      clusters = Idents(seurat_object),
      counts = GetAssayData(seurat_object, slot = "counts")
    )
    """
    
    result = ro.r(r_code)
    return result

def main(data_path):
    result = process_scrna_seurat(data_path)
    print("scRNA-seq analysis with Seurat completed.")

if __name__ == "__main__":
    main('path/to/your/10x/data')
