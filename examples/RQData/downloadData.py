# encoding: UTF-8

"""
立即下载数据到数据库中，用于手动执行更新操作。
"""

from dataService import *
"""
RiceQuant 关于合约的说明见
https://www.ricequant.com/data/futures#Data%E2%80%94Futures-ContinuousContract-MainContract
主力连续合约于指数连续合约
+88 是主力
+99 是指数
"""

if __name__ == '__main__':
    #downloadMinuteBarBySymbol('CU99')
  
    # downloadMinuteBarBySymbol('I88')
    # downloadMinuteBarBySymbol('IF88')
    # downloadMinuteBarBySymbol('RB88')
    # downloadMinuteBarBySymbol('TA88')
   
    # downloadDailyBarBySymbol('I88')
    # downloadDailyBarBySymbol('IF88')
    # downloadDailyBarBySymbol('RB88')
    # downloadDailyBarBySymbol('TA88')

    #downloadDailyBarBySymbol('I88')
    #downloadDailyBarBySymbol('IF88')
    #downloadDailyBarBySymbol('RB88')
    #downloadDailyBarBySymbol('TA88')

    downloadTickBySymbol('IF1901', '2018-12-21', '2018-12-30')