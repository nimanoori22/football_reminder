from selenium import webdriver as wd
from bs4 import BeautifulSoup as  bs
import time
driver = wd.Chrome('path_to_driver')

driver.get('https://varzesh3.com')
time.sleep(1)
page = driver.page_source

soup = bs(page, 'html.parser')

table = soup.select('#widget21')

for item in table:
    team = item.find_all('td', {'class': 'text-center'})
    print(team)