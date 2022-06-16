from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
import urllib.request
import json
import numpy as np
app = Flask(__name__)
#https://developers.google.com/chart/interactive/docs/gallery/barchart?hl=zh-TW
def get_Temperature(urlpath):
    dataurl01=urlpath
    content01=urllib.request.urlopen(dataurl01)
    datas01 = json.loads(content01.read().decode())
    point01=int(datas01['records']['location'][0]['weatherElement'][4]['time'][0]['parameter']['parameterName'])
    point02=int(datas01['records']['location'][0]['weatherElement'][4]['time'][1]['parameter']['parameterName'])
    point03=int(datas01['records']['location'][0]['weatherElement'][4]['time'][2]['parameter']['parameterName'])
    getT=[point01,point02,point03]
    return getT





@app.route('/')
def index():
    taipei=get_Temperature('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82&sort=time')
    kaohsiung=get_Temperature('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&format=JSON&locationName=%E9%AB%98%E9%9B%84%E5%B8%82&sort=time')    
    return render_template('app02.html',taipei01=taipei[0],taipei02=taipei[1],taipei03=taipei[2]\
                         ,kaohsiung01=kaohsiung[0],kaohsiung02=kaohsiung[1],kaohsiung03=kaohsiung[2]   )







if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)