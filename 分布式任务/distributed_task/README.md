
Celery 和 Rearq 实现分布式任务



{}--------Celery----------
https://blog.csdn.net/qq_37049050/article/details/82260151
https://blog.csdn.net/aaahtml/article/details/115131246
Celery 
Celery 是一个由 Python 编写的简单、灵活、可靠的用来处理大量信息的分布式系统,它同时提供操作和维护分布式系统所需的工具。
Celery 专注于实时任务处理，支持任务调度。
说白了，它是一个分布式队列的管理工具，我们可以用 Celery 提供的接口快速实现并管理一个分布式的任务队列。


# 开启celery worker监测并执行实时任务
celery -A tasks worker --loglevel=info
# 开启celery beat监测并执行定时任务
celery -A tasks beat --loglevel=info
# 使用celery的flower控制台，查看存贮在redis中的celery任务队列(需安装flower)
celery -A tasks flower --loglevel=info



{}--------Rearq----------
https://pypi.org/project/rearq/
Rearq 是一个基于redis的分布式任务队列，基于asyncio实现，重写了arq

前端展示页面（展示redis和mysql中的数据），worker工作进程（处理：Task），定时任务进程（处理：CronTasks），需要分别用脚本，启动不同的进程。
会在Redis和mysql中保存不同任务的队列信息。有相应的前端界面可以查看
任务类型：
实时任务：Task
定时任务：CronTasks


# 开启rearq worker 监测并执行 main文件中队列名参数为myqueue函数的实时任务
rearq main:rearq worker -q myqueue

# 开启rearq beat 监测并执行 main文件中timer函数的定时任务
rearq main:rearq timer

# 开启rearq 控制台，查看存贮在redis和mysql中的任务队列和状态
rearq main:rearq server
After server run, you can visit https://127.0.0.1:8000/docs to see all apis and https://127.0.0.1:8000 to see web interface.