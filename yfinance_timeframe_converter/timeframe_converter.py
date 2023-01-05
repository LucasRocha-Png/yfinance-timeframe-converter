from .converter.converter import convert_dataframe
from .checker.basic_checker import basic_checker
from .formater.formater import format_data
from .utils.utils import renames_timeframe
from .checker.checker import checker
import pandas as pd


def timeframe_converter(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:
    """
    Converts YFinance dataframe by the passed timeframe.

    Returns the converted DataFrame.

    Arguments:

    data - pd.DataFrame -> The dataframe you desire to convert

    timeframe_input - string -> The timeframe of the DataFrame

    timeframe_output - string -> The timeframe you desire to convert to
    
    checking - bool -> Checks if all variables are valid, if False, the code will run about 10% faster, but you can have serious errors
    """

    # Renames inputs
    timeframe_input = renames_timeframe(timeframe_input)
    timeframe_output = renames_timeframe(timeframe_output)

    # If input is the same as output, return data
    if timeframe_input == timeframe_output:
        return data

    # If checking == True, do basic checking
    if checking:
        data = basic_checker(data)

    # Converts data to c++ format
    converted_data = format_data(data, timeframe_input, timeframe_output)

    # If Checking == True, do some complex checking
    if checking:
        checker(converted_data, data)

    # Converts dataframe
    df = convert_dataframe(converted_data)
   
    return df    
