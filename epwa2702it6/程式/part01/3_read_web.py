import requests
url = 'https://www.pcschool.com.tw/'
html = requests.get(url)
html.encoding="utf-8"
print(html.text)


htmllist = html.text.splitlines()
for row in htmllist:
   print(row)