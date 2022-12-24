from utils import exception_message
import pandas as pd

def checks_if_data_exists(data):
    """
    Checks if data is a DataFrame
    """
    if type(data) != pd.core.frame.DataFrame:
        exception_message("Data is not a DataFrame!")
        
    if data.shape[0] == 0:
        exception_message("DataFrame has no rows!")
        
    columns = data.columns.to_list()
    if len(columns) == 0:
        exception_message("Their is no columns on the DataFrame")
    
    
    columns_available = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    for column in columns:
        if column not in columns_available:
            exception_message(f"{column} is not a YFinance column available")
        
        
def checks_if_timeframe_exist(timeframe):
    """
    Checks if timeframe exist
    """
    
    timeframes = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    if timeframe not in timeframes:
        exception_message(f"Timeframe: '{timeframe}' do not exists! YFinance only accepts {timeframes}")
    
def checks_if_timeframe_is_the_same_as_data(data, timeframe): 

    """
    Checks if the dataframe in an minimal way, is in the correct timeframe
    """
    
    minutes_timeframe = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h"]
    
    index = data.index.astype(str).to_list()
    value = index[-1]
    
    
    if len(value) == 10 and timeframe not in minutes_timeframe:
        pass
    
    elif len(value) != 10 and timeframe in minutes_timeframe:
        pass
    
    else:   
        exception_message("Timeframe from the data probally is not the same as what was put in the arguments.") 

def checks_if_input_is_lower_than_output(timeframe_input, timeframe_output):
    """
    Checks if input is lower than output, if not, raise error
    """
    timeframes = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    
    index_input = timeframes.index(timeframe_input)
    index_output = timeframes.index(timeframe_output)
    if index_input > index_output:
        exception_message(f"Timeframe input: '{timeframe_input}' is higher than Timeframe output: '{timeframe_output}'")
    
    
#Main function    
def checker(data, timeframe_input, timeframe_output):
    """
    Makes all the checking
    """
    
    # Checks if data exists!
    checks_if_data_exists(data)
    
    # Checks if timeframe exists
    checks_if_timeframe_exist(timeframe_input)
    checks_if_timeframe_exist(timeframe_output)
    
    # Checks if timeframe input is lower than the output
    checks_if_input_is_lower_than_output(timeframe_input, timeframe_output)
    
    # Checks if timeframe is the same as data
    checks_if_timeframe_is_the_same_as_data(data, timeframe_input)
   