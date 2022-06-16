from flask import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, firestore, storage
import MySQLdb
from flask_session import Session
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = './static/'
cred=credentials.Certificate('xxxxxxx.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'xxxxxxx.appspot.com'})
app01 = firebase_admin.initialize_app(cred, {'storageBucket': 'xxxxxxx.appspot.com',}, name='storage')        
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
    user_id = request.form['user_id']
    if (user_id in users) and (request.form['password'] == users[user_id]['password']):
        user = User()
        user.id = user_id
        login_user(user)
        flash(f'{user_id}！歡迎您！')
        return redirect(url_for('from_start'))

    flash('登入失敗,請重新輸入')
    return render_template('index.html')


users = {'abc': {'password': '1234'}}

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message = '網頁不存在~ERROR'


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(user_id):
    if user_id not in users:
        return

    user = User()
    user.id = user_id
    return user


@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    if user_id not in users:
        return

    user = User()
    user.id = user_id


    user.is_authenticated = request.form['password'] == users[user_id]['password']

    return user



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("index.html")
    
    user_id = request.form['user_id']
    if (user_id in users) and (request.form['password'] == users[user_id]['password']):
        user = User()
        user.id = user_id
        login_user(user)
        flash(f'{user_id}！歡迎您！')
        return redirect(url_for('from_start'))

    flash('登入失敗,請重新輸入')
    return render_template('index.html')

@app.route('/logout')
def logout():
    user_id = current_user.get_id()
    logout_user()
    flash(f'{user_id}！歡迎下次再來！')
    return render_template('index.html') 

@app.route("/from_start")
@login_required
def from_start():
    #return render_template("getinfo.html")
    return redirect(url_for('getinfo'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        db = MySQLdb.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
        cursor = db.cursor()
        psort = request.form.get('psort')
        pname = request.form.get('pname')
        pmoney = request.form.get('pmoney')
        file = request.files['pimg']
        filename = file.filename
        #filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bucket = storage.bucket(app=app01)
        blob = bucket.blob('anysell/'+filename)
        blob.upload_from_filename(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        blob.make_public()
        fbimg=blob.public_url
        #pstorage='https://pcschool03.herokuapp.com/static/'+filename
        pstorage=fbimg
        sql ='INSERT INTO product(psort,pname,pmoney, pimg,pstorage) VALUES ("%s","%s", "%s", "%s","%s")' % (psort,pname,pmoney,filename,pstorage)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()                       
        return render_template('upload.html',okk='thanks')
    else:
        return render_template('upload.html')

@app.route('/getinfo')
@login_required
def getinfo():
    db = MySQLdb.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
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
@login_required
def delete_entry():
    if request.method=='POST':
        print(type(request.form['entry_id']))
        db = MySQLdb.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
        cursor = db.cursor()
        #myid=request.POST['pid']
        myid=request.form['entry_id']
        intmid=int(myid)
        myimg=request.form['entry_img']
        cursor.execute('DELETE FROM product WHERE pid =%s',(intmid,))
        db.commit()
        bucket = storage.bucket(app=app01)
        blob_name=myimg
        blob=bucket.blob('anysell/'+blob_name)
        blob.delete()
        print('blob{}deleted.'.format(blob_name))
        return redirect(url_for('getinfo'))
    else:
        return redirect(url_for('getinfo'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)    
    


