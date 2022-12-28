from checkers import checker, basic_check
from format import format_data
import pandas as pd

def convert(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:

    if checking == True:
        basic_check(data)

    data = format_data(data, timeframe_input, timeframe_output)
    #data = [index, columns, values, timeframes]

    if checking == True:
        checker(data)
    



if __name__ == "__main__":
    from utils import download_dataframe
    import time

    # Downloads an database
    df = download_dataframe("AAPL", "1d")

    start = time.time()
    
    for i in range(1):
        convert(df, "1d", "1mo", True)

    end = time.time()
    print(f"Total running:", round(end - start, 10))
