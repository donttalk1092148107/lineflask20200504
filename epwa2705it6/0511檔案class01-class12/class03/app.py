from flask import Flask
import os
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world!!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,{}!</h1>'.format(name)
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
