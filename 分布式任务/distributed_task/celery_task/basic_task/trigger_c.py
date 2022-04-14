#trigger.py

import sys
import time
from tasks_c import add,test_mes


def pm(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
        sys.stdout.flush()
    else:
        print('\r')
        print(res)


r = test_mes.delay()


print(r.get(on_message=pm, propagate=False))