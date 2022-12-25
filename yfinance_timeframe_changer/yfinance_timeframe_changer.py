from checkers import checker
from masks import *
import pandas as pd




def convert_timeframe(data, timeframe_input, timeframe_output, checkers = True):
    """
    Prepears the data for the conversion
    """
    
    # Checks if the data is correct ------------------------
    if checkers:
        checker(data, timeframe_input, timeframe_output)
    #-------------------------------------------------------

    # Checks if timeframe_input is the same as timeframe_output
    if timeframe_input == timeframe_output:
        print("Input is the same as output. Returning DataFrame")
        return data
    #----------------------------------------------------------
    
    
    # Create null mask
    data = data.dropna(how="all")
    null_mask = create_null_mask(data)
    data = data.fillna(0)
    # ----------------
    # null_mask    
    
    # Crete operation_mask
    operation_mask = create_operation_mask(data)
    # --------------------
    
    
    index  = data.index.to_list()
    values = dataframe_to_list(data)
    null_mask = null_mask
    operation_mask = operation_mask
    

    
    
    
    
    
    
    
    



    
    
    
if __name__ == "__main__":
    import time
    from pandas_datareader import data as pdr
    from utils import download_dataframe
    import yfinance as yf
    
    
    

    ticket = "AAPL"
    timeframe = "1d"

    df = download_dataframe(ticket, timeframe)
    starttime = time.time()
    convert_timeframe(data = df, timeframe_input = timeframe, timeframe_output = "1mo", checkers = True)
    endtime = time.time()
    
    print("Runtime = ", round(endtime - starttime, 10))