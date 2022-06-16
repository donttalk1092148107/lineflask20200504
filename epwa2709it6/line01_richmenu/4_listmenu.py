from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('R6CMZv1VI6h9rfrACNCn+SXzh54c4YdjFfGjsh/O7gNdOQMI6PyGjxIw9f6mAxZDuNata21nn28CwFOiU704cuDDNSUZvWUfGxB3afELgcA1ZQ/afvfTw8kzKO6P19fMn+l1xA7ENKx6FDFN7RQ1RQdB04t89/1O/w1cDnyilFU=')

rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)
