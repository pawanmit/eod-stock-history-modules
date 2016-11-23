from TickerHistory import TickerHistory
from BaseDao import BaseDao

class TickerHistoryDao:
    
    def __init__(self):
        self.baseDao = BaseDao()
    
    def insertTickerHistory(self, history):
        formattedSql = "INSERT INTO ticker_history(symbol, name, date, open, high, low, close, volume, exchange) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"
        for tickerHistory in history:
            vars = (tickerHistory.symbol, tickerHistory.name, tickerHistory.date, tickerHistory.open, tickerHistory.high, 
                    tickerHistory.low, tickerHistory.close, tickerHistory.volume, tickerHistory.exchange)
            query = formattedSql.format(*vars)
            try:
                #print query
                self.baseDao.execute(query)
            except Exception, e:
                print e
                print "Error saving ticker history for " + tickerHistory.symbol

    def get_latest_ticker_history(self, symbol, num_rows):
        formattedSql = "SELECT * FROM ticker_history WHERE symbol = '{0}' ORDER BY date DESC LIMIT '{1}'";
        vars = (symbol, num_rows)
        query = formattedSql.format(*vars)
        cursor = self.baseDao.execute(query)
        history = []
        for row in cursor:
            ticker_history = self.get_ticker_history_from_row(row)
            history.append(ticker_history)
        return history   
        
    def get_ticker_history_from_row(self, ticker_history_row):
        ticker_history = TickerHistory()
        ticker_history.id = ticker_history_row[0]
        ticker_history.symbol = ticker_history_row[1]
        ticker_history.date = ticker_history_row[2]
        ticker_history.name = ticker_history_row[3]
        ticker_history.open = ticker_history_row[4]
        ticker_history.high = ticker_history_row[5]
        ticker_history.low = ticker_history_row[6]
        ticker_history.close = ticker_history_row[7]
        ticker_history.volume = ticker_history_row[8]
        ticker_history.exchange = ticker_history_row[9]
        return ticker_history
        
    def commit_transaction(self):
        self.baseDao.commit() 
    
    def rollback_transaction(self):
        self.baseDao.commit() 
