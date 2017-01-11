import sys, getopt,os
#sys.path.append(os.path.join(os.path.dirname(__file__), '../CustFeeds/', '..'))
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
#from DataFrameBarFeed import *
from DataFrameBarFeed import *
#from pyalgotrade import talibext
#from pyalgotrade.talibext import indicator
import talib
import pandas as pd

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument,start=None,end=None):
        super(MyStrategy, self).__init__(feed)
        # We want a 15 period SMA over the closing prices.
        self.__instrument = instrument
        self.__sma = ma.SMA(feed[instrument].getCloseDataSeries(), 15)


    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info("%s" % (self.__sma[-1]))
        # if self.checkTime(bar):
        # 	pass
        # else:
	       #  self.info("%s %s" % (bar.getDateTime(),type(self.__priceDataSeries)))#self.__sma[-1]))



def main(argv):
	data = pd.read_csv('../../Data/GSPC_1m.csv', index_col=2, parse_dates=True,sep=';',decimal=',')
	data.drop(data.columns[[0,1]], axis=1, inplace=True)
	data = data.reindex(data.index.rename('Date Time'))
	data = DataFrameDateFilter(data,date(2012,7,12),date(2012,7,13))
	inst = 'SP500'
	feed = DataFrameBarFeed(dataframe=data, instrument=inst, frequency=barfeed.Frequency.MINUTE,barsHaveAdj=False)
	
	myStrategy = MyStrategy(feed, "SP500",start=date(2012,7,13),end=date(2012,7,14))
	myStrategy.run()




if __name__ == "__main__":
    main(sys.argv[1:])