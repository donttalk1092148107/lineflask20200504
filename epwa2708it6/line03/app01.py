from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
import urllib.request
import json
import numpy as np
app = Flask(__name__)


def get_Temperature(mycity):    
    dataurl='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&elementName=MaxT'
    content=urllib.request.urlopen(dataurl)
    datas = json.loads(content.read().decode())
    
    if mycity=='嘉義縣':
        point=int(datas['records']['location'][0]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新北市':
        point=int(datas['records']['location'][1]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='嘉義市':
        point=int(datas['records']['location'][2]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新竹縣':
        point=int(datas['records']['location'][3]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新竹市':
        point=int(datas['records']['location'][4]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺北市':
        point=int(datas['records']['location'][5]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺南市':
        point=int(datas['records']['location'][6]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='宜蘭縣':
        point=int(datas['records']['location'][7]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='苗栗縣':
        point=int(datas['records']['location'][8]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='雲林縣':
        point=int(datas['records']['location'][9]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='花蓮縣':
        point=int(datas['records']['location'][10]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺中市':
        point=int(datas['records']['location'][11]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺東縣':
        point=int(datas['records']['location'][12]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    else:
        point=int(datas['records']['location'][0]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point


@app.route('/')
def index():
    return render_template('app01.html',myget=get_Temperature('臺北市'))







if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)