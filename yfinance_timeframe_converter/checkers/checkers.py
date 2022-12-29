"""
Checks if all the dataframe is correct
"""

from utils.utils import excepetion_message
from formater.formater import format_row_cpp_to_python
import pandas as pd
import ctypes
import os


archive_folder = os.path.dirname(__file__)
library = ctypes.CDLL(f"{archive_folder}/module/linux/build/libcheckers.so")	

cpp_checker = library.checker
cpp_checker.argtypes = [
                        ctypes.POINTER(ctypes.c_char_p),  # Index
                        ctypes.c_int,                     # Index Len

                        ctypes.POINTER(ctypes.c_char_p),  # Columns names
                        ctypes.c_int,                     # Columns name len

                        ctypes.POINTER(ctypes.c_char_p)]  # Inputs
    
cpp_checker.restype = ctypes.POINTER(ctypes.c_int)

free_array = library.free_array
free_array.argtype = ctypes.POINTER(ctypes.c_int)


def basic_check(data: pd.core.frame.DataFrame) -> None:
    """
    Checks if it's a Pandas DataFrame, and if has rows to be converted
    """    

    if type(data) != pd.core.frame.DataFrame:
        excepetion_message("Data is not a available format! Data should be a Pandas DataFrame")

    if data.shape[0] == 0 or data.shape[1] == 0:
        excepetion_message("Data has no rows or columns!")

    for column in data.columns:
        type_ = data[column].dtype
        if type_ != float and type_ != int:
            excepetion_message(f"The values from {column} column is not allowed")


def return_error(list_errors: list, data: pd.core.frame.DataFrame, timeframes: list) -> None:
    """
    Returns an error based on the list of errors
    """

    columns_available = ["Open", "High", "Low	Close", "Adj Close", "Volume"]
    timeframes_available = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]

    # Convert Timeframes
    timeframes = format_row_cpp_to_python(timeframes, 2, "string")

    # Timeframe does not exists
    if list_errors[0] == 1:
        for timeframe in timeframes:
            if timeframe not in timeframes_available:
                excepetion_message(f"Timeframe {timeframe} does not exist!")

    # Output timeframe is lower than input
    if list_errors[1] == 1:
        excepetion_message(f"Output timeframe {timeframes[1]} is lower than input timeframe {timeframes[0]}!")

    # Columns doesn't exist
    if list_errors[2] == 1:
        for column in data.columns:
            if column not in columns_available:
                excepetion_message(f"Column {column} are not available to be converted yet!")

    # Timeframe passed is not the same as timeframe
    if list_errors[3] == 1:
        excepetion_message(f"Timeframe {timeframes[0]} passed probally is not the same from timeframe!")    

    # Convertion not available
    if list_errors[4] == 1:
        excepetion_message(f"Convertion from {timeframes[0]} to {timeframes[1]} is not available!")




def checker(converted_data: list, data: pd.core.frame.DataFrame) -> None:

    """
    Checks if the DataFrame is able to be converted

    Uses:

    checks_if_timeframes_exists,
    checks_if_input_is_lower_than_output,
    checks_if_columns_exists,
    checks_if_index_is_equal_than_timeframe,
    checks_if_convertion_is_valid
    """

    #[index, columns, values, timeframes]
    index = converted_data[0]
    columns = converted_data[1]
    timeframes = converted_data[3]

    errors = cpp_checker(
                    index, len(index),  
                    columns, len(columns),
                    timeframes   
                    )

    list_errors = format_row_cpp_to_python(errors, 5, "int")

    # If there is an error, calls return error function
    if sum(list_errors) != 0:
        return_error(list_errors, data, timeframes)

    # Free memory of array
    free_array(errors)

if __name__ == "__main__":
	pass