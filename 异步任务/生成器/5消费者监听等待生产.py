# 消费者是生成器
# 一个生成器被一个循环函数调用
# Coroutine 协程

# 主函数一次性获得所有的商品
# 监听等待者是被动方(生成器,等待被触发),等待方可以无限循环，触发方最好不要无线循环

def producer(consumer):
    raw_material = "原材料"
    num = 1
    consumer.send(None)
    # 生产10个商品
    goods_list = []
    while num <= 10:
        print('生产者 Producing %s...' % num)
        print(f"生产者发送第{num}个原材料")
        goods = consumer.send((raw_material,num))
        print(f"生产者获得了{goods}")
        goods_list.append(goods)
        num += 1
    # 关闭生成器
    consumer.close()
    return goods_list
    
    
def consumer():
    goods = ""
    print("消费者触发生成器成功,商品默认值%s" % goods)
    while True:
        raw_material = yield goods
        if not raw_material:
            return
        goods = f"商品{raw_material[1]}"
        print(f"消费者接受到了原材料{raw_material}，并加工成了{goods}")

worker = consumer()
goods_list =  producer(worker)
print(goods_list)
