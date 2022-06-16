import os,sys
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
quote_page ='https://news.u-car.com.tw/article/49072/2019%e5%b9%b49%e6%9c%88%e4%bb%bd%e8%87%ba%e7%81%a3%e6%b1%bd%e8%bb%8a%e5%b8%82%e5%a0%b4%e9%8a%b7%e5%94%ae%e5%a0%b1%e5%91%8a'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#name_box = soup.find('div', attrs={'class': 'datatable'})


fp = open("info.csv","wb")
tables = soup.findAll('table')
tab = tables[2]
for tr in tab.findAll('tr'):
    text = tr.getText()+'\n'
    fp.write(text.encode())
    
##for tr in tab.findAll('tr'):
##    for td in tr.findAll('td'):
##        text = td.getText()
##        fp.write(text.encode())
        

fp.close()

data = np.genfromtxt("info.csv",delimiter = '%',dtype=str,skip_header=2,encoding = 'utf-8')
data01=data[0][2]
data02=data[1][2]
data03=data[2][2]
data04=data[3][2]
data05=data[4][2]
data06=data[5][2]
#print(data01,data02,data03,data04,data05,data06)
labels = 'Toyota', 'Honda', 'Nissan', 'Lexus','Mitsubishi','CMC'
sizes = [data01,data02,data03,data04,data05,data06]
explode = (0, 0.1, 0, 0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()
