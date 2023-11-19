import pandas as pd
import json, os

imagesInFolder = os.listdir(r'C:\Users\LENOVO\Desktop\Ben Brahem 30 USD Scraping Task\Protected Data\4.Download Products Images\ProductsImages')

df = pd.read_excel('Products.xlsx')
data = df['productImageUrl']

for i in range(len(data)):
    
    list_datas = str(data[i]).split('/')
    data[i] = list_datas[len(list_datas)-1]
    if data[i] == 'nan' or data[i] not in imagesInFolder:
        data[i] = ''
    else:
        data[i] = 'https://www.cbdtotally.com/img/ProductsImages/'+ data[i]
        
df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
print(df)
df.to_excel('NewProducts.xlsx', sheet_name='Products', index=False)