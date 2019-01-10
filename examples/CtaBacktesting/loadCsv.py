# encoding: UTF-8

"""
导入MC导出的CSV历史数据到MongoDB中
"""
# add dev vnpy path to search modules
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))

from vnpy.trader.app.ctaStrategy.ctaBase import MINUTE_DB_NAME
from vnpy.trader.app.ctaStrategy.ctaHistoryData import loadMcCsv


if __name__ == '__main__':
    loadMcCsv('IF0000_1min.csv', MINUTE_DB_NAME, 'IF0000')
    loadMcCsv('rb0000_1min.csv', MINUTE_DB_NAME, 'rb0000')

