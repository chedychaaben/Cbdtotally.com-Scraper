from bs4 import BeautifulSoup
import sys 


# Configure
InputFile = f'Products{sys.argv[1]}.html'

paggination = InputFile[8:][:-5]
desiredOutPut = f'Products{paggination}.json'
print('Working on :' , paggination)
htmlFile = open(InputFile, mode='r', encoding='UTF-8')
soup = BeautifulSoup(htmlFile, features="html.parser")
#print(soup.prettify())
Results = soup.findAll("div", { "class" : "fullResult" })


ResultsJsonListOfObjects = []

for i in range(len(Results)):
    Result = Results[i]
    try:
        productImageUrl = Result.find('div', {'class':'mLogo'}).find('img')['src']
    except:
        productImageUrl = ''
    
    productPage = paggination
    productIndexInPage = i+1

    productName = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'org'}).contents[0]
    productSku = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'sku'}).contents[1]
    productPrice = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'price'}).contents[0]
    productEstimatedPrice = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'cookie'}).contents[0]
    productMerchantName = Result.find('div', {'class':'prodmer'}).find('div', {'class':'org'}).find('a').contents[0]
    productMerchantId = Result.find('div', {'class':'prodmer'}).find('div', {'class':'merId'}).find('span').contents[0]
    productMerchantSite = Result.find('div', {'class':'prodmer'}).find('div', {'class':'www'}).find('a').contents[0]
    
    # Cleaning Price
    productPrice = productPrice[8:]
    # Cleaning Estimated Price
    productEstimatedPrice = productEstimatedPrice[6:][:-9]

    object = {
        'productImageUrl' : str(productImageUrl),
        'productPage' : str(productPage),
        'productIndexInPage' : str(productIndexInPage),
        'productName' : str(productName),
        'productSku' : str(productSku),
        'productPrice' : str(productPrice),
        'productEstimatedPrice' : str(productEstimatedPrice),
        'productMerchantName' : str(productMerchantName),
        'productMerchantId' : str(productMerchantId),
        'productMerchantSite' : str(productMerchantSite)
    }
    ResultsJsonListOfObjects.append(object)

# Outputting to json

import json

with open(desiredOutPut, "w", encoding='UTF-8') as data:
    json.dump(ResultsJsonListOfObjects, data, indent=4, sort_keys=True)

print('Done')