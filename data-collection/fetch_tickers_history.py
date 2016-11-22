import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/quandl')
sys.path.append(dir_path + '/db')
import rest_client
import date_time_util
from TickerDao import TickerDao
from TickerHistory import TickerHistory
from TickerHistoryDao import TickerHistoryDao

tickerDao = TickerDao()
tickerHistoryDao = TickerHistoryDao()

def get_tickers_for_updating(last_business_date):
    tickers_for_history_update = []
    tickers = tickerDao.getAllTickers()
    for ticker in tickers:
        if (ticker.last_update_date is None or ticker.last_update_date < last_business_date):
            tickers_for_history_update.append(ticker)
    return tickers_for_history_update        

def get_ticker_history_for_missing_days(ticker, num_days_of_eod_data_missing):
    json = rest_client.get_ticker_eod_data(ticker.symbol, num_days_of_eod_data_missing)
    if json is not None:
        return convertJsonToHistory(ticker, json['dataset']['data'])

def convertJsonToHistory(ticker, data):
    history = []
    for element in data:
        tickerHistory = TickerHistory()
        tickerHistory.symbol = ticker.symbol
        tickerHistory.date = element[0]
        tickerHistory.name = ticker.name
        tickerHistory.open = element[1]
        tickerHistory.high = element[2]
        tickerHistory.low = element[3]
        tickerHistory.close = element[4]
        tickerHistory.volume = element[5]
        tickerHistory.exchange = ticker.exchange        
        history.append(tickerHistory)
    return history

def save_ticker_history(tickerHistor):
    tickerHistoryDao.insertTickerHistory(tickerHistor)
    
def change_ticker_last_updated_date(ticker_id, last_updated_date):
    tickerDao.update_ticker_last_update_date(ticker_id, last_updated_date)

def get_number_of_missing_history_days(ticker, last_business_day):
    if ticker.last_update_date is None:
        return 5
    num_days_of_eod_data_missing = date_time_util.get_num_business_days_between(ticker.last_update_date, last_business_day)
    return num_days_of_eod_data_missing
    
###########################################################    
last_business_day = str(date_time_util.get_last_business_day())
print 'last_business_day:' + last_business_day
tickers = get_tickers_for_updating(last_business_day)
print(str(len(tickers)) + " retrieved")
for ticker in  tickers:
    number_of_missing_history_days = get_number_of_missing_history_days(ticker, last_business_day)
    if number_of_missing_history_days != 0:
        history = get_ticker_history_for_missing_days(ticker, number_of_missing_history_days)
        if history is not None:
            print(str(len(history)) + " retrieved for " + ticker.symbol)
            #change last_updated_date of ticker to last_business_day
            save_ticker_history(history)
            change_ticker_last_updated_date(ticker.ticker_id, last_business_day)
            print('History saved for ' + ticker.symbol)
            count = count + 1
        else:
            print "No history retrieved for " + ticker.symbol
tickerDao.commit_transaction()
tickerHistoryDao.commit_transaction()            
###########################################################        
        
    
    
#print tickers