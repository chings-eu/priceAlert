#from alpha_vantage.timeseries import TimeSeries
#api_key = 'VNGAOQZWONTD9F9L'
#ts = TimeSeries(key=api_key)
#symbol = 'TSLA'

#def get_current_av(symbol):
#    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
#    current_price = data['05. price']
#    return float(current_price)

import yfinance as yf

def get_current(symbol):
    stock = yf.Ticker(symbol)
    return stock.history().tail(1)['Close'].iloc[0]
