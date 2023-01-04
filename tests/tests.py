import yfinance_timeframe_converter as converter
from pandas_datareader import data as pdr
import yfinance as yf
import time

ticket = "AAPL"
input_timeframe = "1d"
output_timeframe  = "1wk"

yf.pdr_override()  
df = pdr.get_data_yahoo(tickers=ticket, interval=input_timeframe)

# Pass the dataframe, the timeframe of the Dataframe, and the timeframe desired. Returns the converted DataFrame
start = time.time()
converted_timeframe = converter.timeframe_converter(df, input_timeframe, output_timeframe)
end = time.time()
print('Execution time:', end - start, 'seconds')