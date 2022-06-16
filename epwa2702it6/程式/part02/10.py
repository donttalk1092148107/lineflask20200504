import matplotlib.pyplot as plt
import urllib.request
import json
import numpy as np

def get_Temperature(urlpath):
    dataurl01=urlpath
    content01=urllib.request.urlopen(dataurl01)
    datas01 = json.loads(content01.read().decode())
    point01=int(datas01['records']['location'][0]['weatherElement'][4]['time'][0]['parameter']['parameterName'])
    point02=int(datas01['records']['location'][0]['weatherElement'][4]['time'][1]['parameter']['parameterName'])
    point03=int(datas01['records']['location'][0]['weatherElement'][4]['time'][2]['parameter']['parameterName'])
    getT=[point01,point02,point03]
    return getT

taipei=get_Temperature('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82&sort=time')
kaohsiung=get_Temperature('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&format=JSON&locationName=%E9%AB%98%E9%9B%84%E5%B8%82&sort=time')

plt.subplot(2, 1, 1)
plt.plot([1,2,3], taipei, marker='o',mfc='green',mec='red',markersize=12)
plt.axis([0, 4, 20, 40])
plt.title('Taipei')
plt.ylabel('Temperature')

plt.subplot(2, 1, 2)
plt.plot([1,2,3], kaohsiung, marker='*',mec='red',ls='--',markersize=6)
plt.axis([0, 4, 20, 40])
plt.xlabel('Kaohsiung')
plt.ylabel('Temperature')

plt.show()
