import requests
from bs4 import BeautifulSoup
import sqlite3

#尋找 “iphone 11 pro max”
url = 'https://tw.buy.yahoo.com/search/product?p=iphone%2011%20pro%20max'
conn = sqlite3.connect('01_yahoo.db')
c = conn.cursor()
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for asus in soup.find_all('li', {'class':'BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b'}):
    values = list(asus.stripped_strings)[0:2]
    c.execute('insert into yahoo_price(title, price) values (?, ?)', values)
    conn.commit()
    print(values)

conn.close()
