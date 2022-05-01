# http://tushare.org/trading.html
# https://tushare.pro/document/1?doc_id=5
# https://tushare.pro/document/2?doc_id=14
import tushare as ts

# ts.set_token(settings.TUSHARE_API)
# 以上方法只需要在第一次或者token失效后调用，完成调取tushare数据凭证的设置，正常情况下不需要重复设置。也可以忽略此步骤，直接用pro_api('your token')完成初始化

# 如果上一步骤ts.set_token('your token')无效或不想保存token到本地，也可以在初始化接口里直接设置token:
# pro = ts.pro_api(settings.TUSHARE_API)
# pro = ts.pro_api()
df = ts.get_hist_data('300003')  # 一次性获取全部日k线数据
print(df)
