import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

url = 'https://svetoslavov.bg/%d1%86%d0%b5%d0%bd%d0%b8-%d0%bd%d0%b0-%d0%b4%d0%b8%d0%b7%d0%b5%d0%bb-%d0%bd%d0%b0-%d0%b5%d0%b4%d1%80%d0%be/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('div', class_='elementor-widget-container').find_all('em')
print(rows)

