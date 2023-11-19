import pandas as pd
import json


df = pd.read_excel('Merchants.xlsx')
data = df['merchantImageUrl']

for i in range(len(data)):
    
    list_datas = str(data[i]).split('/')
    data[i] = list_datas[len(list_datas)-1]
    if data[i] == 'nan':
        data[i] = ''
    else:
        data[i] = 'https://www.cbdtotally.com/img/MerchantsImages/'+ data[i]
        
df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
print(df)

df.to_excel('NewMerchants.xlsx', sheet_name='Merchants', index=False)