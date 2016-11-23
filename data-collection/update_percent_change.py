import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../db')
from TickerDao import TickerDao
from TickerHistory import TickerHistory
from TickerHistoryDao import TickerHistoryDao

tickerDao = TickerDao()
tickerHistoryDao = TickerHistoryDao()

def get_tickers_for_updating():
    tickers = tickerDao.getAllTickers()
    return tickers

def get_latest_two_ticker_history(ticker):
    ticker_history = tickerHistoryDao.get_latest_ticker_history(ticker.symbol, ticker.exchange, 2)
    return ticker_history

def calculate_percentage_change_for_latest(ticker_history):
    latest_close_price = ticker_history[0].close
    previous_close_price = ticker_history[1].close
    relative_change = (latest_close_price - previous_close_price) / previous_close_price
    percent_change = relative_change * 100
    return "{0:.2f}".format(percent_change)

def update_ticker_history(ticker_history, percent_change):
    tickerHistoryDao.update_percent_change(ticker_history.id, percent_change)

tickers =  get_tickers_for_updating()
for ticker in tickers:
    ticker_history = get_latest_two_ticker_history(ticker)
    if ticker_history and len(ticker_history) > 1:
        percent_change = calculate_percentage_change_for_latest(ticker_history)
        update_ticker_history(ticker_history[0], percent_change)
        print ticker.symbol + ':' + str(percent_change)
    else:
        print 'Unable to update percent change for:' + ticker.symbol
tickerHistoryDao.commit_transaction()        