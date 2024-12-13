import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from load_data import load_data, preprocess_data

def predict_future(df):
    # Preprocess data if needed
    df = preprocess_data(df)
    
    # Extract year and month from the date column
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['month'] = pd.to_datetime(df['date']).dt.month
    
    # Define features and target variable
    X = df[['year', 'month']]
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
    # Load data
    file_path = 'data/your_data_file.csv'
    df = load_data(file_path)
    
    # Predict future data
    if df is not None:
        future_data = predict_future(df)
        print(future_data)
