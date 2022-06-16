from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
import urllib.request
import json
import numpy as np
app = Flask(__name__)
#https://developers.google.com/chart/interactive/docs/gallery/barchart?hl=zh-TW
dataurl01='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82&elementName=MinT&sort=time'

content01=urllib.request.urlopen(dataurl01)
datas01 = json.loads(content01.read().decode())
#print(datas01)
point01=int(datas01['records']['location'][0]['weatherElement'][0]['time'][0]['parameter']['parameterName'])
point02=int(datas01['records']['location'][0]['weatherElement'][0]['time'][1]['parameter']['parameterName'])
point03=int(datas01['records']['location'][0]['weatherElement'][0]['time'][2]['parameter']['parameterName'])



@app.route('/')
def index():
    return render_template('app01.html',point01=point01,point02=point02,point03=point03)







if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)