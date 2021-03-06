import sys
sys.path.append('..')
import DBConstants
import sqlite3

print DBConstants.PATH_TO_STOCKS_DB

conn = sqlite3.connect(DBConstants.PATH_TO_STOCKS_DB)
c = conn.cursor()

print "Creating schema for stocks.db......"

# Create table
c.execute('''CREATE TABLE ticker_history
            (
            ticker_history_id integer primary key autoincrement,
            symbol text not null,
            name text not null,
            date text not null, 
            open real not null, 
            high real not null, 
            low real not null, 
            close real not null, 
            volume real not null, 
            exchange text not null,
            unique (symbol, exchange, date))'''
            )
c.execute('''CREATE TABLE ticker
                (ticker_id integer primary key autoincrement,
                symbol text not null,
                name text not null,
                exchange text  not null, 
                last_update_date text default null,
                unique (symbol, exchange)
                )'''
        )

print "Creating indexes..."
c.execute('''CREATE INDEX ticker_history_index_1 ON ticker_history(symbol, exchange);''')
c.execute('''CREATE UNIQUE INDEX ticker_history_index_2 ON ticker_history(symbol, exchange, date);''')
print "Indexes Created..."


conn.commit()
conn.close()

print "Finished!!"