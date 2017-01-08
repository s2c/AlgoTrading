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
    

if __name__ == "__main__":
    main(sys.argv[1:])