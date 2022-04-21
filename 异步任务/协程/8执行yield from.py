
def get_value(value):
    print(f"接受到需要被处理的值{value}")
    print(f"开始异步处理值{value}")
    middle = yield from process_value(value)
    result = middle + "处理完成"
    return result

def process_value(value):
    value = value + "加工完成"
    yield value
    return value

func = get_value("0")

result = func.send(None)
print(result)
try:
    result = func.send(None)
    print(result)
except StopIteration as e:
    print(e.value)
