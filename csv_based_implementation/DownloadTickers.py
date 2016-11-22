import urllib2
import csv
import json
import Constants


baseDir = Constants.BASE_DIR
feedsDir = Constants.FEED_DIR
tickersFileName =  Constants.TICKERS_FILE_NAME
masterTickersFileUrl = baseDir + '/' + feedsDir + '/' + tickersFileName
apiKey = Constants.QUANDL_API_KEY
apiUrl = Constants.QUANDL_EOD_API_URL
def getTickerFromRow(csvRow):
    ticker = row[0].split('/')[1]
    return ticker

def getTickerDescriptionFromApi(ticker):
    url = apiUrl + '/' + ticker + ".json?rows=1&api_key=" + apiKey + "&column_index=0"
    try:
        page = urllib2.urlopen(url)
        content = page.read()
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "Unable to get information  for " + ticker
    parsed_json = json.loads(content)
    description = parsed_json['dataset']['description']
    return description

def findBetween( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def getExchangeFromDescription(description):
    stringPrecedingExchange = '<p><b>Exchange</b>: '
    stringSuffixingExchange = '</p>'
    exchange = findBetween(description, stringPrecedingExchange, stringSuffixingExchange)
    return exchange

def writeTickersToCsv(tickers, exchange):
    tickersFileUrl = baseDir + "/" + feedsDir + "/" + exchange + "/" + tickersFileName;
    tickersFile = open(tickersFileUrl, 'w')
    print 'writing ' + str(len(tickers)) + ' tickers for exchange ' + exchange + ' to file ' + tickersFileUrl
    for ticker in tickers:
        tickersFile.write("%s\n" % ticker)
    tickersFile.close()


nasdaqStockSymbols = []
nyseStockSymbols = []

count=0
with open(masterTickersFileUrl, 'rU') as csvfile:
    tickersReader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in tickersReader:
        ticker =  getTickerFromRow(row)
        description =  getTickerDescriptionFromApi(ticker)
        exchange = getExchangeFromDescription(description)
        if exchange == 'NASDAQ':
            nasdaqStockSymbols.append(ticker)

        if exchange == 'NYSE':
            nyseStockSymbols.append(ticker)
        print ticker + "-" + exchange
        count = count + 1
        if count%100 == 0:
            print str(count) + " csv rows processed"
            #break

writeTickersToCsv(sorted(nasdaqStockSymbols), 'NASDAQ')
writeTickersToCsv(sorted(nyseStockSymbols), 'NYSE')