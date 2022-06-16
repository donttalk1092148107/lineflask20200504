import requests
import json

headers = {"Authorization":"Bearer R6CMZv1VI6h9rfrACNCn+SXzh54c4YdjFfGjsh/O7gNdOQMI6PyGjxIw9f6mAxZDuNata21nn28CwFOiU704cuDDNSUZvWUfGxB3afELgcA1ZQ/afvfTw8kzKO6P19fMn+l1xA7ENKx6FDFN7RQ1RQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 843},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "LINE圖文選單範例",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "文字",
          "text": "Hello, World!"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "uri",
          "label": "網址",
          "uri": "https://www.google.com/"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "location",
          "label": "位置"
        }
      }
   ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
