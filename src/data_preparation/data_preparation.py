# File: src/data_preparation/data_preparation.py

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def load_and_merge_data(genetic_data_file, phenotype_data_file):
    """Load and merge genetic and phenotype data."""
    genetic_data = pd.read_csv(genetic_data_file)
    phenotype_data = pd.read_csv(phenotype_data_file)
    merged_data = pd.merge(genetic_data, phenotype_data, on='sample_id')
    return merged_data

def preprocess_data(data):
    """Preprocess data: handle missing values and standardize features."""
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data_imputed), columns=data_imputed.columns)
    return data_scaled

def main(genetic_data_file, phenotype_data_file, output_file):
    merged_data = load_and_merge_data(genetic_data_file, phenotype_data_file)
    preprocessed_data = preprocess_data(merged_data)
    preprocessed_data.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    main('genetic_data.csv', 'phenotype_data.csv', 'preprocessed_data.csv')
