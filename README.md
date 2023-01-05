# yfinance-timeframe-converter
### Converts an YFinance DataFrame to other timeframe

Instead of calling the yFinance's API again, why not just to convert your current DataFrame, making the whole process faster? Or to convert it to a non-downloadable timeframe? 

This is what **yfinance-timeframe-converter** does.

Convert your DataFrame to up to **33 timeframes** of your choise, **22 more than the yFinance** timeframes available.

Uses C++ functions to make all process faster, converting large amount of data in less than 0.1 seconds.

## How to use
### How to convert a DataFrame
The `timeframe_converter` function allows you to convert your DataFrame.

To convert a DataFrame, pass the original DataFrame, the DataFrame's timeframe, and the output desired timeframe.
```python
import yfinance_timeframe_converter as converter
from pandas_datareader import data as pdr
import yfinance as yf

ticket = "AAPL"
input_timeframe = "1d"
output_timeframe  = "1wk"

yf.pdr_override()  
df = pdr.get_data_yahoo(tickers=ticket, interval=input_timeframe)

# Pass the dataframe, the timeframe of the Dataframe, and the timeframe desired. Returns the converted DataFrame
converted_timeframe = converter.timeframe_converter(df, input_timeframe, output_timeframe)
```

### Arguments
- `data` - pd.DataFrame -> The dataframe you desire to convert
- `timeframe_input` - string -> The timeframe of the DataFrame
- `timeframe_output` - string -> The timeframe you desire to convert to
- `checking` - bool -> Checks if all variables are valid, if False, the code will run about 10% faster, you can have serious errors

#
### How many timeframes are available to use?
```python
import yfinance_timeframe_converter as converter

# Gets all timeframes available to donwload from yFinance - 13 timeframes
print(converter.yfinance_available_timeframes) # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 

# Gets all timeframes available to pass as input to the function - 35 timeframes
print(converter.converter_available_inputs) # ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h", "90m", "2h", "3h", "4h", "6h", ... "4mo", "6mo", "1yr", "2yr"] 

# Gets all Outputs available of the function - 33 timeframes
print(converter.converter_available_outputs) # ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h", "90m", "2h", "3h", "4h", "6h", ... "4mo", "6mo", "1yr", "2yr"] 

# Gets all convertions available
print(converter.available_convertions) # {"1m" = ["2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", "1h"...]}
```
