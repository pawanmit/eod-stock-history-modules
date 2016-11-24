import sys
import os 
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../db')
sys.path.append(dir_path + '/..')
import date_time_util
from TickerHistory import TickerHistory
from TickerHistoryDao import TickerHistoryDao
from BasicJsonEncoder import BasicJsonEncoder



def get_most_advanced_tickers(exchange, last_business_day):
    advanced_tickers = tickerHistoryDao.get_ticker_history_ordered_by_column(exchange, last_business_day, 'percent_change', 'DESC', 10);
    return advanced_tickers

def get_most_declined_tickers(exchange, last_business_day):
    declined_tickers = tickerHistoryDao.get_ticker_history_ordered_by_column(exchange, last_business_day, 'percent_change', 'ASC', 10);
    return declined_tickers

def get_most_active_tickers(exchange, last_business_day):
    active_tickers = tickerHistoryDao.get_ticker_history_ordered_by_column(exchange, last_business_day, 'volume', 'DESC', 10);
    return active_tickers

tickerHistoryDao = TickerHistoryDao()
last_business_day = str(date_time_util.get_last_business_day())
exchange = 'NYSE'
most_advanced_tickers = get_most_advanced_tickers(exchange, last_business_day)
most_declined_tickers = get_most_declined_tickers(exchange, last_business_day)
most_active_tickers = get_most_active_tickers(exchange, last_business_day)

daily_highlight = {'most_advanced_tickers': most_advanced_tickers, 'most_declined_tickers': most_declined_tickers, 'most_active_tickers': most_active_tickers}

#print most_advanced_tickers[1].toJSON()
#print json.dumps(daily_highlight, cls=BasicJsonEncoder)
print json.dumps(daily_highlight, cls=BasicJsonEncoder, sort_keys=True, indent=4, separators=(',', ': '))