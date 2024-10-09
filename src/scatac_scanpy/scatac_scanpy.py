# File: src/scatac_scanpy/scatac_scanpy.py

import scanpy as sc
import anndata as ad
import numpy as np
import matplotlib.pyplot as plt

def process_scatac_scanpy(adata):
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    
    sc.pp.normalize_total(adata)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    
    adata = adata[:, adata.var.highly_variable]
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata)
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    
    return adata

def visualize_results(adata):
    sc.pl.umap(adata, color=['leiden'], show=False)
    plt.savefig('scatac_umap_clusters.png')
    plt.close()

def main(file_path):
    adata = ad.read_h5ad(file_path)
    adata = process_scatac_scanpy(adata)
    visualize_results(adata)
    print("scATAC-seq analysis with Scanpy completed.")

if __name__ == "__main__":
    main('path/to/your/scatac/data.h5ad')
