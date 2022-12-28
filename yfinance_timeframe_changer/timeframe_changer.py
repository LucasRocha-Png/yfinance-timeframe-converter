from checkers import checker, basic_check
from format import format_data
import pandas as pd

def convert(data: pd.core.frame.DataFrame, timeframe_input: str, timeframe_output: str, checking:bool = True) -> pd.core.frame.DataFrame:

    if checking == True:
        basic_check(data=data)

    data = format_data(data=data, timeframe_input=timeframe_input, timeframe_output=timeframe_output)
    #data = [index, columns, values, timeframes]

    if checking == True:
        checker(data=data)
    



if __name__ == "__main__":
    from utils import download_dataframe
    from threading import Thread
    import time

    # Downloads an database
    timeframe = "1d"
    df = download_dataframe(ticket="AAPL", timeframe=timeframe)

    start = time.time()
    
    for i in range(1_000_000):
        threading.Thread(target = convert, args=(df, timeframe, "1mo", True))

    end = time.time()
    print(f"Total running:", round(end - start, 10))
