# 计划任务
# https://pypi.org/project/crython/
# https://www.cnpython.com/pypi/crython
# https://crython.readthedocs.io/en/latest/expression.html
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376

"""
Represents an entire cron expression.
An expression consists of seven, space delimited fields that represent the following values::
    +------------- second (0 - 59)
    | +------------- minute (0 - 59)
    | | +------------- hour (0 - 23)
    | | | +------------- day (1 - 31)
    | | | | +------------- month (1 - 12)
    | | | | | +------------- weekday (0 - 6) (Sunday to Saturday; 7 is also Sunday)
    | | | | | | +------------- year (1970 - 2099)
    | | | | | | |
    | | | | | | |
    * * * * * * *
"""

# ✳号代表当前位置所有数字的集合，如果是second:*/10，代表每10秒执行一次,总共6次
# 如果hour:21-23，代表21点到23点整点时执行一次,总共3次

from loguru import logger
import crython
import os
import threading

logger.add("logs/{time}.log")

# Fire once immediately after scheduler starts.
# 计划任务开始时，执行一次
@crython.job(expr='@reboot')
def start_init():
    # print(share_global_var)
    share_global_var = 3
    print('计划任务开始执行!{%s} start_init: I am child process (%s) and my parent is %s.' % (share_global_var,os.getpid(), os.getppid()))

# 含参数的定时计划,未指明变量的为item字段接收
@crython.job('safety gloves', second='*/5', name='Homer Simpson')
def para_task(item, name):
    print("Well, I don't need {0}, because I'm {1}. -- Grimey".format(item, name))

# 每次调用创建一个新线程去执行任务
@crython.job(expr='@secondly', ctx='thread')
def muti_threading():
    print('muti_threading: I am child process (%s) and my parent is %s. thread %s is running...' % (os.getpid(), os.getppid(),threading.current_thread().name))

# 每次调用创建一个新进程去执行任务
@crython.job(expr='@secondly', ctx='multiprocess')
def muti_process():
    # print(share_global_var)
    # print('thread %s is running...' % threading.current_thread().name)
    print('multiprocess: I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))


@crython.job(expr="*/3 * * * * * *") # 每3秒执行一次 
def foo():
    local_var = share_global_var +1
    print(f"hello demo{local_var},thread %s is running...{threading.current_thread().name}")


if __name__ == '__main__':
    # 创建子线进行计划任务
    print('主进程开始 thread %s is running...' % threading.current_thread().name)
    # 全局共享变量在reboot和ctx='multiprocess'时会被重置,全局变量在线程中不能被修改
    share_global_var = 1
    crython.start()
    # 使用join，让主线程等待子进程结束，timeout时间内子线程没有结束就退出
    crython.join(timeout=5) # 等待5秒
    print(f'主进程结束{share_global_var}')