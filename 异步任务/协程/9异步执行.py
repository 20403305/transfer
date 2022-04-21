# https://baijiahao.baidu.com/s?id=1714015900283907482&wfr=spider&for=pc

import asyncio
import threading


@asyncio.coroutine
def get_value(value):
    print(f"接受到需要被处理的值{value}")
    print(f"开始异步处理值{value}")
    print('当前线程 (%s)' % threading.currentThread())
    middle = yield from process_value(value)
    result = middle + "处理完成"
    print('当前线程 (%s)' % threading.currentThread())
    return result

@asyncio.coroutine
def process_value(value):
    print('当前线程 (%s)' % threading.currentThread())
    value = value + "加工完成"
    # yield value
    return value

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(get_value("0"))

import asyncio


def running1():
    async def test1():
        print('1')
        await test2()
        print('2')
    async def test2():
        print('3')
        print('4')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test1())
if __name__ == '__main__':
    running1()

# loop.close()要放到最后，否则会报错
loop.close()
