# encoding: UTF-8

import multiprocessing
from datetime import datetime, time
from time import sleep

from dataService import downloadDailyBarBySymbol, setting


#----------------------------------------------------------------------
def runChildProcess():
    """子进程运行函数"""
    print "-" * 60
    print u"开始更新日K线数据"
    
    for symbol in setting["symbols"]:
        downloadDailyBarBySymbol(symbol)
    
    print u"日K线数据更新完成"
    print "-" * 60
    
#----------------------------------------------------------------------
def runParentProcess():
    """守护进程运行函数"""
    updateDate = None   # 已更新数据的日期
    
    while True:
        # 每轮检查等待5秒，避免跑满CPU（浪费算力）
        sleep(5)
        
        currentTime = datetime.now().time()
        
        print "#" * 60
        print u"当前时间为：", currentTime
        
        # 过滤交易日
        today = datetime.now().date()
        weekday = datetime.now().weekday()
        if weekday in [5, 6]:       # 从0开始，周六为5，周日为6
            continue
        
        # 每日5点后开始下载当日数据，通常3:15收盘后（国债）数据提供商需要一定时间清洗数据）
        if currentTime <= time(17, 0):
            continue
        
        # 每日只需要更新一次数据
        if updateDate == today:
            continue
        
        # 启动子进程来更新数据
        p = multiprocessing.Process(target=runChildProcess)
        
        p.start()
        print u"启动子进程"
        
        p.join()
        print u"子进程已关闭"
        
        # 记录当日数据已经更新
        updateDate = today      


if __name__ == "__main__":
    runParentProcess()