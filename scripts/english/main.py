import os
import sys
from preprocess_data import preprocess_data

if __name__ == "__main__":
    # Add the 'scripts' directory to the Python path
    sys.path.append(os.path.join(os.getcwd(), 'scripts'))

    # File paths and directories
    base_dir = os.path.join('data', 'raw')
    input_files = [
        os.path.join(base_dir, 'contract.csv'),
        os.path.join(base_dir, 'internet.csv'),
        os.path.join(base_dir, 'personal.csv'),
        os.path.join(base_dir, 'phone.csv')
    ]
    output_path = os.path.join('data', 'processed', 'processed_data.csv')

    # Execute preprocessing
    preprocess_data(input_files, output_path)
