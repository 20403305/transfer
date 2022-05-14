
# import tushare as ts
# # codes = ['301027']

# # data = ts.get_realtime_quotes(codes)
# # print(data)

# # 初始化pro接口
# pro = ts.pro_api('')

# # 拉取数据
# df = pro.daily(**{
#     "ts_code": "301027.SZ",
#     "trade_date": "",
#     "start_date": "",
#     "end_date": "",
#     "offset": "",
#     "limit": ""
# }, fields=[
#     "trade_date",
#     "close",
# ])
# for i in range(len(df)):
#     print(df.iloc[i])
# print(type(df['close'][0:5].sum()/5))


import pandas
df = pandas.read_csv('301072.csv')
# print(df)
# print(type(df))

# 五日均线列表
ma5 = df['close'].rolling(window=5).mean()
# 获取交易日期
trade_date = df['trade_date']
# print(ma5)
# print(len(ma5))
# print(len(trade_date))
for i in range(len(ma5)-4):
    # if abs(ma5[i+4] - df['close'][i]) < 0.03:
    # if  df['close'][i] > ma5[i+4] :
    # 收盘价大于五日均线，且收盘价与五日均线差值小于0.06
    if df['close'][i] > ma5[i+4] and abs(df['close'][i] - ma5[i+4]) < 0.06:
        print(f'日期:{trade_date[i]}--收盘价:{df["close"][i]}--五日均线值:{ma5[i+4]}')


