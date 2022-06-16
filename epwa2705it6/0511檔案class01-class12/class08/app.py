from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os

app=Flask(__name__)
Bootstrap(app)


@app.route('/form',methods = ['GET','POST'])
def hello_form():
    if request.method == 'POST':
        name=request.form.get('name')
        print(name)
        return render_template('form.html',name=name)
    else:
        return render_template('form.html')
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
