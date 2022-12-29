from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd

def excepetion_message(message: str) -> None:
    """
    Raises a excepetion message
    """

    print(message)
    print("\n\n")
    raise Exception(message)


def download_dataframe(ticket: str = "AAPL", timeframe: str = "1d") -> pd.core.frame.DataFrame:
    """
    Calls a database using YFinance API. This function is usefull only for tests
    """

    timeframes = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    periods = ["7d", "60d", "60d", "60d", "60d", "60d", "60d", "730d", "max", "max", "max" , "max", "max"]

    if timeframe not in timeframes:
        excepetion_message(f"Period {timeframe} not available! Only accepts {timeframes}")

    period = periods[timeframes.index(timeframe)]

    try:
        yf.pdr_override()  
        df = pdr.get_data_yahoo(tickers=ticket, period=period, group_by='ticker', interval=timeframe, threads=True, progress=False)
    except:
        excepetion_message("Error when trying to download DataFrame")    

    return df    

def renames_timeframe(timeframe: str) -> str:
    """
    Renames timeframe from 60m to 1h
    """

    if timeframe == "60m":
        return "1h"

    return timeframe    