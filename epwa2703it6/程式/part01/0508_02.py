import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url = 'https://www.pcschoolonline.com.tw/2017/introcourse.aspx?courseid=NEWClass6'


html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select(".introPanel")
data2 = data1[12].find_all('div', {'class':'text05'})
#print(data2)



for mydata in data2:
    print(mydata.text)
