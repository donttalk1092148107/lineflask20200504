import psycopg2
from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)

database="d22lt2rkasaf2d"
user="uonrecelbyjgcj"
password="9201b61af6dd39ae37cb7e9f62408bae516a7597b29c6102340374b1ff3550a1"
host="ec2-54-81-37-115.compute-1.amazonaws.com"
port="5432"
@app.route('/')
def index():
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    cur.execute("select *  from company")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html',getinfos=rows)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        mid = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        salary = request.form.get('salary')
        cur.execute("insert into company (id,name,age, address, salary) VALUES (%s, %s, %s, %s,%s);", (mid, name, age, address,salary))
        conn.commit()
        conn.close()                 
        return render_template('upload.html',okk='thanks')
    else:
        return render_template('upload.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


    