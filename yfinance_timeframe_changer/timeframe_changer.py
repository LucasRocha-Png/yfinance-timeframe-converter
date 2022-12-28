from converter import convert_timeframe
from checkers import checker, basic_check
from format import format_data
import pandas as pd

def convert(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:
    """
    Converts YFinance DataFrame Timeframes
    """

    # If timeframe_input is the same as timeframe_output there is no reason to convert
    if timeframe_input == timeframe_output:
        return data

    # Basic checking, if it is a DataFrame and if has rows
    if checking == True:
        basic_check(data)

    # Formats pandas DataFrame to C++ datatype
    data = format_data(data, timeframe_input, timeframe_output)

    # Checks if the dataframe can be converted
    if checking == True:
        checker(data)

    # Finally, converts timeframe
    convert_timeframe(data)
    




if __name__ == "__main__":
    from utils import download_dataframe
    import time


    timeframe = "1d"
    df = download_dataframe("AAPL", timeframe)

    start = time.time()
    
    for i in range(1):
        convert(df, timeframe, "1mo", True)

    end = time.time()
    print(f"Total running:", round(end - start, 10))
