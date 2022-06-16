from flask import Flask, render_template

import os
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/user01/<name>')
def user01(name):
    return render_template('user01.html',name=name)    

@app.route('/user02')
def user02():
    users02 = [{"username": "超人一號", "url": "https://www.pcschool.com.tw"},
         {"username": "超人二號", "url": "https://www.pcschool.com.tw"}]
    return render_template('user02.html',users=users02)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
