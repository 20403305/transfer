# celery 实例初始化 
# __init__.py
from celery import Celery
app = Celery('wedo')  # 创建 Celery 实例
app.config_from_object('wedo.config') 
 
# 配置 wedo.config
# config.py
BROKER_URL = 'redis://192.168.88.131:6379/3' # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://192.168.88.131:6379/4' # BACKEND配置，这里使用redis
CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间
CELERY_TIMEZONE='Asia/Shanghai'   # 时区配置
CELERY_IMPORTS = (     # 指定导入的任务模块,可以指定多个
    'wedo.tasks',
    'wedo.period_task'
)