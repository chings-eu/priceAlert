import yfinance as yf
import datetime
import pandas as pd

#symbol = 'TSLA'

def get_yesterday(symbol):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    data = yf.download(symbol, start=yesterday, end=today)
    return data['Close'].iloc[0]
def get_last_day(symbol):
    today = datetime.date.today()
    data = pd.DataFrame() # initiate an empty dataframe
    days = 1 # one day before today
    while(data.empty):
        yesterday = today - datetime.timedelta(days=days)
        data = yf.download(symbol, start=yesterday, end=today)
        days += 1

    return data['Close'].iloc[0]

#if __name__ == '__main__':
#    print(get_last_day(symbol))