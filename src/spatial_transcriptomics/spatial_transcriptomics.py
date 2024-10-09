# File: src/spatial_transcriptomics/spatial_transcriptomics.py

import scanpy as sc
import squidpy as sq
import numpy as np
import matplotlib.pyplot as plt

def process_spatial_data(adata):
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    sc.pp.pca(adata)
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    return adata

def spatial_analysis(adata):
    sq.gr.spatial_neighbors(adata)
    sq.gr.spatial_autocorr(
        adata,
        mode="moran",
        n_perms=100,
        n_jobs=1,
        genes=adata.var_names[adata.var.highly_variable],
    )

def visualize_results(adata):
    sc.pl.spatial(adata, color="leiden", show=False)
    plt.savefig('spatial_clusters.png')
    plt.close()

def main(visium_path):
    adata = sc.read_visium(visium_path)
    adata = process_spatial_data(adata)
    spatial_analysis(adata)
    visualize_results(adata)
    print("Spatial transcriptomics analysis completed.")

if __name__ == "__main__":
    main('path/to/your/visium/data')
