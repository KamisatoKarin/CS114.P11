import pandas as pd
import sys
import csv

input_data = sys.stdin.read()
lines = input_data.splitlines()

usecols = ['CustomerID', 'InvoiceDate']
reader = csv.DictReader(lines)
data = [{col: row[col] for col in usecols} for row in reader]

df = pd.DataFrame(data)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df = df[pd.to_numeric(df['CustomerID'], errors='coerce').notnull()]
df['CustomerID'] = df['CustomerID'].astype(float)

last_purchase = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
min_purchase_date = last_purchase['InvoiceDate'].min()
last_purchase['score'] = (last_purchase['InvoiceDate'] - min_purchase_date).dt.days

output_data = last_purchase[['CustomerID', 'score']]
sys.stdout.write(output_data.to_string(index=False, justify='right'))