# 单线生产消费
# 在消费者中调用生产者的原材料，并将加工后的商品返回给主程序
# 两者都是生成器

# 主函数请求一次获得一个商品

def producer():
    raw_material = "空"
    print("生产者触发生成器成功，原材料默认值%s" % raw_material)
    yield raw_material
    num = 1
    print("开始生产第一个原材料")
    while True:
        raw_material = f"原材料{num}"
        yield raw_material ,num
        num+=1

def consume(product):
    goods = ""
    print("消费者触发生成器成功,商品默认值%s" % goods)
    product.send(None)
    while True:
        raw_material, num = product.send(None)
        goods = f"商品{num}"
        print(f"消费者接受到了{raw_material}，并加工成了{goods}")
        yield goods

get_raw = producer()
get_goods = consume(get_raw)

for i in range(10):
    print(get_goods.send(None))
