class Ticker:
    
    ticker_id = None
    def __init__(self, symbol, name, exchange, last_update_date):        
        self.symbol = symbol
        self.name = name
        self.exchange = exchange
        self.last_update_date = last_update_date
        
    def getDisplayText(self):
        return self.symbol + "," + self.name + ","+ self.exchange