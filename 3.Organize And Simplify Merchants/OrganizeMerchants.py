import pandas as pd
import json


df = pd.read_excel('MerchantsFinal.xlsx')
df.drop(df.columns[[0,1,2,4,6,7,8]], axis=1, inplace=True)
print(df)
df.to_excel('MerchantsOrganized.xlsx', sheet_name='Merchants', index=True)