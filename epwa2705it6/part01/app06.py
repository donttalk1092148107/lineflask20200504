from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>這是index</h1>' 

def show_the_login_form(getusername):
    return 'Hello~ '+getusername

@app.route('/login', methods=['GET', 'POST']) 
def login():
    #if request.method == 'GET': 
    #    return 'Hello GET'

    if request.method == 'POST':
        myusername=request.values['username']
        return show_the_login_form(myusername)
        
        
    else:
        return "<form method='POST' action='/login'><input type='text' name='username' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)