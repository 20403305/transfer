
# https://blog.csdn.net/weixin_44024393/article/details/107410816

# yield 后面可以接任何类型的值
# yield from 后面只可以接可迭代对象
# 在调用yield 所在的函数时，send或next会让函数继续从yield下面继续执行，
# 但是在yield from 所在的函数中，send或next会返回yield from后面的可迭代对象的下一个值，
# 直到遇到yield from后面的可迭代对象的最后一个值，然后返回None，接着继续执行yield from后面的代码


def producer():
    raw_material = 0
    print("生产者触发生成器成功，触发信号值%s" % raw_material)
    # 调用2次 yield from
    while True:
        print(f"发送信号值{raw_material}")
        # goods = yield from "abcd"
        # goods = yield from consume_1(raw_material)
        goods = yield from consume_3(raw_material)
        # goods = yield from consume_3(raw_material)
        print(f"生成者接受到了迭代对象的结束信号{goods}")
        print(f"生成者产生新信号值{raw_material}")

        raw_material += 1
        
def consume_0():
    return "abcd"


def consume_1(raw_material):
    while True:
        goods = "商品" + str(raw_material)
        return goods

def consume_2(raw_material):
    print(f"消费者接受到信号{raw_material}开始自行生成商品")
    i = 0 
    while i < 2:
        goods = "商品" + str(i)
        yield goods
        i+=1

def consume_3(raw_material):
    print(f"消费者接受到信号{raw_material}开始自行生成商品")
    i = 0 
    while i < 2:
        goods = "商品" + str(i)
        yield goods
        i+=1
        return goods


producer_obj = producer()
goods = producer_obj.send(None) 
print(goods)
goods = producer_obj.send(None) 
print(goods)
goods = producer_obj.send(None) 
print(goods)
goods = producer_obj.send(None) 
print(goods)
goods = producer_obj.send(None) 
print(goods)
