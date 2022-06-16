import requests

headers = {"Authorization":"Bearer R6CMZv1VI6h9rfrACNCn+SXzh54c4YdjFfGjsh/O7gNdOQMI6PyGjxIw9f6mAxZDuNata21nn28CwFOiU704cuDDNSUZvWUfGxB3afELgcA1ZQ/afvfTw8kzKO6P19fMn+l1xA7ENKx6FDFN7RQ1RQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-c258c66e72d4d966edf71821d4400db1', 
                       headers=headers)

print(req.text)
