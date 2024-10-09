# File: tests/test_scatac_scanpy.py

import pytest
import scanpy as sc
import numpy as np
from src.scatac_scanpy.scatac_scanpy import process_scatac_scanpy

@pytest.fixture
def sample_scatac_data():
    return sc.AnnData(X=np.random.rand(100, 200))

def test_process_scatac_scanpy(sample_scatac_data):
    processed_adata = process_scatac_scanpy(sample_scatac_data)
    assert 'leiden' in processed_adata.obs.columns
    assert 'X_umap' in processed_adata.obsm
