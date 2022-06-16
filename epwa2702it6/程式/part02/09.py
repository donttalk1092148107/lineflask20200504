import matplotlib.pyplot as plt
import urllib.request
import json
import numpy as np

dataurl01='https://opendata.cwb.gov.tw/api/v1/rest/datastore/\
F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE\
&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82&sort=time'

content01=urllib.request.urlopen(dataurl01)
datas01 = json.loads(content01.read().decode())
#print(datas01)
point01=int(datas01['records']['location'][0]['weatherElement'][4]['time'][0]['parameter']['parameterName'])
point02=int(datas01['records']['location'][0]['weatherElement'][4]['time'][1]['parameter']['parameterName'])
point03=int(datas01['records']['location'][0]['weatherElement'][4]['time'][2]['parameter']['parameterName'])




plt.plot([1,2,3], [point01,point02,point03], 'ro')
plt.axis([0, 5, 20, 50])
#print(point01,point02,point03)
plt.show()

