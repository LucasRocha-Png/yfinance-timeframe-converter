"""
Checks if all the dataframe is correct
"""

from utils.utils import excepetion_message
import pandas as pd
import numpy as np
import ctypes
import os


archive_folder = os.path.dirname(__file__)
library = ctypes.CDLL(f"{archive_folder}/src/build/libcheckers.so")	

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


def return_error(list_errors):
    if list_errors[0] == 1:
        excepetion_message("Timeframe does not exist!")

    elif list_errors[1] == 1:
        excepetion_message("Input timeframe is lower than timeframe output!")

    elif list_errors[2] == 1:
        excepetion_message("Column doesn't exist!")

    elif list_errors[3] == 1:
        excepetion_message("Timeframe passed is not the same from timeframe!")    

def checker(data: list) -> None:

    """
    Checks if the DataFrame is able to be converted

    Uses:

    checks_if_timeframes_exists,
    checks_if_input_is_lower_than_output,
    checks_if_columns_exists,
    checks_if_index_is_equal_than_timeframe.
    """

    #[index, columns, values, timeframes]
    index = data[0]
    columns = data[1]
    timeframes = data[3]

    errors = cpp_checker(
                    index,       # Index
                    len(index),  # Index Len
                    columns,     # Columns
                    len(columns),# Columns len
                    timeframes   # Timeframes
                    )

    list_errors = errors[:4] # To convert C++ array to Python array, must slice cpp array by the total len 

    # If there is an error, calls return error function
    if sum(list_errors) != 0:
        return_error(list_errors)

    # Free memory of array
    free_array(errors)

if __name__ == "__main__":
	pass