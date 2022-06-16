from flask import Flask, redirect, render_template, url_for, request
from werkzeug.utils import secure_filename
from markupsafe import escape
import requests
from markupsafe import Markup
import os
app = Flask(__name__)

def show_the_login_form(getusername):
    return '<h1>Hello~{}-成功存入-</h1>'.format(getusername)

@app.route('/login', methods=['GET', 'POST']) 
def login():
    error = None
    if request.method == 'POST':
        if request.values['username']=='abc' and request.values['password']=='1234':
            f = request.files['the_file']
            filename=secure_filename(f.filename)
            f.save('static/'+ filename)
            return show_the_login_form(request.values['username'])
        else:
            return 'Invalid username/password'
    else:
        return "<form method='POST' action='/login' enctype='multipart/form-data'><input type='text' name='username' />" \
            "</br><input type='text' name='password' /></br><input type='file' name='the_file'>" \
           "<button type='submit'>Submit</button></form>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)