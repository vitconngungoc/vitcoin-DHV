import pandas as pd
from pathlib import Path

file_path = Path('dirty_cafe_sales.csv')
print('exists', file_path.exists())

trash_values = ['ERROR', 'UNKNOWN', 'Unknown', 'error', 'unknown', 'nan', 'NaN']

def clean_cafe_data(file_path):
    df = pd.read_csv(file_path, na_values=trash_values)
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce', format='mixed')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
    df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
    df['Item'] = df['Item'].astype(str).str.strip().str.title()
    df['Payment Method'] = df['Payment Method'].astype(str).str.strip().str.title()
    df['Location'] = df['Location'].astype(str).str.strip().str.title()
    df = df.drop_duplicates(subset=['Transaction ID'], keep='first')
    df['Quantity'] = df.groupby('Item')['Quantity'].transform(lambda x: x.fillna(x.median()))
    df['Price Per Unit'] = df.groupby('Item')['Price Per Unit'].transform(lambda x: x.fillna(x.median()))
    df['Total Spent'] = df['Total Spent'].fillna(df['Quantity'] * df['Price Per Unit'])
    df['Transaction Date'] = df['Transaction Date'].ffill()
    df['Item'] = df['Item'].replace('Nan', 'Unspecified')
    df['Payment Method'] = df['Payment Method'].replace('Nan', 'Not Specified')
    df['Location'] = df['Location'].replace('Nan', 'Unknown')
    return df

_df = clean_cafe_data(file_path)
print('clean shape', _df.shape)
print('nulls after', _df.isnull().sum().to_dict())
print('duplicate transaction ids', _df['Transaction ID'].duplicated().sum())
