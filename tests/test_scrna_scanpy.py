# File: tests/test_scrna_scanpy.py

import pytest
import scanpy as sc
import numpy as np
from src.scrna_scanpy.scrna_scanpy import process_scrna_scanpy

@pytest.fixture
def sample_anndata():
    return sc.AnnData(X=np.random.rand(100, 200))

def test_process_scrna_scanpy(sample_anndata):
    processed_adata = process_scrna_scanpy(sample_anndata)
    assert 'leiden' in processed_adata.obs.columns
    assert 'X_umap' in processed_adata.obsm
