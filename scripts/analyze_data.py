import pandas as pd

def analyze_data(df):
    average_price = df['price'].mean()
    return average_price

if __name__ == "__main__":
    from load_data import load_data
    df = load_data()
    avg_price = analyze_data(df)
    print(f"Average Price: {avg_price}")
