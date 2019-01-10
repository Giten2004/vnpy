# encoding: UTF-8

"""
历史数据服务端。
"""


# add dev vnpy path to search modules
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))

from vnpy.trader.app.ctaStrategy.ctaBacktesting import runHistoryDataServer

runHistoryDataServer()