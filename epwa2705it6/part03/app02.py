from flask import *
import os

from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    return render_template('app_02.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)