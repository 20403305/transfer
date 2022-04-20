# 生产者是生成器
# 一个生成器被一个循环函数调用
# Coroutine 协程

# 主函数一次性获得所有的商品
# 监听等待者是被动方(生成器,等待被触发),等待方可以无限循环，触发方最好不要无线循环

def producer():
    raw_material = "原材料"
    print("生产者触发生成器成功，默认值:%s" % raw_material)
    num = 0
    while True:
        raw_material_list = (raw_material,num)
        yield raw_material_list
        num += 1
        print('生产者 Producing %s...' % num)
        print(f"生产者发送第{num}个原材料")

def consumer(producer):
    producer.send(None)
    deal_num = 1
    # 消费加工10个原材料
    goods_list = []
    while deal_num <= 10:
        raw_material_list = producer.send(None)
        goods = f"商品{raw_material_list[1]}"
        print(f"消费者接受到了原材料{raw_material_list[1]}，并加工成了{goods}")
        goods_list.append(goods)
        deal_num += 1
    # 关闭生成器
    producer.close()
    return goods_list

worker = producer()
goods_list = consumer(worker)
print(goods_list)
        

        
    