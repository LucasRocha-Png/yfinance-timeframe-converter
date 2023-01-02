from converter.converter import convert_dataframe
from checker.basic_checker import basic_checker
from formater.formater import format_data
from utils.utils import renames_timeframe
from checker.checker import checker
import pandas as pd


def timeframe_converter(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:
    """
    Converts YFinance DataFrame Timeframes
    """

    # Renames inputs
    timeframe_input = renames_timeframe(timeframe_input)
    timeframe_output = renames_timeframe(timeframe_output)

    # If input is the same as output, return data
    if timeframe_input == timeframe_output:
        return data

    # If checking == True, do basic checking
    if checking:
        basic_checker(data)

    # Converts data to c++ format
    converted_data = format_data(data, timeframe_input, timeframe_output)

    # If Checking == True, do some complex checking
    if checking:
        checker(converted_data, data)

    # Converts dataframe
    df = convert_dataframe(converted_data)
   
    return df    



    

if __name__ == "__main__":
    from utils.utils import download_dataframe
    import time


    timeframe = "1d"
    output_timeframe = "1mo"
    df = download_dataframe("PETR4.SA", timeframe)

    start = time.time()
    new_df = timeframe_converter(df, timeframe, output_timeframe, True)
    end = time.time()

    print(new_df)

    print("\n")
    print(f"Running Seconds:", round(end - start, 10))
