import tushare as ts

# codes = ['sh', 'sz', 'cyb', '000100', '002958']
codes = ['sh', 'sz', 'cyb', '300003']


def auto_get_tushare_data():
    data = ts.get_realtime_quotes(codes)
    # print(len(data))
    sh_price = round(float(data['price'].values[0]), 2)  # 上证指数 当前价格
    sh_pre_close = round(float(data['pre_close'].values[0]), 2)  # 上证指数 昨日收盘价
    sz_price = round(float(data['price'].values[1]), 2)  # 深证指数 当前价格
    sz_pre_close = round(float(data['pre_close'].values[1]), 2)  # 深证指数 昨日收盘价
    cyb_price = round(float(data['price'].values[2]), 2)  # 创业版指数 当前价格
    cyb_pre_close = round(float(data['pre_close'].values[2]), 2)  # 创业版指数 昨日收盘价
    sh = round(sh_price - sh_pre_close, 2)
    sz = round(sz_price - sz_pre_close, 2)
    cyb = round(cyb_price - cyb_pre_close, 2)
    sh_percent = round(sh / sh_pre_close * 100, 2)
    sz_percent = round(sz / sz_pre_close * 100, 2)
    cyb_percent = round(cyb / cyb_pre_close * 100, 2)
    # print('(', sh_price, sh, sh_percent, ')', '(', sz_price, sz, sz_percent, ')', '(', cyb_price, cyb, cyb_percent, ')')
    # print('(%.2f %.2f %.2f) (%.2f %.2f %.2f) (%.2f %.2f %.2f)'%(sh_price, sh, sh_percent, sz_price, sz, sz_percent, cyb_price, cyb, cyb_percent))
    result = ''
    result += (
        f'上证指数:\n当前价格:{sh_price}\n昨日收盘:{sh_pre_close}\n今日较昨日浮动:{sh};浮动百分比:{sh_percent}%'
    )
    result += (
        f'深证指数:\n当前价格:{sz_price}\n昨日收盘:{sz_pre_close}\n今日较昨日浮动:{sz};浮动百分比:{sz_percent}%'
    )
    result += f'创业版指数:\n当前价格:{cyb_price}\n昨日收盘:{cyb_pre_close}\n今日较昨日浮动:{cyb};浮动百分比:{cyb_percent}%'
    # print(result)
    # print('\n')
    # 从第4个开始遍历就是自己关注的股票代码
    for i in range(3, len(data)):
        price = float(data['price'].values[i])
        pre_close = float(data['pre_close'].values[i])
        # print(data.name.values[i], data.open.values[i], data.price.values[i], round((price-pre_close)/pre_close*100, 2))
        result += f'{data.name.values[i]}:\n当前价格:{price}\n昨日收盘:{pre_close}\n今日较昨日浮动:{round(price-pre_close,2)};浮动百分比:{round((price-pre_close)/pre_close*100, 2)}%'
        # print(f'{data.name.values[i]}:\n当前价格:{price}\n昨日收盘:{pre_close}\n今日较昨日浮动:{round(price-pre_close,2)};浮动百分比:{round((price-pre_close)/pre_close*100, 2)}%')
    # time.sleep(3)
    # print(result)
    return result


if __name__ == "__main__":
    result = auto_get_tushare_data()
    print(result)
