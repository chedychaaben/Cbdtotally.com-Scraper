from bs4 import BeautifulSoup
import sys 


# Configure
InputFile = f'Merchants{sys.argv[1]}.html'

paggination = InputFile[9:][:-5]
desiredOutPut = f'Merchants{paggination}.json'
print('Working on :' , paggination)
htmlFile = open(InputFile, mode='r', encoding='UTF-8')
soup = BeautifulSoup(htmlFile, features="html.parser")
#print(soup.prettify())
Results = soup.findAll("div", { "class" : "fullResult" })


ResultsJsonListOfObjects = []

for i in range(len(Results)):
    Result = Results[i]
    try:
        merchantImageUrl = Result.find('div', {'class':'mLogo'}).find('img')['src']
    except:
        merchantImageUrl = ''

    merchantPage = paggination
    merchantIndexInPage = i+1

    merchantName = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'org'}).find('a').contents[0]
    merchantId = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'merId'}).find('span').contents[0]
    merchantCatagory = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'catagory'}).contents[0]
    merchantWebsite = Result.find('div', {'class':'mGeneral'}).find('div', {'class':'www'}).find('a').contents[0]
    
    merchantPercentagePerSale = Result.find('div', {'class':'mCommKeyword'}).find('span', {'class':'merchantCommissionDisplayNumericValue'}).contents[0]
    merchantPowerRank = Result.find('div', {'class':'mCommKeyword'}).findAll('div', {'class':'stat'})[1].contents[0]
    merchantEPC = Result.find('div', {'class':'mCommKeyword'}).findAll('div', {'class':'stat'})[2].contents[0]
    
    #Cleaning merchantCatagory
    merchantCatagory = merchantCatagory.replace('\n', '').replace(' ', '')
    # Cleaning merchantPercentagePerSale
    merchantPercentagePerSale = merchantPercentagePerSale[:-1]
    # Cleaning merchantEPC
    merchantEPC = merchantEPC[1:]
    
    object = {
        'merchantImageUrl' : str(merchantImageUrl),
        'merchantPage' : str(merchantPage),
        'merchantIndexInPage' : str(merchantIndexInPage),
        'merchantName' : str(merchantName),
        'merchantId' : str(merchantId),
        'merchantCatagory' : str(merchantCatagory),
        'merchantWebsite' : str(merchantWebsite),
        'merchantPercentagePerSale' : str(merchantPercentagePerSale),
        'merchantPowerRank' : str(merchantPowerRank),
        'merchantEPC' : str(merchantEPC)
    }
    ResultsJsonListOfObjects.append(object)

# Outputting to json

import json

with open(desiredOutPut, "w", encoding='UTF-8') as data:
    json.dump(ResultsJsonListOfObjects, data, indent=4, sort_keys=True)

print('Done')