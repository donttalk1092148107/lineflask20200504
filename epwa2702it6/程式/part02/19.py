import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.dcard.tw/f/food')
if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'html.parser')
  stories = soup.find_all('h2', class_='sc-1v1d5rx-2 kZjhSU')
  for s in stories:
    print("標題：" + s.text)

