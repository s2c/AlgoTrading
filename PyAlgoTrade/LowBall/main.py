import sys, getopt
from datetime import date
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
from pyalgotrade.barfeed import csvfeed
from pyalgotrade.bar import Frequency
from pyalgotrade.technical import ma
from pyalgotrade import strategy
from pyalgotrade import dataseries
import .../CustFeeds/DataFrameBarFeed
#from pyalgotrade import talibext
#from pyalgotrade.talibext import indicator
import talib
import pandas as pd

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument,start=None,end=None):
        super(MyStrategy, self).__init__(feed)
        # We want a 15 period SMA over the closing prices.
        self.__instrument = instrument
     #   self.__priceDataSeries = dataseries.SequenceDataSeries()
        self.__sma = ma.SMA(feed[instrument].getCloseDataSeries(), 15)
     #   self.__start = start
     #   self.__end = end

    # def checkTime(self,bar):
    # 	if bar.getDateTime().date() < self.__start:
    # 		self.__sma = None
    # 		return True 
    # 	elif bar.getDateTime().date() > self.__end:
    # 		for each_item in xrange(0,self.__priceDataSeries.__len__()):
    # 			print self.__priceDataSeries.__getitem__(each_item)
    # 		self.stop()
    # 		return True
    # 	else:
    # 		#pass
    # 		#self.__sma = ma.SMA(bar.getPrice(), 15)
    # 		self.__priceDataSeries.appendWithDateTime(bar.getDateTime(),bar.getClose())
    # 		#print bar.getClose(),bar.getDateTime()
    # 		#print self.__priceDataSeries.__getitem__(0)
    # 		#self.stop()
    # 		#return True
    # 		self.__sma = indicator.SMA(self.__priceDataSeries,15)


    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info("%s %s" % (self.__sma[-1]))
        # if self.checkTime(bar):
        # 	pass
        # else:
	       #  self.info("%s %s" % (bar.getDateTime(),type(self.__priceDataSeries)))#self.__sma[-1]))



def main(argv):
	data = pd.read_csv('../../Data/GSPC_1m.csv', index_col=2, parse_dates=True,sep=';',decimal=',')
	data.drop(data.columns[[0,1]], axis=1, inplace=True)
	data = data.reindex(data.index.rename('Date Time'))
	
	inst = 'SP500'
	feed = DataFrameBarFeed(dataframe=data, instrument=inst, frequency=barfeed.Frequency.MINUTE,barsHaveAdj=False)
	# feed.addBarsFromCSV("SP500","../../Data/SP500_Corrected.csv")
	# data_filter =  DateRangeFilter(fromDate=date(2012,7,13), toDate=date(2012,7,14))
	# feed.setBarFilter(data_filter)

	# myStrategy = MyStrategy(feed, "SP500",start=date(2012,7,13),end=date(2012,7,14))
	# myStrategy.run()




if __name__ == "__main__":
    main(sys.argv[1:])