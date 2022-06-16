from flask import Flask, request, abort
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
#https://developers.line.biz/en/docs/messaging-api/using-quick-reply/#introduction

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text
    if text=='11':
        text_message = TextSendMessage(text='今日吃什麼好',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="a1", text="a1"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                                   QuickReplyButton(action=LocationAction(type="location",label="a2")),
                                   QuickReplyButton(action=CameraAction(label="camera", text="a3")),
                                   QuickReplyButton(action=CameraRollAction(label="camera roll", text="a4")),
                                   QuickReplyButton(action=DatetimePickerAction(label="Select date",data="storeId=12345",mode="datetime",initial="2020-05-01t00:00",max="2020-05-30t23:59",min="2020-05-01t00:00")),
                                   QuickReplyButton(action=MessageAction(label="a6", text="a6"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                                    QuickReplyButton(action=MessageAction(label="a7", text="a7"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                                    QuickReplyButton(action=MessageAction(label="a8", text="a8"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                                    QuickReplyButton(action=MessageAction(label="a9", text="a9"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                                    QuickReplyButton(action=MessageAction(label="a10", text="a10"),image_url = 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg'),
                               ]))
                              
        line_bot_api.reply_message(event.reply_token,text_message)  
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='hihihi'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  