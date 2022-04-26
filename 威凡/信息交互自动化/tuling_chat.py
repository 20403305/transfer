import os
import sys
import json
import requests


# 加入前3级目录
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# [print(path) for path in sys.path]
from configs import settings

url = settings.TULING_CHAT_BASE_SETTINGS.url_prefix
headers = settings.TULING_CHAT_BASE_SETTINGS.headers
send_msg = "附近的酒店"
json_msg = {
    "reqType": 0,
    "perception": {"inputText": {"text": send_msg}},
    "userInfo": {"apiKey": settings.TULING_CHAT_BASE_SETTINGS.apiKey, "userId": settings.TULING_CHAT_BASE_SETTINGS.userId}}

res = requests.post(url=url, headers=headers, json=json_msg)

print(f"向图灵发送消息:{send_msg}")
if res.status_code == 200:
    print("发送成功")
    print("图灵平台回复如下：")
    print(json.loads(res.text)["results"][0]["values"]["text"])
else:
    print("发送失败")
