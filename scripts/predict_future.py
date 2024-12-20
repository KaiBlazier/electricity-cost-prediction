import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from load_data import load_data

def predict_future(df):
    # Print column names to verify
    print("Column names:", df.columns)
    
    # Handle non-finite values in the 'Year' and 'Months' columns
    df['Year'] = df['Year'].fillna(0).astype(int)
    df['Months'] = df['Months'].fillna(0).astype(int)
    
    # Ensure column name is correctly identified
    target_column = 'PricePerHour(Cents)'
    if target_column not in df.columns:
        raise KeyError(f"'{target_column}' not found in DataFrame columns: {df.columns.tolist()}")
    
    X = df[['Year', 'Months']]
    y = df[target_column]
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_months = pd.date_range(start='2024-01-01', end='2026-12-01', freq='MS')
    future_data = pd.DataFrame({'Year': future_months.year, 'Months': future_months.month})
    
    predicted_prices = model.predict(future_data)
    future_data['predicted_price'] = predicted_prices
    
    # Add new column for price per hour times 720
    future_data['price_per_month'] = future_data['predicted_price'] * 720
    
    return future_data

if __name__ == "__main__":
    df = load_data()
    future_data = predict_future(df)
    future_data.to_csv('data/future_predictions.csv', index=False)
    print(future_data)
