# Co su dung chatgpt de xu ly output sang pd.dataframe(line14), xu ly phan groupby(line10)
# Hoi copilot ve cach in output dung dinh dang file output1.txt (line15)
import pandas as pd
import sys

use_cols = ['CustomerID', 'InvoiceDate']
df = pd.read_csv(sys.stdin, usecols=use_cols, encoding='unicode_escape', encoding_errors='replace')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

last_purchase = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
min_purchase_date = last_purchase['InvoiceDate'].min()
last_purchase['score'] = (last_purchase['InvoiceDate'] - min_purchase_date).dt.days

output_data = last_purchase[['CustomerID', 'score']]
sys.stdout.write(output_data.to_string(index=False, header = True, justify='right'))