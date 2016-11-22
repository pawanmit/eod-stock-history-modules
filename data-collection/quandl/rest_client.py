import APIConstants
import urllib2
import json
import StringIO
import csv

apiKey = APIConstants.QUANDL_API_KEY
apiUrl = APIConstants.QUANDL_EOD_API_URL

def get_ticker_eod_data(ticker, num_rows):
    if num_rows == 'ALL':
        url = apiUrl + '/' + ticker + ".json?&api_key=" + apiKey
    else:
        url = apiUrl + '/' + ticker + ".json?&api_key=" + apiKey + '&rows=' + str(num_rows)
    content = None
    try:
        page = urllib2.urlopen(url)
        content = page.read()
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "Unable to get information  for " + ticker
    if content is not None:
        parsed_json = json.loads(content)
        return parsed_json
    
def get_all_tickers():
    static_tickers_url = APIConstants.STATIC_TICKERS_URL
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