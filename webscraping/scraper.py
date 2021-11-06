import requests
import lxml
from bs4 import BeautifulSoup

#response = requests.get('https://ch.kompass.com/searchCompanies?acClassif=&localizationCode=CH_17_1721_3203&localizationLabel=St.+Gallen&localizationType=town&text=&searchType=SUPPLIER')
result = requests.get('https://ch.kompass.com/c/debrunner-koenig-ag/ch120311/')
src = result.content
soup = BeautifulSoup(src, 'lxml')

tag = soup.find_all('span', itemprop='streetAddress')
print(tag)
