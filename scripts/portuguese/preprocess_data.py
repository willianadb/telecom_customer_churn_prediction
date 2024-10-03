# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import re

def convert_to_snake_case(df):
    # Substitui espaços por underscores e converte letras maiúsculas para snake_case, ignorando abreviações como ID
    df.columns = [re.sub(r'(?<=[a-z])(?=[A-Z])', '_', col).replace(' ', '_').lower() for col in df.columns]
    return df

def merge_data(files_list):
    try:
        # Carregar e converter os nomes das colunas para snake_case
        df_contract = convert_to_snake_case(pd.read_csv(files_list[0]))
        df_personal = convert_to_snake_case(pd.read_csv(files_list[1]))
        df_internet = convert_to_snake_case(pd.read_csv(files_list[2]))
        df_phone = convert_to_snake_case(pd.read_csv(files_list[3]))

        # Mesclar os DataFrames
        df_merged = pd.merge(df_contract, df_personal, on='customer_id', how='left')
        df_merged = pd.merge(df_merged, df_internet, on='customer_id', how='left')
        df_merged = pd.merge(df_merged, df_phone, on='customer_id', how='left')

        return df_merged
    except Exception as e:
        print(f"Erro ao mesclar arquivos: {e}")
        raise

def preprocess_data(input_files, output_path):
    try:
        # Unir os datasets
        df_merged = merge_data(input_files)

        # Converter as colunas 'begin_date' e 'end_date' para o tipo datetime
        df_merged['begin_date'] = pd.to_datetime(df_merged['begin_date'], errors='coerce')
        df_merged['end_date'] = df_merged['end_date'].replace('No', pd.NaT)  # Substituir 'No' por NaT
        df_merged['end_date'] = pd.to_datetime(df_merged['end_date'], errors='coerce')

        # Converter a coluna 'total_charges' para float, substituindo espaços vazios por NaN
        df_merged['total_charges'] = pd.to_numeric(df_merged['total_charges'], errors='coerce')

        # Tratamento de valores ausentes
        internet_columns = ['internet_service', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
        df_merged[internet_columns] = df_merged[internet_columns].fillna('No')
        df_merged['multiple_lines'] = df_merged['multiple_lines'].fillna('No')

        # Excluir linhas com valores NaN em 'total_charges'
        df_merged.dropna(subset=['total_charges'], inplace=True)

        # Criar a variável alvo com base na coluna 'end_date'
        df_merged['target'] = df_merged['end_date'].notna().astype(int)

        # Feature de duração do contrato
        df_merged['contract_duration'] = (df_merged['end_date'] - df_merged['begin_date']).dt.days
        df_merged['contract_duration'].fillna((pd.to_datetime('2020-02-01') - df_merged['begin_date']).dt.days, inplace=True)

        # Média de cobranças mensais
        df_merged['average_charges'] = df_merged['total_charges'] / df_merged['contract_duration']

        # Cobranças mensais por SeniorCitizen
        df_merged['monthly_charges_per_senior_citizen'] = df_merged['monthly_charges'] * df_merged['senior_citizen']
        df_merged['total_charges_per_senior_citizen'] = df_merged['total_charges'] * df_merged['senior_citizen']

        # Feature de cobranças altas
        df_merged['high_monthly_charges'] = (df_merged['monthly_charges'] > df_merged['monthly_charges'].median()).astype(bool)

        # Feature de contrato de longo prazo
        df_merged['long_term_contract'] = (df_merged['contract_duration'] > 365).astype(bool)

        # Ajustar os tipos de colunas binárias para 'bool'
        df_merged['high_monthly_charges'] = df_merged['high_monthly_charges'].astype(bool)
        df_merged['long_term_contract'] = df_merged['long_term_contract'].astype(bool)

        # Lista das colunas categóricas
        categorical_columns = ['type', 'paperless_billing', 'payment_method', 'gender', 'partner',
                               'dependents', 'internet_service', 'online_security', 'online_backup',
                               'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies',
                               'multiple_lines', 'senior_citizen']

        # Codificar variáveis categóricas usando One-Hot Encoding
        df_encoded = pd.get_dummies(df_merged, columns=categorical_columns, drop_first=True)

        # Lista das colunas numéricas que queremos normalizar
        numeric_features = ['monthly_charges', 'total_charges', 'contract_duration', 'average_charges',
                            'monthly_charges_per_senior_citizen', 'total_charges_per_senior_citizen']

        # Aplicar o scaler nas colunas numéricas
        scaler = StandardScaler()
        df_encoded[numeric_features] = scaler.fit_transform(df_encoded[numeric_features])

        # Mover a coluna 'target' para a última posição
        cols = list(df_encoded.columns)
        cols.append(cols.pop(cols.index('target')))
        df_encoded = df_encoded[cols]

        # Renomear a coluna 'senior_citizen_1' para 'senior_citizen_Yes' para melhor entendimento
        if 'senior_citizen_1' in df_encoded.columns:
            df_encoded.rename(columns={'senior_citizen_1': 'senior_citizen_Yes'}, inplace=True)

        # Salvar o DataFrame pré-processado no caminho especificado
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_encoded.to_csv(output_path, index=False)
        print(f"Conjunto de dados pré-processado exportado para: {output_path}")

    except Exception as e:
        print(f"Erro durante o pré-processamento: {e}")
        raise
