

from pydantic import BaseModel, Field
from requests import request


class RequestCommon(BaseModel):
    headers: dict =  Field(default={'content-type': "application/json"},description="访问服务器头信息")
    apiKey: str = Field(default="", description="webhook_secret--(apiKey)")

class TuLingChatInfoTemplate(RequestCommon):
    url_prefix: str = Field(default="http://openapi.turingapi.com/openapi/api/v2", description="访问服务器地址前缀")
    userId: str = Field(default="", description="userId")

class FeiShuChatInfoTemplate(RequestCommon):
    url_prefix: str = Field(default="https://open.feishu.cn/open-apis/bot/v2/hook/", description="访问服务器地址前缀")
    url_suffix: str = Field(default="", description="访问服务器地址后缀")
    headers: dict =  Field(default={'content-type': "application/json"},description="访问服务器头信息")
    key_value: str = Field(default="", description="包含关键字")