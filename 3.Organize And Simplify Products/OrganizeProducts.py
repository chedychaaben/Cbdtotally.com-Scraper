import pandas as pd
import json


df = pd.read_excel('ProductsFinal.xlsx')
df.drop(df.columns[[0,2,3,5,7,9]], axis=1, inplace=True)
print(df)
df.to_excel('ProductsOrganized.xlsx', sheet_name='Merchants', index=True)