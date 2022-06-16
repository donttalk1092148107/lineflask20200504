from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app_07.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)