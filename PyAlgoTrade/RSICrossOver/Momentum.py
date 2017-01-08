from pyalgotrade import strategy
from pyalgotrade.technical import ma
from pyalgotrade.technical import rsi
from pyalgotrade.technical import cross
import random



class Momentum(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, smaPeriod_low,smaPeriod_high):
        super(Momentum, self).__init__(feed)
        self.__instrument = instrument
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__smaLow = ma.EMA(self.__prices, smaPeriod_low)
        self.__smaHigh = ma.EMA(self.__prices, smaPeriod_high)
        self.__RsiLow = rsi.RSI(self.__prices, smaPeriod_low)
        self.__RsiHigh = rsi.RSI(self.__prices, smaPeriod_high)
        self.__RSILimLow = 40
        self.__RSILimHigh = 60
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
        # If a position was not opened, check if we should enter a long position.
        if self.__smaHigh[-1] is None:
            return
            print(self.__RsiLow[-1])    
        elif self.__position is None:
            if cross.cross_above(self.__smaLow, self.__smaHigh) and self.__RsiLow[-1] < self.__RSILimLow:
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                # Enter a buy market order. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)
                print("ENTERED LONG")
                print (self.__RsiHigh[-1])

            elif cross.cross_below(self.__smaLow, self.__smaHigh) and self.__RsiLow[-1] > self.__RSILimHigh: #and self.__RsiHigh[-1] < self.__RSILim :
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                # Enter a buy market order. The order is good till canceled.
                self.__position = self.enterShort(self.__instrument, shares, True)
                print (self.__RsiHigh[-1])
                print("ENTERED SHORT")

        elif not self.__position.exitActive():
            if self.__position.getEntryOrder().getType() ==1 and self.__RsiHigh[-1] > self.__RSILimLow: #or self.__position.getReturn() > 130 or self.__position.getReturn() < 90):
	            self.__position.exitMarket()
            elif self.__position.getEntryOrder().getType() ==4 or self.__RsiHigh[-1] < self.__RSILimHigh:
                self.__position.exitMarket()
