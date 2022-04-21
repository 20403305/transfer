# https://wenku.baidu.com/view/e701d493fe0a79563c1ec5da50e2524de518d0bb.html
import asyncio
import threading

import aiohttp


async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            result =  await response.text()
            print("get {} length data from:{}".format(len(result), url))

async def main():
    url = "http://python.org"
    await get_url(url)

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())



loop = asyncio.get_event_loop()
tasks = [hello(),main()]
loop.run_until_complete(asyncio.wait(tasks))
loop.run_forever()
