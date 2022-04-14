# tasks.py
import celery
from celery import Celery
import flower
import time
from celery.utils.log import get_task_logger

# 消息队列
redis_broker = "redis://192.168.88.131:6379/3"

# 任务结果存放地
redis_backend = "redis://192.168.88.131:6379/4"

app = Celery('tasks',  backend=redis_backend, broker=redis_broker) #配置好celery的backend和broker

 
logger = logger = get_task_logger(__name__)
class TaskMonitor(celery.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """failed callback"""
        logger.info('task id: {0!r} failed: {1!r}'.format(task_id, exc))
 
    def on_success(self, retval, task_id, args, kwargs):
        """success callback"""
        logger.info('task id:{} , arg:{} , successful !'.format(task_id,args))
 
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """retry callback"""
        logger.info('task id:{} , arg:{} , retry !  einfo: {}'.format(task_id, args, exc))
 
@app.task(base=TaskMonitor, bind=True, name='post_file')
def post_file(self, file_names):
    logger.info(self.request.__dict__)
    try:
        for i, file in enumerate(file_names):
            print('the file %s is posted' % file)
            if not self.request.called_directly:
                self.update_state(state='PROGRESS',
                    meta={'current': i, 'total': len(file_names)})
            time.sleep(2)
    except Exception as exec:
        raise self.retry(exc=exec, countdown=3, max_retries=5)



@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))
    return f'period task done: {self.request.id}'

@app.task
def sum(x, y):
    return x + y
 
@app.task
def mul(x, y):
    time.sleep(5)
    return x * y


@app.task()
def fetch_page(url):
    # 获取网页内容
    print(f"从网页：{url}中获取内容为：celery 链式任务测试")
    return f"celery 链式任务测试"
 
@app.task()
def parse_page(page):
    # 解析网页内容
    return f'解析网页内容：{page}'
 
@app.task(ignore_result=True)
def store_page_info(info, url):
    # 存储网页url解析内容
    return f'存储网页{url}解析内容：{info}'
