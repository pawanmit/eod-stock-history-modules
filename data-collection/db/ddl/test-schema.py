import sys
sys.path.append('..')
import DBConstants
import sqlite3

conn = sqlite3.connect(DBConstants.PATH_TO_STOCKS_DB)
c = conn.cursor()

# Create table
#c.execute("INSERT INTO ticker(symbol, name, exchange) VALUES ('ZYNE','Zynerba Pharmaceuticals Inc.','NASDAQ')")
#c.execute("INSERT INTO ticker_history(symbol, name, date, open, high, low, close, volume, exchange) VALUES ('A','Agilent Technologies Inc.','1999-11-18','45.5','50.0','40.0','44.0','44739900.0','NYSE')")
#conn.commit()

for row in c.execute("SELECT * FROM ticker_history"):
        print row

conn.close()

print "Finished!!"
