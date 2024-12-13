import pandas as pd

def load_data():
    data_files = ['data/2019Usage', 'data/2020Usage', 'data/2021Usage', 'data/2022Usage', 'data/2023Usage']
    dataframes = []
    for file in data_files:
        print(f"Loading file: {file}")
        df = pd.read_csv(file)
        dataframes.append(df)
    combined_df = pd.concat(dataframes)
    return combined_df

if __name__ == "__main__":
    df = load_data()
    print(df.head())

