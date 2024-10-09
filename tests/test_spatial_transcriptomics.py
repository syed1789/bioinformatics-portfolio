# File: tests/test_spatial_transcriptomics.py

import pytest
import scanpy as sc
import numpy as np
from src.spatial_transcriptomics.spatial_transcriptomics import process_spatial_data, spatial_analysis

@pytest.fixture
def sample_spatial_data():
    adata = sc.AnnData(X=np.random.rand(100, 200))
    adata.obsm['spatial'] = np.random.rand(100, 2)
    return adata

def test_process_spatial_data(sample_spatial_data):
    processed_adata = process_spatial_data(sample_spatial_data)
    assert 'leiden' in processed_adata.obs.columns
    assert 'X_umap' in processed_adata.obsm

def test_spatial_analysis(sample_spatial_data):
    processed_adata = process_spatial_data(sample_spatial_data)
    spatial_analysis(processed_adata)
    assert 'spatial_neighbors' in processed_adata.uns
