#trigger.py

import time
from tasks_b import add
result = add.delay(4, 1) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(1)
print('task done: {0}'.format(result.get()))