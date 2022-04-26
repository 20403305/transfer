import base64
import hashlib
import hmac
from datetime import datetime
import requests
import sys
import os


sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)


from configs import settings

WEBHOOK_URL = (
    settings.FEISHU_CHAT_BASE_SETTINGS.url_prefix
    + settings.FEISHU_CHAT_BASE_SETTINGS.url_suffix
)
WEBHOOK_SECRET = settings.FEISHU_CHAT_BASE_SETTINGS.apiKey
key_value = settings.FEISHU_CHAT_BASE_SETTINGS.key_value

timestamp = int(datetime.now().timestamp())


def gen_sign(secret):
    # 拼接时间戳以及签名校验
    string_to_sign = '{}\n{}'.format(timestamp, secret)

    # 使用 HMAC-SHA256 进行加密
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()

    # 对结果进行 base64 编码
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign


def main():
    sign = gen_sign(WEBHOOK_SECRET)
    params = {
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "text",
        "content": {"text": f"{key_value}:\n点火发射！"},
    }

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：{result['msg']}")
        return
    print("消息发送成功")


if __name__ == '__main__':
    main()
