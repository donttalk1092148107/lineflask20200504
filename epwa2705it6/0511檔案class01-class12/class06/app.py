from flask import Flask, render_template

import os
app=Flask(__name__)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    #return render_template('user.html',name=None)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
