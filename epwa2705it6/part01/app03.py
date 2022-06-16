from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>這是index</h1>'   
 
@app.route('/login')
def login():
    return '<h1>這是login</h1>'

@app.route('/user/<username>')
def profile(username):
    return '<h1>{}\'s profile</h1>'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)