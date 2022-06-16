from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
from markupsafe import Markup
app = Flask(__name__)


def show_the_login_form(getusername):
    return '<h1>Hello~{}</h1>'.format(getusername)


@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        mypws=request.values['pws']
        if mypws=='1234':
            result = Markup('<span style="color: green;">PASS</span>')
            return show_the_login_form(result)
        else:
            result = Markup('<span style="color: red;">FAIL</span>')
            return show_the_login_form(result)
    else:
        return "<form method='POST' action='/login'><input type='text' name='pws' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)