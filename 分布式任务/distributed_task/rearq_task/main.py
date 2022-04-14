# main.py
from rearq import ReArq
from rearq.server import models
from tortoise import Tortoise


# rearq 设置
RE_ARQ_REDIS_URL = 'redis://192.168.88.131:6379/2'
# 默认redis_url: str = "redis://localhost:6379/0",
rearq = ReArq(RE_ARQ_REDIS_URL)


@rearq.on_shutdown
async def on_shutdown():
    # you can do some clean work here like close db and so on...
    print("shutdown")


@rearq.on_startup
async def on_startup():
    # init tortoise
    await Tortoise.init(
        db_url=f"mysql://root:123456@192.168.88.131:3306/rearq",
        # models要提前在数据库中创建好job,和jobresult表,否则会报错.详情查看导入的models
        modules={"models": [models]},
    )
    # you should do some initialization work here, such tortoise-orm init and so on...
    print("startup")


@rearq.task(queue="myqueue")
async def add(self, a, b):
    print("add+start")
    return a + b


@rearq.task(cron="*/5 * * * * * *")  # run task per 5 seconds
async def timer(self):
    print("定时任务")
    return "timer"

from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    await rearq.init()


@app.on_event("shutdown")
async def shutdown() -> None:
    await rearq.close()


# then run task in view
@app.get("/test")
async def test():
    job = await add.delay(args=(1, 2))
    return job.info()