from flask import Flask, request, abort
import requests
import urllib.request
import os
import re
from bs4 import BeautifulSoup
import urllib.request
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,
    
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

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
        abort(400)
    return 'OK'



littleurl = "https://www.haagen-dazs.com.tw/products/olaf/"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0', }
littlehtml=requests.get(littleurl,headers=headers)
littlehtml.encoding = 'utf-8'
soup = BeautifulSoup(littlehtml.text, 'html.parser')
littleimg=soup.find('img')
littleh1=soup.find('h1')
littlemyp=soup.find('p')
littlemyr=littleimg['data-src']
littlesayh1= str(littleh1)
littlesaymyp = str(littlemyp)
b=''.join(littlesaymyp)
c=''.join(littlesayh1)
littlemypatn = re.sub('<[^<]+?>', '', b).replace('\n', '').strip()
littlemypatnh1 = re.sub('<[^<]+?>', '', c).replace('\n', '').strip()




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text
    if text=='11':   
        image_message = ImageSendMessage( original_content_url=littlemyr,preview_image_url=littlemyr)
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text=littlemypatnh1),TextSendMessage(text=littlemypatn),image_message])      
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='要選擇什麼蛋糕呢~'))




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
