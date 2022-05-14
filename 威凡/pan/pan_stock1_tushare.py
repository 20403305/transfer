


import tushare as ts
import pandas
import sys
import os
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)
from configs import settings



df = pandas.read_csv('stock_list.csv')
# print(df)
# print(len(df))
# 获取股票代码的列表
ts_code = df['ts_code'].tolist()

print(ts_code[0])

# 初始化pro接口
pro = ts.pro_api(settings.TUSHARE_API)

# 拉取数据
def req_tushare(ts_code):
    # print(f"开始请求-->{ts_code} 的数据")
    df_from_api = pro.daily(**{
        "ts_code": ts_code,
        "trade_date": "",
        "start_date": "20220425",
        "end_date": "20220429",
    }, fields=[
        "ts_code",
        "trade_date",
        "close",
    ])
    return df_from_api

for x in range(len(ts_code)):
    df_from_api = req_tushare(ts_code[x])
    # 五日均线列表
    ma5 = df_from_api['close'].rolling(window=5).mean()
    # 获取交易日期
    trade_date = df_from_api['trade_date']

    # for i in range(len(ma5)-4):
    # 当只有一个5日均线值时，i= 0
    i = 0
    # 收盘价大于五日均线，且收盘价与五日均线差值小于0.06
    if df_from_api['close'][i] > ma5[i+4] and abs(df_from_api['close'][i] - ma5[i+4]) < 0.06:
        print(f'股票代码:{df_from_api["ts_code"][i]}--日期:{trade_date[i]}--收盘价:{df_from_api["close"][i]}--五日均线值:{ma5[i+4]}')