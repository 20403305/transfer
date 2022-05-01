
import json
import re
from datetime import datetime

import requests


def get_workdate_this_year():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",  # 如果接受 br，需要额外安装 `pip install brotlipy`
        "accept-language": "zh-CN,zh;q=0.9",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "referer": "https://wannianli.tianqi.com/",
    }
    try:
        res = requests.get(
            "https://wannianli.tianqi.com/Public/Home/js/workTime.js", headers=headers
        )
        matches = re.search(r"var json='(\{.*\})';", res.text)
        if matches:
            data = matches.group(1)
            this_year = datetime.today().strftime("%Y")
            data = json.loads(data)
            return {
                this_year + k[1:]: True if v["w"] == "上班" else False
                for k, v in data.items()
            }
    except Exception as e:
        print(e)

    return {}


def get_workdate_of_month(year: int, month: int):
    ret = {}
    query_str = f"{year}年{month}月"
    url = f"https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?tn=wisetpl&format=json&resource_id=39043&query={query_str}"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,be;q=0.7",
        "Connection": "keep-alive",
        "Host": "sp1.baidu.com",
        "Referer": "https://www.baidu.com/s?wd=%E4%BB%8A%E5%A4%A9&rsv_spt=1&rsv_iqid=0xc77d2e650003bd96&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=ts_1&rsv_enter=1&oq=2022%25E8%258A%2582%25E5%2581%2587%25E6%2597%25A5&rsv_t=6a9381PGweuDpLBI3EjP%2F%2Fsjin42zIEuSSIK9rI%2FPDocIU%2BQeNqsQMv35uJxOavzQh%2FM&rsv_btype=t&inputT=5249&rsv_pq=bcc2cffd000e5eeb&rsv_sug3=36&rsv_sug1=33&rsv_sug7=101&rsv_sug2=0&prefixsug=jintian&rsp=1&rsv_sug4=6587",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    }
    try:
        res = requests.get(url, headers=headers)
        data = json.loads(res.text)
        for item in data["data"][0]["almanac"]:
            if "status" in item:
                year = int(item["year"])
                month = int(item["month"])
                day = int(item["day"])
                ret[f"{year}{month:02d}{day:02d}"] = (
                    True if item["status"] == "2" else False
                )
    except Exception as e:
        print(e)
    return ret


def is_workday(day=None):
    if day is None:
        day = datetime.today()
    elif isinstance(day, str):
        day = datetime.fromisoformat(day)
    workdate = get_workdate_this_year()
    if not workdate:
        workdate = get_workdate_of_month(day.year, day.month)
    today = day.strftime("%Y%m%d")
    if today in workdate:
        return workdate[today]
    weekday = day.weekday()
    return weekday <= 4


if __name__ == "__main__":
    print(is_workday())
