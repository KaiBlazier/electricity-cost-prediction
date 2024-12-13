import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from load_data import load_data, preprocess_data
import os

def predict_future(df):
    # Preprocess data if needed
    df = preprocess_data(df)
    
    # Extract year and month from the date column
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['months'] = pd.to_datetime(df['date']).dt.months
    
    # Define features and target variable
    X = df[['year', 'months']]
    y = df['price']
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future dates for prediction
    future_months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='MS')
    future_data = pd.DataFrame({'year': future_months.year, 'month': future_months.month})
    
    # Predict future prices
    predicted_prices = model.predict(future_data)
    future_data['predicted_price'] = predicted_prices
    
    return future_data

if __name__ == "__main__":
    data_dir = "data"
    target_files = ['2019Usage', '2020Usage', '2021Usage', '2022Usage', '2023Usage']
    for file_name in os.listdir(data_dir):
        if any(file_name.startswith(target) for target in target_files):
            file_path = os.path.join(data_dir, file_name.replace('.xlsx', '.csv'))
            df = load_data(file_path)
            if df is not None:
                future_data = predict_future(df)
                print(f"Predicted future data for {file_name}:")
                print(future_data)

