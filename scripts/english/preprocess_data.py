# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import re

def convert_to_snake_case(df):
    # Replace spaces with underscores and convert uppercase letters to snake_case, ignoring abbreviations like ID
    df.columns = [re.sub(r'(?<=[a-z])(?=[A-Z])', '_', col).replace(' ', '_').lower() for col in df.columns]
    return df

def merge_data(files_list):
    try:
        # Load and convert column names to snake_case
        df_contract = convert_to_snake_case(pd.read_csv(files_list[0]))
        df_personal = convert_to_snake_case(pd.read_csv(files_list[1]))
        df_internet = convert_to_snake_case(pd.read_csv(files_list[2]))
        df_phone = convert_to_snake_case(pd.read_csv(files_list[3]))

        # Merge DataFrames
        df_merged = pd.merge(df_contract, df_personal, on='customer_id', how='left')
        df_merged = pd.merge(df_merged, df_internet, on='customer_id', how='left')
        df_merged = pd.merge(df_merged, df_phone, on='customer_id', how='left')

        return df_merged
    except Exception as e:
        print(f"Error merging files: {e}")
        raise

def preprocess_data(input_files, output_path):
    try:
        # Merge datasets
        df_merged = merge_data(input_files)

        # Convert the 'begin_date' and 'end_date' columns to datetime
        df_merged['begin_date'] = pd.to_datetime(df_merged['begin_date'], errors='coerce')
        df_merged['end_date'] = df_merged['end_date'].replace('No', pd.NaT)  # Replace 'No' with NaT
        df_merged['end_date'] = pd.to_datetime(df_merged['end_date'], errors='coerce')

        # Convert the 'total_charges' column to float, replacing empty spaces with NaN
        df_merged['total_charges'] = pd.to_numeric(df_merged['total_charges'], errors='coerce')

        # Handle missing values
        internet_columns = ['internet_service', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
        df_merged[internet_columns] = df_merged[internet_columns].fillna('No')
        df_merged['multiple_lines'] = df_merged['multiple_lines'].fillna('No')

        # Drop rows with NaN in 'total_charges'
        df_merged.dropna(subset=['total_charges'], inplace=True)

        # Create the target variable based on the 'end_date' column
        df_merged['target'] = df_merged['end_date'].notna().astype(int)

        # Contract duration feature
        df_merged['contract_duration'] = (df_merged['end_date'] - df_merged['begin_date']).dt.days
        df_merged['contract_duration'].fillna((pd.to_datetime('2020-02-01') - df_merged['begin_date']).dt.days, inplace=True)

        # Average charges
        df_merged['average_charges'] = df_merged['total_charges'] / df_merged['contract_duration']

        # Charges per SeniorCitizen
        df_merged['monthly_charges_per_senior_citizen'] = df_merged['monthly_charges'] * df_merged['senior_citizen']
        df_merged['total_charges_per_senior_citizen'] = df_merged['total_charges'] * df_merged['senior_citizen']

        # High monthly charges feature
        df_merged['high_monthly_charges'] = (df_merged['monthly_charges'] > df_merged['monthly_charges'].median()).astype(bool)

        # Long-term contract feature
        df_merged['long_term_contract'] = (df_merged['contract_duration'] > 365).astype(bool)

        # Adjust binary column types to 'bool'
        df_merged['high_monthly_charges'] = df_merged['high_monthly_charges'].astype(bool)
        df_merged['long_term_contract'] = df_merged['long_term_contract'].astype(bool)

        # List of categorical columns
        categorical_columns = ['type', 'paperless_billing', 'payment_method', 'gender', 'partner',
                               'dependents', 'internet_service', 'online_security', 'online_backup',
                               'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies',
                               'multiple_lines', 'senior_citizen']

        # Encode categorical variables using One-Hot Encoding
        df_encoded = pd.get_dummies(df_merged, columns=categorical_columns, drop_first=True)

        # List of numerical columns to normalize
        numeric_features = ['monthly_charges', 'total_charges', 'contract_duration', 'average_charges',
                            'monthly_charges_per_senior_citizen', 'total_charges_per_senior_citizen']

        # Apply scaler to numerical columns
        scaler = StandardScaler()
        df_encoded[numeric_features] = scaler.fit_transform(df_encoded[numeric_features])

        # Move the 'target' column to the last position
        cols = list(df_encoded.columns)
        cols.append(cols.pop(cols.index('target')))
        df_encoded = df_encoded[cols]

        # Rename 'senior_citizen_1' to 'senior_citizen_Yes' for better understanding
        if 'senior_citizen_1' in df_encoded.columns:
            df_encoded.rename(columns={'senior_citizen_1': 'senior_citizen_Yes'}, inplace=True)

        # Save the preprocessed DataFrame to the specified path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_encoded.to_csv(output_path, index=False)
        print(f"Preprocessed dataset exported to: {output_path}")

    except Exception as e:
        print(f"Error during preprocessing: {e}")
        raise
