import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)
from configs import settings

# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api(settings.TUSHARE_API)

# 拉取数据
df = pro.stock_basic(
    **{
        "ts_code": "",
        "name": "",
        "exchange": "",
        "market": "",
        "is_hs": "",
        "list_status": "",
        "limit": "",
        "offset": "",
    },
    fields=["ts_code", "symbol", "name", "area", "industry", "market", "list_date"]
)
print(df)
