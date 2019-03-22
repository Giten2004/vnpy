# encoding: UTF-8

import csv
from datetime import datetime

from pymongo import MongoClient

from vnpy.trader.app.ctaStrategy.ctaBase import MINUTE_DB_NAME

if __name__ == '__main__':
    mc = MongoClient()
    db = mc[MINUTE_DB_NAME]
    cl = db["IF888"]
    cl.ensure_index("datetime")

    with open("data.csv") as f:
        reader = csv.DictReader(f)

        for d in reader:
            d["open"] = float(d["open"])
            d["high"] = float(d["high"])
            d["low"] = float(d["low"])
            d["close"] = float(d["close"])
            d["volume"] = float(d["volume"])
            d["datetime"] = datetime.strptime(d["date"] + " " + d["time"], "%Y%m%d %H:%M:%S")
            cl.insert(d)
            print d["datetime"]

            


