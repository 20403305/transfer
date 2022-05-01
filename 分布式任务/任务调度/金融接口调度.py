from datetime import datetime
import crython
from loguru import logger

from check_holiday import is_workday
import sys
import os

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

chat_code_path = os.path.join(root_path,'威凡/信息交互自动化')
sys.path.insert(
    0, chat_code_path
)
from chat_robot_2 import send_msg_to_feishu 
from tushare_stock2 import auto_get_tushare_data

logger.add("logs/{time}.log")


@crython.job(expr="*/3 * * * * * *")
def run_daily_weekday():
    if is_workday():
        day = datetime.today()
        logger.info(f"今天是{day}")
        auto_get_tushare_data()


@crython.job(expr="*/10 * * * * * *")
def run_daily_weekend():
    # if not is_workday():
    day = datetime.today()
    logger.info(f"今天是{day}")
    logger.info("温馨提醒:今天不是工作日")
    result = auto_get_tushare_data()
    send_msg_to_feishu(result)


if __name__ == "__main__":
    crython.start()
    crython.join()
