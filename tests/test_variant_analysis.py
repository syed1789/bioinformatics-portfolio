# File: tests/test_variant_analysis.py

import pytest
import pandas as pd
from src.variant_analysis.variant_analysis import load_vcf, annotate_variants, filter_variants

@pytest.fixture
def sample_vcf_data():
    return pd.DataFrame({
        'CHROM': ['chr1', 'chr1', 'chr2'],
        'POS': [100, 200, 300],
        'REF': ['A', 'G', 'T'],
        'ALT': ['T', 'C', 'G'],
        'MAF': [0.01, 0.05, 0.1]
    })

def test_load_vcf(tmp_path):
    # Create a temporary VCF file
    vcf_file = tmp_path / "test.vcf"
    vcf_file.write_text("CHROM\tPOS\tREF\tALT\nchr1\t100\tA\tT\n")
    
    df = load_vcf(str(vcf_file))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1

def test_annotate_variants(sample_vcf_data):
    annotated_df = annotate_variants(sample_vcf_data)
    assert 'MAF' in annotated_df.columns

def test_filter_variants(sample_vcf_data):
    filtered_df = filter_variants(sample_vcf_data, maf_threshold=0.05)
    assert len(filtered_df) == 2

