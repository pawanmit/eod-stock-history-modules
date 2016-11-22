import sys
sys.path.append('..')
import DBConstants
import sqlite3

conn = sqlite3.connect(DBConstants.PATH_TO_STOCKS_DB)
c = conn.cursor()

print "Dropping schema for stocks.db......"

# Create table
c.execute('''DROP TABLE ticker_history''')
c.execute('''DROP TABLE ticker''')

conn.commit()
conn.close()

print "Finished!!"