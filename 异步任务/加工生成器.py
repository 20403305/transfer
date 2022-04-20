# 加工生成器

def gen_double_num():
    output = "当前传出值：None"
    print("触发生成器成功，默认值%s" % output)
    while True:
        input = yield output
        output = input * 2
        print("当前传入值：%s,即将传出值：%s" % (input, output))

get_double_num = gen_double_num()
get_double_num.send(None)
# 获取4的2倍数
result = get_double_num.send(4)
print(result)
# 获取16的2倍数
result = get_double_num.send(16)
print(result)
