import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url = 'https://www.pcschoolonline.com.tw/2017/newbie1.aspx'


html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
data1 = sp.select(".footer2")

data2 = data1[0].find_all('div', {'class':'col-md-3 col-sm-12 text-center'})
for mydata in data2:
    print(mydata.text)

