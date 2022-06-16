from flask import Flask, redirect, render_template, url_for, request
import os
import pytesseract
import tempfile
from werkzeug.utils import secure_filename
from PIL import Image
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/'
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static')
line_bot_api = LineBotApi('Al/l03pu6nUd11ro6cFpLgR3hxm1thgTywNKyriQfrFdXo2GUA73WG947WFgnNmXwqQ5snb/B0hGmESwircJJGbI14WbZjt+Z7Uny5UmhxcDwJ3+9+Hq08WGodfRULM52/X8bTEt0HgakHNQMHUa1AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6faff680a90bd296c261a2cd2f78970d')

@app.route('/')
def index():
    image = Image.open(r'static/photo.jpeg')
    code = pytesseract.image_to_string(image)
    print(code)
    return render_template('index.html',codes=code)
    
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
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


# Other Message Type
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return
 
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)
    getImg=request.host_url + os.path.join('static', dist_name)

    image = Image.open(os.path.join('static', dist_name))
    code = pytesseract.image_to_string(image)
    
    print(code)
    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='-圖片轉文字為-'),
            TextSendMessage(text=code)            
        ])



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  