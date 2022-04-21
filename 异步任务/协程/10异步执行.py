
import asyncio
import threading


# 异步中的报错会到结束时统一抛出
@asyncio.coroutine
def get_value(value):
    print(f"接受到需要被处理的值{value}")
    print(f"开始异步处理值{value}")
    print('get_value yield from 任务前线程 (%s)' % threading.currentThread())
    middle = yield from process_value(value)
    # 不判断midlle类型，若返回为空，会直接中断执行,最后统一报错
    if middle is not  None:
        result = middle + "处理完成"
    else:
        result = "没有返回值"
    print('get_value yield from 任务后线程 (%s)' % threading.currentThread())
    return result

@asyncio.coroutine
def process_value(value):
    print('process_value当前线程 (%s)' % threading.currentThread())
    value = value + "加工完成"
    # 没有被@asyncio.coroutine装饰的函数，需要调用yield from,如果不调用，会报错
    # yield value
    # yield from value
    return value

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def test_0():
    # "abcd"没有被@asyncio.coroutine装饰
    result  = yield from "abcd"
    print(result)

@asyncio.coroutine
def test_1():
    # "abcd"没有被@asyncio.coroutine装饰
    result  = yield "abcd"
    print(result)



print('当前线程 (%s)' % threading.currentThread())
# 获取EventLoop:
loop = asyncio.get_event_loop()

start_time = loop.time()
print("开始时间：",start_time)

future_task = asyncio.ensure_future(get_value("原材料0")) 
print(future_task,'未执行') 

# 执行coroutine
tasks = [get_value("原材料0"),get_value("原材料2"), hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))

print(future_task,'执行完了') 

loop.close()
# 统计
end_time = loop.time()
print("结束时间：",end_time)
print("总耗时：",end_time-start_time)
