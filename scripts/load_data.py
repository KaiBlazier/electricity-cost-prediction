import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    data_files = ['data/2019Usage_converted.csv', 'data/2020Usage_converted.csv', 'data/2021Usage_converted.csv', 'data/2022Usage_converted.csv', 'data/2023Usage_converted.csv']
    dataframes = []
    for file in data_files:
        print(f"Loading file: {file}")
        df = pd.read_csv(file)
        dataframes.append(df)
    combined_df = pd.concat(dataframes)
    return combined_df

def split_data(df, target_column):
    if target_column not in df.columns:
        raise KeyError(f"'{target_column}' not found in DataFrame columns: {df.columns.tolist()}")
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    target_column = 'PricePerHour(cents)'  # Replace with your actual target column name
    X_train, X_test, y_train, y_test = split_data(df, target_column)
    print(f"Training data shape: {X_train.shape}, {y_train.shape}")
    print(f"Test data shape: {X_test.shape}, {y_test.shape}")
