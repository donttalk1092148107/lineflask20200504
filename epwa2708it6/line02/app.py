from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from firebase import firebase
firebase = firebase.FirebaseApplication('https://xxxxxxx.firebaseio.com/',None)
import os
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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print(event)
    text=event.message.text
    if (text=="溫度"):
        global firebase
        Temperature = firebase.get('/Temperature',None)
        if Temperature>=30:
            buttons_template = TemplateSendMessage(
            alt_text='溫度',
            template=ButtonsTemplate(
                title='現在溫度:'+str(Temperature)+'度',
                text='溫度過高，記得多喝水',
                thumbnail_image_url='https://i.imgur.com/GZaK9yz.jpg',
                actions=[
                    MessageTemplateAction(
                        label='想查尋濕度嗎?',
                        text='濕度'
                    )                    
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template)
        elif Temperature<=29 and Temperature >=18 :
            buttons_template = TemplateSendMessage(
            alt_text='溫度',
            template=ButtonsTemplate(
                title='現在溫度:'+str(Temperature)+'度',
                text='溫度適中，記得多喝水',
                thumbnail_image_url='https://i.imgur.com/8tcjJVz.jpg',
                actions=[
                    MessageTemplateAction(
                        label='想查尋濕度嗎?',
                        text='濕度'
                    )                    
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template)
        else:
            buttons_template = TemplateSendMessage(
            alt_text='溫度',
            template=ButtonsTemplate(
                title='現在溫度:'+str(Temperature)+'度',
                text='溫度寒冷，記得保暖',
                thumbnail_image_url='https://i.imgur.com/yDpvjWc.jpg',
                actions=[
                    MessageTemplateAction(
                        label='想查尋濕度嗎?',
                        text='濕度'
                    )                    
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template)
    elif(text=="濕度"):
        Humidity = firebase.get('/Humidity',None)
        if Humidity>50:
            buttons_template = TemplateSendMessage(
            alt_text='濕度',
            template=ButtonsTemplate(
                title='現在濕度:'+str(Humidity)+'度',
                text='濕度過高，爆炸前記得多喝水',
                thumbnail_image_url='https://i.imgur.com/RhNHbxg.jpg',
                actions=[
                    MessageTemplateAction(
                        label='想查尋溫度嗎?',
                        text='溫度'
                    )                    
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template)
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='現在濕度:'+str(Humidity)+'度'))       
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='輸入「溫度 or 濕度」'))
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
