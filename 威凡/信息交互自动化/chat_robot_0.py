import  requests
import sys
import os
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)
from configs import settings

key_value = settings.FEISHU_CHAT_BASE_SETTINGS.key_value

msg = {"msg_type":"text","content":{"text":f"{key_value}\nrequest example"}}

url = (
    settings.FEISHU_CHAT_BASE_SETTINGS.url_prefix
    + settings.FEISHU_CHAT_BASE_SETTINGS.url_suffix
)

headers = settings.FEISHU_CHAT_BASE_SETTINGS.headers

res = requests.post(url=url,headers=headers,json=msg)
res.raise_for_status()
result = res.json()
print(result)