from utils.utils import exception_message
from formater.formater import format_cpp_row_to_python
import pandas as pd

def return_error_by_list(list_errors: list, data: pd.core.frame.DataFrame, timeframes: list) -> None:
    """
    Returns an error based on the list of errors
    """

    columns_available = ["Open", "High", "Low	Close", "Adj Close", "Volume"]
    timeframes_available = ["1m", "2m", "3m", "5m", "15m", "30m", "60m", "90m", "1h", "2h", "3h", "4h", "1d", "5d", "1wk", "1mo", "3mo", "6mo", "1yr"]

    # Convert Timeframes
    timeframes = format_cpp_row_to_python(timeframes, 2, "string")

    # Timeframe does not exists
    if list_errors[0] == 1:
        for timeframe in timeframes:
            if timeframe not in timeframes_available:
                exception_message(f"Timeframe {timeframe} does not exist! Only accepts {timeframes_available}")

    # Output timeframe is lower than input
    if list_errors[1] == 1:
        exception_message(f"Output timeframe {timeframes[1]} is lower than input timeframe {timeframes[0]}!")

    # Columns doesn't exist
    if list_errors[2] == 1:
        for column in data.columns:
            if column not in columns_available:
                exception_message(f"Column {column} are not available to be converted yet!")

    # Timeframe passed is not the same as timeframe
    if list_errors[3] == 1:
        exception_message(f"Timeframe {timeframes[0]} passed probally is not the same from timeframe!")    

    # Convertion not available
    if list_errors[4] == 1:
        exception_message(f"Convertion from {timeframes[0]} to {timeframes[1]} is not available!")
