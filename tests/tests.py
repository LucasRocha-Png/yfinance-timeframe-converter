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
print(converted_timeframe)
end = time.time()
print('Execution time:', end - start, 'seconds')

# Gets all timeframes available to donwload from yFinance - 13 timeframes
#print(converter.yfinance_available_timeframes) # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 

# Gets all timeframes available to pass as input to the function - 35 timeframes
#print(converter.converter_available_inputs) # ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h", "90m", "2h", "3h", "4h", "6h", ... "4mo", "6mo", "1yr", "2yr"] 

# Gets all Outputs available of the function - 33 timeframes
#print(converter.converter_available_outputs) # ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h", "90m", "2h", "3h", "4h", "6h", ... "4mo", "6mo", "1yr", "2yr"] 

# Gets all convertions available
#print(converter.available_convertions) # {"1m" = ["2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h"...]}