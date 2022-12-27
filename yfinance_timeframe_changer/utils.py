import pandas as pd

def excepetion_message(message: str) -> None:
    """
    Raises a excepetion message
    """

    print(message)
    print("\n\n")
    raise Exception(message)


def download_dataframe(ticket: str = "AAPL", interval: str = "1d") -> pd.core.frame.DataFrame:
    """
    Calls a database using YFinance API. This function is usefull only for tests
    """

    from pandas_datareader import data as pdr
    import yfinance as yf
    import pandas as pd  


    intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    periods = ["7d", "60d", "60d", "60d", "60d", "60d", "60d", "730d", "max", "max", "max" , "max", "max"]

    if interval not in intervals:
        excepetion_message(f"Period not available! Only accepts {interval}")

    period = periods[intervals.index(interval)]

    try:
        yf.pdr_override()  
        df = pdr.get_data_yahoo(ticket, period = period, group_by = 'ticker', interval = interval, threads = True, progress = False)
    except:
        excepetion_message("Ticket probaly doesn't exist!")    

    return df    

    