# celery_config.py
from datetime import timedelta
from celery.schedules import crontab
 
CELERYBEAT_SCHEDULE = {
    'ptask': {
        'task': 'tasks.period_task',
        'schedule': timedelta(seconds=5),
    },
}
 
CELERY_RESULT_BACKEND = 'redis://192.168.88.131:6379/4'
# 如果定时任务涉及到 datetime 需要在配置中加入时区信息，否则默认是以 utc 为准。例如中国可以加上
CELERY_TIMEZONE = 'Asia/Shanghai'