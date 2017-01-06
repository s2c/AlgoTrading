# import MyStrategy
# import sys, getopt
# from pyalgotrade import plotter
# from pyalgotrade.tools import yahoofinance
# from pyalgotrade.stratanalyzer import sharpe


# def main(argv):
#     instrument = argv[0]
#     plot = argv[1]
#     smaPeriodLow = 30
#     smaPeriodHigh = 90
#     #stockList = ["AAPL", "GOOG", "MSFT","NOK","INX","DIA"]
#     # Download the bars.
#     feed = yahoofinance.build_feed([instrument], 2006,2007, "./Data2")

#     strat = MyStrategy.MyStrategy(feed, instrument, smaPeriodLow,smaPeriodHigh)
#     sharpeRatioAnalyzer = sharpe.SharpeRatio()
#     strat.attachAnalyzer(sharpeRatioAnalyzer)

#     if plot:
#         plt = plotter.StrategyPlotter(strat, True, False, True)
    
#     strat.run()
#     print "Sharpe ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05)

#     if plot:
#         plt.plot()


# if __name__ == "__main__":
#     main(sys.argv[1:])



import 
import sys, getopt
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades

def main(argv):
 #   instrument = argv[0]
    stockList = ["AAPL", "GOOG", "MSFT","NOK","DIA","^GSPC"]
    plot = argv[0]
    smaPeriodLow = 7
    smaPeriodHigh = 15
    # Download the bars.
    totalPortVal = 0
    totalCumRet = 0
    totalSharpeRat = 0
    stockCount = 0
    divider = 1
    errCount = 0
    for count,symbol in enumerate(stockList, start=1):
        if count % divider == 0:
            try:
                feed = yahoofinance.build_feed([symbol], 2001,2003, "./Data2")
            except :
                errCount = errCount + 1
                continue
            strat = MyStrategy.MyStrategy(feed, symbol, smaPeriodLow,smaPeriodHigh)
            retAnalyzer = returns.Returns()
            strat.attachAnalyzer(retAnalyzer)
            sharpeRatioAnalyzer = sharpe.SharpeRatio()
            strat.attachAnalyzer(sharpeRatioAnalyzer)

            if plot:
                plt = plotter.StrategyPlotter(strat, True, False, True)
               
            strat.run()
           
            print "Final portfolio value: $%.2f" % strat.getResult()
            print "Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100)

            if plot:
                plt.plot()
            totalPortVal = totalPortVal +  strat.getResult()
            totalCumRet = totalCumRet + (retAnalyzer.getCumulativeReturns()[-1] * 100)
            totalSharpeRat = totalSharpeRat + (sharpeRatioAnalyzer.getSharpeRatio(0.05)) 
            stockCount = stockCount + 1
                
    print errCount,stockCount
    print totalPortVal/stockCount
    print totalCumRet/stockCount
    print totalSharpeRat/stockCount
if __name__ == "__main__":
    main(sys.argv[1:])