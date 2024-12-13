import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def analyze_data(df):
    # Summary statistics
    print("Summary Statistics:")
    print(df.describe())

    # Visualize data
    plt.figure(figsize=(10, 6))
    sns.histplot(df['column_name'], kde=True)
    plt.title('Distribution of Column Name')
    plt.xlabel('Column Name')
    plt.ylabel('Frequency')
    plt.show()

    # Identify trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='date_column', y='value_column')
    plt.title('Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

if __name__ == "__main__":
    data_dir = "data"
    target_files = ['2019Usage', '2020Usage', '2021Usage', '2022Usage', '2023Usage']
    for file_name in os.listdir(data_dir):
        if any(file_name.startswith(target) for target in target_files):
            file_path = os.path.join(data_dir, file_name.replace('.xlsx', '.csv'))
            df = load_data(file_path)
            if df is not None:
                analyze_data(df)

