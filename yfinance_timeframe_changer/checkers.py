"""
Checks if all the dataframe is correct
"""

import pandas as pd
from utils import excepetion_message
import ctypes
import os

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

    
	
	
	
archive_folder = os.path.dirname(__file__)
library = ctypes.CDLL(f"{archive_folder}/checkers/build/libcheckers.so")	

cpp_checker = library.checker
cpp_checker.argtypes = [
                        ctypes.POINTER(ctypes.c_char_p),  # Index
                        ctypes.c_int,                     # Index Len

                        ctypes.POINTER(ctypes.c_char_p),  # Columns names
                        ctypes.c_int,                     # Columns name len

                        ctypes.POINTER(ctypes.c_char_p)]  # Inputs
    


def checker(data: pd.core.frame.DataFrame) -> None:

    """
    Checks if the DataFrame is able to be converted
    """

    #[index, columns, values, timeframes]
    index = data[0]
    columns = data[1]
    timeframes = data[3]

    errors = cpp_checker(
                        index,
                        len(index),

                        columns,
                        len(columns),

                        timeframes
                        )


if __name__ == "__main__":
	pass