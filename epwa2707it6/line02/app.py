from flask import Flask, request, abort
import os,sys

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import  (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,VideoSendMessage,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,ImagemapSendMessage,
    ImageSendMessage,BaseSize,URIImagemapAction,MessageImagemapAction,ImagemapArea,MessageTemplateAction)

app = Flask(__name__)



line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


# 監聽所有來自 /callback 的 Post Request
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


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    #print(event)
    usern=profile.display_name
    msg = event.message.text
    if msg=='熱銷主打':
        image_carousel_template = TemplateSendMessage(
            alt_text='熱銷主打',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.desen.com.tw/y1.jpg',
                        title='莓好雙12免運組',
                        text='生乳捲-草莓雙漩酸酸甜甜、香氣四溢的草莓果餡，與細膩滑順的北海道奶霜融合成獨特的雙漩雙味，勾動每一顆蠢蠢欲動的心',
                        actions=[
                            URIAction(
                                label='-立即購買-',
                                uri='https://www.yannick.com.tw/product.php?pid_for_show=5821'
                                )
                            ]
                        ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.desen.com.tw/y02.jpg',
                        title='週末小確幸免運',
                        text='亞尼克生乳捲，夢想村派塔',
                        actions=[
                            URIAction(
                                label='-立即購買-',
                                uri='https://www.yannick.com.tw/website_module.php?website_module_classify_sn=216'
                                )
                            ]
                        ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.desen.com.tw/y3.jpg',
                        title='隨享卡寄捲/午茶套餐',
                        text='聰明消費省更多，免揪團享優惠，可跨店提領，提領無限期',
                        actions=[
                            URIAction(
                                label='-立即購買-',
                                uri='https://www.yannick.com.tw/website_module_detail.php?website_module_classify_sn=118&website_module_sn=193'
                                )
                            ]
                        )
                    
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, image_carousel_template)
    elif msg=='YTM':
        message = VideoSendMessage(
            original_content_url='https://www.desen.com.tw/ytm.mp4',
            preview_image_url='https://www.desen.com.tw/ytm.jpg'
            )
        line_bot_api.reply_message(event.reply_token, message)
    elif msg=='熱銷商品':      
        buttons_template = ButtonsTemplate(
            title='Hi:'+usern, text='亞尼克堅持使用好料、堅守新鮮品質的王道', actions=[
                URIAction(label='亞尼克生乳捲', uri='https://www.yannick.com.tw/category.php?type=1&arem1=702&arem=149'),
                URIAction(label='夢想村派塔', uri='https://www.yannick.com.tw/category.php?type=1&arem1=703&arem=149'),
                URIAction(label='亞尼克起司磚',uri='https://www.yannick.com.tw/category.php?type=1&arem1=761&arem=149'),
                PostbackAction(label='【其它】商品..', data='ping', text='其它商品')              
                ])
        template_message = TemplateSendMessage(
            alt_text='熱銷商品', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif msg=='其它商品':
        buttons_template = ButtonsTemplate(
            title='Hi:'+usern, text='亞尼克堅持使用好料、堅守新鮮品質的王道', actions=[
                URIAction(label='人氣拌手禮', uri='https://www.yannick.com.tw/category.php?type=1&arem1=704&arem=149'),
                URIAction(label='生。磅蛋糕', uri='https://www.yannick.com.tw/product.php?pid_for_show=5655&category_sn=781'),
                URIAction(label='生日蛋糕',uri='https://www.yannick.com.tw/category.php?type=1&arem1=705&arem=149'),
                URIAction(label='巴斯克生起司',uri='https://www.yannick.com.tw/product.php?pid_for_show=5660&category_sn=826')              
                ])
        template_message = TemplateSendMessage(
            alt_text='熱銷商品', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif msg=='隨享卡專區':
        image_carousel_template = TemplateSendMessage(
            alt_text='隨享卡專區',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.desen.com.tw/y0004.jpg',
                        title='隨享卡',
                        text='線上虛擬卡，隨時分享儲存您的幸福',
                        actions=[
                            URIAction(
                                label='-立即申請-',
                                uri='https://www.yannick.com.tw/website_module.php?website_module_classify_sn=210'
                                )
                            ]
                         )               
                    
                    ]
               )
            )
        
        line_bot_api.reply_message(event.reply_token, image_carousel_template)
    elif msg=='手作DIY':
        message = TemplateSendMessage(
            alt_text='手作DIY課程',
            template=ConfirmTemplate(
                text='Hi:'+usern+' 提供手作DIY課程，歡迎了解呦^^',
                actions=[
                    URIAction(label='報名手作DIY', uri='https://www.yannick.com.tw/website_module.php?website_module_classify_sn=189'),
                    URIAction(label='查尋手作課程', uri='https://www.yannick.com.tw/website_module.php?website_module_classify_sn=189')
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    else:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='Hi:'+usern+'-請點選下方選單按鈕，可查尋相關訊息呦-^^-')])
    
 
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.1', port=port)  


