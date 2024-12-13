import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(df):
    # Handle missing values
    df = df.dropna()

    # Feature engineering (if needed)
    # df['new_feature'] = df['existing_feature'] * 2

    return df

def split_data(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    file_path = 'data/your_data_file.csv'
    target_column = 'target_column_name'
    df = load_data(file_path)
    if df is not None:
        df = preprocess_data(df)
        X_train, X_test, y_train, y_test = split_data(df, target_column)
        print("Data loaded and split successfully.")
