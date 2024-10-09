# File: tests/test_data_preparation.py

import pytest
import pandas as pd
import numpy as np
from src.data_preparation.data_preparation import load_and_merge_data, preprocess_data

@pytest.fixture
def sample_genetic_data():
    return pd.DataFrame({
        'sample_id': ['S1', 'S2', 'S3'],
        'gene1': [0, 1, 2],
        'gene2': [2, 1, 0]
    })

@pytest.fixture
def sample_phenotype_data():
    return pd.DataFrame({
        'sample_id': ['S1', 'S2', 'S3'],
        'phenotype': ['A', 'B', 'A']
    })

def test_load_and_merge_data(sample_genetic_data, sample_phenotype_data, tmp_path):
    genetic_file = tmp_path / "genetic.csv"
    phenotype_file = tmp_path / "phenotype.csv"
    sample_genetic_data.to_csv(genetic_file, index=False)
    sample_phenotype_data.to_csv(phenotype_file, index=False)
    
    merged_data = load_and_merge_data(str(genetic_file), str(phenotype_file))
    assert len(merged_data) == 3
    assert 'phenotype' in merged_data.columns

def test_preprocess_data(sample_genetic_data):
    preprocessed_data = preprocess_data(sample_genetic_data)
    assert preprocessed_data.isna().sum().sum() == 0  # No missing values
    assert np.allclose(preprocessed_data.mean(), 0, atol=1e-10)  # Centered around 0
    assert np.allclose(preprocessed_data.std(), 1, atol=1e-10)  # Standard deviation of 1
