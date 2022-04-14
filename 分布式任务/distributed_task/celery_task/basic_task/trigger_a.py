#trigger.py

import time
from tasks_a import add
result = add.delay(4, 1) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(1)
print('task done: {0}'.format(result.get()))

# value = result.get() # 任务返回值
# print(result.__dict__) # 结果信息
# print(result.successful()) # 是否成功
# print(result.fail()) # 是否失败
# print(result.ready()) # 是否执行完成
# print(result.state) # 状态 PENDING -> STARTED -> SUCCESS/FAIL