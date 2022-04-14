from celery.utils.log import get_logger
from tasks_d import fetch_page, parse_page, store_page_info, sum, mul, post_file
from celery import group, chain, chord

logger = get_logger(__name__)


try:
    result = mul.apply_async(args=(2, 2))
    value = result.get() # 等待任务执行完毕后，才会返回任务返回值
    print(value)
except mul.OperationalError as exc: # 任务异常处理
    logger.exception('Sending task raised: %r', exc)

# 组合任务:
# 多个任务并行执行, group
# 多个任务链式执行，chain：第一个任务的返回值作为第二个的输入参数，以此类推
# 链式任务中前一个任务的返回值默认是下一个任务的输入值之一 ( 不想让返回值做默认参数可以用 si() 或者 s(immutable=True) 的方式调用 )。
# 这里的 s() 是方法 celery.signature() 的快捷调用方式，signature 具体作用就是生成一个包含调用任务及其调用参数与其他信息的对象，个人感觉有点类似偏函数的概念：先不执行任务，而是把任务与任务参数存起来以供其他地方调用。
result = group(sum.s(i, i) for i in range(5))()
result.get()
print(result.get())
# [0, 2, 4, 6, 8]
result = chain(sum.s(1,2), sum.s(3), mul.s(3))()
result.get()
print(result.get())
# ((1+2)+3)*3=18


# 链式任务
def update_page_info(url):
    # fetch_page -> parse_page -> store_page
    chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
    chain()

url = 'mock_url'
# 方法1
update_page_info(url)
# 方法2--不可用
# fetch_page.apply_async((url), link=[parse_page.s(), store_page_info.s(url)])