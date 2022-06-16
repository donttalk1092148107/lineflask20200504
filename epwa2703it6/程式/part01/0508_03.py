import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url = 'https://www.pcschoolonline.com.tw/2017/student_01_Announcement.aspx'


html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
fp = open("myClass.csv","wb")
tables = sp.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView2'})
columns = [th.text.replace('\n', '').replace('\r', '').replace('\,','') for th in tables.find('tr').find_all('th')]
trs = tables.find_all('tr')[1:]
rows = list()
for tr in trs:
    rows.append([td.text.replace('\n', '').replace('\r', '').replace(' ', '') for td in tr.find_all('td')])




print(rows[:5])
df = pd.DataFrame(data=rows[:3], columns=columns)
print(df.head(100))

df.to_csv('myClass.csv')