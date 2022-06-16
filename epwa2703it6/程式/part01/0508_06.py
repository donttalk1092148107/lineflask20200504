import requests
from bs4 import BeautifulSoup
import sqlite3
url = 'https://www.pcschoolonline.com.tw/2017/introcourse.aspx?courseid=NEWClass6'


conn = sqlite3.connect('02_myclass.db')
c = conn.cursor()
res = requests.get(url)
sp = BeautifulSoup(res.text, 'html.parser')

data1 = sp.select(".introPanel")
data2 = data1[0].find_all('div', {'class':'text05'})
#print(data2)

for mydata in data2:
    values = list(mydata.stripped_strings)[0:1]
    c.execute('insert into class(name) values (?)', values)
    conn.commit()
    print(values)

conn.close()