from utils.utils import exception_message
import ctypes
import sys
import os

plataform = sys.platform

archive_folder = os.path.dirname(__file__)

if plataform != "win32":
    library = ctypes.CDLL(f"{archive_folder}/module/linux/build/libconvert_timeframe.so")	
else:
    exception_message("App not available in Windows yet!")        

cpp_convert_timeframe = library.convert_timeframe
cpp_convert_timeframe.argtypes = [
                        ctypes.POINTER(ctypes.c_char_p),  # Index
                        ctypes.c_int,                     # Index Len

                        ctypes.POINTER(ctypes.c_char_p),  # Columns names
                        ctypes.c_int,                     # Columns name len

                        ctypes.POINTER(ctypes.c_double),  # Values
                        ctypes.c_int,                     # Values len

                        ctypes.POINTER(ctypes.c_char_p)]  # Inputs


def convert_timeframe(data: list):
    index = data[0]
    columns = data[1]
    values = data[2]
    timeframes = data[3]

    cpp_convert_timeframe(index, len(index), columns, len(columns), values, len(values), timeframes)
    