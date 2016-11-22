import csv
import Constants
import QuandlApiUtil
import sys
import FileIOUtil

#Downloads ticker history since beginninng of that ticker from a list of tickers
baseDir = Constants.BASE_DIR
feedsDir = Constants.FEED_DIR
tickersFileName =  Constants.TICKERS_FILE_NAME
masterTickersFileUrl = baseDir + '/' + feedsDir + '/' + tickersFileName
apiKey = Constants.QUANDL_API_KEY
apiUrl = Constants.QUANDL_EOD_API_URL
exchanges = Constants.EXCHANGES

exchange = sys.argv[1]
tickersFileUrl = baseDir + "/" + feedsDir + "/" + exchange + "/" + tickersFileName;
print "Reading " + tickersFileUrl
count = 0
with open(tickersFileUrl, 'rU') as csvfile:
    tickersReader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in tickersReader:
        ticker = row[0]
        ticker_eod_data = QuandlApiUtil.get_ticker_eod_data(ticker)
        if ticker_eod_data is not None:
            csvData = FileIOUtil.convertJsonToCsv(ticker_eod_data)
            FileIOUtil.write_ticker_eod_data(ticker, exchange, csvData)
            #print tickerHistory
            count = count + 1
            if count % 25 == 0:
                print str(count) + " tickers processed for " + exchange
                #break
        continue