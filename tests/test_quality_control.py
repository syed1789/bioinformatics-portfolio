# File: tests/test_quality_control.py

import pytest
import pandas as pd
import numpy as np
from src.quality_control.quality_control import calculate_qc_metrics, plot_quality_distribution

@pytest.fixture
def sample_sequencing_data():
    return pd.DataFrame({
        'quality': np.random.rand(100) * 40,
        'gc_content': np.random.rand(100)
    })

def test_calculate_qc_metrics(sample_sequencing_data):
    metrics = calculate_qc_metrics(sample_sequencing_data)
    assert 'total_reads' in metrics
    assert 'avg_quality' in metrics
    assert 'gc_content' in metrics

def test_plot_quality_distribution(sample_sequencing_data, tmp_path):
    plot_quality_distribution(sample_sequencing_data)
    assert (tmp_path / 'quality_distribution.png').exists()


