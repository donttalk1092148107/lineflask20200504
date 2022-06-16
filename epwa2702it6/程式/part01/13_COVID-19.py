import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url = 'https://www.worldometers.info/coronavirus/'


html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
fp = open("13_COVID-19.csv","wb")
tables = sp.find('table', {'id': 'main_table_countries_today'})
#print(tables)
columns = [th.text.replace('\n', '') for th in tables.find('tr').find_all('th')]
#print(columns)
trs = tables.find_all('tr')[1:]
rows = list()
for tr in trs:
    rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
print(rows[:5])
df = pd.DataFrame(data=rows, columns=columns)
print(df.head(100))

df.to_csv('Coronavirus.csv')
