import Constants
import csv

baseDir = Constants.BASE_DIR
feedsDir = Constants.FEED_DIR

def convertJsonToCsv(json):
    data = json['dataset']['data']
    csvColumns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    csvData = []
    csvData.append(csvColumns)
    for element in data:
        csvRow = [element[0], element[1], element[2], element[3], element[4], element[5]]
        csvData.append(csvRow)
    return csvData

def write_ticker_eod_data(ticker, exchange, eod_data):
    ticker_eod_csv_url = baseDir + "/" + feedsDir + "/" + exchange + "/" + ticker + ".csv";
    print 'Writing ' + str(len(eod_data)) + ' lines of data to file ' + ticker_eod_csv_url
    with open(ticker_eod_csv_url, "wb") as ticker_eod_csv:
        writer = csv.writer(ticker_eod_csv)
        writer.writerows(eod_data)

def prepend_ticker_eod_data(ticker, exchange, new_eod_data):
    ticker_eod_csv_url = baseDir + "/" + feedsDir + "/" + exchange + "/" + ticker + ".csv";
    with open(ticker_eod_csv_url, 'rb') as f:
        reader = csv.reader(f)
        existing_ticker_eod = list(reader)
    del existing_ticker_eod[0]
    new_eod_data.extend(existing_ticker_eod)
    write_ticker_eod_data(ticker, exchange, new_eod_data)

def read_rows_from_ticker_history(ticker, exchange, num_rows):
    ticker_eod_csv_url = baseDir + "/" + feedsDir + "/" + exchange + "/" + ticker + ".csv";
    count = 0
    rows = []
    with open(ticker_eod_csv_url, 'rU') as ticker_eod_csv:
        ticker_eod_reader = csv.reader(ticker_eod_csv, delimiter=',', quotechar='\"')
        while count < num_rows:
            row = next(ticker_eod_reader)
            rows.append(row)
            count = count + 1
    return rows