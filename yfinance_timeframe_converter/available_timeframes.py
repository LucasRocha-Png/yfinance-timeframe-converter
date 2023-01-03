# "All yfinance timeframes available for download."
yfinance_available_timeframes = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]

# "All timeframes that the function 'timeframe_converter' converts to"    
converter_available_inputs = ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", 
                                "1h", "90m", "2h", "3h", "4h", "6h", "8h", "12h",
                                "1d", "2d", "3d", "5d", "6d", "10d", "15d",
                                "1wk", "1mo", "2mo", "3mo", "4mo", "6mo", "1yr", "2yr"]

# "All timeframes that the function 'timeframe_converter' converts to"    
converter_available_outputs = ["1m", "2m", "3m", "4m", "5m", "6m", "10m", "12m", "15m", "20m", "30m", "60m", 
                                "1h", "2h", "3h", "4h", "6h", "8h", "12h",
                                "1d", "2d", "3d", "6d", "10d", "15d",
                                "1wk", "1mo", "2mo", "3mo", "4mo", "6mo", "1yr", "2yr"]

# Assigns all convertions available
_ = converter_available_outputs

available_convertions = {}
for timeframe in converter_available_outputs:
    available_convertions[timeframe] = _[_.index(timeframe)+1:]
