import os
import sys
from preprocess_data import preprocess_data

if __name__ == "__main__":
    # Adicionar o diretório 'scripts' ao caminho do Python
    sys.path.append(os.path.join(os.getcwd(), 'scripts'))

    # Caminhos de arquivos e diretórios
    base_dir = os.path.join('data', 'raw')
    input_files = [
        os.path.join(base_dir, 'contract.csv'),
        os.path.join(base_dir, 'internet.csv'),
        os.path.join(base_dir, 'personal.csv'),
        os.path.join(base_dir, 'phone.csv')
    ]
    output_path = os.path.join('data', 'processed', 'processed_data.csv')

    # Executar o pré-processamento
    preprocess_data(input_files, output_path)
