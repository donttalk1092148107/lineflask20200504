from flask import *
import os
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, firestore, storage
import MySQLdb
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = './static/'
cred=credentials.Certificate('pcschoolline.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'pcschoolline.appspot.com'})
app01 = firebase_admin.initialize_app(cred, {'storageBucket': 'pcschoolline.appspot.com',}, name='storage')        
pstorage=''
@app.route("/")
def index():    
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        db = MySQLdb.connect("us-cdbr-east-06.cleardb.net", "b9d5e0986cfc58", "9e0c1166", "heroku_8002f92dacd4943", charset='utf8' )
        cursor = db.cursor()
        psort = request.form.get('psort')
        pname = request.form.get('pname')
        pmoney = request.form.get('pmoney')
        file = request.files['pimg']
        filename = file.filename
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bucket = storage.bucket(app=app01)
        blob = bucket.blob(filename)
        blob.upload_from_filename(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blob.make_public()
        fbimg=blob.public_url
        #print(fbimg)
        #pstorage='https://pcschool04.herokuapp.com/static/'+filename
        pstorage=fbimg
        sql ='INSERT INTO product(psort,pname,pmoney, pimg,pstorage) VALUES ("%s","%s", "%s", "%s","%s")' % (psort,pname,pmoney,filename,pstorage)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()                       
        return render_template('uploadF01.html',okk='thanks')
    else:
        return render_template('uploadF01.html')

@app.route('/getinfo')
def getinfo():
    db = MySQLdb.connect("us-cdbr-east-06.cleardb.net", "b9d5e0986cfc58", "9e0c1166", "heroku_8002f92dacd4943", charset='utf8' )
    cursor = db.cursor()
    sql ='SELECT * FROM product'
    try:
        cursor.execute(sql)
        U=cursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    return render_template('getinfo.html',u=U)

@app.route('/deletec',methods=['GET', 'POST'])
def delete_entry():
    if request.method=='POST':
        print(type(request.form['entry_id']))
        #MySQLdb.connect("主機", "帳號", "密碼", "default schema", charset='utf8' )
        db = MySQLdb.connect("us-cdbr-east-06.cleardb.net", "b9d5e0986cfc58", "9e0c1166", "heroku_8002f92dacd4943", charset='utf8' )
        cursor = db.cursor()
        #myid=request.POST['pid']
        myid=request.form['entry_id']
        intmid=int(myid)
        myimg=request.form['entry_img']
        print(myimg)
        cursor.execute('DELETE FROM product WHERE pid =%s',(intmid,))
        db.commit()
        bucket = storage.bucket(app=app01)
        blob_name=myimg
        blob=bucket.blob(blob_name)
        blob.delete()
        print('blob{}deleted.'.format(blob_name))
        return redirect(url_for('getinfo'))
    else:
        return redirect(url_for('getinfo'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)    
    


