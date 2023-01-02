from formater.formater import format_cpp_row_to_python
from utils.utils import exception_message
import pandas as pd
import numpy as np
import ctypes
import sys
import os

plataform = sys.platform

archive_folder = os.path.dirname(__file__)

if plataform == "win32": 
    exception_message("Module not available in Windows yet!")     	
else:
    library = ctypes.CDLL(f"{archive_folder}/module/build/libconvert_timeframe.so")
       


# Convert Index Function -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
cpp_convert_index = library.convert_index
# Accepts index, len index, and timeframes
cpp_convert_index.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]  
cpp_convert_index.restype = ctypes.POINTER(ctypes.c_char_p)  # Returns converted index

# Convert Values -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
cpp_convert_values = library.convert_values
# Accepts values, lenght_values, normal index, len normal index, converted index, len converted index, columns and len columns
cpp_convert_values.argtypes = [
                            ctypes.POINTER(ctypes.c_double), ctypes.c_int,
                            ctypes.POINTER(ctypes.c_char_p), ctypes.c_int, 
                            ctypes.POINTER(ctypes.c_char_p), ctypes.c_int, 
                            ctypes.POINTER(ctypes.c_char_p), ctypes.c_int
                            ]

cpp_convert_values.restype = ctypes.POINTER(ctypes.c_double)

# Free memory array -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
cpp_free_memory_char = library.free_array_char
cpp_free_memory_char.argtype = ctypes.POINTER(ctypes.c_char_p)

cpp_free_memory_double = library.free_array_double
cpp_free_memory_double.argtype = ctypes.POINTER(ctypes.c_double)


def convert_dataframe(data: list) -> pd.core.frame.DataFrame:
    """
    Get data and send it to the C++ function
    """

    index = data[0]
    columns = data[1]
    values = data[2]
    timeframes = data[3]

    # Converts columns
    converted_columns = format_cpp_row_to_python(columns, len(columns), "string")

    # Converts index -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    index_result = cpp_convert_index(index, len(index), timeframes)
    lenght_index = int(str(index_result[0], "UTF-8"))
    converted_index = format_cpp_row_to_python(index_result, lenght_index, "string")
    
    # Converts Values -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    values_result = cpp_convert_values(values, len(values), index, len(index), index_result, lenght_index, columns, len(columns))
    lenght_columns = len(converted_columns)

    converted_index = converted_index[1:]
    converted_values = format_cpp_row_to_python(values_result, ((lenght_index) * lenght_columns)-1, "double")
    converted_values = np.array(converted_values).reshape(-1, lenght_index).tolist()

    # Free memory -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    cpp_free_memory_char(index_result)
    cpp_free_memory_double(values_result)


    # Create DataFrame -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    df = pd.DataFrame(converted_values).T
    df.columns = converted_columns
    df.index = converted_index

    return df




    
    

    