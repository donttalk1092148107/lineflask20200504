from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape
import requests
import urllib.request
import json
import numpy as np

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

def get_Temperature(mycity):    
    dataurl='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8EAE6282-6B0A-43EF-A9C6-E4A9B4256CCE&elementName=MaxT'
    content=urllib.request.urlopen(dataurl)
    datas = json.loads(content.read().decode())
    
    if mycity=='嘉義縣':
        point=int(datas['records']['location'][0]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新北市':
        point=int(datas['records']['location'][1]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='嘉義市':
        point=int(datas['records']['location'][2]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新竹縣':
        point=int(datas['records']['location'][3]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='新竹市':
        point=int(datas['records']['location'][4]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺北市':
        point=int(datas['records']['location'][5]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺南市':
        point=int(datas['records']['location'][6]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='宜蘭縣':
        point=int(datas['records']['location'][7]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='苗栗縣':
        point=int(datas['records']['location'][8]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='雲林縣':
        point=int(datas['records']['location'][9]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='花蓮縣':
        point=int(datas['records']['location'][10]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺中市':
        point=int(datas['records']['location'][11]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    elif mycity=='臺東縣':
        point=int(datas['records']['location'][12]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point
    else:
        point=int(datas['records']['location'][0]['weatherElement'][0]['time'][2]['parameter']['parameterName'])
        return point


@app.route('/')
def index():
    return render_template('app01.html',myget=get_Temperature('臺北市'))



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
    msg = event.message.text
    if msg=='嘉義縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('嘉義縣')))
    elif msg=='新北市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('新北市')))
    elif msg=='嘉義市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('嘉義市')))
    elif msg=='新竹縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('新竹縣')))
    elif msg=='新竹市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('新竹市')))
    elif msg=='臺北市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('臺北市')))
    elif msg=='臺南市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('臺南市')))
    elif msg=='宜蘭縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('宜蘭縣')))
    elif msg=='苗栗縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('苗栗縣')))
    elif msg=='雲林縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('雲林縣')))
    elif msg=='花蓮縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('花蓮縣')))
    elif msg=='臺中市':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('臺中市')))
    elif msg=='臺東縣':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=get_Temperature('臺東縣')))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='-三十六小時天氣預報-目前提供[嘉義縣][新北市][嘉義市][新竹縣][新竹市][臺北市][臺南市][宜蘭縣][苗栗縣][雲林縣][花蓮縣][臺中市][臺東縣]'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)