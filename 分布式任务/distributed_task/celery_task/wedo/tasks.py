# 任务的定义
# 简单任务  tasks.py
import celery
import time
from celery.utils.log import get_task_logger
from wedo import app
 
@app.task
def sum(x, y):
    return x + y
 
@app.task
def mul(x, y):
    time.sleep(5)
    return x * y