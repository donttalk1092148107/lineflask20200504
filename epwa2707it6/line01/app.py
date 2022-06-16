from flask import Flask, request, abort
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage,
    VideoSendMessage, AudioSendMessage, LocationSendMessage ,ImagemapSendMessage,
    BaseSize, Video, ImagemapArea, ExternalLink, URIImagemapAction, MessageImagemapAction,
    TemplateSendMessage,ButtonsTemplate, MessageAction, PostbackAction, URIAction,
    CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn,
    FlexSendMessage, BubbleContainer, ImageComponent, QuickReply, QuickReplyButton,
    ConfirmTemplate,
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#https://github.com/line/line-bot-sdk-python
#https://github.com/line/line-bot-sdk-python#message-objects
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg=='貼圖':
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=11539, sticker_id=52114117))
    elif msg=='1':
        text_message = TextSendMessage(text='Hello, world')
        line_bot_api.reply_message(event.reply_token,text_message)
    elif msg=='2':
        image_message = ImageSendMessage(original_content_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
        preview_image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif msg=='3':
        video_message = VideoSendMessage(original_content_url='https://www.desen.com.tw/pcschoolonline.mp4',
        preview_image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg')
        line_bot_api.reply_message(event.reply_token,video_message)
    elif msg=='4':
        audio_message = AudioSendMessage(original_content_url='https://www.desen.com.tw/pcschoolonline.mp4',duration=240000)
        line_bot_api.reply_message(event.reply_token,audio_message)
    elif msg=='5':
        location_message = LocationSendMessage(title='台北認證', address='台北市中正區公園路30號3F',
         latitude=25.044603, longitude=121.516779)
        line_bot_api.reply_message(event.reply_token,location_message)
    elif msg=='6':
        sticker_message = StickerSendMessage(package_id='11537',sticker_id='52002745')
        line_bot_api.reply_message(event.reply_token,sticker_message)
    elif msg=='7':
        imagemap_message = ImagemapSendMessage(
    base_url='https://i.imgur.com/Ytz67R7.jpg',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://www.pcschoolonline.com.tw',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)

        line_bot_api.push_message(event.source.user_id, imagemap_message)
    elif msg=='8':
        buttons_template_message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackAction(
                label='postback',
                display_text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            ),
            URIAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
        line_bot_api.push_message(event.source.user_id, buttons_template_message)
    elif msg=='9':
        confirm_template_message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackAction(
                label='postback',
                display_text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            )
        ]
    )
)   
        line_bot_api.push_message(event.source.user_id, confirm_template_message)
    elif msg=='10':
        carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message1',
                        text='message text1'
                    ),
                    URIAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageAction(
                        label='message2',
                        text='message text2'
                    ),
                    URIAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
        line_bot_api.push_message(event.source.user_id, carousel_template_message)   
    elif msg=='11':
        image_carousel_template_message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
                action=PostbackAction(
                    label='postback1',
                    display_text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
                action=PostbackAction(
                    label='postback2',
                    display_text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
        line_bot_api.push_message(event.source.user_id, image_carousel_template_message)   
    elif msg=='12':
        flex_message = FlexSendMessage(
    alt_text='hello',
    contents=BubbleContainer(
        direction='ltr',
        hero=ImageComponent(
            url='https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
            size='full',
            aspect_ratio='20:13',
            aspect_mode='cover',
            action=URIAction(uri='http://example.com', label='label')
        )
    )
)
        line_bot_api.push_message(event.source.user_id, flex_message)  
    elif msg=='13':
        flex_message = FlexSendMessage(
    alt_text='hello',
    contents={
        'type': 'bubble',
        'direction': 'ltr',
        'hero': {
            'type': 'image',
            'url': 'https://www.pcschoolonline.com.tw/updimg/Teacher/Teacher_a001.jpg',
            'size': 'full',
            'aspectRatio': '20:13',
            'aspectMode': 'cover',
            'action': { 'type': 'uri', 'uri': 'http://example.com', 'label': 'label' }
        }
    }
)
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif msg=='14':
        text_message = TextSendMessage(text='Hello, world',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="label", text="text"))
                               ]))
        line_bot_api.reply_message(event.reply_token,text_message)                       
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)  
