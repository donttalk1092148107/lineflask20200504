from urllib.parse import urlparse
#返回的6個部分：scheme(協議)、netloc(網路位置)、path(路徑)、params(路徑段引數)、query(查詢)、fragment(片段)
url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'
o = urlparse(url)
print(o) 

print("scheme={}".format(o.scheme))
print("netloc={}".format(o.netloc))
print("port={}".format(o.port))
print("path={}".format(o.path))
print("query={}".format(o.query))