import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url = 'https://www.pcschoolonline.com.tw/2017/introcourse.aspx?courseid=NEWClass6'

html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
data1 = sp.select(".text05")
#print(data1)

for mydata in data1:
    print(mydata.text)
