from converter.converter import convert_timeframe
from checkers.basic_checker import basic_checker
from checkers.checkers import checker
from utils.utils import renames_timeframe
from formater.formater import format_data
import pandas as pd


def timeframe_converter(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:
    """
    Converts YFinance DataFrame Timeframes
    """

    timeframe_input = renames_timeframe(timeframe_input)
    timeframe_output = renames_timeframe(timeframe_output)

    if timeframe_input == timeframe_output:
        return data

    if checking == True:
        basic_checker(data)

    converted_data = format_data(data, timeframe_input, timeframe_output)

    if checking == True:
        checker(converted_data, data)

    convert_timeframe(converted_data)
    




if __name__ == "__main__":
    from utils.utils import download_dataframe
    import time


    timeframe = "1d"
    df = download_dataframe("AAPL", timeframe)

    start = time.time()
    
    for i in range(1):
        timeframe_converter(df, timeframe, "1mo", True)

    end = time.time()
    print(f"Total running:", round(end - start, 10))
