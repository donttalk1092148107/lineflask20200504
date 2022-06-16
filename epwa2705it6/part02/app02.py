from flask import Flask, redirect, render_template, url_for, request
from bs4 import BeautifulSoup
import os
import re
import requests
import os,sqlite3


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('Sqlite01.sqlite')
    cursor = conn.execute('select * from password')
    a=[]
    for row in cursor:
        a.append(row)
    conn.close()
    return render_template('app02_01.html', sendDs=a)       
    


@app.route('/input_data',methods = ['GET','POST'])
def input_data():
    if request.method == 'POST':
        conn = sqlite3.connect('Sqlite01.sqlite')
        name = request.form.get('name')
        pws= request.form.get('pass')
        sqlstr="insert into password values('{}','{}');".format(name,pws)
        conn.execute(sqlstr)
        conn.commit()
        conn.close()        
        return render_template('app02_02.html',okk='thanks')
    else:
        return render_template('app02_02.html')




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)