import pandas as pd
import os

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    # Handle missing values
    df = df.dropna()  # Drop rows with missing values
    # Alternatively, you can fill missing values with a specific value or method
    # df = df.fillna(method='ffill')  # Forward fill

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert data types if necessary
    # For example, convert a column to datetime
    # df['date_column'] = pd.to_datetime(df['date_column'])

    # Rename columns for consistency
    df = df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))

    return df

def save_clean_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")

if __name__ == "__main__":
    data_dir = "data"
    target_files = ['2019Usage', '2020Usage', '2021Usage', '2022Usage', '2023Usage']
    for file_name in os.listdir(data_dir):
        if any(file_name.startswith(target) for target in target_files):
            file_path = os.path.join(data_dir, file_name.replace('.xlsx', '.csv'))
            df = load_data(file_path)
            if df is not None:
                cleaned_df = clean_data(df)
                output_file_path = file_path.replace('.csv', '_cleaned.csv')
                save_clean_data(cleaned_df, output_file_path)
