from checkers import checker
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
        return data
    #----------------------------------------------------------
    
    
    
    



    
    
    
if __name__ == "__main__":
    from pandas_datareader import data as pdr
    from utils import download_dataframe
    import yfinance as yf

    ticket = "AAPL"
    timeframe = "1m"

    df = download_dataframe(ticket, timeframe)

    convert_timeframe(data = df, timeframe_input = timeframe, timeframe_output = "1d", checkers = True)
    print("Everythin Ok!")