# 单线生产消费
# 在生产者中将原材料发送给消费者获得商品加工后的商品，再返回给主程序
# 两者都是生成器

# 主函数请求一次获得一个商品

def producer(consumer):
    raw_material = "空"
    print("生产者触发生成器成功，原材料默认值%s" % raw_material)
    num = 1
    consumer.send(None) 
    while True:
       print(f"生产第{num}个原材料")
       yield consumer.send(num) 
       # send方法只能发送一个值
       # yield consumer.send(raw_material,num) 
       num += 1

def consumer():
    goods = ""
    print("消费者触发生成器成功,商品默认值%s" % goods)
    while True:
        # raw_material, num = yield goods
        num = yield goods
        goods = f"商品{num}"
        print(f"消费者接受到了原材料{num}，并加工成了{goods}")
        # print(f"消费者接受到了{raw_material}，并加工成了{goods}")

worker = consumer()
trigger = producer(worker)
good1 = trigger.send(None)
print(good1)
good2 = trigger.send(None)
print(good2)

        