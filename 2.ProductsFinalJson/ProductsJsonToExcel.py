import pandas as pd
import json

ranges = ['1-50','51-100','101-150','151-200','201-250','251-300','301-350','351-400','401-450','451-500']
df= None

for i in range(len(ranges)):
    this_range = ranges[i]
    if i == 0:
        df = pd.read_json(f'Products{this_range}.json')
    else:
        this_df = pd.read_json(f'Products{this_range}.json')
        df = pd.concat([df, this_df], ignore_index=True, sort=False)

df.to_excel('ProductsFinal.xlsx', sheet_name='Merchants', index=False)