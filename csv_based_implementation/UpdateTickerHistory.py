import csv
import sys
import Constants
import QuandlApiUtil
import FileIOUtil
import DateTimeUtil


baseDir = Constants.BASE_DIR
feedsDir = Constants.FEED_DIR
activeTickersFileName =  Constants.ACTIVE_TICKERS_FILE_NAME

#Updates ticker history for list of tickers from last update date to last business date

last_business_day = str(DateTimeUtil.get_last_business_day())
exchange = sys.argv[1]
#exchange = 'NYSE'
tickersFileUrl = baseDir + "/" + feedsDir + "/" + exchange + "/" + activeTickersFileName
print "Reading " + tickersFileUrl

def get_ticker_eod_for_missing_days(ticker, num_days_of_eod_data_missing):
    json = QuandlApiUtil.get_ticker_eod_data(ticker, num_days_of_eod_data_missing)
    csvData = FileIOUtil.convertJsonToCsv(json)
    return csvData

with open(tickersFileUrl, 'rU') as csvfile:
    tickersReader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in tickersReader:
        last_eod_update_date = None
        ticker = row[0]
        rows = []
        try:
            row = FileIOUtil.read_rows_from_ticker_history(ticker, exchange, 2)
            #first row is header, hence ignoring row[0]. date last updated is first col of row
            last_eod_update_date = row[1][0]
        except Exception, e:
            print 'Not able to read eod data for ticker:' + ticker
        if last_eod_update_date is not None:
            num_days_of_eod_data_missing = DateTimeUtil.get_num_business_days_between(last_eod_update_date, last_business_day)
            rows = get_ticker_eod_for_missing_days(ticker, num_days_of_eod_data_missing)
            FileIOUtil.prepend_ticker_eod_data(ticker, exchange, rows)
            print str("Updated EOD for ticker:" + ticker)
        continue
    #print rows

