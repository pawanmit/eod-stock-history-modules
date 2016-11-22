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

    def commit_transaction(self):
        self.baseDao.commit() 
    
    def rollback_transaction(self):
        self.baseDao.commit() 
