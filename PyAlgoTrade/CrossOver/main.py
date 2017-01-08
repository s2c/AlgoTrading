import sma_crossover
import sys, getopt
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
from pyalgotrade.stratanalyzer import sharpe


def main(argv):
    instrument = argv[0]
    plot = argv[1]
    smaPeriodLow = 15
    smaPeriodHigh = 90

    # Download the bars.
    feed = yahoofinance.build_feed([instrument], 2006,2007, ".")

    strat = sma_crossover.SMACrossOver(feed, instrument, smaPeriodLow,smaPeriodHigh)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)

    if plot:
        plt = plotter.StrategyPlotter(strat, True, False, True)
    #   plt.getInstrumentSubplot(instrument).addDataSeries("sma", strat.getSMA())

    strat.run()
    print "Sharpe ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05)

    if plot:
        plt.plot()


if __name__ == "__main__":
    main(sys.argv[1:])