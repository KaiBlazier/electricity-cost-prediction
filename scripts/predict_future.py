import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future(df):
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['month'] = pd.to_datetime(df['date']).dt.month
    X = df[['year', 'month']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    
    future_months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='MS')
    future_data = pd.DataFrame({'year': future_months.year, 'month': future_months.month})
    predicted_prices = model.predict(future_data)
    
    future_data['predicted_price'] = predicted_prices
    return future_data

if __name__ == "__main__":
    from load_data import load_data
    df = load_data()
    future_data = predict_future(df)
    print(future_data)
