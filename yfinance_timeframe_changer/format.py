from utils import excepetion_message
import ctypes


def format_row(row, type):
    """
    Converts an row to the type setted
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
        excepetion_message(f"Type {type} not permitted!")

    return row  


def format_data(data):
    """
    Formats data for a format that C++ accepts
    """


    data = data.dropna(how="all")
    data = data.fillna(0)

    index = data.index.astype(str).to_list()
    index = format_row(index, "string")

    columns = data.columns.to_list()
    columns = format_row(columns, "string")

    values = []
    for column in data.columns:
        values.extend(data[column])
    values = format_row(values, "float")

    data = [index, columns, values]
    return data
    