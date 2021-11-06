import requests
from bs4 import BeautifulSoup

#response = requests.get('https://ch.kompass.com/searchCompanies?acClassif=&localizationCode=CH_17_1721_3203&localizationLabel=St.+Gallen&localizationType=town&text=&searchType=SUPPLIER')
result = requests.get('https://ch.kompass.com/c/debrunner-koenig-ag/ch120311/', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})
src = result.content
soup = BeautifulSoup(src, 'html.parser')

tag = soup.find_all('span', class_='spRight')
#print(tag)
