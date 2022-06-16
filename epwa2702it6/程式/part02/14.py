import os,sys
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import requests
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
quote_page ='https://www.kingautos.net/236950'
#page = urllib.request.urlopen(quote_page)
#soup = BeautifulSoup(page, 'html.parser')
#name_box = soup.find('div', attrs={'class': 'datatable'})
res = requests.get(quote_page)
soup = BeautifulSoup(res.text, 'lxml')

tables = soup.select('table')
df_list = []
for table in tables:
    df_list.append(pd.concat(pd.read_html(table.prettify())))
df = pd.concat(df_list)
df.to_csv('aa.csv')

df01 = pd.read_csv("aa.csv",skiprows=2,skipfooter=19,dtype=str,encoding = 'utf8',engine='python')
print(df01)
###dfarea=df01[2:11]
carN=df01['品牌/集團']
carP=df01['2018總銷量(輛)']
print(carP)
labels = carN
sizes =carP
explode = (0.1,0,0,0,0,0,0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()
