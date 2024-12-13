import os
import pandas as pd

def convert_to_csv(file_path):
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format")
        
        csv_file_path = file_path.replace('.xlsx', '.csv')
        df.to_csv(csv_file_path, index=False)
        print(f"Converted {file_path} to {csv_file_path}")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    data_dir = "data"
    target_files = ['2019Usage', '2020Usage', '2021Usage', '2022Usage', '2023Usage']
    for file_name in os.listdir(data_dir):
        if any(file_name.startswith(target) for target in target_files):
            file_path = os.path.join(data_dir, file_name)
            convert_to_csv(file_path)

