# File: src/quality_control/quality_control.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_qc_metrics(sequencing_data):
    """Calculate quality control metrics for sequencing data."""
    qc_metrics = {
        'total_reads': len(sequencing_data),
        'avg_quality': np.mean(sequencing_data['quality']),
        'gc_content': np.mean(sequencing_data['gc_content']),
    }
    return qc_metrics

def plot_quality_distribution(sequencing_data):
    """Plot the distribution of read qualities."""
    plt.figure(figsize=(10, 6))
    plt.hist(sequencing_data['quality'], bins=50)
    plt.title('Distribution of Read Qualities')
    plt.xlabel('Quality Score')
    plt.ylabel('Count')
    plt.savefig('quality_distribution.png')
    plt.close()

def main(sequencing_file):
    sequencing_data = pd.read_csv(sequencing_file)
    qc_metrics = calculate_qc_metrics(sequencing_data)
    plot_quality_distribution(sequencing_data)
    print(qc_metrics)

if __name__ == "__main__":
    main('path/to/your/sequencing_data.csv')
