import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")
data2=data1[0].select(".contents_box02")[2]

print(data2.text)

#data2 = data1[0].find('div', {'class':'contents_box02'})
#data12 = data1[0].data11[0]

#print(data12)

#data3 = data2.find_all('div', {'class':'ball_tx'})
#print(data3)