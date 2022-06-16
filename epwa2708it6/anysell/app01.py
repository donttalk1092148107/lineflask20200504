from flask import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, firestore, storage
import MySQLdb
import random
from flask_session import Session

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    ImageSendMessage,URIAction,
    LocationMessage,
    ImagemapSendMessage,
    ImageCarouselColumn,
    ImageCarouselTemplate,Video,ExternalLink,
    ConfirmTemplate,PostbackAction,MessageAction,
    PostbackTemplateAction,FlexSendMessage,
    TemplateSendMessage, ButtonsTemplate, URITemplateAction,CarouselColumn,
    BaseSize,URIImagemapAction,MessageImagemapAction,ImagemapArea,CarouselTemplate
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bucket = storage.bucket(app=app01)
        blob = bucket.blob('anysell/'+filename)
        blob.upload_from_filename(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        blob.make_public()
        fbimg=blob.public_url
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


def getimginfo(getA):
    db = MySQLdb.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
    cursor = db.cursor()
    sql ="SELECT pstorage FROM product WHERE pid = '%s'"% getA
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        strR=list(results)
        return strR[0]
    except:
        print ("Error: unable to fecth data")
    db.close()


def getinfoRand(getA):
    db = MySQLdb.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
    cursor = db.cursor()
    sql ="SELECT * FROM product WHERE psort= '%s'"% getA
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        print(results)
        a=[]
        ra=[]
        myaa=''
        for row in results:
            arow=list(row)
            a.append(arow)
        ra=random.sample(a,3)            
        return ra
        
    except:
        print ("Error: unable to fecth data")
    db.close()



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    usern=profile.display_name
    
    #print(event)
    msg = event.message.text
    if msg=='上衣':
        myans=getinfoRand('上衣')
        mymessage = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=myans[0][5],
                        action=PostbackAction(
                            label=myans[0][2],
                            text=myans[0][2],
                            data='action=buy&itemid=1'
                            )
                        ),
                    ImageCarouselColumn(
                        image_url=myans[1][5],
                        action=PostbackAction(
                            label=myans[1][2],
                            text=myans[1][2],
                            data='action=buy&itemid=1'
                            )
                        ),
                    ImageCarouselColumn(
                        image_url=myans[2][5],
                        action=PostbackAction(
                            label=myans[2][2],
                            text=myans[2][2],
                            data='action=buy&itemid=1'
                            )
                        ), 
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, mymessage)
    elif msg=='裙子':
        myans=getinfoRand('裙子')
        line_bot_api.reply_message(event.reply_token,[
                                                      TextSendMessage(text=myans[0][2]),
                                                      ImageSendMessage(original_content_url=myans[0][5], preview_image_url=myans[0][5]),
                                                      TextSendMessage(text=myans[1][2]),
                                                      ImageSendMessage(original_content_url=myans[1][5], preview_image_url=myans[1][5]),
                                                     ])
    elif msg=='褲子':
        myans=getinfoRand('褲子')
        image_carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=myans[0][5],
                        title=myans[0][1],
                        text=myans[0][2],
                        actions=[
                            PostbackAction(label='褲子類', data='ping', text='褲子類'),
                            ]
                        ),
                    CarouselColumn(
                        thumbnail_image_url=myans[1][5],
                        title=myans[1][1],
                        text=myans[1][2],
                        actions=[
                            PostbackAction(label='褲子類', data='ping', text='褲子類'),
                            ]
                        ),
                    CarouselColumn(
                        thumbnail_image_url=myans[2][5],
                        title=myans[2][1],
                        text=myans[2][2],
                        actions=[
                            PostbackAction(label='褲子類', data='ping', text='褲子類'),
                            ]
                        )
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, image_carousel_template)
    elif msg=='尋問店家':
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='請留下您的問題及連絡方式，我們會盡快和您連絡')])
    elif msg=='門市訊息':
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='營業時間:全年無休，請電店家:(02)2382-6015')]) 
    else:
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='營業時間:全年無休，請電店家:(02)2382-6015')])  
      
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)