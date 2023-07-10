# determine if nyse is open now
# import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
service = Service(binary_path)
dvr = webdriver.Chrome(service=service, options=options)
url = 'https://www.tradinghours.com/open?'
dvr.get(url)

# response = requests.get('https://www.tradinghours.com/open?')
# print(response)
soup = BeautifulSoup(dvr.page_source, 'lxml')
# print(soup.prettify())
market_status_element = soup.find(
    'main', attrs={'role': 'main'}
).find(
    'div', attrs={'class': 'container'}
).find(
    'p', attrs={'class': 'display-6 text-center my-5 font-weight-bold'}
).find(
    'span', attrs={'class': 'text-open font-weight-bold'}
).find('u'
)

market_status = market_status_element.text.strip()
print(market_status == 'Yes')