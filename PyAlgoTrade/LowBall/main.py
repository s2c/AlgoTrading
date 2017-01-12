import sys, getopt,os
#sys.path.append(os.path.join(os.path.dirname(__file__), '../CustFeeds/', '..'))
from datetime import date,time
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
from pyalgotrade import plotter
from pyalgotrade.barfeed import csvfeed
from pyalgotrade.bar import Frequency
from pyalgotrade import strategy
from pyalgotrade import dataseries
from DataFrameBarFeed import *
from pyalgotrade import strategy
from pyalgotrade.technical import ma
from pyalgotrade.technical import rsi
from pyalgotrade.technical import cross
import talib
import pandas as pd

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, smaPeriod_low,smaPeriod_high):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__smaLow = ma.SMA(self.__prices, smaPeriod_low)
        self.__smaHigh = ma.SMA(self.__prices, smaPeriod_high)

    def onBars(self, bars):
    	if self.__position is None:
	    	#if bars[self.__instrument].getDateTime().time() > time(11,0,0):
            shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
            # Enter a buy market order. The order is good till canceled.
            self.__position = self.enterLong(self.__instrument, shares, True)
            #  print("Entered Long")
        #elif not self.__position.exitActive()  and bars[self.__instrument].getDateTime().time() > time(13,0,0):
        #    self.__position.exitMarket()
     	elif not self.__position.exitActive():
     		self.__position.exitMarket()
     	# self.info("%s %s" % (bars[self.__instrument].getClose(),bars[self.__instrument].getDateTime()))

def main(argv):
	data = pd.read_csv('../../Data/GSPC_1m.csv', index_col=2, parse_dates=True,sep=';',decimal=',')
	data.drop(data.columns[[0,1]], axis=1, inplace=True)
	data = data.reindex(data.index.rename('Date Time'))
	data = DataFrameDateFilter(data,date(2012,7,9),date(2012,7,10))
	inst = 'SP500'
	feed = DataFrameBarFeed(dataframe=data, instrument=inst, frequency=barfeed.Frequency.MINUTE,barsHaveAdj=False)
	
	myStrategy = MyStrategy(feed, "SP500",smaPeriod_high=60,smaPeriod_low=15)

	sharpeRatioAnalyzer = sharpe.SharpeRatio()
	myStrategy.attachAnalyzer(sharpeRatioAnalyzer)

	# Attach a returns analyzers to the strategy.
	returnsAnalyzer = returns.Returns()
	myStrategy.attachAnalyzer(returnsAnalyzer)

	plt = plotter.StrategyPlotter(myStrategy)
	plt.getOrCreateSubplot("returns").addDataSeries("Simple returns", returnsAnalyzer.getReturns())
	myStrategy.run()
	myStrategy.info("Final portfolio value: $%.2f" % myStrategy.getResult())
	print "Sharpe ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05)

	plt.plot()




if __name__ == "__main__":
    main(sys.argv[1:])