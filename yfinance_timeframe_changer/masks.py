import pandas as pd

def create_operation_mask(data):
    """
    Makes a mask telling which kind of operation the column will suffer
    """

    columns = data.columns.to_list()
    
    columns_available = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    operations_available = ["first", "max", "min", "last", "last", "sum"]
    
    mask = []
    for column in columns:
        mask.append(operations_available[columns_available.index(column)])
        
    return mask    
    
def dataframe_to_list(data):
    """
    Turn an dataframe to list
    """
    
    columns = data.columns
    mask = []
    for column in columns:
        mask.append(data[column].tolist())
    return mask    
    
def create_null_mask(data):
    """
    Create a dataframe telling if the value is null or not
    """
    
    data = data.notna()
    mask = dataframe_to_list(data)
    
    return mask
    

    