from utils.utils import excepetion_message
import pandas as pd
import ctypes


def format_row_python_to_cpp(row: list, type: str) -> list:
    """
    Formats an python row to C++ row
    """        
    
    if type == "float":
        row = (ctypes.c_float * len(row))(*row)
    
    elif type == "int":
        row = (ctypes.c_int * len(row))(*row)

    elif type == "double":
        row = (ctypes.c_double * len(row))(*row)   

    elif type == "bool":
        row = (ctypes.c_bool * len(row))(*row)         

    elif type == "string":
        row = list(map(lambda x: str.encode(x), row))
        row = (ctypes.c_char_p * len(row))(*row)

    else:
        excepetion_message(f"Type {type} can't be formated!")

    return row  

def format_row_cpp_to_python(row: list, len_row: int, type: str) -> list:
    """
    Formats a C++ row to Python Row
    """

    new_row = []

    if type == "string":
        for value in row:
            if value != None:
                new_row.append(str(value, "UTF-8"))   
            if len_row == len(new_row):
                break

    elif type in ["float", "bool", "int", "double"]:
        new_row = row[:len_row]            

    return new_row


def format_data(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str) -> list:
    """
    Formats data for a format that C++ accepts
    """


    data = data.dropna(axis=0)
    #data = data.fillna(0)

    index = data.index.astype(str).to_list()
    index = format_row_python_to_cpp(index, "string")

    columns = data.columns.to_list()
    columns = format_row_python_to_cpp(columns, "string")

    values = data.to_numpy().ravel(order='F').tolist() # Reshape dataframe
    values = format_row_python_to_cpp(values, "double")

    timeframes = [timeframe_input, timeframe_output]
    timeframes = format_row_python_to_cpp(timeframes, "string")

    data = [index, columns, values, timeframes]
    return data
    