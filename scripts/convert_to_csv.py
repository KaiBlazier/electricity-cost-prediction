import pandas as pd

def convert_excel_to_csv(excel_file, csv_file):
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    files = ['2019Usage', '2020Usage', '2021Usage', '2022Usage', '2023Usage']
    for file in files:
        convert_excel_to_csv(f'data/{file}.xlsx', f'data/{file}_converted.csv')

