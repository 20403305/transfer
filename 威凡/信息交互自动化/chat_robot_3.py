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

key_value = settings.FEISHU_CHAT_BASE_SETTINGS.key_value


class LarkBot:
    def __init__(self, secret: str) -> None:
        if not secret:
            raise ValueError("invalid secret key")
        self.secret = secret

    def gen_sign(self, timestamp: int) -> str:
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        hmac_code = hmac.new(
            string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
        ).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')

        return sign

    def send(self, content: str) -> None:
        timestamp = int(datetime.now().timestamp())
        sign = self.gen_sign(timestamp)

        params = {
            "timestamp": timestamp,
            "sign": sign,
            "msg_type": "text",
            # "content": {"text": content},
            "content": {"text": f"{key_value}:\n{content}"},
        }
        resp = requests.post(url=WEBHOOK_URL, json=params)
        resp.raise_for_status()
        result = resp.json()
        if result.get("code") and result["code"] != 0:
            print(result["msg"])
            return
        print("消息发送成功")


def main():

    import re
    import subprocess

    WEBHOOK_SECRET = settings.FEISHU_CHAT_BASE_SETTINGS.apiKey

    # 利用正则表达式获取 IP 字符串
    IPV4_PATTERN = r"IPv4.*: (?P<ip>.*)\n"
    ipconfig = subprocess.run("ipconfig", capture_output=True, text=True).stdout
    ip = re.search(IPV4_PATTERN, ipconfig).group("ip")

    bot = LarkBot(secret=WEBHOOK_SECRET)
    bot.send(content=f"当前工位的电脑 IP 是：{ip}")


if __name__ == '__main__':
    main()
