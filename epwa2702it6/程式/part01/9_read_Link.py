from bs4 import BeautifulSoup
import requests

url = 'https://www.pcschoolonline.com.tw/'
html = requests.get(url)
html.encoding="utf-8"

sp=BeautifulSoup(html.text,"html.parser")
links=sp.find_all("a")
for link in links:
    href=link.get("href")
    
    if  href != None and href.startswith("http://"): 
        print(href)