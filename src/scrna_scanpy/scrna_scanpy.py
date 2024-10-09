# File: src/scrna_scanpy/scrna_scanpy.py

import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt

def process_scrna_scanpy(adata):
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
    
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    
    adata = adata[:, adata.var.highly_variable]
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver='arpack')
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    sc.tl.umap(adata)
    sc.tl.leiden(adata)
    
    return adata

def visualize_results(adata):
    sc.pl.umap(adata, color=['leiden'], show=False)
    plt.savefig('umap_clusters.png')
    plt.close()

def main(data_path):
    adata = sc.read_10x_mtx(data_path)
    adata = process_scrna_scanpy(adata)
    visualize_results(adata)
    print("scRNA-seq analysis with Scanpy completed.")

if __name__ == "__main__":
    main('path/to/your/10x/data')

