from pyalgotrade import strategy
from pyalgotrade.technical import ma
from pyalgotrade.technical import rsi
from pyalgotrade.technical import cross
import random


# Strategy Takes a list of instruments and tries to lowball on the price
class MyStrat(strategy.BacktestingStrategy):
    def __init__(self, feed, instruments):
        super(MyStrat, self).__init__(feed)
        self.__instruments = instruments
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
    
    def getSMA(self):
        return self.__smaLow,self.__smaHigh

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):
        