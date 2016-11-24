import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/quandl')
sys.path.append(dir_path + '/../db')
sys.path.append(dir_path + '/..')
import rest_client
import date_time_util
from Ticker import Ticker
from TickerDao import TickerDao

def get_active_tickers(last_business_date):
    tickers = []
    ticker_rows = rest_client.get_all_tickers()
    for ticker_row in ticker_rows:
        last_trade_day = ticker_row[3]
        if last_trade_day == last_business_date:
            ticker =  get_ticker_from_row(ticker_row)
            tickers.append(ticker)
    return tickers

def get_ticker_from_row(ticker_row):
    symbol = ticker_row[0].replace('.', '_')
    name = ticker_row[1]
    exchange = ticker_row[2]
    ticker = Ticker(symbol, name, exchange, None)
    return ticker
        

def save_tickers(tickers):
    tickerDao = TickerDao()
    tickerDao.delete_all_tickers()
    tickerDao.insert_tickers(tickers)

last_business_day = str(date_time_util.get_last_business_day())
print "Fetching tickers active on "  + last_business_day

tickers =   get_active_tickers(last_business_day) 
save_tickers(tickers)