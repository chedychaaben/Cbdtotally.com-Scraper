import pandas as pd
import json, requests, os

from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False


df = pd.read_excel('MerchantsOrganized.xlsx')

for image_url in df['merchantImageUrl']:
    image_url = str(image_url)
    url_texts = image_url.split('/')
    image_name = url_texts[len(url_texts)-1]


    if is_url(image_url):
        if not os.path.exists(image_name):
            img_data = requests.get(image_url).content
            with open(image_name, 'wb') as handler:
                handler.write(img_data)