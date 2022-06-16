from flask import Flask, redirect, render_template, url_for, request
from bs4 import BeautifulSoup
import os
import re
import requests
app = Flask(__name__)

url = 'https://www.pcschoolonline.com.tw/2017/introcourse.aspx?courseid=NEWClass6'

@app.route('/')
def index():
    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data1 = sp.select(".text05")
    return render_template('app01_01.html', sendDs=data1)  

@app.route('/index01')
def index01():
    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data1 = sp.select(".introPanel")    
    a=[]
    for headline in data1[0].find_all('div', {'class':'text05'}):
        a.append(headline.text)
    return render_template('app01_01.html', sendDs=a) 
  

@app.route('/index02')
def index02():
    APPLE_DAILY_HEADLINE = 'http://www.appledaily.com.tw/appledaily/hotdaily/headline'
    print('頻果今日焦點')
    resp = requests.get(APPLE_DAILY_HEADLINE).text
    soup = BeautifulSoup(resp, 'html.parser')
    a=[]   
    for headline in soup.find('ul', 'all').find_all('li'):
        a.append(headline.find('div', 'aht_title').text)
    return render_template('app01_01.html', sendDs=a)


@app.route('/index03')
def index03():
    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data1 = sp.select(".introPanel")    
    a=[]
    for headline in data1[12].find_all('div', {'class':'text05'}):
        a.append(headline.text)
    return render_template('app01_03.html', sendDs=a) 


@app.route('/index04',methods = ['GET','POST'])
def index04():
    if request.method == 'POST':
        html = requests.get(url).text
        sp = BeautifulSoup(html, 'html.parser')
        data1 = sp.select(".introPanel")    
        a=[]
        name=int(request.form.get('name'))
        for headline in data1[name].find_all('div', {'class':'text05'}):
            a.append(headline.text)
        return render_template('app01_04.html', sendDs=a)
        
    else:
        return render_template('app01_04.html')




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)