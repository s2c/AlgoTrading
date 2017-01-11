# -*- coding: utf-8 -*-
from datetime import datetime
from zipline.api import order, record, symbol,order_target
from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_bars_from_yahoo
from collections import OrderedDict
import pytz
import pandas as pd
import pyexcel


# data = {}
# data["SP500"] = pd.read_csv("../../Data/GSPC_1m.csv", index_col=2, parse_dates=True,sep=';',decimal=',')
# data["SP500"].drop(data["SP500"].columns[[0,1]], axis=1, inplace=True)

# panel = pd.Panel(data)
# panel.minor_axis = ['Open', 'High', 'Low', 'Close', 'Volume']

# panel.major_axis = panel.major_axis.tz_localize(pytz.utc)

# print panel["SP500"].head()

# Load data manually from Yahoo! finance
start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc).date()
end = datetime(201z,1,1,0,0,0,0, pytz.utc).date()
 
# data = load_bars_from_yahoo(stocks=['SPY'], start=start,end=end)

# def initialize(context):
# 	context.security = symbol('SPY')

# def handle_data(context,data):
# 	MA1 = data[context.security].mavg(50)
# 	MA2 = data[context.security].mavg(100)
# 	date = str(data[context.security].datetime)[:10]
# 	current_price = data[context.security].price
# 	current_positions = context.portfolio.positions[symbol('SPY')].amount
# 	cash = context.portfolio.cash
# 	value = context.portfolio.portfolio_value
# 	current_pnl = context.portfolio.pnl

# 	#code (this will come under handle_data function only)
# 	if (MA1 > MA2) and current_positions == 0:
# 	    number_of_shares = int(cash/current_price)
# 	    order(context.security, number_of_shares)
# 	    record(date=date,MA1 = MA1, MA2 = MA2, Price= 
# 	current_price,status="buy",shares=number_of_shares,PnL=current_pnl,cash=cash,value=value)
	 
# 	elif (MA1 < MA2) and current_positions != 0:
# 	     order_target(context.security, 0)
# 	     record(date=date,MA1 = MA1, MA2 = MA2, Price= current_price,status="sell",shares="--",PnL=current_pnl,cash=cash,value=value)
	 
# 	else:
# 	    record(date=date,MA1 = MA1, MA2 = MA2, Price= current_price,status="--",shares="--",PnL=current_pnl,cash=cash,value=value)

# algo_obj = TradingAlgorithm(initialize=initialize,handle_data=handle_data)
# perf_manual = algo_obj.run(data)
# perf_manual[["MA1","MA2","Price"]].plot()