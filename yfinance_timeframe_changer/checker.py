"""
Checks if all the dataframe is correct
"""

import pandas as pd
from utils import excepetion_message

def basic_check(data):
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

    

def checker(data, timeframe_input, timeframe_output):

    """
    Checks if the DataFrame is able to be converted
    """


    pass