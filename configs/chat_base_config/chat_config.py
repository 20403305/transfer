

from pydantic import BaseModel, Field


class ChatInfoTemplate(BaseModel):
    url_prefix: str = Field(default="http://openapi.turingapi.com/openapi/api/v2", description="访问服务器地址前缀")
    headers: dict =  Field(default={'content-type': "application/json"},description="访问服务器头信息")
    apiKey: str = Field(default="", description="apiKey")
    userId: str = Field(default="", description="userId")