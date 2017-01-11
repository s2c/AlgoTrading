import datetime

#from pandas.io import data
import pandas as pd
from pyalgotrade import strategy
from pyalgotrade import barfeed
from pyalgotrade import bar


# Example BarFeed for dataframes with data for a single instrument.
class DataFrameBarFeed(barfeed.BaseBarFeed):
    def __init__(self, dataframe, instrument, frequency,barsHaveAdj=True):
        super(DataFrameBarFeed, self).__init__(frequency)
        self.registerInstrument(instrument)
        self.__df = dataframe
        self.__instrument = instrument
        self.__next = 0
        self.__barsHaveAdj = barsHaveAdj

    def reset(self):
        super(DataFrameBarFeed, self).reset()
        self.__next = 0

    def peekDateTime(self):
        return self.getCurrentDateTime()

    def getCurrentDateTime(self):
        ret = None
        if not self.eof():
            rowkey = self.__df.index[self.__next]
            ret = rowkey.to_datetime()
        return ret

    def barsHaveAdjClose(self):
        if self.__barsHaveAdj:
            return True
        else:
            return False
    def getNextBars(self):
        ret = None
        if not self.eof():
            # Convert the dataframe row into a bar.BasicBar
            rowkey = self.__df.index[self.__next]
            row = self.__df.ix[rowkey]
            if self.barsHaveAdjClose():
                bar_dict = {
                    self.__instrument: bar.BasicBar(
                        rowkey.to_datetime(),
                        row["open"],
                        row["high"],
                        row["low"],
                        row["close"],
                        row["volume"],
                        row["adj Close"],
                        self.getFrequency()
                    )
                }
            else:
                bar_dict = {
                    self.__instrument: bar.BasicBar(
                        rowkey.to_datetime(),
                        row["open"],
                        row["high"],
                        row["low"],
                        row["close"],
                        row["volume"],
                        None,
                        self.getFrequency()
                    )
                }
            ret = bar.Bars(bar_dict)
            self.__next += 1
        return ret

    def eof(self):
        return self.__next >= len(self.__df.index)

    def start(self):
        pass

    def stop(self):
        pass

    def join(self):
        pass

# class MyStrategy(strategy.BacktestingStrategy):
#     def onBars(self, bars):
#         for instrument in bars.getInstruments():
#             bar = bars[instrument]
#             self.info("%s: %s %s %s %s %s %s" % (
#                 instrument,
#                 bar.getOpen(),
#                 bar.getHigh(),
#                 bar.getLow(),
#                 bar.getClose(),
#                 bar.getAdjClose(),
#                 bar.getVolume(),
#             ))


# def main():
#     inst = 'SP500'
#     data = pd.read_csv('../Data/GSPC_1m.csv', index_col=2, parse_dates=True,sep=';',decimal=',')
#     data.drop(data.columns[[0,1]], axis=1, inplace=True)
#     data = data.reindex(data.index.rename('Date Time'))
#     feed = DataFrameBarFeed(dataframe=data, instrument=inst, frequency=barfeed.Frequency.MINUTE,barsHaveAdj=False)
#     myStrategy = MyStrategy(feed)
#     myStrategy.run()


# if __name__ == "__main__":
#     main()