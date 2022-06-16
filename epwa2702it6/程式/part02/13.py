import os,sys
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import requests


quote_page ='https://auto.ltn.com.tw/news/8556/2/2'
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

df01 = pd.read_csv("aa.csv",skiprows=1,skipfooter=7,dtype=str,encoding = 'utf-8',engine='python')
#dfarea=df01[2:11]
carN=df01['車款']
carP=df01['銷售量']
print(carP)
labels = carN
sizes =carP
explode = (0.1,0,0,0,0,0,0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()
