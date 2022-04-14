# tasks.py
from celery import Celery

# 消息队列
redis_broker = "redis://192.168.88.131:6379/3"

# 任务结果存放地
redis_backend = "redis://192.168.88.131:6379/4"

app = Celery('tasks',  backend=redis_backend, broker=redis_broker) #配置好celery的backend和broker

app.config_from_object('celery_config')
 
@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))
    return f'period task done: {self.request.id}'

