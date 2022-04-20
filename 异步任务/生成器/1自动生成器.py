# 生成器 -- 生成偶数集合

def get_even():
    num= 0
    print("触发生成器成功，当前值为：%s" % num)
    while True:
        yield num
        num= num+2
        print("当前值+2,为：%s" % num)

# 一：引用生成器
get_num = get_even()

# 二：触发生成器
# 方法一：
next(get_num) # 值为0
next(get_num) # 值为2
next(get_num) # 值为4
# 方法二：
get_num.send(None) # 值为6
get_num.send(None) # 值为8
get_num.send(None) # 值为10

# 三：使用生成器,获取小于100的偶数
gen_num_list = []
# 值继续从12开始获取
# 如想重新计算，可以关闭生成器，重新获取
# get_num.close()
# get_num = get_even()
for x in get_num:
    if x < 100:
        gen_num_list.append(x)
    else:
        break
print(gen_num_list)

# 四：对比-->列表筛选器，不可将for的对象换位对象为无限个的生成器，会陷入死循环
new_list = [x for x in gen_num_list if x < 20]
print(new_list)

# 生成固定数量的偶数
def get_even_in_10():
    num= 0
    print("触发生成器成功，当前值为：%s" % num)
    while num<=10:
        yield num
        num= num+2
        print("当前值+2,为：%s" % num)

gen_num_list = get_even_in_10()
gen_num_list.send(None)
# 四：对比-->列表筛选器，可将for的对象换位对象为有限个的生成器,节约内存,可用完就删掉
new_list = [x for x in gen_num_list]
print(new_list)

# 五：释放资源
del new_list
try:
    print(new_list)
except Exception as e:
    print(e)
