
import akshare as ak

# 2点30分的时候，获取当天的日K数据，并计算5日均线，如果当天的收盘价超过5日均线，则触发提醒

# 获取A 股股票代码和简称
ts_code = ak.stock_info_a_code_name()
print(ts_code)

# 获取A 股股票代码和简称


# 拉取数据
# def req_akshare(ts_code):
#     # print(f"开始请求-->{ts_code} 的数据")
#     # 获取 A 股历史行情数据(日频)
#     df_from_api = ak.stock_zh_index_daily_tx(symbol = ts_code,start_date = "20220425",end_date = "20220429",)
#     return df_from_api

# print(req_akshare("sz301072"))
# df_from_api = req_akshare(ts_code["code"][0])



# for x in range(len(ts_code)):
#     df_from_api = req_akshare(ts_code["code"][0])
#     # 五日均线列表
#     ma5 = df_from_api['close'].rolling(window=5).mean()
#     # 获取交易日期
#     trade_date = df_from_api['date']

#     for i in range(len(ma5)-4):
#         # 收盘价大于五日均线，且收盘价与五日均线差值小于0.06
#         if df_from_api['close'][i] > ma5[i+4] and abs(df_from_api['close'][i] - ma5[i+4]) < 0.06:
#             print(f'股票代码:{ts_code[x]}--日期:{trade_date[i]}--收盘价:{df_from_api["close"][i]}--五日均线值:{ma5[i+4]}')

