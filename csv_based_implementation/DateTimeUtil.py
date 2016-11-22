from datetime import date, timedelta, datetime
from pytz import timezone

def getDateFromString(dateString):
    dateAttributes = dateString.split('-')
    return date(int(dateAttributes[0]), int(dateAttributes[1]), int(dateAttributes[2]))

def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate

#returns last business day
def get_last_business_day():
    est_timezone = timezone('US/Eastern')
    est_date_time = datetime.now(est_timezone)
    est_date_str = est_date_time.strftime('%Y-%m-%d')
    est_time_str =  est_date_time.strftime('%H-%M-%S')
    est_date = getDateFromString(est_date_str)
    prev_businessday = None
    #if current time is greater than 18:00 EST then QUANDL feed is updated. Use current date, else use current date-1
    if (est_date.weekday() in range(0, 4) and est_time_str > '18-00-00'):
        prev_businessday =  est_date
    else:
        prev_businessday =  prev_weekday(est_date)
    return prev_businessday

def get_num_business_days_between(last_feed_update_day, last_business_day):
    start = getDateFromString(last_feed_update_day)
    end =   getDateFromString(last_business_day)
    daydiff = end.weekday() - start.weekday()
    days = ((end - start).days - daydiff) / 7 * 5 + min(daydiff, 5) - (max(end.weekday() - 4, 0) % 5)
    return days
