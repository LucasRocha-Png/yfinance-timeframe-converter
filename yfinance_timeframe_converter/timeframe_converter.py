from converter.converter import convert_timeframe
from checkers.checkers import checker, basic_check
from formater.formater import format_data
import pandas as pd


def timeframe_converter(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:
    """
    Converts YFinance DataFrame Timeframes
    """

    # If timeframe_input is the same as timeframe_output there is no reason to convert
    if timeframe_input == timeframe_output:
        return data


    # Basic checking, checks if data is a DataFrame and if has rows
    if checking == True:
        basic_check(data)


    # Formats pandas DataFrame to C++ datatype
    converted_data = format_data(data, timeframe_input, timeframe_output)


    # Checks if the dataframe can be converted
    if checking == True:
        checker(converted_data, data)


    # Finally, converts timeframe
    convert_timeframe(converted_data)
    




if __name__ == "__main__":
    from utils.utils import download_dataframe
    import time


    timeframe = "1d"
    df = download_dataframe("AAPL", timeframe)

    start = time.time()
    
    for i in range(500):
        timeframe_converter(df, timeframe, "1mo", True)

    end = time.time()
    print(f"Total running:", round(end - start, 10))
