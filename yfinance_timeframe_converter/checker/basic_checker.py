from ..utils.utils import exception_message
import pandas as pd

def basic_checker(data: pd.core.frame.DataFrame) -> None:
    """
    Checks if it's a Pandas DataFrame, and if has rows to be converted
    """    

    if type(data) != pd.core.frame.DataFrame:
        exception_message("Data is not a available format! Data should be a Pandas DataFrame")

    if data.shape[0] == 0 or data.shape[1] == 0:
        exception_message("Data has no rows or columns!")

    for column in data.columns:
        type_ = data[column].dtype
        if type_ != float and type_ != int:
            exception_message(f"The values from {column} column is not allowed")