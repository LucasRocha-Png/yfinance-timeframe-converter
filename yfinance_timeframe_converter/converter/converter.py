from formater.formater import format_cpp_row_to_python
from utils.utils import exception_message
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


# Free memory array -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
cpp_free_memory_char = library.free_array_char
cpp_free_memory_char.argtype = ctypes.POINTER(ctypes.c_char_p)

cpp_free_memory_double = library.free_array_double
cpp_free_memory_double.argtype = ctypes.POINTER(ctypes.c_double)


def convert_dataframe(data: list):
    """
    Get data and send it to the C++ function
    """

    index = data[0]
    columns = data[1]
    values = data[2]
    timeframes = data[3]


    # Converts index -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    cpp_index = cpp_convert_index(index, len(index), timeframes)
    lenght_index = int(str(cpp_index[0], "UTF-8"))

    # Values -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    cpp_convert_values(values, len(values), index, len(index), cpp_index, lenght_index, columns, len(columns))
    

    