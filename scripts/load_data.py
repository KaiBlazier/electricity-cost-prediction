import pandas as pd

def load_data():
    data_files = ['data/2019Usage.csv', 'data/2020Usage.csv', 'data/2021Usage.csv', 'data/2022Usage', 'data/2023Usage.csv']
    dataframes = [pd.read_csv(file) for file in data_files]
    combines_df = pd.concat(dataframes)
    return combined_df

if __name__ == "__main__":
    df = load_data()
    print(df.head())