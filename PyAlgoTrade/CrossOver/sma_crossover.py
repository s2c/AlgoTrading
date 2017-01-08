from pyalgotrade import strategy
from pyalgotrade.technical import ma
from pyalgotrade.technical import rsi
from pyalgotrade.technical import cross
import random



class SMACrossOver(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, smaPeriod_low,smaPeriod_high):
        super(SMACrossOver, self).__init__(feed)
        self.__instrument = instrument
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__smaLow = ma.SMA(self.__prices, smaPeriod_low)
        self.__smaHigh = ma.SMA(self.__prices, smaPeriod_high)
        self.__RsiLow = rsi.RSI(self.__prices, smaPeriod_low)
        self.__RsiHigh = rsi.RSI(self.__prices, smaPeriod_high)
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
        if self.__position is None:
            if cross.cross_above(self.__smaLow, self.__smaHigh) > 0:# and cross.cross_below(self.__RsiHigh, self.__RsiLow) > 0:
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                # Enter a buy market order. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)
                print("Entered Long")
             #   print(type(self.__position.getEntryOrder().getAction()))
        # If a position was not opened, check if we should enter a short position if possible.
            # elif cross.cross_below(self.__smaLow, self.__smaHigh) > 0:# and cross.cross_below(self.__RsiHigh, self.__RsiLow) > 0:
            #     shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
            #     # Enter a buy market order. The order is good till canceled.
            #     self.__position = self.enterShort(self.__instrument, shares, True)
            #     print("Entered Short")
                #print(type(self.__position.getEntryOrder().getAction()))        
        # Check if we have to exit the position.
        elif not self.__position.exitActive():
            if self.__position.getEntryOrder().getAction() == 1 and cross.cross_below(self.__smaLow, self.__smaHigh) > 0 :
	            self.__position.exitMarket()
            # elif self.__position.getEntryOrder().getAction() == 4 and cross.cross_above(self.__smaLow, self.__smaHigh) > 0:
            # 	self.__position.exitMarket()