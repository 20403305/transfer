
#tasks.py

# 2.3 任务状态回调


import time
from celery import Celery, Task
from celery.utils.log import get_task_logger
 
# 消息队列
redis_broker = "redis://192.168.88.131:6379/3"

# 任务结果存放地
redis_backend = "redis://192.168.88.131:6379/4"

app = Celery('tasks',  backend=redis_backend, broker=redis_broker) #配置好celery的backend和broker
 
logger = get_task_logger(__name__)
@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.__dict__)
    return x + y

@app.task(bind=True)
def test_mes(self):
    for i in range(1, 11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS", meta={'p': i*10})
    return 'finish'