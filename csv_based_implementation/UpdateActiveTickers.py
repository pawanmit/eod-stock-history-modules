import urllib2
import csv
import Constants
import StringIO

baseDir = Constants.BASE_DIR
feedsDir = Constants.FEED_DIR
activeTickersFileName =  Constants.ACTIVE_TICKERS_FILE_NAME

#get the list of tickers and download the active ones, then group them by exchange they are traded on
def getTickerEODData():
    static_tickers_url = Constants.STATIC_TICKERS_URL
    try:
        page = urllib2.urlopen(static_tickers_url)
        content = page.read()
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "Unable to get information  from " + static_tickers_url
    if content is not None:
        f = StringIO.StringIO(content)
        csvReader = csv.reader(f, delimiter=',')
        print static_tickers_url + " downloaded."
        return list(csvReader)


def updateActiveTickers(activeNyseTickers, activeNasdaqTickets):
    tickerRows = getTickerEODData()
    last_business_date = '2016-11-16'
    for tickerRow in tickerRows:
        ticker = tickerRow[0]
        ticker = ticker.replace('.', '_')
        name = tickerRow[1]
        last_trade_day = tickerRow[3]
        exchange = tickerRow[2]
        if last_trade_day == last_business_date:
            if exchange == 'NYSE':
                activeNyseTickers.append(ticker + ',' + name)
            if exchange == 'NASDAQ':
                activeNasdaqTickets.append(ticker + ',' + name)

def writeTickersToCsv(tickers, exchange):
    tickersFileUrl = baseDir + "/" + feedsDir + "/" + exchange + "/" + activeTickersFileName;
    tickersFile = open(tickersFileUrl, 'w')
    print 'writing ' + str(len(tickers)) + ' tickers for exchange ' + exchange + ' to file ' + tickersFileUrl
    for ticker in tickers:
        tickersFile.write("%s\n" % ticker)
    tickersFile.close()

activeNyseTickers = []
activeNasdaqTickers = []

updateActiveTickers(activeNyseTickers, activeNasdaqTickers)

writeTickersToCsv(activeNyseTickers, "NYSE")
writeTickersToCsv(activeNasdaqTickers, "NASDAQ")