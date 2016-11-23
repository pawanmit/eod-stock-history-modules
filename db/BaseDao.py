import DBConstants
import sqlite3


class BaseDao:
    connection = sqlite3.connect(DBConstants.PATH_TO_STOCKS_DB)
    cursor = connection.cursor()
    
    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor
        
    def commit(self):
        self.connection.commit()
        #self.connection.close()
     
    def closeConnecton(self):
        self.connection.close() 

#print 'it works...'
