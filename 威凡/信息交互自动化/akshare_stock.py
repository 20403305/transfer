
import akshare as ak



# get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date", var="RB", start_day="20180618", end_day="20180718")
# print(get_roll_yield_bar_df)


# result = ak.stock_us_famous_spot_em(symbol = "科技类")
# print(result)



# 日K 触达 5日均线

# 2点30分的时候，获取当天的日K数据，并计算5日均线，如果当天的收盘价超过5日均线，则触发提醒

result = ak.stock_zh_a_daily(symbol = "sh301027", start_date = "20220428", end_date = "20220429",adjust="")

print(result)