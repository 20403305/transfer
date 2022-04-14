
#tasks.py

# 2.2 绑定任务为实例方法


from celery import Celery, Task
from celery.utils.log import get_task_logger
 
# 消息队列
redis_broker = "redis://192.168.88.131:6379/3"

# 任务结果存放地
redis_backend = "redis://192.168.88.131:6379/4"

app = Celery('tasks',  backend=redis_backend, broker=redis_broker) #配置好celery的backend和broker
 
# tasks.py
class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)
 
 
logger = get_task_logger(__name__)

@app.task(base= MyTask ,bind=True)
def add(self, x, y):
    logger.info(self.request.__dict__)
    return x + y