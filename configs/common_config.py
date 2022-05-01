from collections import defaultdict

from typing import Optional
from configs.chat_base_config.chat_config import FeiShuChatInfoTemplate, TuLingChatInfoTemplate

from pydantic import AnyHttpUrl, BaseSettings

class _Const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("constant reassignment error!")
        self.__dict__[key] = value



class ConstInfo(_Const, BaseSettings):
    VERSION: int = 1
    API_VER_STR: str = f"/v{VERSION}"
    TERMS_OF_SERVICE: AnyHttpUrl = "https://google.com"
    # 文档信息
    DOCS_URL: str = f"{API_VER_STR}/docs"
    # 项目信息
    PROJECT_NAME: str = "Python成长之路"
    DESCRIPTION: str = "Python学习记录"


class Settings(BaseSettings):
    #  常量不可修改的信息
    CONST_: ConstInfo = ConstInfo()

    # 基本信息
    DEBUG: bool = False
    PORT: int = 8000

    # token过期时间 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # mysql 配置
    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = "root"
    MYSQL_HOST: str = "127.0.0.1"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "test"

    # redis配置
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379

    # 信息交互自动化相关配置
    # 1.图灵聊天机器人
    TULING_CHAT_BASE_SETTINGS = TuLingChatInfoTemplate()
    # 2.飞书机群聊器人
    FEISHU_CHAT_BASE_SETTINGS = FeiShuChatInfoTemplate()
    # 3.Finnhub股票查询 apikey(token)
    FINNHUB_APIKEY :str = None 
    TUSHARE_API :str = None 
    

    MAP = defaultdict(lambda: None)
    # MAP = defaultdict(dict)

    class Config:
        case_sensitive = True
        env_file = ".env"  # 使用环境变量文件或者环境变量  pip install pydantic[dotenv]
        env_file_encoding = "utf-8"

    @property
    def MYSQL_DATABASE_URL(self):
        return f"mysql+pymysql://{self.MYSQL_USERNAME}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}/{self.MYSQL_DATABASE}?charset=utf8mb4"

    @property
    def REDIS_URL(self):
        return (
            f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}?encoding=utf-8"
            if self.REDIS_PASSWORD
            else f"redis://:{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}?encoding=utf-8"
        )