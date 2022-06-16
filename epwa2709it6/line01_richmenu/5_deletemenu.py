from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('R6CMZv1VI6h9rfrACNCn+SXzh54c4YdjFfGjsh/O7gNdOQMI6PyGjxIw9f6mAxZDuNata21nn28CwFOiU704cuDDNSUZvWUfGxB3afELgcA1ZQ/afvfTw8kzKO6P19fMn+l1xA7ENKx6FDFN7RQ1RQdB04t89/1O/w1cDnyilFU=')

line_bot_api.delete_rich_menu('richmenu-c258c66e72d4d966edf71821d4400db1')
