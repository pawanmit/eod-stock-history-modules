import json
class TickerHistory:
    id = None
    symbol = None
    date = None
    name = None
    open = None
    high = None
    low = None
    close = None
    volume = None
    exchange = None
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)    