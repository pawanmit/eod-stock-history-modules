import Constants
import urllib2
import json

apiKey = Constants.QUANDL_API_KEY
apiUrl = Constants.QUANDL_EOD_API_URL

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