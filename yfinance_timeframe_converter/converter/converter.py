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
       

cpp_convert_index = library.convert_index
cpp_convert_index.argtypes = [
                            ctypes.POINTER(ctypes.c_char_p),  # Index
                            ctypes.c_int,                     # Index Len

                            ctypes.POINTER(ctypes.c_char_p)# Inputs
                            ]  
         


def convert_dataframe(data: list):
    """
    Get data and send it to the C++ function
    """
    index = data[0]
    columns = data[1]
    values = data[2]
    timeframes = data[3]

    # Converts index
    cpp_convert_index(index, len(index), timeframes)

    