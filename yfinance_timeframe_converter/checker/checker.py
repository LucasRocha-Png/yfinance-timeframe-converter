from formater.formater import format_cpp_row_to_python
from checker.return_error import return_error_by_list
from utils.utils import exception_message
import pandas as pd
import ctypes
import sys
import os

plataform = sys.platform
archive_folder = os.path.dirname(__file__)

if plataform == "win32":
    exception_message("Module not available in Windows yet!")    
else:
    library = ctypes.CDLL(f"{archive_folder}/module/build/libcheckers.so")	
    
# Imports function checker from cpp
cpp_checker = library.checker
cpp_checker.argtypes = [
                        ctypes.POINTER(ctypes.c_char_p),  # Index
                        ctypes.c_int,                     # Index Len

                        ctypes.POINTER(ctypes.c_char_p),  # Columns names
                        ctypes.c_int,                     # Columns name len

                        ctypes.POINTER(ctypes.c_char_p)]  # Inputs
    
cpp_checker.restype = ctypes.POINTER(ctypes.c_int)

# Imports function to free the memory from cpp
free_array = library.free_array
free_array.argtype = ctypes.POINTER(ctypes.c_int)


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

    list_errors = format_cpp_row_to_python(errors, 4, "int")

    # If there is an error, calls return error function
    if sum(list_errors) != 0:
        return_error_by_list(list_errors, data, timeframes)

    # Free memory of array
    free_array(errors)

if __name__ == "__main__":
	pass