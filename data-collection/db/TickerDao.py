from BaseDao import BaseDao
from Ticker import Ticker

class TickerDao:
    
    def __init__(self):
        self.baseDao = BaseDao()
    
    def insertTickers(self, tickers):
        count = 0
        formattedSql = 'INSERT INTO ticker(symbol, name, exchange) VALUES ("{0}","{1}","{2}")'
        for ticker in tickers:
            vars = (ticker.symbol, ticker.name, ticker.exchange)
            query = formattedSql.format(*vars)
            try:
                #print query
                self.baseDao.execute(query)
                count +=1
            except Exception, e:
                print e
                print "Error saving ticker " + ticker.getDisplayText()
            #continue
        self.baseDao.commit()     
        print str(count) + " tickers saved into ticker table"
        
    def getAllTickers(self):
        query = 'SELECT * FROM ticker'
        tickers = []
        cursor = self.baseDao.execute(query)
        for row in cursor:
            ticker_entity = self.get_ticker_entity_from_row(row)
            tickers.append(ticker_entity)
        self.baseDao.commit() 
        #print str(len(tickers)) + " tickers retrieved from ticker table"
        return tickers
           
    def get_ticker_entity_from_row(self, ticker_row):
        symbol = ticker_row[1]
        name = ticker_row[2]
        exchange = ticker_row[3]
        last_update_date = ticker_row[4]
        ticker_entity = Ticker(symbol, name, exchange, last_update_date)
        ticker_entity.ticker_id = ticker_row[0]
        return ticker_entity
    
    def update_ticker_last_update_date(self, ticker_id, last_update_date):
        formattedSql = 'UPDATE ticker SET last_update_date="{0}" WHERE ticker_id="{1}"'
        vars = (last_update_date, ticker_id)
        query = formattedSql.format(*vars)
        self.baseDao.execute(query)
        
    def commit_transaction(self):
        self.baseDao.commit() 
    
    def rollback_transaction(self):
        self.baseDao.commit() 
        


        
# tickerDao = TickerDao()
# tickerDao.getAllTickers()